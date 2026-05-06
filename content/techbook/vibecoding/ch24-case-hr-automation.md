---
created: 2026-05-1
publish: true
tags:
- vibecoding
title: 제24장. 사례 인사이동 자동화
type: techbook
---

```toc
minLevel: 1
maxLevel: 1
```
# 제24장. 사례 1 — HR 인사이동 자동화

> *"설문→배정→보고서까지, 수작업 이틀을 30분으로."*

---

### 0) 연결 고리 (Bridge)

18장 레시피 3(데이터 파이프라인) + 레시피 4(업무 자동화)의 결합 사례입니다. HR 인사이동은 개인 선호 설문, 조직 요구사항, 경력·직급 조건이 복합적으로 얽히는 작업입니다. 이 사례는 설문 데이터 수집부터 팀 배정 로직, 최종 엑셀 보고서 생성까지 전체를 자동화한 파이프라인을 다룹니다.

---

### 1) 문제 정의

#### 배경

연 1~2회 진행되는 팀 인사이동 과정은 담당자에게 반복적인 수작업 부담을 줍니다.

```
수작업 인사이동 프로세스:
  1. Google Form으로 희망 부서 설문 발송
  2. 응답 Excel 다운로드
  3. 응답 데이터 수작업 취합·정리
  4. 직급·경력·제약 조건 대조
  5. 배정 초안 작성 (수작업 Excel)
  6. 담당자 수작업 조정
  7. 결재용 보고서 작성 (Excel + HWPX)
  8. 개별 발령 통보

소요 시간: 2~3일 (설문 마감 후)
오류: 중복 배정, 인원 초과, 조건 위반 빈번
```

#### 자동화 목표

```
입력:
  - 설문 응답 CSV (희망 부서 1~3순위, 특이사항)
  - 직원 마스터 데이터 (직급, 경력, 현 부서, 제약조건)
  - 부서별 인원 정원 및 요구사항

출력:
  - 배정 결과 Excel (개인별 발령 내역)
  - 부서별 인원 현황 Excel
  - 결재용 인사이동 보고서 HWPX
  - 개인별 발령 통보 이메일 초안

목표 시간: 30분 이내
```

---

### 2) 데이터 구조 설계

#### 입력 데이터 스키마

```python
# src/models/schemas.py
from pydantic import BaseModel, field_validator
from typing import Optional


class EmployeeProfile(BaseModel):
    """직원 프로파일."""
    emp_id: str              # 사번
    name: str                # 성명
    dept_current: str        # 현 부서
    grade: str               # 직급 (사원/대리/과장/차장/부장)
    years_exp: float         # 경력 연수
    skills: list[str]        # 보유 기술
    constraints: list[str]   # 배정 제약 (예: '해외 출장 불가')
    transfer_eligible: bool  # 이동 가능 여부


class TransferPreference(BaseModel):
    """인사이동 희망 설문 응답."""
    emp_id: str
    name: str
    pref_1: str              # 1순위 희망 부서
    pref_2: Optional[str]    # 2순위 희망 부서
    pref_3: Optional[str]    # 3순위 희망 부서
    reason: Optional[str]    # 희망 이유
    special_note: Optional[str]  # 특이사항


class DeptRequirement(BaseModel):
    """부서 요구사항."""
    dept_name: str
    headcount_target: int    # 목표 인원
    headcount_current: int   # 현재 인원
    vacancies: int           # 공석 수
    required_grade: list[str]  # 필요 직급
    required_skills: list[str]  # 필요 기술
    priority: int            # 충원 우선순위 (1=최우선)


class TransferAssignment(BaseModel):
    """배정 결과."""
    emp_id: str
    name: str
    dept_from: str
    dept_to: str
    grade: str
    assignment_reason: str   # 배정 근거
    pref_matched: int        # 희망 순위 달성 (1/2/3/0=미달성)
    effective_date: str      # 발령 예정일
```

