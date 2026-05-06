---
created: 2026-05-1
publish: true
tags:
- vibecoding
title: 제15장. DB·백엔드
type: techbook
---

```toc
minLevel: 1
maxLevel: 1
```
# 제15장. DB·백엔드 — Supabase

> *"데이터베이스를 설치하고 서버를 구성하는 시대는 끝났다. Supabase는 백엔드 전체를 5분 안에 준비한다."*

---

### 0) 연결 고리 (Bridge)

14장에서 Vercel로 프론트엔드를 배포하는 방법을 배웠습니다. 그런데 대부분의 앱은 데이터를 저장하고 불러오는 **백엔드**가 필요합니다. 로그인한 사용자, 제출된 양식 데이터, 누적된 공고 이력 — 이것들을 어디에 저장할까요? 15장에서 다루는 **Supabase**는 PostgreSQL 데이터베이스, 인증, 파일 저장, 실시간 구독을 모두 제공하는 오픈소스 백엔드 플랫폼입니다.

---

### 1) 개념 정의 및 필요성

#### Supabase란?

**Supabase**는 "오픈소스 Firebase 대안"을 표방하는 백엔드 플랫폼으로, PostgreSQL을 기반으로 앱 개발에 필요한 백엔드 인프라를 제공합니다.

**웹:** supabase.com  
**무료 플랜:** 프로젝트 2개, 500MB DB, 1GB 파일 저장  
**오픈소스:** 셀프 호스팅 가능  
**Lovable 연동:** 네이티브 통합 (9장 참조)

#### Supabase가 제공하는 것

```
Supabase = 다음 5가지의 통합 플랫폼

① Database    → PostgreSQL (관계형 DB)
② Auth        → 이메일/OAuth/SMS 인증
③ Storage     → 파일·이미지 저장
④ Realtime    → 실시간 데이터 구독 (WebSocket)
⑤ Edge Functions → 서버리스 함수 (Deno 기반)
```

```
비유:
기존 방식:
  PostgreSQL 서버 설치 → pgAdmin 설정 → 인증 서버 구축
  → 파일 서버 설정 → API 서버 개발 → 수 주 소요

Supabase:
  프로젝트 생성 → 5분 안에 위 모두 사용 가능
```

---

### 2) Supabase 시작하기

#### 프로젝트 생성

```
1. supabase.com → "Start your project" → GitHub로 로그인
2. "New Project" → 조직 선택 → 프로젝트 이름 입력
3. DB 비밀번호 설정 → 리전 선택 (Northeast Asia - 서울 권장)
4. "Create new project" → 약 2분 대기
```

#### 핵심 정보 확인

```
프로젝트 생성 후 Settings → API에서 확인:

Project URL: https://abcdefgh.supabase.co
anon (public) key: eyJhbGc...  ← 클라이언트에서 사용
service_role key: eyJhbGc...  ← 서버에서만 사용 (절대 노출 금지)
```

---

### 3) Database — 테이블 설계와 SQL

#### Table Editor로 테이블 생성

```sql
-- Supabase SQL Editor에서 실행
-- 공고 아카이브 테이블 생성

CREATE TABLE notices (
    id          UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    title       TEXT NOT NULL,
    organization TEXT,
    summary     TEXT,
    importance  TEXT CHECK (importance IN ('상', '중', '하')),
    deadline    DATE,
    url         TEXT,
    source      TEXT,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    processed   BOOLEAN DEFAULT FALSE
);

-- 인덱스 추가 (검색 성능)
CREATE INDEX idx_notices_importance ON notices(importance);
CREATE INDEX idx_notices_deadline ON notices(deadline);
CREATE INDEX idx_notices_created_at ON notices(created_at DESC);
```

> **TIP:** Supabase Table Editor의 UI로도 테이블을 만들 수 있지만, SQL로 작성해두면 Claude에게 "이 SQL을 보고 관련 기능을 구현해줘"라고 요청하기 훨씬 쉽습니다. 스키마 SQL을 SKILL.md에 포함시키는 것을 권장합니다.

#### Claude와 함께 스키마 설계

```
[Claude.ai에서]
"다음 요구사항을 위한 Supabase PostgreSQL 스키마를 설계해줘:

요구사항:
- 직원 정보 관리 (이름, 부서, 직급, 입사일)
- 연차 신청 (신청자, 기간, 사유, 승인 상태)
- 관리자 승인/거절 이력 관리

조건:
- UUID 기본키 사용
- created_at, updated_at 자동 관리
- Row Level Security 적용 고려"

→ Claude가 CREATE TABLE SQL + RLS 정책 전체를 생성
```

