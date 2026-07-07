---
created: 2026-07-01
name: AIissue_202606
publish: true
source: claude
tags:
- AI
- AI이슈
title: ai_issue_월간_202606
type:
- report
---

## ■ 전체 내용 요약

> 작성일: 2026년 7월 1일

- 2026년 6월은 미 상무부의 Anthropic Fable 5·Mythos 5 수출통제 긴급 차단, GPT-5.6 정부 게이티드 출시, OpenAI 최초 전용 추론 칩 Jalapeño 공개 등 AI 역사를 재편하는 사건이 연속으로 발생한 달이었다.
- Alphabet이 단일 기업 역사상 최대 주식 발행(8,475억 달러)을 실행하였으며, Anthropic(6월 1일)·OpenAI(6월 8일)가 동시에 IPO S-1을 SEC에 제출하며 AI 자본시장 사건이 6월에 집중되었다.
- Apple WWDC 2026에서 Google Gemini 탑재 Siri AI가 공개되었고, 중국은 2,950억 달러 국가 AI 인프라 계획 및 GLM-5.2 오픈소스 쇼크로 미국의 수출통제에 정면 대응하였다.
- AI 주도 기술 업계 해고가 일평균 1,115명(2025년 대비 2배)에 달하는 가운데, 한국은 삼성·SK하이닉스와 함께 역사상 최대 규모 반도체 5,200억 달러 투자 계획을 발표하며 AI 반도체 주도권을 선언하였다.

---

## 1. Fable 5·Mythos 5 수출통제 긴급 차단 — AI 모델 킬스위치 현실화

### 사건 경과 및 파장

- 미 상무부가 2026년 6월 12일 오후 5시 21분(ET) Anthropic에 Fable 5·Mythos 5 전면 접근 차단 명령을 발동하였으며, Anthropic은 90분 내에 전 세계 접근을 차단하였다.

Fable 5는 2026년 6월 9일 출시 후 단 4일 만에 강제 차단된 사상 최초의 상업 AI 수출통제 사례다. 상무장관 Howard Lutnick이 서명한 명령서는 "외국 국적자"에 대한 접근을 전면 금지하였으며, 미국 내 근무 중인 외국 국적 Anthropic 직원까지 포함되어 사실상 전 세계 접근이 차단되었다. AWS Bedrock·Google Cloud·Microsoft Foundry·Snowflake 등 모든 플랫폼에서 동시에 서비스가 중단되었다.