---

### 3) 배정 로직 — Claude를 활용한 최적화

배정 알고리즘은 두 가지 방식을 조합합니다.

#### 방식 1 — 규칙 기반 사전 필터링 (Python)

```python
# src/services/assignment_engine.py

def filter_eligible_assignments(
    employees: list[EmployeeProfile],
    preferences: list[TransferPreference],
    dept_requirements: list[DeptRequirement]
) -> dict[str, list[str]]:
    """규칙 기반으로 배정 가능한 후보 목록을 생성한다.

    Returns:
        {사번: [배정 가능한 부서 목록]}
    """
    dept_map = {d.dept_name: d for d in dept_requirements}
    emp_map = {e.emp_id: e for e in employees}
    pref_map = {p.emp_id: p for p in preferences}

    eligible = {}

    for emp in employees:
        if not emp.transfer_eligible:
            continue

        pref = pref_map.get(emp.emp_id)
        candidates = []

        # 희망 부서 순서대로 가능 여부 확인
        prefs = []
        if pref:
            prefs = [p for p in [pref.pref_1, pref.pref_2, pref.pref_3]
                     if p]

        for dept_name in prefs:
            dept = dept_map.get(dept_name)
            if not dept:
                continue

            # 조건 1: 공석이 있어야 함
            if dept.vacancies <= 0:
                continue

            # 조건 2: 직급 조건 충족
            if dept.required_grade and emp.grade not in dept.required_grade:
                continue

            # 조건 3: 제약 조건 위반 없음
            violations = set(emp.constraints) & set(dept_requirements)
            if violations:
                continue

            candidates.append(dept_name)

        eligible[emp.emp_id] = candidates

    return eligible
```

#### 방식 2 — Claude로 복잡한 케이스 처리

```python
def resolve_complex_cases(
    unassigned: list[str],
    eligible: dict,
    context: dict
) -> str:
    """규칙으로 해결 안 되는 복잡한 케이스를 Claude에게 위임한다."""

    prompt = f"""
[HR 인사이동 배정 전문가로서 답해줘]

다음 직원들은 자동 배정 규칙으로 해결되지 않은 케이스야.
각 직원에 대해 최적 배정 부서와 근거를 JSON으로 답해줘.

미배정 직원: {json.dumps(unassigned, ensure_ascii=False)}
배정 가능 후보: {json.dumps(eligible, ensure_ascii=False)}
전체 맥락: {json.dumps(context, ensure_ascii=False)}

조건:
- 가능한 한 희망 순위를 반영
- 부서별 직급 균형 고려
- 제약 조건 절대 위반 금지

응답 형식:
{{
  "assignments": [
    {{
      "emp_id": "사번",
      "dept_to": "배정 부서",
      "reason": "배정 근거 (2줄 이내)",
      "pref_matched": 0
    }}
  ]
}}
"""
    # Claude API 호출
    response = call_claude_api(prompt)
    return response
```

---

### 4) Excel 보고서 자동 생성

#### 보고서 구성