---

### 4) Auth — 인증 시스템

Supabase Auth는 별도 구현 없이 이메일/비밀번호, Google, GitHub 등 다양한 인증 방식을 즉시 제공합니다.

#### 클라이언트 설정

```javascript
// supabase.js
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseKey)
```

#### 이메일 로그인 구현

```javascript
// 회원가입
const { data, error } = await supabase.auth.signUp({
    email: 'user@example.com',
    password: 'password123'
})

// 로그인
const { data, error } = await supabase.auth.signInWithPassword({
    email: 'user@example.com',
    password: 'password123'
})

// 로그아웃
await supabase.auth.signOut()

// 현재 사용자 확인
const { data: { user } } = await supabase.auth.getUser()
```

---

### 5) Row Level Security (RLS) — 데이터 접근 제어

**RLS(Row Level Security)**는 Supabase의 핵심 보안 기능입니다. "로그인한 사용자는 자신의 데이터만 볼 수 있다"처럼 DB 수준에서 접근 권한을 제어합니다.

```sql
-- RLS 활성화
ALTER TABLE notices ENABLE ROW LEVEL SECURITY;

-- 정책 1: 모든 인증 사용자가 공고를 조회할 수 있음
CREATE POLICY "공고 조회는 인증 사용자만"
ON notices FOR SELECT
TO authenticated
USING (true);

-- 정책 2: 서비스 롤(백엔드)만 삽입 가능
CREATE POLICY "공고 삽입은 서비스 롤만"
ON notices FOR INSERT
TO service_role
WITH CHECK (true);
```

```
RLS가 없을 경우:
  anon key로 notices 테이블 전체 조회 가능
  → 외부에서 데이터 무단 접근 가능

RLS 적용 후:
  비로그인 사용자 → 데이터 접근 불가
  로그인 사용자 → 허용된 데이터만 접근
  서비스 롤 → 모든 작업 가능 (백엔드 전용)
```

> **WARNING:** Lovable이 자동 생성한 RLS 정책은 반드시 직접 검토하세요. 너무 허용적이거나(모든 사람이 모든 데이터 접근) 너무 제한적인(아무도 접근 불가) 경우가 있습니다.

---

### 6) 데이터 CRUD — 자바스크립트 클라이언트

```javascript
// ━━━ 조회 (SELECT) ━━━
const { data, error } = await supabase
    .from('notices')
    .select('*')
    .eq('importance', '상')
    .order('deadline', { ascending: true })
    .limit(10)

// ━━━ 삽입 (INSERT) ━━━
const { data, error } = await supabase
    .from('notices')
    .insert({
        title: '2026년 AI 바우처 지원사업 공고',
        organization: 'NIPA',
        importance: '상',
        deadline: '2026-06-30'
    })

// ━━━ 수정 (UPDATE) ━━━
const { data, error } = await supabase
    .from('notices')
    .update({ processed: true })
    .eq('id', noticeId)

// ━━━ 삭제 (DELETE) ━━━
const { data, error } = await supabase
    .from('notices')
    .delete()
    .eq('id', noticeId)
```

---

### 7) Realtime — 실시간 데이터 구독

Supabase Realtime은 DB 변경사항을 실시간으로 클라이언트에 푸시합니다. 새로고침 없이 데이터가 자동 업데이트되는 기능을 구현할 수 있습니다.

```javascript
// 공고 테이블에 새 행이 삽입될 때마다 실시간 수신
const channel = supabase
    .channel('notices-changes')
    .on(
        'postgres_changes',
        { event: 'INSERT', schema: 'public', table: 'notices' },
        (payload) => {
            console.log('새 공고 추가됨:', payload.new)
            // UI 자동 업데이트
            setNotices(prev => [payload.new, ...prev])
        }
    )
    .subscribe()

// 구독 해제
supabase.removeChannel(channel)
```

---

### 8) n8n + Supabase — 자동화 파이프라인 종착점

10장의 n8n 자동화 파이프라인에서 Supabase를 데이터 저장소로 연결합니다.

