---
created: 2026-05-1
publish: true
tags:
- vibecoding
title: 제22장. 사례 4 n8n 로컬 자동화
type: techbook
---

```toc
minLevel: 1
maxLevel: 1
```
# 제22장. 사례 1 — n8n 로컬 자동화 서버

> *"월 전기세 3,000원짜리 서버가 하루 24시간 일한다."*

---

### 0) 연결 고리 (Bridge)

18장 레시피 4(업무 자동화)의 핵심 인프라 구현 사례입니다. 10장에서 n8n의 개념과 기본 사용법을 배웠습니다. 이 장에서는 N100 미니PC를 실제 24시간 자동화 서버로 구축하고, ICT 공고 모니터링·RSS 요약·보고서 배포까지 운영 중인 실제 워크플로우 시스템 전체를 공개합니다.

---

### 1) 하드웨어 및 구성

#### N100 미니PC 선택 이유

```
[N100 미니PC 스펙과 비용]
CPU: Intel N100 (4코어 3.4GHz, 효율 코어 특화)
RAM: 16GB DDR5
SSD: 512GB NVMe
전력 소비: 유휴 6W / 최대 25W
가격: 약 15~20만 원 (알리익스프레스 기준)
연간 전기세: 약 3만~4만 원

비교:
  AWS t3.small (2vCPU/2GB): 월 약 $18 = 연간 약 27만 원
  N100 미니PC: 연간 전기세 3~4만 원 (7~8배 절감)
```

#### 전체 소프트웨어 스택

```yaml
# docker-compose.yml
version: '3.8'

services:

  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=${N8N_PASSWORD}
      - N8N_HOST=localhost
      - N8N_PROTOCOL=http
      - WEBHOOK_URL=https://n8n.mydomain.com
      - TZ=Asia/Seoul
      - GENERIC_TIMEZONE=Asia/Seoul
    volumes:
      - n8n_data:/home/node/.n8n
      - ./scripts:/home/node/scripts  # Python 스크립트 마운트
    networks:
      - automation

  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    restart: unless-stopped
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    networks:
      - automation

  redis:
    image: redis:alpine
    container_name: redis
    restart: unless-stopped
    volumes:
      - redis_data:/data
    networks:
      - automation

  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: unless-stopped
    ports:
      - "9000:9000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    networks:
      - automation

volumes:
  n8n_data:
  ollama_data:
  redis_data:
  portainer_data:

networks:
  automation:
    driver: bridge
```

#### 서버 초기 설정

```bash
# Ubuntu 22.04 기준

# 1. Docker 설치
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# 2. 환경 변수 파일 생성
cat > .env << 'EOF'
N8N_PASSWORD=강력한비밀번호여기
ANTHROPIC_API_KEY=sk-ant-...
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
NOTION_TOKEN=secret_...
EOF

# 3. 스택 실행
docker-compose up -d

# 4. Ollama 모델 다운로드
docker exec ollama ollama pull qwen2.5:14b
docker exec ollama ollama pull gemma3:12b

# 5. Cloudflare Tunnel 설정 (16장 참조)
cloudflared tunnel create automation-server
cloudflared tunnel route dns automation-server n8n.mydomain.com

# 6. 재부팅 후 자동 시작 확인
sudo systemctl enable docker
```

---

### 2) 운영 중인 워크플로우 목록

```
[자동화 서버에서 실행 중인 워크플로우 현황]

워크플로우 1: ICT 공고 수집·분류 (매일 07:50)
  → 4개 기관 API + RSS 수집
  → Ollama로 중요도 분류
  → Slack + Notion 저장

워크플로우 2: AI 뉴스 요약 (매일 08:30)
  → RSS 5개 피드 수집 (영문)
  → Ollama로 한국어 번역·요약
  → Slack #ai-뉴스 전송

워크플로우 3: 주간 트렌드 리포트 (매주 금요일 17:00)
  → Notion DB에서 주간 데이터 조회
  → Claude API로 트렌드 분석
  → Notion 리포트 페이지 자동 생성
  → Slack #팀-전체 공유

워크플로우 4: PDF 파이프라인 트리거 (파일 감지)
  → /data/incoming/ 폴더 새 PDF 감지
  → 19장 파이프라인 자동 실행
  → 완료 시 Slack 알림

워크플로우 5: 오류 감시 (상시)
  → 위 워크플로우 실패 시 자동 실행
  → Slack #시스템-알림 긴급 전송

워크플로우 6: 시스템 헬스체크 (매일 06:00)
  → Docker 컨테이너 상태 확인
  → 디스크 사용량 체크
  → 이상 시 Slack 알림
```

---

### 3) 핵심 워크플로우 — ICT 공고 수집 상세

18장에서 설계한 워크플로우의 실제 n8n 설정값을 공개합니다.

#### 노드별 설정

