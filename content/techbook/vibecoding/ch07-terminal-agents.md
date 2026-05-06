---
created: 2026-05-1
publish: true
tags:
- vibecoding
title: 제7장. 터미널 에이전트
type: techbook
---

```toc
minLevel: 1
maxLevel: 1
```
# 제7장. 터미널 에이전트 — Claude Code / Codex CLI

> *"브라우저 창을 닫고 터미널을 열면, AI가 진짜 개발자가 된다."*

---

### 0) 연결 고리 (Bridge)

6장에서 브라우저 기반 대화형 도구(Claude.ai, ChatGPT, Gemini)를 살펴봤습니다. 이 도구들은 강력하지만 한 가지 한계가 있습니다. **실제 파일을 직접 수정하거나 코드를 실행할 수 없다**는 점입니다. 코드를 생성해도 사람이 복사해서 붙여넣고, 오류가 나면 다시 복사해서 AI에게 가져와야 합니다.

터미널 에이전트는 이 벽을 허뭅니다. AI가 직접 파일을 읽고, 수정하고, 실행하고, 오류를 잡습니다. 7장에서는 레벨 4 에이전트 코딩의 핵심 도구인 **Claude Code**와 **Codex CLI**를 다룹니다.

---

### 1) 개념 정의 및 필요성

#### 터미널 에이전트란?

**터미널 에이전트(Terminal Agent)**란 명령줄 인터페이스(CLI, Command Line Interface)에서 실행되는 AI 에이전트로, 실제 파일 시스템·터미널 명령·외부 API에 직접 접근하여 작업을 수행합니다.

| 구분 | 대화형 도구 (6장) | 터미널 에이전트 (7장) |
|------|-----------------|-------------------|
| 실행 환경 | 브라우저 | 터미널 (로컬 PC) |
| 파일 접근 | 첨부 업로드만 | 직접 읽기·쓰기 |
| 코드 실행 | 불가 | 직접 실행 |
| 오류 처리 | 사람이 복사·붙여넣기 | 자동 감지·수정 |
| 프로젝트 규모 | 파일 몇 개 | 수백 개 파일 프로젝트 |
| 적합 레벨 | 레벨 2 (바이브코딩) | 레벨 4 (에이전트 코딩) |

---

### 2) Claude Code

#### 개념 및 설치

**Claude Code**는 Anthropic이 공식 출시한 터미널 기반 에이전트 코딩 도구입니다. 프로젝트 폴더에서 실행하면 AI가 전체 코드베이스를 컨텍스트로 인식하고, 자연어 지시만으로 파일 생성·수정·실행·디버깅을 자율적으로 수행합니다.

**설치 요구사항:**
- Node.js 18 이상
- Anthropic API 키 또는 Claude Pro/Max 플랜

```bash
# Node.js 설치 확인
node --version   # v18.0.0 이상이어야 함

# Claude Code 설치
npm install -g @anthropic-ai/claude-code

# 설치 확인
claude --version

# API 키 설정 (최초 1회)
export ANTHROPIC_API_KEY="your-api-key-here"
```

> **TIP:** API 키를 매번 입력하지 않으려면 `~/.bashrc` 또는 `~/.zshrc`에 `export ANTHROPIC_API_KEY="..."` 를 추가하세요. Claude Pro/Max 플랜 사용자는 `claude login`으로 브라우저 인증도 가능합니다.

#### Claude Code 실행 방법

```bash
# 프로젝트 폴더로 이동
cd /my-project

# Claude Code 실행
claude

# 실행 후 자연어로 지시
> 이 프로젝트의 구조를 분석하고 README.md를 작성해줘.

> budget_parser.py를 읽고 병합 셀 처리 버그를 수정해줘.
  수정 후 test_budget.pdf로 테스트도 해줘.

> requirements.txt를 확인하고 누락된 패키지가 있으면 추가해줘.
```

#### Claude Code의 핵심 기능

**① 전체 코드베이스 인식**

```bash
# 수백 개 파일로 구성된 프로젝트도 전체 컨텍스트로 인식
my-project/
├── src/          ← 30개 Python 파일
├── tests/        ← 15개 테스트 파일
├── data/         ← CSV, JSON 데이터
└── docs/         ← 문서

# Claude Code는 이 전체 구조를 파악하고
# "src/budget_parser.py와 tests/test_parser.py를
#  함께 수정해줘"처럼 여러 파일을 동시에 다룸
```

**② 자율 디버깅 루프**

```
사람: "스크립트 실행하고 오류 수정해줘"

Claude Code 자동 처리:
  1. python budget_parser.py 실행
  2. 오류 메시지 감지:
     TypeError: 'NoneType' object is not subscriptable
     at line 247
  3. 247번 라인 분석
  4. None 체크 코드 삽입
  5. 재실행 → 성공
  6. 결과 보고: "247번 라인에 None 검사를 추가했습니다."
```