> 출처 : [Anthropic Disabled Fable 5 And Mythos 5 After A U.S. Export-Control Order(Forbes, 2026.06.16)](https://www.forbes.com/sites/anishasircar/2026/06/16/anthropic-disabled-fable-5-and-mythos-5-after-a-us-export-control-order-heres-what-happened/) 
> 출처 : [Statement on the US government directive(Anthropic, 2026.06.12)](https://www.anthropic.com/news/fable-mythos-access)

- Anthropic은 법적으로 명령에 이행하면서도 "수백만 명이 사용 중인 상업 모델을 좁은 잠재적 취약점 하나로 차단하는 것에 동의할 수 없다"고 공식 반박하였다.

정부가 제시한 잠재적 취약점(비유니버설 탈옥)은 GPT-5.5 등 타 공개 모델에서도 동일하게 존재한다는 점을 Anthropic이 명시하였다. 6월 26일 상무부는 Mythos 5에 대해 약 100개 신뢰 기관으로의 제한적 접근을 재허용하였으나 Fable 5는 6월 말 기준 여전히 전면 차단 상태이며, 8월 1일 행정명령 프레임워크 협상이 진행 중이다.

> 출처 : [US orders Anthropic to disable AI models for all foreign nationals(Al Jazeera, 2026.06.13)](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals) 
> 출처 : [U.S. Government Partially Lifts Anthropic AI Export Ban(Forbes, 2026.06.29)](https://www.forbes.com/sites/kateoflahertyuk/2026/06/29/us-government-partially-lifts-anthropic-ai-export-ban-what-it-means/) 
> 출처 : [Claude Fable 5 Banned: US Export Controls Explained(byteiota, 2026.06.15)](https://byteiota.com/claude-fable-5-export-ban-developers/)

**[표 1] Fable 5·Mythos 5 수출통제 주요 일지**

|날짜|사건|
|---|---|
|2026.06.09|Fable 5 공개 출시 (Mythos 클래스 첫 공개 버전, $10/$50 per MTok)|
|2026.06.12 17:21 ET|미 상무부 긴급 수출통제 명령 발동|
|2026.06.12|90분 내 전 세계 접근 차단 완료|
|2026.06.13|David Sacks "이진 선택 제시 후 Dario 거부" 공개|
|2026.06.15|중국 Z.ai, GLM-5.2 출시하며 "미국 AI는 믿을 수 없다" 성명|
|2026.06.26|Mythos 5: 약 100개 신뢰 기관 제한적 재허용, Lutnick 서한|
|2026.06.29|Fable 5: 차단 지속, 8월 1일 EO 프레임워크 협상 중|

---

## 2. GPT-5.6 3계층 출시 & 정부 게이티드 AI 시대 개막

### 주요 발표 내용 및 규제 구도

- OpenAI가 2026년 6월 26일 GPT-5.6 Sol·Terra·Luna 3계층 모델을 정부 승인 20개 파트너사에만 제한 공개하며 '정부 게이티드 AI(government-gated AI)'라는 새로운 시장 구조가 본격화되었다.

Sol은 코딩·과학·사이버 보안 최강 모델($5/$30 per MTok), Terra는 일상 업무 균형형(GPT-5.5 성능 대비 50% 저렴), Luna는 고속·저비용 볼륨형으로 계층화되었다. OpenAI는 "현재 정부 접근 프로세스가 장기 기본값이 되어서는 안 된다"고 공개적으로 밝혔다. Trump 행정부 서명 AI 사이버 보안 행정명령에 따라 OpenAI·Anthropic·Google·xAI·Microsoft 5개 기업이 프론티어 모델 출시 전 30일 정부 사전 접근 제공에 동의하였으며, Meta는 유일한 거부 기업으로 정부 압박을 받고 있다.

> 출처 : [OpenAI releases powerful new GPT-5.6 model under restrictions(Axios, 2026.06.26)](https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump) 
> 출처 : [Previewing GPT-5.6 Sol: a next-generation model(OpenAI, 2026.06.26)](https://openai.com/index/previewing-gpt-5-6-sol/) 
> 출처 : [Government-Gated AI: OpenAI, Anthropic & a New Era(Digital Applied, 2026.06.26)](https://www.digitalapplied.com/blog/us-government-gated-ai-models-new-release-paradigm-2026)

**[표 2] GPT-5.6 3계층 모델 사양 비교**

|모델|용도|가격(입력/출력, 100만 토큰)|주요 특징|
|---|---|---|---|
|Sol|코딩·과학·사이버 보안|$5 / $30|최강 추론, 강화 안전 스택|
|Terra|일상 업무 균형형|GPT-5.5 대비 50% 저렴|GPT-5.5 성능, 2배 효율|
|Luna|고속·저비용 볼륨형|최저가|고속·대량 파이프라인|

---

## 3. OpenAI 최초 전용 추론 칩 Jalapeño 공개

### 칩 개발 현황 및 전략적 의미

- OpenAI와 Broadcom이 2026년 6월 24일 LLM 추론 전용 맞춤형 칩 'Jalapeño'를 공개하였다. 설계 시작에서 테이프아웃까지 단 9개월, 고성능 ASIC 역사상 최단 개발 주기로 평가된다.

Jalapeño는 ChatGPT·Codex·API 등 OpenAI 서비스의 추론(inference) 비용 절감에 특화된 ASIC으로, OpenAI가 자체 LLM 이해를 바탕으로 커널·메모리 이동·네트워킹·서빙 패턴을 최적화하였다. 엔지니어링 샘플이 GPT-5.3-Codex-Spark 워크로드를 생산 목표 주파수·전력에서 구동하고 있으며, 현재 최고 성능 가속기 대비 '와트당 성능 대폭 향상'이 초기 테스트에서 확인되었다. 개발 과정에 OpenAI의 AI 모델을 활용하여 설계·최적화 일부를 가속화하였다.

> 출처 : [OpenAI and Broadcom unveil LLM-optimized inference chip(OpenAI, 2026.06.24)](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/) 
> 출처 : [OpenAI unveils its first custom chip, built by Broadcom(TechCrunch, 2026.06.24)](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
> 출처 : [OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership(CNBC, 2026.06.24)](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)

- 2026년 말 Microsoft 등 데이터센터 파트너와 함께 기가와트 규모 데이터센터에 초도 배치가 예정되어 있으며, Broadcom과 함께 멀티제너레이션 컴퓨팅 플랫폼 로드맵을 구축 중이다.

Broadcom CEO Hock Tan은 "고객 6개사(하이퍼스케일러)의 컴퓨팅 수요가 2026년에 그치지 않고 2027년, 2028년까지 오히려 상승한다"고 밝혔다. OpenAI 그렉 브록만 "세계는 컴퓨팅 파워 경제로 이동하고 있으며, Jalapeño는 컴퓨팅을 더 풍부하게 만들기 위한 풀스택 인프라 전략의 일부"라고 강조하였다. Broadcom 주가는 AI 호재로 2026년 첫 5개월간 18% 상승하였다.

> 출처 : [OpenAI and Broadcom Unveil LLM-Optimized Intelligence Processor(Broadcom, 2026.06.24)](https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor) 
> 출처 : [OpenAI unveils first custom AI inference chip, Jalapeño(VentureBeat, 2026.06.24)](https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models)

---

## 4. Alphabet 8,475억 달러 역사상 최대 주식 발행 & 앤트로픽·OpenAI 동시 IPO S-1 제출

### AI 자본시장 사건 집중

- Alphabet이 2026년 6월 1일 800억 달러 주식 발행을 발표하고 6월 2일 8,475억 달러로 증액 확정하였다. 주요 기술 기업의 AI 인프라 목적 단일 최대 주식 발행 기록이다.

Class A·C 보통주 및 6.25% 우선전환주 공개 발행(300억 달러) + 40억 달러 시장가 발행 프로그램(Q3 시작) + Berkshire Hathaway 사모 투자(100억 달러)로 구성되었다. 발행 목적은 "전례 없는 고객 수요를 충족하는 AI 컴퓨팅 인프라 투자"이며, 알파벳은 2026년 설비투자를 최대 1,900억 달러로 상향 조정하였다. CFO Anat Ashkenazi는 "2027년 설비투자가 2026년 최대 1,900억 달러를 유의미하게 초과할 것"이라고 밝혔다.

> 출처 : [Alphabet Inc. Form 8-K: $84.75 Billion Equity Capital Raise(SEC, 2026.06.02)](https://www.sec.gov/Archives/edgar/data/0001652044/000119312526257724/d83560dex992.htm) 
> 출처 : [Alphabet plans to raise $80 billion from stock sales(CNBC, 2026.06.01)](https://www.cnbc.com/2026/06/01/alphabet-to-raise-80-billion-from-stock-sales-to-fund-ai-buildout.html)

- 앤트로픽이 2026년 6월 1일, OpenAI가 6월 8일 각각 비공개 IPO 등록신청서(Form S-1)를 SEC에 제출하며 AI 역사상 최초로 두 최대 경쟁 AI 스타트업이 동시 상장을 추진하게 되었다.

앤트로픽은 Q2 2026 연환산 매출 470억 달러 목표, 첫 영업이익 약 5억 5,900만 달러 달성이 예상되며 2026년 10월 상장을 목표로 Goldman Sachs·JPMorgan·Morgan Stanley가 주관한다. OpenAI는 CFO Sarah Friar가 임직원에게 "2027년 상장이 목표"라고 통보하여 일정 연기 가능성이 부상하였으며, SpaceX-xAI도 6월에 공개 S-1을 제출(기업가치 약 1조 7,700억 달러 목표)하며 AI 자본시장 사건이 6월에 집중되었다.

> 출처 : [AI Talent War: Anthropic & OpenAI IPO S-1 Timeline(Kingy.ai, 2026.06.19)](https://kingy.ai/ai/ai-talent-war-noam-shazeer-john-jumper-openai-anthropic-google/) 
> 출처 : [OpenAI postpones GPT-5.6 and IPO(Techzine, 2026.06.27)](https://www.techzine.eu/news/applications/142488/openai-postpones-gpt-5-6-and-ipo-why/)

**[표 3] 2026년 6월 AI 자본시장 주요 사건**

|기업|사건일|내용|규모|
|---|---|---|---|
|Alphabet|2026.06.01~02|역사상 최대 주식 발행 확정|8,475억 달러|
|Anthropic|2026.06.01|비공개 IPO S-1 SEC 제출|목표 기업가치 9,000억+ 달러|
|OpenAI|2026.06.08|비공개 IPO S-1 SEC 제출|목표 기업가치 1조 달러, 2027년 상장 잠정|
|SpaceX-xAI|2026.06(공개)|공개 S-1 나스닥 제출|목표 기업가치 1조 7,700억 달러|

---

## 5. Apple WWDC 2026: Google Gemini 탑재 Siri AI 전면 재건

### 핵심 발표 및 전략적 의미

- 2026년 6월 8일 Apple WWDC 2026에서 Tim Cook CEO(마지막 기조연설) 주재로 Google Gemini 기반의 완전 재설계 Siri AI가 공개되었다.

Siri AI는 Google Gemini 모델(1.2조 파라미터 맞춤 구축, 연간 약 10억 달러 라이선스)을 Private Cloud Compute를 통해 구동하며, 2024년 약속했으나 출시하지 못한 개인화·앱간 연동·화면 인식 기능을 2년 만에 처음으로 제공한다. Apple은 Siri가 iOS 27 Extensions를 통해 ChatGPT·Claude 등 타사 AI 모델을 기본 어시스턴트로 선택할 수 있도록 개방하였다. iOS 27·macOS 27(Golden Gate)·iPadOS 27·watchOS 27 등 전 플랫폼이 27 버전으로 전환되었으며, SiriKit 지원 종료를 예고하고 App Intents를 Siri 타사 앱 호출 의무 인터페이스로 지정하였다.

> 출처 : [WWDC 2026: Apple unveils Siri AI, Gemini-powered Apple Intelligence(Business Standard, 2026.06.09)](https://www.business-standard.com/amp/technology/tech-news/wwdc-2026-apple-unveils-siri-ai-gemini-powered-apple-intelligence-more-126060900042_1.html) 
> 출처 : [WWDC 2026: Siri AI Runs on Google's $1B Gemini Deal(Tech Insider, 2026.06.08)](https://tech-insider.org/wwdc-2026-siri-ai-gemini-deal/) 
> 출처 : [WWDC 2026: Everything announced on Siri AI, iOS 27(TechCrunch, 2026.06.09)](https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/)

**[표 4] Apple WWDC 2026 핵심 발표 요약**

|항목|내용|
|---|---|
|Siri AI 기반 모델|Google Gemini 맞춤 모델(1.2조 파라미터 추정)|
|라이선스 규모|연간 약 10억 달러(다년 계약)|
|신규 OS 버전|iOS 27, macOS 27 Golden Gate, iPadOS 27 등 전 플랫폼|
|주요 신기능|앱간 연동, 화면 인식, 개인 컨텍스트, Siri 독립 앱|
|개발자 변경|SiriKit 지원 종료 예고, App Intents 의무화|
|경영 전환|Tim Cook 마지막 WWDC 기조연설, John Ternus 9월 1일 CEO 승계|

---

## 6. 중국 2,950억 달러 국가 AI 인프라 & GLM-5.2 오픈소스 쇼크

### 중국 국가 AI 전략 및 오픈소스 대응

- 중국 NDRC·재정부 주도로 5개년간 2조 위안(약 2,950억 달러) 국가 AI 데이터센터 건설 계획이 수립 중이며, 기술의 80% 이상을 Huawei 등 국내 공급업체에서 조달하여 Nvidia·AMD를 사실상 배제한다는 방침이다.

China Mobile·China Telecom 등 국영 통신사가 전국 상호 연결 컴퓨팅 허브를 운영하는 구조로, 초장기 국채 및 전략 산업 투자 국가 펀드로 재원을 조달한다. Bloomberg에 따르면 중국 데이터센터는 노동·부품·건설 비용이 미국 대비 낮아 동일 금액으로 더 큰 인프라 구축이 가능하다.

> 출처 : [China Plans $295 Billion Investment to Build Nationwide AI Data Centers(Bloomberg, 2026.06.09)](https://www.bloomberg.com/news/articles/2026-06-09/china-prepares-295-billion-plan-to-fund-nationwide-ai-buildout) 
> 출처 : [China preps $295 billion plan to fund nationwide AI buildout(Spokesman, 2026.06.11)](https://www.spokesman.com/stories/2026/jun/11/china-preps-295-billion-plan-to-fund-nationwide-ai/)

- Z.ai(구 Zhipu AI)가 6월 13일 GLM-5.2를 MIT 라이선스로 공개하며 Fable 5 수출통제 명령 다음 날 "미국 AI 의존 불가론"을 공개 제기하였다.

GLM-5.2는 Artificial Analysis Intelligence Index v4.1에서 51점으로 MiniMax-M3(44점)·DeepSeek V4 Pro(44점)·Gemini 3.1 Pro(46점)를 모두 상회하는 오픈웨이트 최강 모델이다. 가격은 입력 1.40달러/100만 토큰, 출력 4.40달러로 GPT-5.5(5달러/30달러) 대비 입력 3.6배, 출력 6.8배 저렴하다. 744억 파라미터(활성 40억) MoE 구조, 컨텍스트 윈도우 4배 확장(100만 토큰)이 핵심 사양이다.

> 출처 : [GLM-5.2: China's Zhipu AI Beats Even Google's Top Models(Trending Topics, 2026.06.18)](https://www.trendingtopics.eu/glm-5-2-chinas-zhipu-ai-beats-even-googles-top-models-with-its-new-open-llm/) 
> 출처 : [China's $295 Billion AI Infrastructure Plan(FourWeekMBA, 2026.06.24)](https://fourweekmba.com/china-295-billion-ai-infrastructure-sovereign-stack/)

**[표 5] GLM-5.2 vs 주요 모델 비교 (2026년 6월 기준)**

|모델|Intelligence Index|입력($/ 100만 토큰)|출력($/100만 토큰)|구분|
|---|---|---|---|---|
|GLM-5.2 (Z.ai)|51 (오픈웨이트 1위)|$1.40|$4.40|오픈소스 MIT|
|Gemini 3.1 Pro|46|$3.50|$10.50|클로즈드|
|MiniMax-M3|44|-|-|오픈소스|
|GPT-5.5 (OpenAI)|비공개|$5.00|$30.00|클로즈드|
|Claude Opus 4.8|비공개|$5.00|$25.00|클로즈드|
|DeepSeek V4-Pro|44|$0.44|$0.87|오픈소스, 영구 인하|

> 출처 : [GLM 5.2 Could Be China's New AI Wrecking Ball(Investing.com, 2026.06.19)](https://www.investing.com/analysis/glm-52-could-be-chinas-new-ai-wrecking-ball-200682604)

---

## 7. AI 인재 전쟁 최고조: Transformer 아버지 OpenAI, AlphaFold 개발자 Anthropic 이적

### AI 연구 인재 쟁탈전 현황

- Google Gemini 공동 수석 Noam Shazeer가 2026년 6월 18일 OpenAI에 합류하였다. Google이 2024년 약 27억 달러를 지불하며 영입한 지 22개월 만이다.

Shazeer는 현대 AI의 기반이 되는 Transformer 아키텍처를 소개한 2017년 논문 "Attention Is All You Need"의 공동 저자로, "Transformer의 아버지"로 불린다. Sam Altman은 "OpenAI 창립 초기부터 가장 함께 일하고 싶었던 사람, 10년이 걸렸지만 기다린 보람이 있을 것"이라고 공개 환영하였다.

> 출처 : [Gemini Co-Lead Noam Shazeer Quits Google, Joins OpenAI Before IPO(BeinCrypto, 2026.06.18)](https://beincrypto.com/noam-shazeer-google-gemini-joins-openai-ipo/) 
> 출처 : [OpenAI Bolsters Ranks With AI Pioneer Noam Shazeer(Bitcoin World, 2026.06.19)](https://bitcoinworld.co.in/openai-hires-noam-shazeer-dean-ball-ipo/)

- AlphaFold 공동 개발자·2024년 노벨화학상 공동 수상자 John Jumper가 6월 19일 Google DeepMind를 떠나 Anthropic으로 이적하며 AI 기초 과학 인재의 방향성도 명확해졌다.

Alphabet 주가는 6월 22일 5~6% 하락하였으며, Bloomberg는 DeepMind 내부에서 기업 AI 코딩 툴 영역의 경쟁 열세에 대한 우려가 제기되고 있다고 보도하였다. 1주일 내 2명의 최고 연구자 이탈은 Google의 인재 유지 전략의 구조적 한계를 드러냈다.

> 출처 : [Google Loses Two Top AI Researchers To OpenAI & Anthropic(Search Engine Journal, 2026.06.22)](https://www.searchenginejournal.com/google-loses-two-top-ai-researchers-to-openai-anthropic/580201/) 
> 출처 : [AI Talent War: Shazeer, Jumper, OpenAI, Anthropic(Kingy.ai, 2026.06.19)](https://kingy.ai/ai/ai-talent-war-noam-shazeer-john-jumper-openai-anthropic-google/)

---

## 8. AI 주도 대규모 구조조정: 기술 업계 일평균 1,115명 해고

### AI 해고 현황 및 계량 지표

- 2026년 6월 29일 기준 기술 업계에서 연간 267건, 총 185,894명이 영향을 받았으며 일평균 1,115명의 해고가 발생하고 있다. 이는 2025년 일평균 564명의 2배 수준이다.

2026년 확인된 기술 업계 해고 중 56%가 AI·자동화·머신러닝을 원인으로 명시하였으며, 이는 150개 기업에서 156,270명에 영향을 미쳤다. 단일 최대 해고는 Oracle 3만 명이며, BCG 보고서에 따르면 미국 컴퓨터·수학 직종의 자동화 비율이 2025년 32%에서 2026년 52%로 급상승하였다. Stanford 연구에 따르면 AI 고노출 직종에서 22~25세 취업률이 13% 감소하였다.

> 출처 : [Tech Layoffs Hit 1,115 a Day in 2026(TechTimes, 2026.06.16)](https://www.techtimes.com/articles/318466/20260616/tech-layoffs-hit-1115-day-2026-companies-cite-ai-cuts-fail-boost-returns.htm) 
> 출처 : [2026 Tech Layoffs Tracker(SkillSyncer, 2026.06.29)](https://skillsyncer.com/layoffs-tracker) 
> 출처 : [AI Will Reshape More Jobs Than It Replaces(BCG, 2026.04.03)](https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces)

- 2026년 5월 Gartner 연구(350개 기업)에서 AI 이유 해고 기업이 재무 성과 개선을 보이지 못한 것으로 나타나 AI 해고의 실질적 경제 효과에 대한 의문이 제기되고 있다.

OpenAI CEO Sam Altman은 "일부 기업이 어차피 단행할 구조조정에 AI를 명분으로 활용(AI 워싱)하고 있다"고 공개 인정하였다. California주는 5월 21일 AI 해고 공시 제도화를 검토하는 행정명령을 발령하였고, Colorado주 AI Act는 6월 30일부터 시행 중이다.

> 출처 : [AI And Layoffs in 2026(SaaSultra, 2026.06.29)](https://www.saasultra.com/ai-layoffs-statistics-shakeup/)

**[표 6] 2026년 AI 관련 기술 업계 해고 핵심 지표**

|지표|2025년|2026년(6월 말)|변화|
|---|---|---|---|
|연간 해고 이벤트 수|338건|267건(진행 중)|-|
|누적 영향 인원|205,773명|185,894명|진행 중|
|일평균 해고 인원|564명/일|1,115명/일|+98%|
|AI 원인 명시 해고 비율|8% 미만|56%|+48%p↑|
|22~25세 AI노출 직종 취업률 변화|-|-13%(Stanford 연구)|청년 직격|

---

## 9. AI 모델 가격 전쟁 & 오픈웨이트 생태계 급성장

### 가격 경쟁 및 오픈소스 확산 현황

- 6월 한 달 동안 DeepSeek V4-Pro 가격이 영구 인하(입력 0.44달러/100만 토큰), GLM-5.2 출시, GitHub Copilot의 에이전트 세션 사용량 기반 과금 전환 등 AI 모델 가격 전쟁이 본격화되었다.

DeepSeek V4-Pro는 GPT-5.5(5달러) 대비 입력 토큰에서 11.4배, 출력(30달러 대비 0.87달러) 기준 34.5배 저렴하다. GitHub CPO Mario Rodriguez는 "단일 장기 에이전트 세션 비용이 월 기본 채팅 사용량 전체와 맞먹는다"고 공식 확인하였다. Cursor·Windsurf·GitHub Copilot 등 주요 AI 코딩 도구 전반에서 월정액에서 사용량 기반 과금 체계로 전환이 이루어지고 있다.

> 출처 : [AI News Today June 30 2026(Build Fast with AI, 2026.06.30)](https://www.buildfastwithai.com/blogs/ai-news-today-june-30-2026) 
> 출처 : [AI News Today June 26 2026(Build Fast with AI, 2026.06.26)](https://www.buildfastwithai.com/blogs/ai-news-today-june-26-2026)

- ChatGPT의 전 세계 AI 챗봇 웹 방문 점유율이 54.7%로 2025년 2월 76.5% 대비 급락하였으며, Claude는 같은 기간 203M에서 824M 웹 방문으로 306% 성장하였다.

Google Gemini는 27.4%로 2위를 유지하며 6개월간 104% 성장하였다. Fable 5 수출통제 사건은 "모델 가중치가 공개된 오픈웨이트 모델은 상무장관이 차단할 수 없다"는 오픈웨이트의 구조적 경쟁 우위를 극적으로 부각시켰다.

> 출처 : [AI News Today June 8 2026(Build Fast with AI, 2026.06.08)](https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026)

---

## 10. 한국, 삼성·SK하이닉스와 5,200억 달러 반도체 메가 투자 선언

### 핵심 발표 및 글로벌 의미

- 이재명 대통령이 2026년 6월 29일 삼성전자·SK하이닉스와 함께 800조 원(약 5,200억 달러) 반도체 생태계 국가 투자 계획을 발표하였다. 미국 CHIPS Act 직접 보조금(약 520억 달러)의 10배에 해당하는 역사상 최대 규모 반도체 투자다.

삼성전자·SK하이닉스가 각각 2개씩 총 4개의 신규 반도체 팹을 전라남북도 광주·전남 지역에 건설하며, 별도 550조 원 투자로 SK·GS·네이버 등 참여 기업이 AI 데이터센터 3개를 구축하여 초도 용량 8.4GW를 목표로 한다. 정부는 팹 건설 승인 기간을 기존 2040년대에서 2030년대 중반으로 최대 12년 단축한다고 발표하였다.

> 출처 : [South Korea unveils $520 billion investment plan with Samsung and SK Hynix(Tom's Hardware, 2026.06.30)](https://www.tomshardware.com/tech-industry/semiconductors/south-korea-unveils-usd520-billion-investment-plan-with-samsung-and-sk-hynix-to-expand-memory-chip-dominance) 
> 출처 : [South Korea announces $520bn chip plant project(Nikkei Asia, 2026.06.30)](https://asia.nikkei.com/business/tech/semiconductors/south-korea-announces-520bn-chip-plant-project-with-samsung-sk-hynix) 
> 출처 : [South Korea to invest $576 billion in AI chip production(CNN, 2026.06.29)](https://www.cnn.com/2026/06/29/business/south-korea-ai-investment-samsung-skhynix)

- SK하이닉스는 이번 주 삼성전자를 제치고 한국 시가총액 1위 기업으로 올라섰으며(삼성전자가 26년간 유지해 온 자리), AI 모델 훈련·추론에 필수적인 HBM(고대역폭 메모리) 공급에서 엔비디아의 핵심 공급자로 자리매김하고 있다.

SK하이닉스는 나스닥 ADR 상장을 추진 중이며, 조달 자금 약 296억 5,000만 달러를 국내 생산 능력 확장에 투입할 예정이다. 이재명 대통령은 "다른 어떤 나라보다 빠르게 AI의 핵심 요소를 확보해야 한다"며 반도체·물리 AI·AI 데이터센터를 '3대 메가 프로젝트'로 명명하였다.

> 출처 : [Samsung SK Hynix $520 billion chip plants South Korea(Yahoo Finance, 2026.06.30)](https://finance.yahoo.com/technology/ai/articles/samsung-sk-hynix-520-billion-115246649.html) 
> 출처 : [South Korea says Samsung and SK Hynix investing in AI, semiconductor mega-projects(CNBC, 2026.06.29)](https://www.cnbc.com/2026/06/29/samsung-sk-hynix-reported-1point3-reported-trillion-spending-plans.html)

**[표 7] 한국 반도체·AI 메가 투자 구성**

| 투자 항목               | 규모                  | 주요 내용                    |
| ------------------- | ------------------- | ------------------------ |
| 반도체 팹 건설(삼성·SK하이닉스) | 800조 원(약 5,200억 달러) | 광주·전남 지역 각 2개 팹, HBM 중심  |
| 충청권 패키징 허브          | 81조 원               | HBM 고도 패키징 클러스터          |
| AI 데이터센터 건설         | 550조 원              | SK·GS·네이버 등 참여, 초도 8.4GW |
| 정부·지자체 지원           | 30조 원+(15년)         | 허가 기간 최대 12년 단축, 세금 지원   |


---

## 11. 종합 시사점 및 전망

### 단기 전망 (2026년 하반기)

- AI 모델 수출통제 프레임워크가 8월 1일 행정명령 시한을 기점으로 구체화될 전망이며, Fable 5 전면 복원 여부 및 구체적 승인 기준 공개가 업계 최대 관심사다.
- OpenAI Jalapeño 칩의 2026년 말 초도 배치가 예정대로 이루어질 경우 추론 비용 절감 효과가 2027년 이후 재무 지표에 반영될 것으로 기대된다.
- 앤트로픽 2026년 10월 상장이 AI 기업 사상 첫 공모의 기준점이 되며, 앤트로픽의 밸류에이션 공개가 전체 AI 스타트업 재평가를 촉발할 전망이다.

### 중기 전망 (향후 1년)

- '정부 게이티드 AI'가 제도적으로 정착되면서 오픈웨이트 모델의 구조적 경쟁 우위가 강화되고, 기업의 AI 공급망 다각화(multi-vendor) 전략이 필수 리스크 관리 수단으로 자리잡을 것이다.
- 한국 5,200억 달러 투자는 2030년대 중반 HBM 및 AI 반도체 공급 구조를 근본적으로 바꿀 잠재력을 가지며, 삼성의 HBM 반격과 SK하이닉스의 나스닥 상장이 단기 시장 변수다.
- 중국 2,950억 달러 AI 인프라 계획이 실행되면 2028~2029년 중국 AI 컴퓨팅 역량이 획기적으로 도약할 전망이다.

### 국내 정책 시사점

- 미국 AI 수출통제가 한국 기업의 AI 서비스 공급망에 미치는 직접 영향을 전수 조사하고, 오픈웨이트 모델 활용 비중을 높이는 다중 공급망 전략 수립이 시급하다.
- 5,200억 달러 반도체 투자와 연계하여 AI 추론 특화 칩(ASIC) 및 NPU 국내 생태계 육성 방안을 국가 AI 기본법 시행 계획과 통합 설계할 필요가 있다.
- AI 주도 해고 일평균 1,115명 추세에 대응하여 고용노동부의 AI 전환 지원 프로그램, 직업훈련 제도 업데이트, AI 해고 공시 의무화 입법 논의를 조속히 추진할 필요가 있다.

---

## 관련근거 및 출처

[Anthropic Disabled Fable 5 And Mythos 5 After A U.S. Export-Control Order(Forbes, 2026.06.16)](https://www.forbes.com/sites/anishasircar/2026/06/16/anthropic-disabled-fable-5-and-mythos-5-after-a-us-export-control-order-heres-what-happened/)

[Statement on the US government directive to suspend access to Fable 5 and Mythos 5(Anthropic, 2026.06.12)](https://www.anthropic.com/news/fable-mythos-access)

[US orders Anthropic to disable AI models for all foreign nationals(Al Jazeera, 2026.06.13)](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals)

[U.S. Government Partially Lifts Anthropic AI Export Ban(Forbes, 2026.06.29)](https://www.forbes.com/sites/kateoflahertyuk/2026/06/29/us-government-partially-lifts-anthropic-ai-export-ban-what-it-means/)

[Claude Fable 5 Banned: US Export Controls Explained(byteiota, 2026.06.15)](https://byteiota.com/claude-fable-5-export-ban-developers/)

[Anthropic disables Fable and Mythos AI models following U.S. government export ban(Fortune, 2026.06.13)](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/)

[OpenAI releases powerful new GPT-5.6 model under restrictions(Axios, 2026.06.26)](https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump)

[Previewing GPT-5.6 Sol: a next-generation model(OpenAI, 2026.06.26)](https://openai.com/index/previewing-gpt-5-6-sol/)

[Government-Gated AI: OpenAI, Anthropic & a New Era(Digital Applied, 2026.06.26)](https://www.digitalapplied.com/blog/us-government-gated-ai-models-new-release-paradigm-2026)

[OpenAI launches a limited preview of GPT-5.6(Engadget, 2026.06.26)](https://www.engadget.com/2203102/openai-starts-previewing-gpt-56-and-its-three-variants/)

[OpenAI postpones GPT-5.6 and IPO(Techzine, 2026.06.27)](https://www.techzine.eu/news/applications/142488/openai-postpones-gpt-5-6-and-ipo-why/)

[OpenAI and Broadcom unveil LLM-optimized inference chip Jalapeño(OpenAI, 2026.06.24)](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)

[OpenAI unveils its first custom chip, built by Broadcom(TechCrunch, 2026.06.24)](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)

[OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership(CNBC, 2026.06.24)](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)

[OpenAI and Broadcom Unveil LLM-Optimized Intelligence Processor(Broadcom, 2026.06.24)](https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor)

[OpenAI unveils first custom AI inference chip Jalapeño(VentureBeat, 2026.06.24)](https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models)

[Alphabet Inc. Form 8-K: $84.75 Billion Equity Capital Raise(SEC, 2026.06.02)](https://www.sec.gov/Archives/edgar/data/0001652044/000119312526257724/d83560dex992.htm)

[Alphabet plans to raise $80 billion from stock sales(CNBC, 2026.06.01)](https://www.cnbc.com/2026/06/01/alphabet-to-raise-80-billion-from-stock-sales-to-fund-ai-buildout.html)

[Alphabet Raises $84.75 Billion for AI Infrastructure(Enterprise DNA, 2026.06.06)](https://enterprisedna.co/resources/news/alphabet-google-84-billion-ai-infrastructure-raise-2026/)

[AI Talent War: Anthropic & OpenAI IPO S-1 Timeline(Kingy.ai, 2026.06.19)](https://kingy.ai/ai/ai-talent-war-noam-shazeer-john-jumper-openai-anthropic-google/)

[OpenAI postpones IPO: why?(Techzine, 2026.06.27)](https://www.techzine.eu/news/applications/142488/openai-postpones-gpt-5-6-and-ipo-why/)

[WWDC 2026: Apple unveils Siri AI, Gemini-powered Apple Intelligence(Business Standard, 2026.06.09)](https://www.business-standard.com/amp/technology/tech-news/wwdc-2026-apple-unveils-siri-ai-gemini-powered-apple-intelligence-more-126060900042_1.html)

[WWDC 2026: Siri AI Runs on Google's $1B Gemini Deal(Tech Insider, 2026.06.08)](https://tech-insider.org/wwdc-2026-siri-ai-gemini-deal/)

[WWDC 2026: Everything announced on Siri AI, iOS 27, Apple Intelligence(TechCrunch, 2026.06.09)](https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/)

[WWDC 2026: iOS 27, New Siri & Dev Tools(Lushbinary, 2026.06.08)](https://lushbinary.com/blog/wwdc-2026-announcements-ios-27-siri-developer-guide/)

[China Plans $295 Billion Investment to Build Nationwide AI Data Centers(Bloomberg, 2026.06.09)](https://www.bloomberg.com/news/articles/2026-06-09/china-prepares-295-billion-plan-to-fund-nationwide-ai-buildout)

[China preps $295 billion plan to fund nationwide AI buildout(Spokesman, 2026.06.11)](https://www.spokesman.com/stories/2026/jun/11/china-preps-295-billion-plan-to-fund-nationwide-ai/)

[GLM-5.2: China's Zhipu AI Beats Even Google's Top Models(Trending Topics, 2026.06.18)](https://www.trendingtopics.eu/glm-5-2-chinas-zhipu-ai-beats-even-googles-top-models-with-its-new-open-llm/)

[GLM 5.2 Could Be China's New AI Wrecking Ball(Investing.com, 2026.06.19)](https://www.investing.com/analysis/glm-52-could-be-chinas-new-ai-wrecking-ball-200682604)

[China's $295 Billion AI Infrastructure Plan(FourWeekMBA, 2026.06.24)](https://fourweekmba.com/china-295-billion-ai-infrastructure-sovereign-stack/)

[Gemini Co-Lead Noam Shazeer Quits Google, Joins OpenAI Before IPO(BeinCrypto, 2026.06.18)](https://beincrypto.com/noam-shazeer-google-gemini-joins-openai-ipo/)

[OpenAI Bolsters Ranks With Noam Shazeer Ahead of IPO(Bitcoin World, 2026.06.19)](https://bitcoinworld.co.in/openai-hires-noam-shazeer-dean-ball-ipo/)

[Google Loses Two Top AI Researchers To OpenAI & Anthropic(Search Engine Journal, 2026.06.22)](https://www.searchenginejournal.com/google-loses-two-top-ai-researchers-to-openai-anthropic/580201/)

[AI Talent War: Shazeer, Jumper, OpenAI, Anthropic(Kingy.ai, 2026.06.19)](https://kingy.ai/ai/ai-talent-war-noam-shazeer-john-jumper-openai-anthropic-google/)

[Tech Layoffs Hit 1,115 a Day in 2026(TechTimes, 2026.06.16)](https://www.techtimes.com/articles/318466/20260616/tech-layoffs-hit-1115-day-2026-companies-cite-ai-cuts-fail-boost-returns.htm)

[2026 Tech Layoffs Tracker(SkillSyncer, 2026.06.29)](https://skillsyncer.com/layoffs-tracker)

[AI And Layoffs in 2026(SaaSultra, 2026.06.29)](https://www.saasultra.com/ai-layoffs-statistics-shakeup/)

[AI Will Reshape More Jobs Than It Replaces(BCG, 2026.04.03)](https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces)

[AI News Today June 30 2026(Build Fast with AI, 2026.06.30)](https://www.buildfastwithai.com/blogs/ai-news-today-june-30-2026)

[AI News Today June 8 2026(Build Fast with AI, 2026.06.08)](https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026)

[South Korea unveils $520 billion investment plan with Samsung and SK Hynix(Tom's Hardware, 2026.06.30)](https://www.tomshardware.com/tech-industry/semiconductors/south-korea-unveils-usd520-billion-investment-plan-with-samsung-and-sk-hynix-to-expand-memory-chip-dominance)

[South Korea announces $520bn chip plant project(Nikkei Asia, 2026.06.30)](https://asia.nikkei.com/business/tech/semiconductors/south-korea-announces-520bn-chip-plant-project-with-samsung-sk-hynix)

[South Korea to invest $576 billion in AI chip production with Samsung and SK Hynix(CNN, 2026.06.29)](https://www.cnn.com/2026/06/29/business/south-korea-ai-investment-samsung-skhynix)

[Samsung SK Hynix $520 billion chip plants South Korea 2026(Yahoo Finance, 2026.06.30)](https://finance.yahoo.com/technology/ai/articles/samsung-sk-hynix-520-billion-115246649.html)

[South Korea says Samsung and SK Hynix investing in AI, semiconductor mega-projects(CNBC, 2026.06.29)](https://www.cnbc.com/2026/06/29/samsung-sk-hynix-reported-1point3-reported-trillion-spending-plans.html)

[South Korea is investing $520 billion in Samsung and SK Hynix(TweakTown, 2026.06.30)](https://www.tweaktown.com/news/112402/south-korea-is-investing-dollars520-billion-in-samsung-and-sk-hynix-to-build-more-hbm-fabs-for-ai/index.html)