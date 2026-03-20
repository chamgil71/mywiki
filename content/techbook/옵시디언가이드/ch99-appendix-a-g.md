---
created:
  '{ date }': null
publish: true
status: 진행중
tags: []
title: ch99-appendix-a-g
type: techbook
---

# 부록 A. 필수 단축키 완전 레퍼런스

| 기능 | Windows/Linux | Mac |
|---|---|---|
| **탐색** | | |
| 퀵 스위처 (파일 열기) | Ctrl+O | Cmd+O |
| 명령 팔레트 | Ctrl+P | Cmd+P |
| 전체 검색 | Ctrl+Shift+F | Cmd+Shift+F |
| 그래프 뷰 | Ctrl+G | Cmd+G |
| 뒤로 | Alt+← | Cmd+Alt+← |
| 앞으로 | Alt+→ | Cmd+Alt+→ |
| **편집** | | |
| 새 노트 | Ctrl+N | Cmd+N |
| 저장 | Ctrl+S | Cmd+S |
| 굵게 | Ctrl+B | Cmd+B |
| 기울임 | Ctrl+I | Cmd+I |
| 내부 링크 | Ctrl+K | Cmd+K |
| 실행 취소 | Ctrl+Z | Cmd+Z |
| 재실행 | Ctrl+Y | Cmd+Shift+Z |
| **뷰** | | |
| 편집/미리보기 전환 | Ctrl+E | Cmd+E |
| 좌측 사이드바 | Ctrl+\ | Cmd+\ |
| 우측 사이드바 | Ctrl+Shift+\ | Cmd+Shift+\ |
| 탭 닫기 | Ctrl+W | Cmd+W |
| 분할 화면 | Ctrl+Shift+V | Cmd+Shift+V |
| **Templater** | | |
| 템플릿 삽입 | Alt+E | Option+E |
| 현재 파일에 실행 | Alt+R | Option+R |

---

# 부록 B. 추천 플러그인 50선

## 필수 (Must Have) — 10종
| 플러그인 | 용도 | 다운로드 |
|---|---|---|
| Templater | 고급 템플릿 자동화 | 400만+ |
| Dataview | SQL 스타일 쿼리 대시보드 | 700만+ |
| Advanced Tables | 표 편집 자동화 | 200만+ |
| Calendar | 데일리 노트 달력 탐색 | 200만+ |
| Obsidian Git | Git 자동 백업 | 100만+ |
| Excalidraw | 손 그림 다이어그램 | 200만+ |
| Linter | 노트 품질 자동 관리 | 80만+ |
| QuickAdd | 빠른 노트 캡처 자동화 | 150만+ |
| Tasks | 할일 고급 관리 | 200만+ |
| Kanban | 칸반 보드 | 100만+ |

## 생산성 향상 — 15종
| 플러그인 | 용도 |
|---|---|
| Various Complements | 자동완성 (단어·링크) |
| Smart Connections | AI 기반 연관 노트 추천 |
| Periodic Notes | 주간·월간·연간 노트 |
| Natural Language Dates | 자연어로 날짜 입력 |
| Breadcrumbs | 노트 계층 탐색 |
| Graph Analysis | 그래프 심화 분석 |
| Timelines | 노트를 타임라인으로 시각화 |
| Checklist | 체크박스 고급 관리 |
| Reminder | 노트 기반 리마인더 |
| Spaced Repetition | 플래시카드 복습 |
| Longform | 장편 글쓰기 도구 |
| Typewriter Scroll | 타이프라이터 스크롤 효과 |
| Sliding Panes | 슬라이딩 패널 뷰 |
| Commander | 리본·메뉴 커스터마이즈 |
| Hover Editor | 호버 팝업 편집 |

## 시각화 — 10종
| 플러그인 | 용도 |
|---|---|
| Charts | Dataview 기반 차트 생성 |
| Mermaid Tools | Mermaid 다이어그램 도우미 |
| Draw.io | draw.io 다이어그램 |
| Obsidian Map View | 지도 기반 노트 시각화 |
| File Tree Alternative | 파일 트리 대체 뷰 |
| Customizable Sidebar | 사이드바 커스터마이즈 |
| Minimal Theme Settings | Minimal 테마 세부 설정 |
| Style Settings | 테마 변수 GUI 편집 |
| Icon Folder | 폴더·파일 아이콘 설정 |
| Banners | 노트 상단 배너 이미지 |

## 연구·학술 — 10종
| 플러그인 | 용도 |
|---|---|
| Zotero Integration | Zotero 문헌 관리 연동 |
| Citations | BibTeX 인용 |
| PDF++ | PDF 주석·하이라이트 |
| Readwise Official | Readwise 독서 하이라이트 동기화 |
| Annotator | 웹 페이지 주석 |
| Extract Highlights | PDF 하이라이트 추출 |
| Note Refactor | 노트 분할·재구성 |
| Local REST API | 외부 앱과 연동 API |
| Shell Commands | 터미널 명령어 실행 |
| BRAT | 베타 플러그인 설치 도구 |