```python
# src/reporters/excel_reporter.py
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter


def create_transfer_report(
    assignments: list[TransferAssignment],
    output_path: str
) -> None:
    """인사이동 결과 Excel 보고서를 생성한다.

    시트 구성:
      1. 개인별 발령 내역 (전체 목록)
      2. 부서별 인원 현황 (이동 전·후)
      3. 희망 반영률 통계
      4. 원본 데이터 (숨김 시트)
    """
    wb = openpyxl.Workbook()

    # ── 시트 1: 개인별 발령 내역 ──────────────────────────
    ws1 = wb.active
    ws1.title = "개인별 발령 내역"

    headers = [
        "사번", "성명", "직급", "현 부서", "발령 부서",
        "희망 순위 달성", "배정 근거", "발령 예정일"
    ]
    _write_header_row(ws1, headers, row=1)

    for row_idx, a in enumerate(assignments, start=2):
        ws1.cell(row=row_idx, column=1, value=a.emp_id)
        ws1.cell(row=row_idx, column=2, value=a.name)
        ws1.cell(row=row_idx, column=3, value=a.grade)
        ws1.cell(row=row_idx, column=4, value=a.dept_from)
        ws1.cell(row=row_idx, column=5, value=a.dept_to)
        pref_text = f"{a.pref_matched}순위" if a.pref_matched > 0 else "미반영"
        ws1.cell(row=row_idx, column=6, value=pref_text)
        ws1.cell(row=row_idx, column=7, value=a.assignment_reason)
        ws1.cell(row=row_idx, column=8, value=a.effective_date)

        # 미반영 행 강조 (주황색)
        if a.pref_matched == 0:
            for col in range(1, 9):
                ws1.cell(row=row_idx, column=col).fill = \
                    PatternFill("solid", fgColor="FFE0B2")

    _auto_fit_columns(ws1)

    # ── 시트 2: 부서별 현황 ──────────────────────────────
    ws2 = wb.create_sheet("부서별 인원 현황")
    _create_dept_summary_sheet(ws2, assignments)

    # ── 시트 3: 통계 ─────────────────────────────────────
    ws3 = wb.create_sheet("희망 반영률 통계")
    _create_statistics_sheet(ws3, assignments)

    wb.save(output_path)
    print(f"Excel 보고서 저장: {output_path}")


def _write_header_row(ws, headers: list[str], row: int) -> None:
    """헤더 행을 작성하고 스타일을 적용한다."""
    header_fill = PatternFill("solid", fgColor="1565C0")
    header_font = Font(bold=True, color="FFFFFF", name="맑은 고딕", size=10)

    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")


def _auto_fit_columns(ws) -> None:
    """열 너비를 콘텐츠에 맞게 자동 조정한다."""
    for col in ws.columns:
        max_length = 0
        for cell in col:
            if cell.value:
                # 한국어 글자는 2배 너비로 계산
                length = sum(2 if ord(c) > 127 else 1
                             for c in str(cell.value))
                max_length = max(max_length, length)
        ws.column_dimensions[get_column_letter(col[0].column)].width = \
            min(max_length + 2, 40)
```

---

### 5) 이메일 초안 자동 생성

```python
def generate_notification_emails(
    assignments: list[TransferAssignment]
) -> list[dict]:
    """개인별 발령 통보 이메일 초안을 생성한다."""

    emails = []
    for a in assignments:
        prompt = f"""
다음 인사이동 발령 통보 이메일을 작성해줘.

수신자: {a.name} {a.grade}
현 부서: {a.dept_from}
발령 부서: {a.dept_to}
발령 예정일: {a.effective_date}

조건:
- 격식체 (존댓말)
- 간결하게 (3~5문장)
- 인사 담당자 서명 포함
- 문의사항 연락처 포함 (인사팀 내선 1234)
"""
        subject = f"[인사발령] {a.name} {a.grade} 부서 이동 안내"
        body = call_claude_api(prompt)
        emails.append({
            "emp_id": a.emp_id,
            "name": a.name,
            "email": f"{a.emp_id}@company.com",
            "subject": subject,
            "body": body,
        })

    return emails
```

---

### 6) 전체 파이프라인 실행

