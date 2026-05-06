---
created: 2026-05-1
publish: true
tags:
- vibecoding
title: 제26장. 재사용 가능한 자산 만들기
type: techbook
---

```toc
minLevel: 1
maxLevel: 1
```
# 제26장. 재사용 가능한 자산 만들기

> *"좋은 자산은 한 번 만들고 열 번 쓴다."*

---

### 0) 연결 고리 (Bridge)

25장에서 오류를 처리하는 방법을 배웠습니다. 오류에서 배운 교훈, 잘 작동한 코드, 검증된 프롬프트 — 이것들이 다음 프로젝트에서 재사용되지 않으면 매번 처음부터 시작하는 것과 다르지 않습니다. 26장에서는 AI 협업에서 쌓인 모든 경험을 **다음 프로젝트의 시작점을 높이는 영구 자산**으로 만드는 방법을 체계적으로 다룹니다.

---

### 1) 재사용 가능한 자산의 5가지 유형

```
유형 1 — SKILL.md (AI 지시서)
  재사용 범위: 동일 프로젝트 + 유사 프로젝트
  저장 위치: GitHub 레포 루트 + Obsidian 00-SKILL-MD/
  수명: 프로젝트 유지 기간 + α

유형 2 — 프롬프트 템플릿
  재사용 범위: 동일 유형의 모든 작업
  저장 위치: Obsidian 01-Prompts/ + Notion 팀 위키
  수명: 도구 메이저 버전 변경 전까지

유형 3 — 코드 스니펫 라이브러리
  재사용 범위: 언어·프레임워크가 같은 모든 프로젝트
  저장 위치: GitHub 개인 레포 (snippets/)
  수명: 반영구

유형 4 — 워크플로우 템플릿 (n8n JSON)
  재사용 범위: 동일 패턴의 자동화
  저장 위치: GitHub + n8n 내보내기
  수명: n8n 메이저 버전 변경 전까지

유형 5 — 프로젝트 스타터 킷
  재사용 범위: 새 프로젝트 시작 시
  저장 위치: GitHub Template Repository
  수명: 반영구
```

---

### 2) 코드 스니펫 라이브러리

자주 쓰이는 코드 패턴을 검색 가능한 형태로 보관합니다.

#### 스니펫 파일 구조

```
snippets/
├── python/
│   ├── file_handling.py      ← 파일 입출력 패턴
│   ├── excel_patterns.py     ← openpyxl 자주 쓰는 패턴
│   ├── pdf_parsing.py        ← pdfplumber 핵심 패턴
│   ├── api_clients.py        ← httpx 클라이언트 패턴
│   ├── db_patterns.py        ← SQLAlchemy CRUD 패턴
│   └── amount_utils.py       ← 한국 금액 처리 유틸
├── n8n/
│   ├── slack-notification.json
│   ├── notion-insert.json
│   └── error-handler.json
└── prompts/
    ├── code-generation.md
    ├── document-writing.md
    └── data-analysis.md
```

#### 스니펫 예시 — 한국 금액 처리 유틸

```python
# snippets/python/amount_utils.py
"""
한국 정부 문서·금융 데이터에서 공통으로 쓰이는
금액 파싱·포맷팅 유틸리티.

재사용 현황:
  - KAIB2026 파이프라인 (2026-02)
  - HR 인사이동 보고서 (2026-03)
  - 개인금융 파이프라인 (2026-04)
"""
import re
from typing import Optional


def parse_krw(raw: str | None) -> Optional[int]:
    """한국 금액 문자열을 정수(원)로 변환한다.

    지원 형식:
        '1,234,567'     → 1234567
        '1234567'       → 1234567
        '1,234백만'     → 1234000000  (단위: 백만)
        '(△123,456)'   → -123456
        '△123,456'     → -123456
        '-', '–', ''   → None

    Args:
        raw: 원시 금액 문자열
    Returns:
        정수 원 금액 또는 None
    """
    if raw is None:
        return None
    raw = str(raw).strip()
    if raw in ('-', '–', '—', '', 'N/A', '○', '-'):
        return None

    is_negative = bool(re.search(r'[△▲(]', raw))

    # 단위 처리
    unit = 1
    if '억' in raw:
        unit = 100_000_000
    elif '백만' in raw:
        unit = 1_000_000
    elif '만' in raw:
        unit = 10_000

    digits = re.sub(r'[^0-9]', '', raw)
    if not digits:
        return None

    amount = int(digits) * unit
    return -amount if is_negative else amount


def format_krw(amount: int | None,
               unit: str = '원',
               show_sign: bool = False) -> str:
    """정수 금액을 한국 형식 문자열로 변환한다.

    Args:
        amount: 정수 금액 (원 단위)
        unit: 표시 단위 ('원', '백만원', '억원')
        show_sign: 부호 표시 여부 (+/-)

    Returns:
        포맷된 금액 문자열
    """
    if amount is None:
        return '-'

    divisors = {'원': 1, '백만원': 1_000_000, '억원': 100_000_000}
    divisor = divisors.get(unit, 1)
    value = amount / divisor

    if value == int(value):
        formatted = f"{int(value):,}"
    else:
        formatted = f"{value:,.1f}"

    if show_sign and amount > 0:
        formatted = f"+{formatted}"

    return f"{formatted}{unit}"
```