## 외관·UX — 5종
| 플러그인 | 용도 |
|---|---|
| Hider | UI 요소 선택적 숨기기 |
| Focus Mode | 집중 모드 (방해 요소 제거) |
| Zen | 글쓰기 집중 모드 |
| Cursor Position | 커서 위치 상태 표시줄 |
| Status Bar Organizer | 상태 표시줄 정리 |

---

# 부록 C. CSS 스니펫 모음집

## C-1. 전체 폰트 설정 (Google Fonts Noto Sans KR)
```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
body {
  --font-text-theme: "Noto Sans KR", sans-serif;
  --font-interface-theme: "Noto Sans KR", sans-serif;
}
code, pre { font-family: "JetBrains Mono", monospace !important; }
```

## C-2. 노트 최대 너비
```css
.markdown-preview-view,
.markdown-source-view.mod-cm6 .cm-content {
  max-width: 800px !important;
  margin: 0 auto;
}
```

## C-3. 헤딩 스타일
```css
.markdown-rendered h1 { color: #7C3AED; border-bottom: 2px solid #7C3AED; padding-bottom: 4px; }
.markdown-rendered h2 { color: #0284C7; border-left: 4px solid #0284C7; padding-left: 12px; }
.markdown-rendered h3 { color: #059669; }
.cm-header-1 { color: #7C3AED !important; }
.cm-header-2 { color: #0284C7 !important; }
.cm-header-3 { color: #059669 !important; }
```

## C-4. 표 스타일
```css
.markdown-rendered table { border-collapse: collapse; width: 100%; font-size: 0.9em; }
.markdown-rendered th { background-color: var(--interactive-accent); color: white; padding: 8px 12px; }
.markdown-rendered td { padding: 6px 12px; border-bottom: 1px solid var(--background-modifier-border); }
.markdown-rendered tr:nth-child(even) td { background-color: var(--background-secondary); }
```

## C-5. 가독성 개선
```css
.markdown-rendered { line-height: 1.8; letter-spacing: 0.01em; word-break: keep-all; }
.markdown-rendered h1, .markdown-rendered h2, .markdown-rendered h3 { line-height: 1.3; }
```

## C-6. 이미지 스타일
```css
.markdown-rendered img { display: block; margin: 16px auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }
.markdown-rendered img + em { display: block; text-align: center; font-size: 0.85em; color: var(--text-muted); margin-top: -8px; }
```

## C-7. PARA 폴더 아이콘
```css
.nav-folder-title[data-path="10-PROJECTS"] .nav-folder-title-content::before { content: "📋 "; }
.nav-folder-title[data-path="20-AREAS"] .nav-folder-title-content::before { content: "🏠 "; }
.nav-folder-title[data-path="30-RESOURCES"] .nav-folder-title-content::before { content: "📚 "; }
.nav-folder-title[data-path="90-ARCHIVES"] .nav-folder-title-content::before { content: "🗄️ "; }
.nav-folder-title[data-path="00-INBOX"] .nav-folder-title-content::before { content: "📥 "; }
```

---

# 부록 D. Dataview 쿼리 레퍼런스

## 기본 쿼리 유형
```
LIST   → 노트 목록
TABLE  → 표 형식
TASK   → 체크박스 할일
CALENDAR → 달력 형식
```

## 자주 쓰는 쿼리 패턴

### 최근 수정 노트
```dataview
TABLE file.mtime AS "수정일"
FROM ""
SORT file.mtime DESC
LIMIT 10
```

### 태그별 목록
```dataview
LIST
FROM #독서노트
SORT file.name ASC
```

### 미완료 할일
```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
```

### 속성 필터 (status)
```dataview
TABLE status, due_date AS "마감"
FROM "10-PROJECTS"
WHERE status = "진행중"
SORT due_date ASC
```

### 날짜 범위 필터
```dataview
TABLE file.ctime AS "생성일"
FROM ""
WHERE file.ctime >= date(2024-01-01) AND file.ctime < date(2024-02-01)
SORT file.ctime DESC
```

### 평균·합계 (숫자 속성)
```dataview
TABLE rating, pages
FROM #독서노트
WHERE status = "완료"
SORT rating DESC
```

### 인라인 쿼리
```
오늘 날짜: `= date(today)`
이번 주: `= date(today).weekyear`
파일 수: `= length(filter(dv.pages(), (p) => p.file.path))`
```

---

# 부록 E. Templater 문법 레퍼런스

## 날짜·시간
```javascript
<% tp.date.now("YYYY-MM-DD") %>          // 2024-01-15
<% tp.date.now("YYYY년 MM월 DD일") %>    // 2024년 01월 15일
<% tp.date.now("HH:mm") %>              // 09:30
<% tp.date.now("dddd", 0, "ko") %>      // 월요일
<% tp.date.now("YYYY-MM-DD", -1) %>     // 어제
<% tp.date.now("YYYY-MM-DD", 1) %>      // 내일
<% tp.date.now("YYYY-[W]ww") %>         // 2024-W03
```