**③ Git 연동**

```bash
# Claude Code가 자동으로 Git 작업 처리
> 오늘 작업한 내용을 커밋해줘.

# 자동으로:
# 1. git diff로 변경사항 확인
# 2. 변경 내용을 요약한 커밋 메시지 작성
# 3. git add . && git commit -m "..." 실행
```

**④ CLAUDE.md — 프로젝트 영구 컨텍스트**

Claude Code는 프로젝트 루트의 `CLAUDE.md` 파일을 자동으로 읽습니다. 4장의 SKILL.md와 같은 개념이지만, Claude Code 전용으로 사용됩니다.

```markdown
# CLAUDE.md (프로젝트 루트에 저장)

## 프로젝트 개요
KAIB2026 예산 파싱 파이프라인

## 핵심 규칙
- Python 3.11 사용
- 주석은 한국어
- 금액 필드는 항상 정수 타입

## 절대 수정 금지 파일
- /data/budget_2026.pdf (원본)
- /config/db_schema.sql (스키마 고정)

## 실행 방법
python src/budget_parser.py --year 2026
```

---

### 3) Claude Code 권한 모드

Claude Code는 작업 전 사람에게 확인을 요청하는 기본 모드와, 자율 실행 모드 두 가지를 제공합니다.

| 모드 | 명령 | 특징 | 권장 상황 |
|------|------|------|----------|
| **기본 모드** | `claude` | 파일 수정·실행 전 확인 요청 | 중요한 프로젝트, 학습 중 |
| **자율 모드** | `claude --dangerously-skip-permissions` | 확인 없이 자율 실행 | Git 백업 완료 후, 반복 자동화 |

```bash
# 기본 모드 — 파일 수정 전 확인
claude
> requirements.txt 업데이트해줘
# AI: "requirements.txt를 수정하려 합니다. 진행할까요? [y/n]"

# 자율 모드 — 확인 없이 실행 (Git 백업 필수)
git add . && git commit -m "backup before agent run"
claude --dangerously-skip-permissions
> requirements.txt 업데이트하고 테스트까지 실행해줘
```

> **WARNING:** `--dangerously-skip-permissions` 모드는 AI가 확인 없이 파일을 삭제하거나 덮어쓸 수 있습니다. 반드시 Git 커밋 후 사용하고, 운영 서버에서는 절대 사용하지 마세요.

---

### 4) OpenAI Codex CLI

#### 개념 및 설치

**Codex CLI**는 OpenAI가 출시한 터미널 기반 에이전트로, GPT-4o 기반으로 동작합니다. Claude Code와 유사하지만 **샌드박스 격리 실행**이 특징입니다. 코드를 실제 시스템이 아닌 격리된 환경에서 실행하므로 안전성이 높습니다.

```bash
# 설치
npm install -g @openai/codex

# API 키 설정
export OPENAI_API_KEY="your-api-key-here"

# 실행
codex

# 또는 단일 명령 실행
codex "budget_parser.py의 병합 셀 처리 버그를 수정해줘"
```

#### Claude Code vs Codex CLI 비교

| 항목 | Claude Code | Codex CLI |
|------|-------------|-----------|
| **기반 모델** | Claude 4 (Sonnet/Opus) | GPT-4o |
| **파일 접근** | 직접 접근 | 샌드박스 격리 |
| **실행 안전성** | 권한 확인 모드 | 샌드박스로 격리 |
| **멀티모달** | 이미지 첨부 가능 | 이미지 첨부 가능 |
| **한국어** | 매우 우수 | 우수 |
| **오픈소스** | 비공개 | 일부 공개 |
| **Git 연동** | 자동 커밋 지원 | 수동 |
| **CLAUDE.md** | 자동 인식 | 별도 설정 필요 |
| **비용** | Claude Pro/API | OpenAI API |
| **추천 상황** | 한국어 프로젝트, 문서 포함 작업 | 보안 중시, GPT 생태계 선호 |

#### Codex CLI 실행 예시

```bash
# 단일 작업 모드
codex "현재 폴더의 Python 파일들을 분석하고
       타입 힌트가 없는 함수를 찾아서 추가해줘"

# 대화 모드
codex
> 테스트 커버리지를 확인해줘
> 커버리지가 낮은 함수를 우선순위로 테스트 코드를 작성해줘
```

---

### 5) 실무 시나리오 — 터미널 에이전트 전체 워크플로

**상황:** 정부 PDF 예산문서 10개를 파싱해서 DB에 저장하는 파이프라인 구축