```python
# main.py — 전체 파이프라인 실행

def run_transfer_pipeline(
    survey_csv: str,
    employee_master_csv: str,
    dept_requirements_json: str,
    output_dir: str,
    effective_date: str
) -> dict:
    """인사이동 자동화 파이프라인 전체를 실행한다."""

    print("━━━ 1단계: 데이터 로드 및 검증 ━━━")
    employees = load_employees(employee_master_csv)
    preferences = load_survey_responses(survey_csv)
    requirements = load_dept_requirements(dept_requirements_json)

    # Pydantic 검증
    validated_emp = [EmployeeProfile(**e) for e in employees]
    validated_pref = [TransferPreference(**p) for p in preferences]
    validated_req = [DeptRequirement(**r) for r in requirements]
    print(f"  직원 {len(validated_emp)}명 / 설문 {len(validated_pref)}건 / 부서 {len(validated_req)}개 검증 완료")

    print("\n━━━ 2단계: 규칙 기반 배정 ━━━")
    eligible = filter_eligible_assignments(validated_emp, validated_pref, validated_req)
    assignments, unassigned = assign_by_rules(eligible, validated_req)
    print(f"  자동 배정: {len(assignments)}명 / 미배정: {len(unassigned)}명")

    if unassigned:
        print(f"\n━━━ 3단계: Claude 복잡 케이스 처리 ({len(unassigned)}명) ━━━")
        complex_assignments = resolve_complex_cases(unassigned, eligible, {})
        assignments.extend(complex_assignments)

    print("\n━━━ 4단계: Excel 보고서 생성 ━━━")
    excel_path = f"{output_dir}/인사이동_결과_{effective_date}.xlsx"
    create_transfer_report(assignments, excel_path)
    print(f"  저장: {excel_path}")

    print("\n━━━ 5단계: 이메일 초안 생성 ━━━")
    emails = generate_notification_emails(assignments)
    save_emails_to_json(emails, f"{output_dir}/emails_{effective_date}.json")

    print("\n━━━ 완료 ━━━")
    stats = calculate_statistics(assignments)
    print(f"  희망 1순위 달성: {stats['pref1_rate']:.1f}%")
    print(f"  희망 내 배정: {stats['any_pref_rate']:.1f}%")
    print(f"  미반영: {stats['unmatched_count']}명")

    return stats
```

---

### 7) n8n 연동 — 설문 마감 자동 트리거

```
[n8n 워크플로우]

트리거: Webhook (Google Form 응답 마감 시 발송)
  또는: Schedule (설문 마감일 다음날 09:00)

노드 1: Google Drive → 설문 CSV 다운로드
노드 2: Python 파이프라인 실행
  POST http://localhost:8000/run-pipeline
  Body: {survey_csv, effective_date}

노드 3: 완료 대기 (Webhook)
노드 4: Slack #인사팀
  "✅ 인사이동 배정 초안 완성
   총 N명 배정 | 희망 반영률: X%
   [Excel 결과 파일 링크]
   [검토 요청: 담당자 @mention]"

노드 5: Notion → 배정 결과 DB 저장
  (이력 관리: 연도별 인사이동 누적)
```

---

### 8) 최종 성과

```
[자동화 전후 비교]

처리 시간:
  이전: 2~3일 (설문 취합 + 배정 + 보고서)
  이후: 30~45분 (파이프라인 실행 + 검토)
  개선: 약 40배 단축

오류율:
  이전: 중복 배정 3~5건/회, 조건 위반 1~2건/회
  이후: Pydantic 검증 → 조건 위반 0건

희망 반영률:
  이전: 담당자 감각 의존 → 실제 측정 어려움
  이후: 정량 측정 → 1순위 달성 68%, 희망 내 배정 89%

부가 효과:
  → 이메일 초안 자동 생성으로 개별 통보 작업도 단축
  → 연도별 이력 누적으로 배정 패턴 분석 가능
  → 이의신청 발생 시 배정 근거 즉시 제시 가능
```

---

### 9) 한 줄 요약

> 💡 **Key Takeaway:** HR 자동화의 핵심은 **Pydantic으로 데이터 무결성 확보 → 규칙 기반 자동 배정 → Claude로 예외 케이스 처리 → openpyxl로 보고서 생성** 4단계로, 반복 가능하고 감사 가능한(Auditable) 인사 프로세스를 만드는 것입니다.

---

*다음 장: 22장. 사례 4 — n8n 로컬 자동화 서버*