## 파일 정보
```javascript
<% tp.file.title %>                      // 파일명 (확장자 제외)
<% tp.file.folder() %>                   // 현재 폴더 경로
<% tp.file.creation_date("YYYY-MM-DD") %> // 생성일
```

## 사용자 입력
```javascript
<% await tp.system.prompt("제목:") %>                     // 텍스트 입력
<% await tp.system.prompt("우선순위:", "2") %>            // 기본값 있는 입력
<% await tp.system.suggester(["A", "B"], ["a", "b"]) %>  // 선택 드롭다운
```

## JavaScript 블록
```javascript
<%*
// 조건문
if (condition) { tR += "텍스트"; }

// 반복문
for (let i = 0; i < 3; i++) { tR += `항목 ${i}\n`; }

// 날짜 계산
const days = ["일","월","화","수","목","금","토"];
tR += days[parseInt(tp.date.now("d"))];
%>
```

---

# 부록 F. YAML 속성 표준 템플릿 모음

## 기본 노트
```yaml
---
tags: []
date: {{date:YYYY-MM-DD}}
status: inbox
---
```

## 독서 노트 (20종)
```yaml
---
title: ""
author: ""
translator: ""
publisher: ""
published: 
status: "읽는중"
started: 
finished: 
pages: 
progress: 0
rating: 
difficulty: 
recommend: 
tags: [독서노트]
genre: ""
language: "한국어"
related: []
source: ""
---
```

## 프로젝트 노트
```yaml
---
type: project
title: ""
area: ""
status: "기획"
priority: 2
start_date: 
due_date: 
owner: ""
tags: [project]
progress: 0
---
```

## 회의록
```yaml
---
tags: [회의록]
date: 
project: ""
meeting_type: ""
status: "완료"
---
```

## 데일리 노트
```yaml
---
tags: [데일리노트]
date: 
week: 
---
```

---

# 부록 G. 트러블슈팅 완전 가이드

## G-1. 동기화 문제

**증상:** 모바일에서 최신 노트가 보이지 않음
```
해결 순서:
1. 인터넷 연결 확인
2. 동기화 앱(iCloud/Dropsync) 상태 확인
3. 강제 동기화 실행
4. 옵시디언 앱 재시작
5. iCloud의 경우: 설정 → Apple ID → iCloud → iCloud Drive → 이 기기에서 내려받기
```

**증상:** 충돌 파일이 생성됨
```
해결:
1. 두 충돌 파일 내용 비교
2. 최신·완전한 버전으로 내용 합치기
3. 충돌 복사본 삭제
4. 예방: 기기 전환 전 동기화 완료 확인
```

## G-2. 플러그인 오류

**증상:** 특정 플러그인이 오류를 발생시킴
```
진단:
1. 모든 플러그인 비활성화
2. 오류가 사라지면 → 플러그인 하나씩 활성화하며 원인 찾기
3. 원인 플러그인 발견 → GitHub Issues 확인
4. 업데이트 또는 대안 플러그인 찾기
```

## G-3. 성능 문제

**증상:** 보관소 로딩이 느림
```
원인 & 해결:
- 보관소 내 파일 수 과다 → Archives로 이동
- 대용량 첨부 파일 → 외부 저장소 이용
- 무거운 플러그인 → 미사용 플러그인 비활성화
- Dataview 실시간 인덱싱 → Dataview 캐시 설정 조정
```

## G-4. YAML 오류

**증상:** "Invalid YAML" 또는 속성이 인식되지 않음
```
흔한 원인:
- 콜론(:) 뒤 공백 없음 → "title:텍스트" → "title: 텍스트"
- 탭 들여쓰기 사용 → 공백 2칸으로 변경
- 값에 콜론 포함 → 따옴표로 감싸기 "제목: 부제"
- 날짜 형식 오류 → YYYY-MM-DD 형식 사용
```

## G-5. Dataview 쿼리 문제

**증상:** 쿼리 결과가 비어있음
```
확인 순서:
1. FROM 조건의 태그/폴더 이름 정확히 일치하는지 확인
   태그: #태그명 (# 포함), 폴더: "폴더명" (따옴표 포함)
2. WHERE 조건의 속성명이 실제 YAML 속성명과 동일한지 확인
3. Dataview 설정 → 인덱싱 갱신 실행
4. 인라인 DV 활성화 확인
```

**증상:** TABLE 쿼리에서 빈 셀이 있음
```
해결: 해당 속성이 일부 노트에만 있거나 이름이 다른 경우
WHERE 조건으로 해당 속성이 있는 노트만 필터:
  WHERE rating != null
  WHERE status != ""
```

---

*부록 끝 | 옵시디언 완전 정복 — 두 번째 뇌 만들기*