```bash
# 1. 프로젝트 초기화
mkdir kaib2026-pipeline && cd kaib2026-pipeline
git init

# 2. CLAUDE.md 작성 (4장 SKILL.md 기반)
cat > CLAUDE.md << 'EOF'
# KAIB2026 파이프라인
목적: 과기부 PDF → SQLite DB 자동 저장
언어: Python 3.11
주요 라이브러리: pdfplumber, pandas, sqlalchemy
주석: 한국어 필수
EOF

# 3. Claude Code 실행
claude

# 4. 단계별 지시
> 프로젝트 구조를 설계해줘.
  PDF 파싱 → JSON 정규화 → DB 저장 3단계 파이프라인.
  각 단계를 독립 모듈로 분리하고 폴더 구조를 만들어줘.
  실제 파일은 아직 만들지 말고 구조만.

[검토 후 승인]

> 1단계 모듈(pdf_to_json.py)을 작성해줘.
  입력: /data/*.pdf
  출력: /output/raw/*.json
  pdfplumber 사용, 병합 셀 처리 포함.

[파일 생성 확인 후]

> /data/sample.pdf로 1단계 테스트 실행해줘.
  결과 샘플 3개 보여줘.

[결과 검토 후 2단계 진행]

# 5. 작업 완료 후 커밋
> 오늘 작업 내용 Git 커밋해줘.
  커밋 메시지는 한국어로.
```

---

### 6) 안티 패턴 (Anti-Pattern)

**① Git 없이 에이전트 실행**  
터미널 에이전트는 수십 개 파일을 동시에 수정합니다. Git 없이 실행하면 잘못된 수정을 되돌릴 방법이 없습니다. 에이전트 실행 전 커밋은 필수입니다.

**② CLAUDE.md 없이 대규모 프로젝트 작업**  
CLAUDE.md가 없으면 AI가 프로젝트 규칙을 모르고 일관성 없는 코드를 생성합니다. 프로젝트 시작 시 가장 먼저 만들어야 할 파일입니다.

**③ 운영 DB에 직접 연결된 환경에서 실행**  
개발 환경과 운영 환경을 반드시 분리하세요. 에이전트가 실수로 운영 DB 데이터를 삭제하거나 덮어쓸 수 있습니다.

**④ 너무 긴 단일 지시**  
"처음부터 끝까지 다 만들어줘"는 에이전트가 중간에 방향을 잃을 가능성이 높습니다. 5장의 단계별 위임 패턴을 터미널 에이전트에도 동일하게 적용하세요.

---

### 7) 트러블슈팅 & 주의사항

**Q. Claude Code 설치 후 `claude` 명령어를 찾을 수 없습니다.**
```bash
# npm global 경로 확인
npm config get prefix
# 출력된 경로/bin 을 PATH에 추가

# 예: ~/.bashrc에 추가
export PATH="$HOME/.npm-global/bin:$PATH"
source ~/.bashrc
```

**Q. 에이전트가 계속 같은 오류를 반복합니다.**  
→ "지금까지 시도한 방법과 결과를 요약하고, 다른 접근법을 제안해줘"라고 요청하세요. AI가 같은 방법을 반복하는 루프에서 벗어나게 합니다.

**Q. 작업 중 컨텍스트가 너무 길어져 느려집니다.**  
→ `/clear` 명령으로 컨텍스트를 초기화할 수 있습니다. CLAUDE.md가 있으면 초기화 후에도 프로젝트 맥락은 유지됩니다.

```bash
# Claude Code 내에서
> /clear    # 컨텍스트 초기화
> /help     # 사용 가능한 명령어 목록
> /cost     # 현재까지 사용한 API 비용 확인
```

**Q. Windows에서 사용할 수 있나요?**  
→ WSL2(Windows Subsystem for Linux) 환경을 권장합니다. 네이티브 Windows 터미널도 지원되지만 일부 기능에 제한이 있을 수 있습니다.

> **TIP:** 처음 터미널 에이전트를 사용한다면 **기존 프로젝트가 아닌 새 빈 폴더**에서 시작하세요. "간단한 Python 스크립트 하나를 만들어줘"처럼 작은 작업으로 도구의 동작 방식을 먼저 익힌 뒤 실제 프로젝트에 적용하는 것이 안전합니다.

---

### 8) 한 줄 요약

> 💡 **Key Takeaway:** 터미널 에이전트는 AI가 **직접 파일을 읽고·수정하고·실행하는 레벨 4 에이전트** 도구로, Git 백업과 CLAUDE.md 설정을 갖추면 대규모 프로젝트를 자연어 지시만으로 구축할 수 있습니다.

---

*다음 장: 8장. AI 에디터 — Cursor / Windsurf*