```
[노드 1] Schedule Trigger
  Rule: 0 50 7 * * 1-5   (평일 07:50)

[노드 2~5] HTTP Request × 4 (병렬 실행)

  노드 2 — NIPA 공고:
    Method: GET
    URL: https://www.nipa.kr/api/v1/notice
    Query Parameters:
      category: ai
      size: 20
      sort: createdAt,desc
    Headers:
      Accept: application/json

  노드 3 — NIA 공고:
    Method: GET
    URL: https://www.nia.or.kr/site/nia_kor/ex/bbs/List.do
    (HTML 스크래핑 방식 — CSS Selector 파싱)

  노드 4 — IITP RSS:
    URL: https://www.iitp.kr/kr/1/notice/list.xml
    (RSS Feed 노드 사용)

  노드 5 — MSIT 공고:
    URL: https://www.msit.go.kr/bbs/rss.do?bbsSeqNo=74

[노드 6] Merge
  Mode: Append All Inputs
  (4개 소스 데이터 통합)

[노드 7] Code (중복 제거 + SQLite 조회)
  Language: JavaScript
  Code:
    const Database = require('better-sqlite3');
    const db = new Database('/home/node/scripts/notices.db');

    // 이미 처리한 URL 목록 조회
    const processed = db.prepare(
      'SELECT url FROM processed_notices'
    ).all().map(r => r.url);
    const processedSet = new Set(processed);

    // 신규 항목만 필터
    return $input.all().filter(item =>
      item.json.url && !processedSet.has(item.json.url)
    );

[노드 8] AI Agent (Ollama)
  Model: qwen2.5:14b
  Base URL: http://ollama:11434/v1
  System Message:
    "당신은 ICT 정책 전문가입니다.
     각 공고를 분석해서 반드시 다음 JSON 형식으로만 응답하세요:
     {
       'title': '공고명',
       'org': '기관명',
       'summary': '핵심 내용 2줄 이내',
       'importance': '상/중/하',
       'deadline': 'YYYY-MM-DD (없으면 null)',
       'tags': ['태그1', '태그2'],
       'reason': '중요도 판단 이유 1줄'
     }"
  Human Message: "{{$json.raw_content}}"

[노드 9] Code (JSON 파싱)
  Code:
    try {
      const parsed = JSON.parse($input.item.json.text);
      return { json: { ...parsed, url: $input.item.json.url } };
    } catch {
      return { json: { importance: '하', title: '파싱 실패' } };
    }

[노드 10] IF
  Condition: {{$json.importance}} equals "상"

[노드 11a] Slack (중요도 '상')
  Webhook URL: {{$env.SLACK_WEBHOOK_URL}}
  Message (Blocks):
    [
      {
        "type": "header",
        "text": {"type": "plain_text", "text": "📢 중요 공고 알림"}
      },
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "*{{$json.title}}*\n{{$json.summary}}"
        }
      },
      {
        "type": "section",
        "fields": [
          {"type": "mrkdwn", "text": "*기관:* {{$json.org}}"},
          {"type": "mrkdwn", "text": "*마감:* {{$json.deadline}}"},
          {"type": "mrkdwn", "text": "*중요도:* {{$json.importance}}"}
        ]
      },
      {
        "type": "actions",
        "elements": [{
          "type": "button",
          "text": {"type": "plain_text", "text": "원문 보기"},
          "url": "{{$json.url}}"
        }]
      }
    ]

[노드 11b] Notion (전체 저장)
  Database ID: {{$env.NOTION_NOTICES_DB}}
  Properties:
    공고명 (title): {{$json.title}}
    기관 (text): {{$json.org}}
    요약 (text): {{$json.summary}}
    중요도 (select): {{$json.importance}}
    마감일 (date): {{$json.deadline}}
    URL (url): {{$json.url}}
    태그 (multi-select): {{$json.tags}}
    수집일 (date): {{new Date().toISOString().split('T')[0]}}

[노드 12] Code (SQLite 이력 저장)
  Code:
    const Database = require('better-sqlite3');
    const db = new Database('/home/node/scripts/notices.db');
    db.prepare(
      'INSERT OR IGNORE INTO processed_notices (url, processed_at) VALUES (?, ?)'
    ).run($json.url, new Date().toISOString());
    return $input.item;
```

---

### 4) AI 뉴스 요약 워크플로우

```
[워크플로우 2 — AI 뉴스 요약 (08:30)]

소스 RSS 피드:
  - https://feeds.feedburner.com/oreilly/radar
  - https://ai.googleblog.com/feeds/posts/default
  - https://openai.com/blog/rss
  - https://www.anthropic.com/rss.xml
  - https://huggingface.co/blog/feed.xml

처리 흐름:
  RSS 수집 → 24시간 내 새 항목 필터
  → Ollama (gemma3:12b)로 한국어 번역·3줄 요약
  → 중요도 점수 (1~5)
  → 점수 4 이상만 Slack 전송

Slack 메시지 형식:
  🤖 *오늘의 AI 뉴스* ({{날짜}})

  1. [OpenAI] GPT-5 출시 발표 ⭐⭐⭐⭐⭐
     → 멀티모달 강화, 추론 속도 2배 향상
     → 한국어 지원 대폭 개선
     [원문 읽기]

  2. [Anthropic] Claude 코드 생성 벤치마크 1위
     → HumanEval 97.2% 달성
     [원문 읽기]
```

