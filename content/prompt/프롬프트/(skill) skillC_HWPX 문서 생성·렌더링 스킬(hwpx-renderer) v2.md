---
created: 2026-03-06
publish: true
tags: []
title: (skill) skillC_HWPX 문서 생성·렌더링 스킬
type:
- prompt
version: '2.0'
---

## 0. 역할 경계 (Pipeline 상 위치) ★ 신규

이 스킬은 **포맷 변환기**다. 내용 생성·요약·수정은 절대 하지 않는다.

```
[Skill A] 초안 작성 (보고서 작성, 시장 조사 등)
   ↓
[Skill B] 문장 정제 (sentence-normalizer) → □ ○ ― 구조화 완료
   ↓
[Skill C] HWPX 변환 (본 스킬) ← 여기서는 내용을 건드리지 않는다
```

|항목|Skill A|Skill B|Skill C (본 스킬)|
|---|---|---|---|
|내용 생성|○|✕|**✕ (절대 금지)**|
|문체·길이 조정|✕|○|**✕ (절대 금지)**|
|구조 분해|△|○|✕|
|포맷·레이아웃 변환|✕|✕|**◎**|

> ⚠️ **Skill B 결과물을 입력으로 받을 때, 텍스트를 단 한 글자도 수정하지 않는다.** 슬롯이 부족하더라도 내용을 요약·합치지 않는다. → 슬롯을 XML로 복제하여 늘린다 (§5.3 참조)

---

## 1. 핵심 원칙 (모든 경우 강제)

1. **템플릿 우선순위** (예외 절대 없음)
    
    - 1순위: 사용자 업로드 `.hwpx` 파일 (`/mnt/user-data/uploads/` 내)
    - 2순위: 기본 제공 템플릿 (`assets/report-template.hwpx` 등)
    - 3순위: `HwpxDocument.new()` → **보고서·공문·기안문 등 양식 문서에서는 절대 금지**
2. **치환 전략 우선순위** (안정성 최우선)
    
    - 기본: **ZIP-level 전체 치환** (HwpxDocument.open()보다 훨씬 안전)
    - 보조: 필요한 경우에만 `python-hwpx` API 사용 (표 추가·셀 병합·그림 삽입 등)
3. **XML 이스케이프 필수** ★ 신규
    
    - 치환값 삽입 전 반드시 `xml_escape()` 적용 (§5.1 참조)
    - 미적용 시 `&`, `<`, `>` 등이 XML을 손상시켜 파일 열람 불가
4. **슬롯 수 일치 원칙** ★ 신규
    
    - 입력 블록 수 > 템플릿 슬롯 수인 경우 → 내용 축소 금지, XML 슬롯 복제로 대응 (§5.3 참조)
    - 입력 블록 수 < 템플릿 슬롯 수인 경우 → 남은 슬롯을 빈 문자열로 치환
5. **필수 후처리**
    
    - 모든 저장/치환 후 → `fix_namespaces.py` 반드시 실행
    - 실행하지 않으면 한글 뷰어에서 빈 페이지 또는 깨짐 발생
6. **XML 유효성 검증 필수** ★ 신규
    
    - `fix_namespaces.py` 실행 후 `xml.etree.ElementTree`로 파싱 유효성 검증
    - 검증 실패 시 즉시 중단하고 오류 위치 탐색 후 재처리
7. **플레이스홀더 전수 확인**
    
    - 치환 전: 템플릿 내 플레이스홀더 종류·개수 카운트
    - 치환 후: 잔존 여부 100% 확인 → 잔존 시 실패 처리

---

## 2. 지원 입력 형태

|입력 유형|사용 사례|처리 방식 추천|
|---|---|---|
|자유 대화형 지시|사용자와 실시간으로 내용 조정|ZIP-level 치환 + 부분 API 조작|
|**Skill B 결과물 (MD/구조화 텍스트)**|**sentence-normalizer 이후 파이프라인**|**내용 무변경 원칙 + 슬롯 복제 방식**|
|사용자 제공 .hwpx 양식|회사/기관 고유 양식 사용 시|**무조건** 해당 파일 기반 ZIP 치환|
|복잡한 표·레이아웃 필요|셀 병합, 다단, 그림 삽입 등|ZIP 치환 후 python-hwpx API 병행|