#### 스니펫 검색 방법

```bash
# 키워드로 스니펫 검색
grep -r "병합 셀" snippets/python/
grep -r "Slack" snippets/n8n/

# 또는 Obsidian에서 태그 검색
# #snippet #python #금액처리
```

---

### 3) n8n 워크플로우 템플릿 라이브러리

자주 쓰이는 n8n 워크플로우를 JSON으로 내보내 재사용합니다.

#### 핵심 템플릿 목록

```
[n8n 워크플로우 템플릿]

1. 기본 Slack 알림 패턴
   파일: slack-basic-notification.json
   구성: Schedule → 처리 → IF → Slack 성공/실패
   재사용: 모든 자동화의 기본 뼈대

2. Notion DB 저장 패턴
   파일: notion-db-insert.json
   구성: 트리거 → 데이터 변환 → Notion Insert → 확인
   재사용: 모든 데이터 아카이빙 워크플로우

3. 오류 감시 패턴
   파일: error-handler-template.json
   구성: Error Trigger → 메시지 포맷 → Slack 긴급 채널
   재사용: 모든 워크플로우에 연결

4. HTTP → AI 요약 → Slack 패턴
   파일: rss-ai-summary.json
   구성: RSS/HTTP → AI Agent → IF 중요도 → Slack
   재사용: 모든 콘텐츠 모니터링 자동화
```

#### n8n 워크플로우 내보내기/가져오기

```
내보내기:
  n8n 대시보드 → 워크플로우 선택
  → 우상단 ⋮ 메뉴 → Download
  → JSON 파일 저장 → GitHub에 커밋

가져오기:
  n8n 대시보드 → 새 워크플로우
  → 우상단 ⋮ 메뉴 → Import from File
  → 저장된 JSON 선택
  → Credentials(API 키) 재연결
```

---

### 4) GitHub Template Repository — 프로젝트 스타터 킷

새 프로젝트를 시작할 때 처음부터 올바른 구조로 시작하게 해주는 템플릿입니다.

#### Python 파이프라인 스타터 킷

```
python-pipeline-starter/
├── .github/
│   └── workflows/
│       └── test.yml              ← 자동 테스트 설정
├── src/
│   ├── __init__.py
│   ├── collectors/               ← 데이터 수집
│   ├── processors/               ← 데이터 처리
│   ├── storage/                  ← DB 저장
│   └── utils/
│       ├── amount_utils.py       ← 재사용 유틸 포함
│       ├── logging_config.py     ← 표준 로깅 설정
│       └── validators.py         ← 공통 Pydantic 모델
├── tests/
│   └── conftest.py
├── data/                         ← 원본 (수정 금지)
├── output/
├── .env.example                  ← 환경 변수 템플릿
├── .gitignore                    ← Python + .env 제외
├── CLAUDE.md                     ← Claude Code 컨텍스트
├── SKILL.md                      ← 프로젝트 규칙 (작성 필요)
├── requirements.txt
└── README.md
```

#### GitHub Template 설정 방법

```
1. GitHub에서 템플릿 레포 생성
   Settings → ✅ "Template repository" 체크

2. 새 프로젝트 시작 시:
   GitHub → "Use this template" 버튼
   → 새 레포 이름 입력 → 생성

3. 로컬에서:
   git clone [새 레포 URL]
   cd [프로젝트명]
   cp .env.example .env
   # SKILL.md 수정 후 시작
```

---