```
[n8n 워크플로우]

공고 수집 → AI 분류 → Supabase 저장

n8n Supabase 노드 설정:
  Operation: Insert Row
  Table: notices
  Fields:
    title       → {{$json.title}}
    organization → {{$json.org}}
    summary     → {{$json.ai_summary}}
    importance  → {{$json.importance}}
    deadline    → {{$json.deadline}}
    url         → {{$json.url}}

결과:
→ 매일 자동으로 Supabase에 공고 적재
→ Vercel 앱에서 실시간 조회 가능
→ Supabase 대시보드에서 직접 데이터 확인·수정
```

---

### 9) Storage — 파일 저장

```javascript
// 파일 업로드 (PDF, 이미지 등)
const { data, error } = await supabase.storage
    .from('documents')         // 버킷 이름
    .upload(
        `reports/${fileName}`, // 저장 경로
        fileObject,            // File 객체
        { contentType: 'application/pdf' }
    )

// 공개 URL 생성
const { data } = supabase.storage
    .from('documents')
    .getPublicUrl(`reports/${fileName}`)

console.log(data.publicUrl) // https://xxx.supabase.co/storage/v1/object/...
```

---

### 10) 실무 시나리오 — AI 공고 관리 시스템 전체 스택

```
[완전한 풀스택 구성]

데이터 흐름:
  공공데이터 API
    ↓ (n8n 수집)
  Claude AI 분류·요약
    ↓ (n8n Supabase 노드)
  Supabase PostgreSQL DB
    ↓ (Supabase JS Client)
  Vercel (Next.js 앱)
    ↓
  사용자 브라우저

기술 스택:
  수집·자동화: n8n + Ollama
  DB·인증: Supabase
  프론트엔드: Next.js (또는 Lovable 생성)
  배포: Vercel
  알림: Slack (n8n 연동)
  지식 관리: Obsidian

총 비용 (월):
  n8n 셀프호스팅 (N100 미니PC): 전기세 ~3,000원
  Supabase 무료 플랜: 0원
  Vercel 무료 플랜: 0원
  합계: ~3,000원/월
```

---

### 11) 안티 패턴 (Anti-Pattern)

**① service_role 키를 클라이언트 코드에 사용**
service_role 키는 RLS를 무시하고 모든 데이터에 접근합니다. 절대로 브라우저에 노출되면 안 됩니다. 서버 측 코드(Vercel Functions, n8n)에서만 사용하세요.

**② RLS 없이 anon 키로 운영**
RLS를 설정하지 않으면 anon 키만 알면 누구나 전체 데이터를 조회·수정할 수 있습니다. 프로덕션 배포 전 반드시 RLS를 설정하세요.

**③ 무료 플랜 DB를 운영 데이터 저장소로 사용**
Supabase 무료 플랜은 7일 이상 접속이 없으면 프로젝트가 일시 중지됩니다. 실제 팀이 사용하는 데이터는 유료 플랜을 사용하세요.

---

### 12) 트러블슈팅 & 주의사항

**Q. 데이터 삽입 시 RLS 오류가 납니다.**
```
새 row violates row-level security policy
→ 현재 사용자(또는 anon)에게 INSERT 권한이 없음
→ Supabase 대시보드 → Authentication → Policies에서 정책 확인
→ 또는 service_role 키를 사용하는 서버 측 코드로 이전
```

**Q. Realtime이 작동하지 않습니다.**
→ Supabase 대시보드 → Database → Replication에서 해당 테이블의 Realtime이 활성화되어 있는지 확인하세요.

**Q. 무료 플랜에서 프로젝트가 일시 중지됐습니다.**
→ Supabase 대시보드에서 "Restore project"를 클릭하면 재활성화됩니다. n8n의 스케줄 워크플로우를 주 1회 이상 실행하면 자동으로 활성 상태를 유지할 수 있습니다.

> **TIP:** Claude에게 Supabase 스키마 SQL을 보여주고 "이 스키마에 맞는 TypeScript 타입을 생성해줘" 또는 "이 테이블을 조회하는 React 훅을 만들어줘"라고 요청하면, 스키마 기반의 타입-안전한 코드를 즉시 얻을 수 있습니다.

---

### 13) 한 줄 요약

> 💡 **Key Takeaway:** Supabase는 PostgreSQL DB·인증·파일·실시간 기능을 하나의 플랫폼에서 제공하여, AI로 만든 앱에 **완전한 백엔드를 5분 안에 연결**할 수 있게 해주는 핵심 인프라입니다.

---

*다음 장: 16장. 네트워크·접근 — Cloudflare Tunnel / Tailscale / Portainer*