---

## 3. 폴더 구조 및 참조 파일

```
skills/user/hwpx/
├── assets/
│   └── report-template.hwpx          # 기본 보고서 양식 (표지+목차+본문 구조)
│   └── (향후) official-doc-template.hwpx  # 공문/기안문용
├── references/
│   ├── report-style.md               # 보고서 문체·표현·기호 체계
│   ├── official-doc-style.md         # 공문·기안문 작성법
│   └── xml-internals.md              # 저수준 XML 구조 참고용
├── scripts/
│   └── fix_namespaces.py             # 네임스페이스 복구 스크립트 (필수!)
└── evals/
    └── evals.json
```

---

## 4. 기본 워크플로우 (모든 경우 공통)

```
[1] 템플릿 결정 및 /home/claude/ 작업 디렉토리로 복사
    ↓
[2] 템플릿 플레이스홀더 전수 조사
    → 종류별 개수 카운트 (□ N개, ○ N개, ― N개, ※ N개)
    ↓
[3] 입력 블록 수와 슬롯 수 비교
    → 블록 수 > 슬롯 수: XML 슬롯 복제 (§5.3)
    → 블록 수 ≤ 슬롯 수: 남은 슬롯은 빈 문자열 치환
    ↓
[4] XML 이스케이프 적용 후 ZIP-level 치환 수행 (§5.1, §5.2)
    ↓
[5] 필요 시 python-hwpx API로 추가 작업 (표·그림 등)
    ↓
[6] fix_namespaces.py 실행 (subprocess.run 필수)
    ↓
[7] XML 유효성 검증 (§5.4)
    ↓
[8] 플레이스홀더 잔존 여부 최종 확인
    ↓
[9] /mnt/user-data/outputs/ 로 이동 → present_files
```

---

## 5. 핵심 함수 (직접 포함 필수)

### 5.1 XML 이스케이프 함수 ★ 신규

```python
def xml_escape(s: str) -> str:
    """
    치환값 삽입 전 반드시 호출.
    & 를 가장 먼저 치환해야 이중 변환(&amp;amp;) 방지.
    """
    return (s.replace("&", "&amp;")   # ← 반드시 첫 번째
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&apos;"))
```

> ❌ 이스케이프 없이 치환하면:
> 
> - `R&D` → XML 파싱 오류 → 파일 손상 (열람 불가)
> - `<모델명>` → XML 태그로 오인 → 구조 파괴

### 5.2 ZIP-level 치환 함수

```python
import zipfile, os

def zip_replace(src_path, dst_path, replacements):
    """모든 Contents/*.xml 텍스트 일괄 치환 (고정값용)"""
    tmp = dst_path + ".tmp"
    with zipfile.ZipFile(src_path, "r") as zin:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename.startswith("Contents/") and item.filename.endswith(".xml"):
                    text = data.decode("utf-8")
                    for old, new in replacements.items():
                        # 고정값도 이스케이프 적용
                        text = text.replace(old, xml_escape(new))
                    data = text.encode("utf-8")
                zout.writestr(item, data)
    os.replace(tmp, dst_path)


def zip_replace_sequential(src_path, dst_path, old_text, new_list):
    """
    section*.xml 내 동일 플레이스홀더를 순서대로 치환 (순차 블록용).
    ★ xml_escape() 필수 적용
    ★ new_list 길이 != 슬롯 수 → 사전에 슬롯 복제(§5.3) 또는 빈값 패딩으로 일치시킬 것
    """
    tmp = dst_path + ".tmp"
    with zipfile.ZipFile(src_path, "r") as zin:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if "section" in item.filename and item.filename.endswith(".xml"):
                    text = data.decode("utf-8")
                    for new_val in new_list:
                        text = text.replace(old_text, xml_escape(new_val), 1)  # ★ 이스케이프
                    data = text.encode("utf-8")
                zout.writestr(item, data)
    os.replace(tmp, dst_path)
```

### 5.3 슬롯 복제 함수 ★ 신규