### 5) 자산 업데이트 트리거 — 언제 업데이트하나

```
자산을 업데이트해야 하는 5가지 신호:

신호 1 — 같은 버그를 두 번째 만났을 때
  → 해당 버그를 막는 규칙을 SKILL.md에 추가

신호 2 — "이 코드 어디서 보지 않았나?" 생각이 들 때
  → 해당 코드를 스니펫으로 저장

신호 3 — 새 팀원이 같은 질문을 할 때
  → 답변을 팀 SKILL.md 또는 Notion 위키에 추가

신호 4 — AI가 같은 잘못된 패턴을 반복할 때
  → SKILL.md의 금지 사항에 추가

신호 5 — 프로젝트가 완전히 끝났을 때
  → 회고 문서 작성 + 핵심 자산 아카이빙
```

---

### 6) 프로젝트 완료 회고 — 자산화 루틴

프로젝트가 완료되면 다음 순서로 자산화합니다.

```
[프로젝트 완료 회고 템플릿 — 30분]

## [프로젝트명] 완료 회고
날짜: YYYY-MM-DD

### 잘 된 것
- 무엇이 예상보다 빠르게 진행됐는가?
- 어떤 도구/프롬프트가 특히 효과적이었는가?

### 어려웠던 것
- 가장 많은 시간이 걸린 문제는?
- v15까지 간 이유는 무엇이었는가?

### 다음에 처음부터 할 일
- 이번에 삽질한 것 중 처음부터 알았다면 
  하지 않았을 것들

### 재사용 자산
□ SKILL.md 최종 버전 GitHub 커밋
□ 핵심 프롬프트 Obsidian에 저장
□ 재사용 가능한 함수 snippets/ 에 추가
□ n8n 워크플로우 JSON 내보내기
□ README 업데이트 (다음 사람이 실행할 수 있게)

### 다음 프로젝트에 전달할 한 문장
"이 프로젝트에서 가장 중요한 교훈은 _____ 이다."
```

---

### 7) 팀 자산 공유 체계

개인 자산을 팀 전체가 활용하는 구조를 만들면 조직의 AI 역량이 개인 숙련에서 팀 자산으로 전환됩니다.

```
[팀 AI 자산 저장소 구조]

GitHub Organization: my-team/ai-assets

레포 1: ai-assets (메인)
  README.md     ← 자산 인덱스
  SKILL-MD/     ← 팀 공통 + 프로젝트별 SKILL.md
  snippets/     ← 코드 스니펫 라이브러리
  n8n-flows/    ← 워크플로우 템플릿

레포 2: project-starters
  python-pipeline/   ← Python 파이프라인 스타터
  nextjs-app/        ← Next.js + Supabase 스타터

Notion: AI 협업 위키
  → 신규 팀원 온보딩 가이드
  → 도구별 사용 가이드 요약
  → 자주 쓰는 프롬프트 TOP 10

Obsidian 공유 볼트: (팀 공유 드라이브 또는 GitHub)
  → 검증된 프롬프트 전체 아카이브
```

---

### 8) 자산 품질 기준

모든 자산이 같은 수준의 재사용성을 가지지는 않습니다.

```
자산 등급 기준:

⭐ (등급 1) — 임시 메모
  사용 횟수: 1회
  문서화: 없음
  재사용 가능성: 낮음

⭐⭐ (등급 2) — 로컬 스니펫
  사용 횟수: 2~3회
  문서화: 간단한 주석
  재사용 가능성: 중간

⭐⭐⭐ (등급 3) — 팀 공유 자산
  사용 횟수: 3회 이상
  문서화: 사용법, 예시, 주의사항 포함
  재사용 가능성: 높음
  조건: 다른 사람이 설명 없이 사용 가능

목표: 모든 재사용 자산이 ⭐⭐⭐ 등급
조건: README.md에 "이 코드/프롬프트를 처음 보는 사람도
      5분 안에 사용할 수 있는가?"를 기준으로 판단
```

---

### 9) 한 줄 요약

> 💡 **Key Takeaway:** 재사용 자산은 저절로 쌓이지 않습니다. **프로젝트 완료 시 30분의 회고·정리 루틴**이 다음 프로젝트의 시작점을 높이고, 팀의 AI 협업 역량을 개인 경험에서 조직 자산으로 전환시킵니다.

---

*다음 장: 27장(8부 첫 장). 일반인 입문 로드맵*