---

### 5) 시스템 헬스체크 워크플로우

```python
# scripts/health_check.py
# n8n Code 노드에서 실행하는 헬스체크 스크립트

import subprocess
import shutil
import json


def check_system_health() -> dict:
    """시스템 상태를 점검하고 결과를 반환한다."""
    health = {
        "status": "정상",
        "warnings": [],
        "containers": {},
        "disk": {},
    }

    # Docker 컨테이너 상태 확인
    result = subprocess.run(
        ["docker", "ps", "--format", "{{.Names}}\t{{.Status}}"],
        capture_output=True, text=True
    )
    for line in result.stdout.strip().split('\n'):
        if '\t' in line:
            name, status = line.split('\t', 1)
            health["containers"][name] = status
            if "Up" not in status:
                health["warnings"].append(f"컨테이너 다운: {name}")

    # 디스크 사용량 확인
    total, used, free = shutil.disk_usage("/")
    used_pct = used / total * 100
    health["disk"] = {
        "used_gb": round(used / (1024**3), 1),
        "free_gb": round(free / (1024**3), 1),
        "used_pct": round(used_pct, 1),
    }
    if used_pct > 85:
        health["warnings"].append(f"디스크 {used_pct:.0f}% 사용 중")

    if health["warnings"]:
        health["status"] = "경고"

    return health
```

---

### 6) 오류 처리 워크플로우

```
[오류 감시 워크플로우 — 모든 워크플로우에 연결]

설정 방법:
  각 워크플로우 Settings → Error Workflow → "오류 감시" 선택

오류 감시 워크플로우 내용:

노드 1: Error Trigger (자동 실행됨)
  → 실패한 워크플로우 정보 자동 수신

노드 2: Code (오류 메시지 포맷)
  const wf_name = $input.item.json.workflow.name;
  const node_name = $input.item.json.execution.lastNodeExecuted;
  const error_msg = $input.item.json.execution.error?.message;
  const exec_id = $input.item.json.execution.id;

  return {
    json: {
      message: `❌ 워크플로우 실패\n` +
               `워크플로우: ${wf_name}\n` +
               `실패 노드: ${node_name}\n` +
               `오류: ${error_msg}\n` +
               `실행 ID: ${exec_id}`,
      severity: "error"
    }
  };

노드 3: Slack (#시스템-알림)
  Channel: #시스템-알림
  Message: {{$json.message}}

노드 4: Notion (오류 로그 DB)
  Properties:
    제목: {{wf_name}} 실패
    발생일시: {{NOW}}
    오류 내용: {{error_msg}}
    상태: 확인 필요
```

---

### 7) 유지보수 — 주간 운영 루틴

```
[매주 월요일 오전 — 10분]

1. Portainer 접속 (Tailscale → http://100.x.x.x:9000)
   → 컨테이너 전체 정상 여부 확인
   → 로그에 반복 오류 없는지 확인

2. n8n 실행 이력 확인
   → 지난 주 실행 실패 건수 확인
   → 실패 패턴 분석 (API 변경, Rate Limit 등)

3. 디스크 사용량 확인
   → 처리 완료 PDF를 /data/archive/로 이동
   → 오래된 raw JSON 정리

[분기별 — 30분]

1. Ollama 모델 업데이트
   docker exec ollama ollama pull qwen2.5:14b

2. n8n 버전 업데이트
   docker-compose pull n8n
   docker-compose up -d n8n

3. 워크플로우 JSON 백업
   n8n 대시보드 → 전체 워크플로우 Export
   → GitHub에 백업
```

---

### 8) 최종 성과

```
[운영 3개월 실적 기준]

처리량:
  총 실행 횟수: 약 2,400회
  처리 공고 건수: 약 3,800건
  AI 뉴스 요약: 약 480건
  오류 발생률: 1.2% (API 변경·네트워크 장애)

시간 절감:
  공고 확인 시간: 일 30분 → 0분 (Slack 수신)
  뉴스 모니터링: 일 20분 → 0분
  보고서 준비: 주 2시간 → 30분

운영 비용:
  N100 미니PC 구매: 17만 원 (일회성)
  월 전기세: 약 3,200원
  Claude API: 약 월 8,000원 (주간 리포트 전용)
  n8n 셀프호스팅: 0원
  합계: 약 월 12,000원

클라우드 대비 절감:
  동급 클라우드 서비스 (n8n Cloud Pro): 월 약 50달러 = 약 70,000원
  → 월 약 58,000원 절감 (연간 약 70만 원)
```

---

### 9) 한 줄 요약

> 💡 **Key Takeaway:** N100 미니PC + Docker + n8n + Ollama 조합으로 **월 1만 원대 비용으로 클라우드급 24시간 자동화 서버**를 구축할 수 있으며, 핵심은 오류 감시 워크플로우와 정기 헬스체크로 무인 운영 안정성을 확보하는 것입니다.

---

*다음 장: 23장. 사례 5 — 개인금융 데이터 파이프라인 + Streamlit*