입력 블록 수가 템플릿 슬롯 수보다 많을 때 사용한다. **내용을 축소하거나 합치는 것은 절대 금지.** 슬롯을 늘려서 맞춘다.

```python
def expand_slots(src_path, dst_path, placeholder, target_count):
    """
    placeholder가 target_count개가 될 때까지 마지막 occurrence를 복제.
    
    동작 원리:
    - 현재 슬롯 수 파악
    - 부족한 수만큼: 마지막 슬롯의 XML 단락 블록을 찾아 뒤에 복제 삽입
    
    Args:
        placeholder: 예) "헤드라인M 폰트 16포인트(문단 위 15)"
        target_count: 필요한 슬롯 수 (입력 블록 수)
    """
    import re, zipfile, os

    tmp = dst_path + ".tmp"
    with zipfile.ZipFile(src_path, "r") as zin:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if "section" in item.filename and item.filename.endswith(".xml"):
                    text = data.decode("utf-8")
                    current_count = text.count(placeholder)

                    if current_count < target_count:
                        # 마지막 플레이스홀더를 포함하는 <hp:p>...</hp:p> 블록 추출
                        # placeholder 위치 기준으로 앞뒤 <hp:p ~ </hp:p> 범위를 찾아 복제
                        pattern = r'(<hp:p\b[^>]*>(?:(?!<hp:p\b).)*?' + re.escape(placeholder) + r'.*?</hp:p>)'
                        matches = list(re.finditer(pattern, text, re.DOTALL))

                        if matches:
                            last_match = matches[-1]
                            clone_block = last_match.group(0)
                            insert_pos = last_match.end()
                            needed = target_count - current_count
                            insertion = clone_block * needed
                            text = text[:insert_pos] + insertion + text[insert_pos:]

                    data = text.encode("utf-8")
                zout.writestr(item, data)
    os.replace(tmp, dst_path)


# 사용 예시
# 템플릿에 □ 슬롯이 8개인데 입력 블록이 22개인 경우:
# expand_slots(WORK, WORK, "헤드라인M 폰트 16포인트(문단 위 15)", 22)
# 이후 zip_replace_sequential() 로 22개 치환
```

### 5.4 XML 유효성 검증 함수 ★ 신규

```python
import xml.etree.ElementTree as ET
import zipfile

def validate_xml(hwpx_path):
    """
    fix_namespaces 실행 후 반드시 호출.
    파싱 실패 시 오류 위치(line, column)와 전후 문맥을 출력.
    """
    targets = ["Contents/section0.xml", "Contents/header.xml"]
    all_valid = True

    with zipfile.ZipFile(hwpx_path, "r") as z:
        for fname in targets:
            content = z.read(fname).decode("utf-8")
            try:
                ET.fromstring(content)
                print(f"  ✅ {fname}: 유효")
            except ET.ParseError as e:
                all_valid = False
                # 오류 위치 파악
                line, col = e.position if hasattr(e, 'position') else (0, 0)
                # 바이트 위치로 변환하여 전후 문맥 출력
                lines = content.split('\n')
                ctx = lines[line-1] if line > 0 and line <= len(lines) else ""
                print(f"  ❌ {fname}: {e}")
                print(f"     오류 위치 line {line}, col {col}")
                print(f"     문맥: {repr(ctx[max(0,col-40):col+40])}")
                print(f"     → xml_escape() 누락 여부 확인. 특히 & < > 문자")

    return all_valid

# 사용 예시
# if not validate_xml(WORK):
#     raise RuntimeError("XML 유효성 검증 실패 - 출력 중단")
```

### 5.5 슬롯 수 사전 점검 함수 ★ 신규

```python
def check_slot_counts(hwpx_path, placeholder_map):
    """
    치환 시작 전 슬롯 수와 입력 블록 수를 비교하여 경고/복제 필요 여부 안내.
    
    Args:
        placeholder_map: {플레이스홀더 문자열: 입력 블록 리스트} 딕셔너리
    
    Returns:
        needs_expansion: True이면 expand_slots() 호출 필요
    """
    needs_expansion = False
    with zipfile.ZipFile(hwpx_path, "r") as z:
        for fname in z.namelist():
            if "section" in fname and fname.endswith(".xml"):
                text = z.read(fname).decode("utf-8")
                for ph, blocks in placeholder_map.items():
                    slot_count = text.count(ph)
                    block_count = len(blocks)
                    if block_count > slot_count:
                        print(f"  ⚠️  슬롯 부족: [{ph[:20]}...] 슬롯={slot_count} / 블록={block_count}")
                        print(f"      → expand_slots() 호출 필요")
                        needs_expansion = True
                    elif block_count < slot_count:
                        print(f"  ℹ️  슬롯 초과: [{ph[:20]}...] 슬롯={slot_count} / 블록={block_count}")
                        print(f"      → 남은 {slot_count - block_count}개 슬롯은 빈 문자열로 패딩")
                    else:
                        print(f"  ✅ 슬롯 일치: [{ph[:20]}...] {slot_count}개")
    return needs_expansion

# 사용 예시
# placeholder_map = {
#     "헤드라인M 폰트 16포인트(문단 위 15)": headline_list,
#     "휴면명조 15포인트(문단위 10)": body1_list,
#     "휴면명조 15포인트(문단 위 6)": body2_list,
#     "중고딕 13포인트(문단 위 3)": source_list,
# }
# if check_slot_counts(WORK, placeholder_map):
#     expand_slots(WORK, WORK, "헤드라인M 폰트 16포인트(문단 위 15)", len(headline_list))
#     # ... 나머지 슬롯도 동일하게 처리
```

---

## 6. Skill B 파이프라인 입력 처리 규칙 ★ 신규

sentence-normalizer(Skill B) 결과물을 입력으로 받을 때의 처리 규칙.

### 6.1 입력 구조 예시

```
□ 피지컬 AI 시대로의 패러다임 전환 본격화
○ 2026년 현재 글로벌 AI 산업은 소프트웨어 경계를 넘어 물리적 세계로 ...
― 2025년 하반기를 기점으로 하드웨어와 AI 알고리즘의 융합이 ...
```

### 6.2 처리 원칙

```
1. □ → 헤드라인 슬롯 (헤드라인M 폰트 16포인트)
2. ○ → 중분류 슬롯 (휴면명조 15포인트(문단위 10))
3. ― → 소분류 슬롯 (휴면명조 15포인트(문단 위 6))
4. * 출처: → 참조 슬롯 (중고딕 13포인트(문단 위 3))

규칙:
- 텍스트는 기호(□ ○ ―)를 제거한 나머지를 그대로 삽입
- 요약·수정·합치기 절대 금지
- 슬롯 부족 시 expand_slots() 호출
```

### 6.3 MD 파일 파싱 예시 코드

```python
def parse_skill_b_output(md_text):
    """
    Skill B(sentence-normalizer) 결과 MD를 파싱하여
    레벨별 블록 리스트 반환.
    텍스트는 원문 그대로 보존.
    """
    headlines, body1, body2, sources = [], [], [], []

    for line in md_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("□ "):
            headlines.append(line[2:].strip())
        elif line.startswith("○ "):
            body1.append(line[2:].strip())
        elif line.startswith("― "):
            body2.append(line[2:].strip())
        elif line.startswith("* 출처:") or line.startswith("* 자료:"):
            sources.append(line[2:].strip())

    return headlines, body1, body2, sources

# 사용 예시
# with open("/mnt/user-data/outputs/정제_피지컬AI_보고서.md") as f:
#     md_text = f.read()
# headlines, body1, body2, sources = parse_skill_b_output(md_text)
# print(f"□ {len(headlines)}개 / ○ {len(body1)}개 / ― {len(body2)}개 / ※ {len(sources)}개")
```

---

## 7. JSON 구조 입력 시 치환 규칙 (파이프라인용)

```json
{
  "document": {
    "title": "2026년도 사업 추진 계획",
    "blocks": [
      {"level": "headline", "marker": "□", "text": "추진 배경"},
      {"level": "body_1",   "marker": "○", "text": "시장 변화에 따른 ..."},
      {"level": "body_2",   "marker": "―", "text": "구체적으로는 ..."},
      {"level": "source",   "marker": "*", "text": "출처: 기관명, ..."}
    ]
  }
}
```

→ `report-template.hwpx` 기준으로

- `헤드라인M 폰트 16포인트(문단 위 15)` → □ 내용 순차 치환
- `휴먼명조 15포인트(문단위 10)` → ○ 내용 순차 치환
- `휴먼명조 15포인트(문단 위 6)` → ― 내용 순차 치환
- `중고딕 13포인트(문단 위 3)` → ※/출처 내용 순차 치환

---

## 8. 복잡한 표·레이아웃 처리 가이드

1. 먼저 ZIP-level로 텍스트 치환 완료
2. 이후 `HwpxDocument.open(work_file)` 해서 추가 작업
    
    ```python
    from hwpx import HwpxDocumentdoc = HwpxDocument.open(work_file)table = doc.find_table_by_text("기존 표 제목")table.set_cell_text(2, 3, "새 값")table.merge_cells(1,1,1,3)doc.save(work_file)
    ```
    
3. 저장 후 **다시** fix_namespaces.py 실행
4. 저장 후 **다시** validate_xml() 실행

---

## 9. Quick Reference Table

|요구사항|추천 접근법|
|---|---|
|Skill B 결과물 → HWPX 변환|parse_skill_b_output() → check_slot_counts() → expand_slots() → zip_replace_sequential()|
|슬롯 수 부족|expand_slots()로 복제 (내용 축소 절대 금지)|
|특수문자 포함 텍스트|xml_escape() 필수 적용 후 치환|
|대화형 내용 조정|ZIP 치환 + 대화하며 매핑 수정|
|사용자 제공 양식|무조건 해당 파일 복사 → ZIP 치환|
|복잡한 표·셀 병합·그림|ZIP 치환 후 python-hwpx API 병행|
|최종 무결성 확인|validate_xml() + 플레이스홀더 잔존 확인|

---

## 10. 주의사항 (Top 12)

1. HwpxDocument.open()은 복잡한 양식에서 실패 가능성 있음 → ZIP 치환 우선
2. fix_namespaces.py는 **subprocess.run**으로 호출 (exec 금지)
3. 플레이스홀더 조사 없이 치환 시작 금지 → check_slot_counts() 먼저 실행
4. 순차 치환 시 new_list 길이 != 슬롯 수 → expand_slots() 또는 빈값 패딩으로 반드시 일치
5. 날짜 형식: `2026. 3. 5.` (월·일 0 생략)
6. 글꼴은 임베딩 안 됨 → 열람 환경에 해당 글꼴 필요
7. 보고서 스타일 → `references/report-style.md` 필수 확인
8. 공문서 → `references/official-doc-style.md` 필수 확인
9. 레이아웃은 한글 앱이 결정 → 과도한 XML 조작 자제
10. 최종 출력 전 플레이스홀더 잔존 여부 100% 확인
11. **★ 치환값에 & < > " ' 포함 시 xml_escape() 필수** → 미적용 시 파일 손상 (열람 불가)
    - & 를 가장 먼저 치환할 것 (순서 중요: &→& 먼저, 나머지 후)
    - 특히 `R&D`, `<모델명>`, URL 쿼리스트링 등에 주의
12. **★ fix_namespaces 실행 후 validate_xml() 로 XML 파싱 유효성 반드시 검증**
    - 검증 실패 시 즉시 중단 → 오류 위치(line, col) 확인 → xml_escape() 누락 여부 점검

---

## 변경 이력

|버전|일자|변경 내용|
|---|---|---|
|v1|최초|기본 ZIP-level 치환 워크플로우|
|v2|2026. 3. 5.|§0 역할 경계 명시 추가 / §1 XML 이스케이프·슬롯 수 일치·XML 유효성 검증 원칙 추가 / §5.1 xml_escape() 함수 추가 / §5.2 zip_replace_sequential xml_escape 적용 / §5.3 expand_slots() 슬롯 복제 함수 추가 / §5.4 validate_xml() 함수 추가 / §5.5 check_slot_counts() 함수 추가 / §6 Skill B 파이프라인 처리 규칙 신규 / 주의사항 11·12번 추가|