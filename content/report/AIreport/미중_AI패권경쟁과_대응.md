---
created: 2026-07-30
modified: 2026-07-30
publish: true
source: claude
tags:
- AI패권경쟁
title: 미중 AI 패권경쟁과 대응
type:
- report
---

```toc
minLevel: 2
maxLevel: 3
```
# 미중 AI 패권경쟁과 대응

**작성일** 2026년 7월 30일
**분석범위** 2025년 하반기 ~ 2026년 7월 (정책·규제 동향은 최근 3개월 중점)

---

## 전체 내용 요약

**경쟁의 축이 세 번째 국면으로 이동했다.** 미중 AI 경쟁은 모델 성능 경쟁(2023~2024)에서 컴퓨팅·인프라 확보 경쟁(2024~2025)을 거쳐, 현재는 모델 배포권·거버넌스 통제 경쟁으로 이동했다. 미중 최상위 모델 간 성능 격차가 Elo 2.7% 수준으로 사실상 소멸한 상황에서, 경쟁의 실질 수단은 "누가 더 좋은 모델을 만드는가"가 아니라 "누가 모델의 접근과 배포를 통제하는가"로 전환되었다.

**미국의 통제 수단은 이미 실증되었으나, 그 실효성은 오픈웨이트 앞에서 흔들리고 있다.** 2026년 6월 미 상무부가 수출통제 지시만으로 이미 출시된 프론티어 모델의 전 세계 고객 접근을 차단하고 복원한 사건은, 신규 입법 없이도 배포권 통제가 작동함을 입증했다. 그러나 중국 오픈웨이트 모델이 배포 지형을 장악하고 근프론티어급 개방모델이 통제 체계 밖에서 출현하면서, 가중치 통제의 유효성 자체가 미국 내 논쟁 대상이 되었다.

**한국은 상류 강점과 하류 의존이 병존하는 비대칭 구조에 놓여 있다.** HBM과 AI 특허, 주목모델 수에서는 세계 상위권이지만, AI 가속기와 클라우드 소프트웨어, 프론티어 모델 계층은 미국·중국에 의존한다. 동시에 VEU 폐지로 미국 수출통제에 직접 노출되어 있으며, HBM 가격 급등이 국가 GPU 확보 목표의 달성 자체를 위협하고 있다.

**대응의 핵심은 물량 확보에서 접근권 보장으로 프레임을 확장하는 것이다.** 지금까지의 인프라 전략이 GPU 물량 확보에 집중되어 왔다면, 배포권 통제 국면에서는 모델 접근권 자체가 단절될 수 있는 리스크가 새로 추가된다. 따라서 인프라, 모델, 규제, 공급망, 생태계 5개 축에서 각각 이중화와 협상 레버리지 확보가 병행되어야 한다.

**한국의 좌표를 통제 대상국에서 통제 설계 참여국으로 이동시켜야 한다.** 미국 연방·주 입법이 10^26 FLOPs와 매출 5억 달러 기준으로 수렴하고 있으므로, 한국 AI 기본법의 기준을 이에 정합화하면 국제 규범 논의에 참여할 자격을 확보할 수 있다.

---

## 1. 개요 — AI 산업동향의 변화와 경쟁 축의 이동

### 1.1 AI 산업 전반의 현재 이슈

#### 1.1.1 시장·투자 규모의 재편

글로벌 AI 시장 규모는 기관별 정의 차이로 편차가 커서 단일 수치 인용이 부적절하다. 2026년 추정치만 보아도 5,400억 달러에서 9,000억 달러까지 벌어진다.

| 기관                  | 2026년 시장규모 | CAGR               | 도달 전망          |
| ------------------- | ---------- | ------------------ | -------------- |
| Grand View Research | 5,395억 달러  | 30.6% (2026~2033)  | 2033년 3.5조 달러  |
| MarketsandMarkets   | 6,019억 달러  | 29.3% (2026~2033)  | 2033년 3.64조 달러 |
| Statista            | 6,176억 달러  | 14.82% (2026~2032) | 2032년 1.42조 달러 |
| Precedence Research | 9,000억 달러  | 18.73% (2026~2035) | 2035년 4.22조 달러 |

> 출처 : [Artificial Intelligence Market Size & Share Report, 2026-2033(Grand View Research)](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market)
>
> 출처 : [Artificial Intelligence (AI) Market Report 2026-2033(MarketsandMarkets)](https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-market-74851580.html)

정책 근거로는 시장조사기관의 추정치보다 실제 투자 집계가 신뢰도가 높다. 2025년 글로벌 기업 AI 투자는 5,817억 달러로 2024년 2,530억 달러 대비 약 130% 증가하여 2021년 종전 최고치인 3,600억 달러를 경신했다. 국가별 격차는 오히려 확대되었는데, 미국 민간투자 2,859억 달러는 중국 124억 달러의 23배 이상이다.

> 출처 : [The 2026 AI Index Report(Stanford HAI, 2026.04.13)](https://hai.stanford.edu/ai-index/2026-ai-index-report)

하이퍼스케일러 CAPEX는 컴퓨팅 확보 경쟁의 가장 직접적인 증거다. Alphabet, Amazon, Meta, Microsoft 4사의 2026년 합산 CAPEX 가이던스는 약 7,250억 달러로, 2025년 약 4,100억 달러 대비 77% 증가했다.

| 기업        | 2026 CAPEX 가이던스  |
| --------- | ---------------- |
| Amazon    | 약 2,000억 달러      |
| Microsoft | 약 1,900억 달러      |
| Alphabet  | 1,750억~1,850억 달러 |
| Meta      | 1,150억~1,350억 달러 |

> 출처 : [Google, Microsoft, Meta, and Amazon capex spending to hit $725 billion in 2026(Tom's Hardware)](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)

주목할 점은 Microsoft CFO가 1,900억 달러 중 250억 달러를 메모리·부품 가격 상승 탓으로 지목한 것이다. 이는 CAPEX 증가분의 상당 부분이 물량 확대가 아니라 단가 상승에 기인함을 시사하며, 한국의 GPU 조달 예산에도 동일한 압력이 작용한다. 다만 2026년 7월 하순 실적 발표 이후 CAPEX 급증에 대한 투자자 반발이 나타나면서 지속가능성 논쟁도 병존하고 있다.

> 출처 : [Big Tech earnings slam into a market in revolt over AI spending(Fortune, 2026.07.26)](https://fortune.com/2026/07/26/big-tech-earnings-meta-microsoft-apple-amazon-market-revolt-ai-spending/)

#### 1.1.2 컴퓨팅 공급 병목 — HBM이 핵심 제약

컴퓨팅 희소성은 선도 AI 랩조차 기본 서비스 유지에 제약을 받는 수준이다. Anthropic은 2026년 3월 유료 사용자의 피크시간 세션 제한을 강화했고, 5월에는 경쟁사 xAI의 Colossus 클러스터 용량을 2029년까지 월 12.5억 달러에 임차하기로 합의했다. 선도 랩이 직접 경쟁사로부터 인프라를 구매해야 한다는 사실은 컴퓨팅이 여전히 AI 개발의 실질적 제약임을 명확히 보여준다.

> 출처 : [What Export Controls on Anthropic's Most Advanced Models Mean for Europe(AI Frontiers)](https://ai-frontiers.org/articles/what-export-controls-on-anthropics-most-advanced-models-mean-for-europe)

병목의 핵심은 HBM이다. HBM 가격 급등이 GPU와 서버 단가를 끌어올리며 동일 예산으로 확보 가능한 물량을 축소시킨다. 이는 후술할 한국 GPU 확보 사업의 최대 리스크와 직결된다.

#### 1.1.3 모델 성능 수렴과 오픈웨이트의 부상

미중 최상위 모델 간 성능 격차는 사실상 소멸 수준으로 축소되었다. Chatbot Arena Elo 기준으로 2026년 3월 Anthropic Claude Opus 4.6이 1,503점을 기록해 최고 중국 모델인 ByteDance의 1,464점을 2.7%, 약 39점 차이로 선도하고 있다. 2023년 5월과 비교하면 격차가 사실상 소멸한 것이다.

오픈웨이트 모델의 코딩 성능도 프론티어 모델과 좁혀졌다. DeepSeek과 Kimi급 오픈모델은 SWE-Bench Verified에서 Claude Opus 4.x의 약 80.8% 수준에 도달했다.

> 출처 : [Best Open Source LLM 2026: DeepSeek, Kimi, Qwen Ranked(Tech Insider)](https://tech-insider.org/best-open-source-llm-2026/)

에이전트 성능의 도약과 채택 속도 또한 주목할 만하다. SWE-bench Verified는 1년 만에 인간 기준의 60%에서 100% 근접으로, 컴퓨터 작업 에이전트 성능은 12%에서 66.3%로 상승했다. 생성형 AI는 3년 만에 전 세계 인구의 53%에 도달해 PC나 인터넷보다 빠른 확산 속도를 보였고, 조직 채택률은 88%에 이르렀다.

> 출처 : [Stanford's AI Index for 2026 Shows the State of AI(IEEE Spectrum)](https://spectrum.ieee.org/state-of-ai-index-2026)

한편 5개 하이퍼스케일러가 글로벌 AI 컴퓨팅의 3분의 2 이상을 통제하는 구조는 시스템적 취약성으로 지적된다. 이는 소수 사업자에 대한 정책적 개입만으로도 전 세계 접근이 좌우될 수 있다는 뜻이며, 다음 절에서 다룰 통제 국면과 직접 연결된다.

### 1.2 경쟁 축의 이동 — 맥락 분석

#### 1.2.1 3단계 이동 구조

앞의 데이터를 종합하면 미중 AI 경쟁의 성격은 세 단계로 이동해 왔다.

**1단계(2023~2024) 모델 성능 경쟁**에서는 파라미터 규모와 벤치마크 점수가 우위의 지표였다. 결과적으로 성능 격차가 Elo 2.7% 수준으로 축소·소멸했으며, 성능 자체로는 더 이상 우위를 확정할 수 없게 되었다.

**2단계(2024~2025) 컴퓨팅·인프라 확보 경쟁**은 성능이 상향평준화되자 경쟁이 학습·추론 자원 확보로 이동한 국면이다. 주요 수단은 GPU 수출통제, 데이터센터 건설, 전력 확보, CAPEX 확대였다. 컴퓨팅은 여전히 제약으로 작동하지만, 중국의 자립화 진척으로 통제만으로 봉쇄하기는 어려워졌다.

**3단계(2026~) 배포권·거버넌스 통제 경쟁**이 현재 국면이다. 모델을 만들 능력과 돌릴 자원을 완전히 봉쇄할 수 없다면, 남은 수단은 완성된 모델이 누구에게 도달하는지를 통제하는 것이다. 수단으로는 오픈웨이트 가중치 통제 논의, 고성능 모델 출시 사전검토, 신뢰 파트너 제도를 통한 접근권 계층화가 동원된다. 오픈웨이트 규제와 모델 출시 차단권 논의가 왜 지금 등장하는지는 이 지점에서 설명된다.

#### 1.2.2 경쟁 축 이동 정리표

| 구분        | 1단계 (2023~2024)   | 2단계 (2024~2025)        | 3단계 (2026~)           |
| --------- | ----------------- | ---------------------- | --------------------- |
| 경쟁 성격     | 모델 성능             | 컴퓨팅·인프라 확보             | 배포권·거버넌스 통제           |
| 핵심 자원     | 알고리즘·데이터·인재       | GPU·HBM·전력·데이터센터       | 모델 접근권·가중치·규범         |
| 주요 정책수단   | 사실상 없음(시장경쟁)      | 반도체 수출통제, 국가 컴퓨팅 투자    | 가중치 통제, 사전검토, 접근권 계층화 |
| 승패 기준     | 벤치마크 우위           | 확보 물량·전력               | 누가 누구의 접근을 끊을 수 있는가   |
| 대표 사건     | GPT-4·DeepSeek 등장 | AI 확산 규칙, NDRC 컴퓨팅 그리드 | 2026.06 프론티어 모델 접근 차단 |
| 한국의 노출 지점 | 모델 경쟁력            | GPU 확보 예산·HBM          | 모델 접근권 단절 리스크         |

#### 1.2.3 이 프레임에 대한 반증 가능성

균형을 위해 이 프레임의 한계도 명시한다.

첫째, 컴퓨팅 경쟁이 끝난 것이 아니다. CAPEX 7,250억 달러와 랩 간 컴퓨팅 임차는 2단계가 여전히 진행 중임을 보여준다. 따라서 3단계는 2단계를 대체한 것이 아니라 중첩된 것으로 보는 것이 정확하다.

둘째, 배포권 통제의 실효성 자체가 미확정이다. 중국 오픈웨이트가 배포 지형을 장악한 상황에서 통제는 미국 모델에만 적용되어 자국 산업만 제약할 수 있다는 비판이 미국 내에서 제기되고 있다. 이 논쟁은 2.4절에서 상세히 다룬다.

따라서 본 보고서는 "3단계로 완전히 이동했다"기보다 "통제 경쟁이 새로 추가되어 3층 구조가 되었다"는 관점을 취한다.

### 1.3 분석 범위 및 방법

대상 국가는 미국과 중국을 중심축으로 하고, 비교 대상으로 한국을 배치한다. EU와 일본, 대만은 벤치마킹 사례로만 참조한다. 대상 시기는 정책·규제 동향의 경우 2026년 4월부터 7월까지를 중점으로 하고, 기업 동향은 최근 3개월, 시장 데이터는 최근 6개월을 기준으로 삼는다. 4대 영역인 시장, 기업, 정책, 기술 가운데 본 보고서는 주제 특성상 정책·규제 영역에 비중을 두고, 시장·기업·기술 데이터는 정책 분석의 근거로 활용한다.

출처 신뢰도는 정부 공식문서와 법안 원문, 기업 공식성명, 공식 지수보고서를 1순위로 하고, 법무법인과 전략연구소 분석을 2순위, 전문 언론을 3순위로 둔다. 핵심 수치는 2개 이상 출처 교차검증을 원칙으로 하며, 출처 간 불일치는 본문에 명시한다. 확인되지 않은 사항은 추정하지 않고 확인되지 않음으로 표기한다.

---

## 2. 미국 심층 동향분석

### 2.1 오픈웨이트 모델 규제 움직임

#### 2.1.1 정책 경과 — 유보에서 부분 통제로

2024년 미국은 규제 유보를 권고했다. NTIA는 「Dual-Use Foundation Models with Widely Available Model Weights」 보고서에서 오픈웨이트 모델 가중치를 지금 제한하지 말되 위험을 모니터링하고 향후 제한 가능성을 유지하라는 신중한 낙관 노선을 권고했다.

> 출처 : [FACT SHEET: NTIA AI Report Calls for Monitoring, But Not Mandating Restrictions of Open AI Models(NTIA)](https://www.ntia.gov/other-publication/2024/fact-sheet-ntia-ai-report-calls-monitoring-not-mandating-restrictions-open-ai-models)

2025년 1월에는 폐쇄형 가중치만 통제 대상에 포함되었다. BIS의 「Framework for AI Diffusion」, 이른바 AI 확산 규칙은 신규 ECCN 4E091을 신설하여 폐쇄형 프론티어 모델 가중치를 최초로 수출통제 대상에 포함했다. 임계치는 10^26 연산을 초과해 훈련된 폐쇄형 모델이다. 결정적으로 오픈웨이트 모델 가중치는 CCL에 추가되지 않아 EAR99로 분류되면서 통제 대상에서 제외되었다. 현행 제도상 오픈웨이트는 통제 공백 상태인 것이다.

> 출처 : [BIS Issues Long Awaited Export Controls on AI(WilmerHale)](https://www.wilmerhale.com/en/insights/publications/20250205-bis-issues-long-awaited-export-controls-on-ai)

2025년 5월 이 규칙은 시행 이틀 전인 13일에 철회되었다. BIS는 규칙이 관료적이고 미국 혁신을 저해하며 동맹 외교를 훼손한다고 밝히면서 향후 대체 규칙 발표를 예고했다. 다만 ECCN 4E091은 공식 폐지되지 않아 CFR에 잔존하며, GAO는 2026년 5월 12일 결정(B-337935)에서 비집행의 적법성에 의문을 제기했다. 언제든 재활성화될 수 있는 잠재적 통제 수단이 남아 있는 셈이다.

> 출처 : [BIS Rescinds AI Diffusion Rule(Freshfields)](https://www.freshfields.com/en/our-thinking/blogs/a-fresh-take/bis-rescinds-ai-diffusion-rule-issues-notice-of-high-probability-enforcement-r-102kp9j)
>
> 출처 : [Department of Commerce Announces Rescission(BIS)](https://www.bis.gov/press-release/department-commerce-rescinds-biden-era-artificial-intelligence-diffusion-rule-strengthens-chip-related)

#### 2.1.2 현 상태 정리

오픈웨이트 규제의 현 상태는 제도적 공백과 재활성화 가능성의 병존으로 요약된다. 명시적 통제는 없고 오픈웨이트는 EAR99로 분류된다. 그러나 ECCN 4E091이 잔존하고 BIS 대체 규칙이 예고된 상태이며, 후술할 수출통제 지시 방식으로 실질적 통제가 우회 작동할 수 있다. 따라서 미국이 오픈웨이트를 규제하지 않고 있다는 판단은 정확하지 않으며, 규제 수단을 보류 상태로 보유하고 있다는 서술이 정확하다.

### 2.2 고성능 모델 출시 통제권 관련 동향

#### 2.2.1 행정명령 14409호 — 자발적 프레임워크의 형식

2026년 6월 2일 행정명령 14409호 "Promoting Advanced AI Innovation and Security"가 프론티어 모델의 사전 정부검토 프레임워크를 수립했다. 개발자는 자발적으로 최대 30일간 출시 전 접근을 정부, 즉 신뢰 파트너에게 제공할 수 있다. 3(c)조는 강제적 정부 라이선스나 사전승인, 허가 요건 창설을 승인하는 것으로 해석되지 않는다고 명시적으로 부인했다.

특히 주목할 점은 "covered frontier model"의 정의 방식이다. 고정 FLOPs 임계치가 아니라 NSA 주도의 기밀 사이버역량 벤치마킹 절차로 위임되어, 2026년 8월 1일경까지 임계치를 설정하도록 했다.

> 출처 : [New Executive Order Addressing Early Government Access to Frontier AI Models(WilmerHale)](https://www.wilmerhale.com/en/insights/client-alerts/20260602-new-executive-order-addressing-early-government-access-to-frontier-ai-models)

이 위임 방식은 두 가지 함의를 갖는다. 임계치가 비공개 기준으로 설정되므로 외국 기업이나 정부는 자국 모델이 대상인지 사전에 알기 어렵다. 또한 기준 변경이 입법 없이 가능하므로 통제 범위의 신축성이 높다.

#### 2.2.2 실증 사건 — 수출통제 지시를 통한 배포 차단

자발적 프레임워크라는 형식과 별개로, 실질적 통제 지렛대는 수출통제 권한이다. 2026년 6월 사건이 이를 입증했다.

| 시점 | 사건 |
|---|---|
| 2026.04.07 | Anthropic Project Glasswing 출범(사이버 방어 컨소시엄, AWS·Apple·Google·Microsoft·NVIDIA 등) |
| 2026.05 | OpenAI Daybreak 발표(계층형 사이버모델 접근) |
| 2026.06.02 | 행정명령 14409호 발효 |
| 2026.06.12 | 상무부 수출통제 지시(Lutnick 장관 서한) → Anthropic이 Claude Fable 5·Mythos 5를 전 고객 대상 중단 |
| 2026.06.26 | 미 정부가 Glasswing 파트너 포함 일부 미국 조직에 Mythos 5 복원 승인 |
| 2026.06.30 | 통제 해제 |
| 2026.07.01 | Fable 5 일반 복원 |
| 2026.07.09 | OpenAI GPT-5.6(Sol·Terra·Luna) 출시, 프리뷰 기간 정부에 신뢰 파트너 명단 공유 |
| 2026.07.14 | 백악관 사이버보안 클리어링하우스 Gold Eagle 공식 출범 |

> 출처 : [White House Frontier AI Model Access, July 2026(Vorp Labs)](https://vorplabs.com/ai-regulatory-updates/reports/2026-07-frontier-model-access)

이 사건의 정책적 함의는 세 가지다. 첫째, 신규 입법이 필요하지 않았다. 기존 수출통제 권한만으로 이미 출시된 모델의 전 세계 접근을 차단할 수 있음이 확인되었다. 둘째, 속도가 빨랐다. 지시부터 서비스 중단까지 실질적 지연이 없었으며 사전 협의나 유예 절차가 작동하지 않았다. 셋째, 복원이 계층적으로 진행되었다. 해제 과정이 일괄이 아니라 미국 조직 우선에서 일반 복원 순서로 이루어졌다. 통제 상태에서는 국적에 따른 접근 계층화가 즉시 발생한다는 뜻이며, 한국 사용자와 기업이 통제 국면에서 후순위에 놓일 수 있음을 시사한다.

#### 2.2.3 연방·주 입법 동향 — 임계치의 수렴

Great American AI Act(GAAIA) 토론초안이 최초의 포괄 연방 AI 거버넌스 프레임워크로 제시되었다. 2026년 6월 4일 Jay Obernolte 하원의원과 Lori Trahan 하원의원이 발의한 269페이지 분량의 초안이다. 프론티어 모델은 10^26 FLOPs 초과 훈련으로, 대형 프론티어 개발자는 연매출 5억 달러 초과로 정의한다. 프론티어 개발자에게 공시와 제3자 감사, 내부고발자 보호 의무를 부과하며, 3년간 주 법률 선점 조항을 포함한다. 선점은 모델 개발 규제에 한정되고 배포 후 활동과 일반법은 제외된다.

> 출처 : [Frontier AI Goes Federal: How the Great American AI Act Compares to State Laws(Future of Privacy Forum)](https://fpf.org/blog/frontier-ai-goes-federal-how-the-great-american-ai-act-compares-to-state-laws/)

컴퓨팅 임계치 10^26 FLOPs와 매출 5억 달러가 사실상 표준으로 수렴하고 있다.

| 규제 | 컴퓨팅 임계치 | 매출/비용 임계치 | 상태 |
|---|---|---|---|
| EO 14409(연방) | 고정 없음 — NSA 사이버역량 벤치마크 | 없음 | 시행 중 |
| GAAIA(연방 초안) | >10^26 FLOPs | >5억 달러(대형 개발자) | 토론초안(미발의) |
| California SB 53/TFAIA | >10^26 FLOPs | >5억 달러 | 시행(2026.01.01) |
| Illinois SB 315 | >10^26 연산 | >5억 달러 | 서명, 2027.01.01 시행 |
| NY RAISE Act | >10^26 연산 | >5억 달러 매출(원안 >1억 달러 컴퓨팅비용) | 2026.03.19 시행 |
| BIS ECCN 4E091 | >10^26 연산 | 해당없음 | 2025.05.13 철회(CFR 잔존) |

> 출처 : [California Enacts SB 53(Mayer Brown)](https://www.mayerbrown.com/en/insights/publications/2025/10/california-enacts-sb-53)
>
> 출처 : [Illinois Frontier AI Safety Law(Davis Wright Tremaine)](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/07/illinois-frontier-ai-safety-law)
>
> 출처 : [NY Overhauls Frontier AI Transparency Law(Davis Wright Tremaine)](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/04/ny-overhauls-frontier-ai-transparency-law)

Illinois SB 315은 2026년 5월 27일 하원 만장일치 통과와 6월 26일 주지사 이송을 거쳐 프론티어 모델 안전관행에 대한 연 1회 제3자 감사를 최초로 의무화했다. 주 법무장관이 위반당 최대 300만 달러의 민사벌을 부과할 수 있다.

> 출처 : [AI: The Washington Report — July 2026 Edition(Mintz)](https://www.mintz.com/insights-center/viewpoints/54941/2026-07-08-ai-washington-report-july-2026-edition)

임계치 수렴은 한국에 실무적 시사점을 준다. 10^26 FLOPs와 5억 달러가 국제 사실표준으로 굳어지면, 이 기준과 무관하게 설계된 국내 규제는 상호운용성 문제를 낳고 국내 기업은 이중 규제 부담을 지게 된다.

### 2.3 하드웨어 수출통제와의 연계 구조

미국의 통제는 세 개 계층으로 확장되는 구조를 이룬다. 첫 번째 계층은 칩이다. 첨단 컴퓨팅 IC가 ECCN 3A090과 4A090으로 통제되며, 2026년 H20과 성능을 낮춘 H200은 25% 수출세와 건별 라이선싱을 조건으로 2026년 1월 15일부터 대중 판매가 승인되었으나 프론티어 Blackwell급 B30A는 차단되었다. 두 번째 계층은 클라우드 접근으로, IaaS 접근과 VEU 검증최종사용자 제도가 해당한다. 세 번째 계층은 모델 가중치로, ECCN 4E091과 사실상의 수출통제 지시가 여기에 속한다.

> 출처 : [2026 AI export controls: chip rules and model choice(eCorpIT)](https://ecorpit.com/ai-regulation-export-controls-enterprise-models-2026/)

AI 확산 규칙 철회 후 미국은 단일 글로벌 프레임워크에서 국가별·건별 라이선싱 체제로 전환했다. 이는 예측가능성 측면에서 한국에 불리하다. 일괄 티어 체계에서는 자국의 위치를 사전에 알 수 있으나, 건별 라이선싱에서는 매 사안마다 외교적 협상이 필요하다. 동시에 협상 여지가 생긴다는 점에서 기회 요인도 된다. 한국의 HBM 우위가 협상 레버리지로 작동할 수 있는 구조다.

### 2.4 산업계·연구계 대응과 논쟁 구도

프론티어 랩과 규제 완화 진영의 입장이 명확히 갈린다. OpenAI와 Anthropic 등 프론티어 랩은 정부와의 사전검토와 컨소시엄 협력에 협조적이다. Project Glasswing, Daybreak, GPT-5.6 프리뷰 명단 공유 등이 이를 보여준다. 다만 이 협조가 자발적 선택인지 통제 회피를 위한 순응인지는 확인되지 않았다.

규제 완화 진영의 입장은 더 명확하다. 전 백악관 AI·크립토 고문이자 현 PCAST 공동의장인 David Sacks는 2026년 7월 17일 Kimi K3 벤치마크 결과를 계기로 프론티어 모델 사전승인을 위한 새 연방기관을 밀어붙이는 것은 AI 경쟁에서 지는 길이며, 스스로 발목을 잡으면 나머지 세계는 미국의 규칙을 따르지 않을 것이라고 공개 반대했다.

> 출처 : [White House Frontier AI Model Access, July 2026(Vorp Labs)](https://vorplabs.com/ai-regulatory-updates/reports/2026-07-frontier-model-access)

논쟁의 핵심 축을 정리하면 다음과 같다.

| 쟁점 | 통제 강화론 | 통제 완화론 |
|---|---|---|
| 근거 | 국가안보, 사이버·CBRN 오용 방지 | 혁신 저해, 오픈소스 생태계 위축 |
| 실효성 판단 | 프론티어 능력은 소수 랩에 집중되어 통제 가능 | 중국 오픈웨이트가 통제 밖에 존재해 무의미 |
| 결과 예측 | 오용 억제 및 시간 확보 | 미국 기업만 제약, 중국 스택으로 이탈 |
| 대표 사례 | 2026.06 Anthropic 차단 사건 | Kimi K3 개방 출시 |

이 논쟁이 미결 상태라는 점 자체가 한국 대응 설계의 전제가 된다. 어느 방향으로 결론이 나든 대응 가능한 이중화 구조가 필요하다.

---

## 3. 중국 심층 동향분석

### 3.1 미국 규제에 대한 정부 차원 대응

#### 3.1.1 대응 수출통제 — 희토류를 통한 역압박

중국은 2026년 6월 22일 미국 기업 10곳을 수출통제 목록에 추가했다. 여기에 미국의 희토류 독립 전략 핵심 기업인 MP Materials와 USA Rare Earth가 포함되었다. MP Materials는 연방투자 5.5억 달러를, USA Rare Earth는 16억 달러 LOI를 받은 기업이다. 미국의 공급망 자립 시도 자체를 표적으로 삼은 것이다.

IEA의 2024년 데이터 기준으로 중국은 자석용 희토류 채굴 60%, 정제 91%, 영구자석 제조 94%를 점유한다. 특히 중류에 해당하는 정제와 자석 단계의 집중도가 압도적이다.

> 출처 : [China Targets the U.S. Rare Earth Comeback(FDD, 2026.06.24)](https://www.fdd.org/analysis/2026/06/24/china-targets-the-u-s-rare-earth-comeback/)
>
> 출처 : [Rare Earth Export Restrictions One Year Later(CSIS)](https://www.csis.org/analysis/rare-earth-export-restrictions-one-year-later)

#### 3.1.2 국내 컴퓨팅 자립 의무화

중국은 조달 규제를 통해 외국산 가속기를 구조적으로 배제하고 있다. 2025년 8월 데이터센터 국산칩 50% 이상 조달 요건을 도입했고, 11월에는 국가 재정 지원 프로젝트에서 외국산 가속기를 전면 배제했다. 진척률 30% 미만 프로젝트는 이미 설치된 Nvidia와 AMD, Intel 하드웨어를 제거하도록 지시했다. 정부 조달 승인 목록에서도 Nvidia를 배제하고 Huawei와 Cambricon만 포함했다.

> 출처 : [Chinese AI Chips Landscape 2026(Presenc AI)](https://presenc.ai/research/chinese-ai-chips-landscape-2026)

이는 미국 통제에 대한 수동적 대응이 아니라, 자국 시장을 국산 생태계 육성 수요로 전환하는 능동적 산업정책이다.

### 3.2 오픈웨이트 전략의 역이용

#### 3.2.1 배포 지형의 장악

중국 오픈웨이트 모델은 실사용 기준으로 이미 다수 지위를 확보했다. OpenRouter 토큰 소비 기준으로 2026년 5월 중국 오픈웨이트 모델이 약 61%를 점유했다. 가장 많이 쓰이는 상위 5개 중 4개가 중국산이며, Meta Llama는 순위에서 이탈했다. Hugging Face 신규 LLM 파생모델의 약 40%가 Qwen 기반이고, 중국이 지난 1년 전체 다운로드의 약 41%를 차지했다.

> 출처 : [China's Open-Weight Takeover(Chris Zeoli / Datagravity)](https://www.datagravity.dev/p/chinas-open-weight-takeover)

Alibaba Qwen은 Hugging Face 누적 다운로드에서 Meta Llama를 추월했고, MIT 연구는 중국 오픈소스 모델이 총 다운로드에서 미국 모델을 추월했다고 밝혔다.

> 출처 : [What's next for Chinese open-source AI(MIT Technology Review, 2026.02.12)](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/)

#### 3.2.2 근프론티어 개방모델의 출현

Moonshot AI는 2026년 7월 17일 Kimi K3를 출시했다. 2.8조 파라미터로 세계 최대 오픈소스 모델을 주장하며, Frontend Code Arena 리더보드에서 1,679점으로 1위를 기록해 Claude Fable 5를 상회했다. 이 사건의 전략적 의미는 성능 순위 자체가 아니라, 미국 접근통제 체계 밖에 근프론티어급 모델이 존재하게 되었다는 사실이다. 미국이 자국 모델 접근을 통제하는 동안 동급 대안이 무료로 공개되는 구조가 성립한 것이다.

> 출처 : [White House Frontier AI Model Access, July 2026(Vorp Labs)](https://vorplabs.com/ai-regulatory-updates/reports/2026-07-frontier-model-access)

#### 3.2.3 전략적 의도 해석

중국의 오픈웨이트 공세는 단순한 기술 공개가 아니라 세 가지 전략 목표를 겨냥한 것으로 해석된다.

첫째는 생태계 락인이다. Qwen 기반 파생모델이 40%를 차지하는 구조는 글로벌 개발자의 도구와 워크플로우를 중국 스택에 종속시키며, 향후 전환비용이 진입장벽으로 작동한다. 둘째는 통제 무력화다. 미국이 가중치를 통제해도 동급 대안이 개방되어 있으면 통제의 비용은 미국 기업이 부담하고 효과는 상실된다. 셋째는 표준과 규범의 주도권이다. 사실상 표준을 선점하면 향후 국제 규범 논의에서 유리한 위치를 확보한다.

단, 이 해석은 정책 의도에 대한 추론이며 중국 정부의 명시적 전략 문서로 확인된 바는 아니다.

### 3.3 자국 반도체·인프라 대체 진척도

#### 3.3.1 AI 가속기 생산 계획

중국산 가속기 생산은 확대되고 있으나 성능 격차는 잔존한다.

| 항목 | 내용 |
|---|---|
| Huawei Ascend 910C | 2026년 약 60만개 생산 목표(2025년의 약 2배), Ascend 계열 전체 최대 160만 다이 |
| Ascend 950PR 성능 | 1.56 PFLOPS FP4 — H20의 약 2.8배 |
| 성능 격차 | 다가올 Ascend 950은 Nvidia VR200의 약 6% 성능 수준 |
| Cambricon | 2026년 약 50만개 목표(Siyuan 590·690 최대 30만) |
| SMIC | 2025년 매출 93억 달러(16% 증가), 2026년 110억 달러 초과 전망, 7nm 생산능력 2배 확대 계획 |

> 출처 : [Huawei to double output of Ascend AI chips(RCR Wireless)](https://www.rcrwireless.com/20250930/ai-infrastructure/huawei-ai-chips-2)
>
> 출처 : [Cambricon targets 500,000 AI chips in 2026(Tom's Hardware)](https://www.tomshardware.com/tech-industry/semiconductors/cambricon-targets-500000-ai-chips-in-2026-as-china-accelerates-domestic-hardware-push)

#### 3.3.2 HBM이 절대적 제약

중국 자립화의 실질적 상한은 HBM이다. 국산 HBM은 2026년 910C급 패키지 약 25만~30만개 수준으로 생산 상한을 규정한다. TSMC 다이뱅크, 즉 Sophgo를 경유해 확보한 약 290만 다이가 소진된 이후에는 SMIC 웨이퍼와 국산 CXMT HBM 패키징에 전적으로 의존해야 한다. TSMC는 이 건으로 10억 달러 벌금을 부과받았다.

다만 소프트웨어 측면의 진척은 빠르다. Huawei와 Cambricon, Hygon, Moore Threads가 DeepSeek V4 출시 당일 적응에 성공하여 동시 배포 단계에 진입했다.

> 출처 : [Huawei Ascend Production Ramp(SemiAnalysis)](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)

한국 관점에서 이 대목이 중요하다. 중국의 병목이 HBM이라는 사실은 한국의 HBM 우위가 미중 양측 모두에 대한 레버리지임을 의미한다.

#### 3.3.3 데이터센터·전력 인프라

NDRC 주도의 국가 AI 컴퓨팅 그리드 계획이 추진되고 있다. 2026년 6월 Bloomberg 보도에 따르면 향후 5년 약 2조 위안, 2,950억 달러 규모이며 국산칩 80% 이상 요건이 붙는다. 전력망 통합까지 포함하면 5조 위안, 약 7,400억 달러에 이른다. Nvidia와 AMD는 구조적으로 배제되며 China Mobile과 China Telecom이 운영을 주도한다.

> 출처 : [China plans $295 billion AI data center buildout with domestic chips(Yahoo Finance/Bloomberg)](https://finance.yahoo.com/sectors/technology/articles/china-plans-295-billion-ai-125238341.html)

다만 전력이 풍부하면 AI 경쟁에서 이긴다는 단순한 서사는 재검토가 필요하다. 동수서산 프로젝트는 과잉건설과 저활용, 전송 병목으로 다수 데이터센터가 유휴 상태다. 데이터센터 전력 수요는 2026년부터 2030년까지 3,000억~5,000억 kWh 증가할 전망으로, 같은 기간 전력수요 증가분의 18%를 차지한다.

> 출처 : [Abundant electricity isn't enough: China's overbuilt AI computing power is underused(ASPI)](https://www.aspistrategist.org.au/abundant-electricity-isnt-enough-chinas-overbuilt-ai-computing-power-is-underused/)

이는 한국 AI데이터센터 정책에도 시사점을 준다. 물리적 용량 확보와 실제 활용률은 별개의 과제이며, 수요 연계 없는 건설은 유휴자산을 낳는다.

### 3.4 자국 규제 체계 — 미국식 통제와의 성격 차이

중국은 2023년부터 생성형 AI 관리 잠행 조치를 시행하고 있으며, 콘텐츠와 이념 통제, 라벨링 의무가 중심이다. 미중 규제의 성격 차이를 정리하면 다음과 같다.

| 구분 | 미국 | 중국 |
|---|---|---|
| 규제 목적 | 국제 확산 차단, 국가안보 | 국내 콘텐츠·이념 통제 |
| 주요 수단 | 수출통제, 사전검토, 접근 계층화 | 서비스 등록, 콘텐츠 심사, 라벨링 |
| 규제 대상 | 모델의 대외 이동·배포 | 모델의 국내 산출물 |
| 오픈웨이트 취급 | 통제 공백(잠재적 통제 보유) | 적극 장려(대외 배포 전략) |

이 차이는 중요하다. 중국은 대외 배포를 장려하고 국내 산출물을 통제하는 반면, 미국은 대외 배포를 제한하고 국내 산출물은 상대적으로 자유롭게 둔다. 양국의 규제 방향이 정반대이며, 이 비대칭이 오픈웨이트 지형에서 중국에 유리하게 작동한다.

---

## 4. 한국과의 비교분석

### 4.1 5개 축 비교 프레임

| 구분 | 미국 | 중국 | 한국 |
|---|---|---|---|
| 모델·오픈웨이트 | 프론티어 최상위(Elo 1,503). 오픈웨이트는 통제 공백·잠재 통제 | 근프론티어 개방 공세(Kimi K3 2.8조). 배포 지형 61% 장악 | 주목모델 5개로 3위. 소버린 모델 약 300억 파라미터급, 한국어·비용효율 특화 |
| 컴퓨팅·인프라 | 하이퍼스케일러 CAPEX 7,250억 달러. 글로벌 컴퓨팅 3분의 2 통제 | NDRC 2,950억 달러 국산칩 그리드. 국산 가속기 연 100만개 이상 목표 | GPU 확보사업 2조 805억원(1만 5,000장 목표), 국가AI컴퓨팅센터 2조 5,000억원 이상 |
| 규제·거버넌스 | 10^26 FLOPs·5억 달러 수렴. EO 14409와 주법 병존, 연방 선점 논쟁 | 생성형 AI 잠행조치. 콘텐츠·라벨링 중심 | AI 기본법 시행(2026.01.22). 위험기반·진흥 중심, 계도기간 운영 |
| 공급망 위치 | 설계·SW 우위, 제조는 대만·한국 의존. 희토류 취약 | 희토류 중류 90% 이상 장악. HBM·선단공정 취약 | HBM 세계 우위. 로직·SW 취약. VEU 폐지로 직접 노출 |
| 생태계·인재 | 세계 인재 집중, 민간투자 2,859억 달러 | 대규모 내수·개발자 생태계 락인 전략 | AI 특허 인구당 1위, 도입률 증가 1위. 그러나 인재 순유출 OECD 35위, 민간투자 취약 |

### 4.2 한국의 현 좌표

#### 4.2.1 AI 기본법 체계와 미국식 통제의 정합성

「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」이 2026년 1월 22일 전면 시행되었다. 2024년 12월 26일 국회를 통과했으며 재석 264명 중 260명이 찬성했다. EU에 이어 세계 두 번째 포괄 AI 법률이지만, EU가 고위험 규제 적용을 2027년 말까지 유예한 상황이므로 실질적 전면 적용은 한국이 세계 최초다.

위험기반 접근으로 고영향 AI 사전관리와 영향평가, 생성형 AI 투명성 의무, 해외 사업자 국내대리인 지정을 부과한다. 전반적으로 EU AI Act 대비 진흥에 무게를 둔다. 과태료 계도기간을 1년 이상 운영할 예정이어서 실제 부과는 2027년 이후로 전망된다.

> 출처 : [2026년 1월 시행 앞둔 'AI 기본법'(MS TODAY)](https://www.mstoday.co.kr/news/articleView.html?idxno=99963)
>
> 출처 : [인공지능기본법 완벽 가이드(상상력집단)](https://edu.imaginationgroup.co.kr/korea-ai-basic-law-guide-2026/)

정합성 관점에서 두 가지 발견이 있다. 첫째, 오픈웨이트 모델 관련 별도 규정은 확인되지 않는다. 미국이 통제 공백 상태에서 잠재적 통제를 보유한 것과 달리 한국은 논의 자체가 부재하다. 둘째, 컴퓨팅 임계치 기반 분류 개념이 도입되지 않아 미국 연방·주 규제와의 기준 정합성이 확보되지 않았다.

#### 4.2.2 국가 GPU 확보 로드맵과 그 리스크

「2026년 AI컴퓨팅자원 활용기반 강화사업」은 2026년 3월 12일 공고되었다. 총사업비 2조 805억원으로 최신 GPU 1만 5,000장 확보를 목표로 한다. 협약기간은 2031년 12월 31일까지 약 68개월이며, 2026년 구축과 서비스 개시 후 2027년부터 2031년까지 운영하는 구조다. 정부가 GPU 구매·구축 비용을 지원하고 사업자가 GPUaaS 형태로 산학연에 제공한다. 2026년 6월 초 네이버클라우드, 삼성SDS, 엘리스그룹 3파전으로 최종 협상 단계에 진입했다.

> 출처 : [2조원 규모 국가 GPU 확충 닻 올렸다(ZDNet Korea, 2026.03.12)](https://zdnet.co.kr/view/?no=20260312182846)

HBM 가격 급등이 최대 리스크다. 업계는 메모리 가격 상승으로 동일 예산에서 확보 가능한 GPU 물량이 크게 줄었다고 지적하며, 유력 3사 제안 물량을 합쳐도 1만 5,000장 목표에 미달할 가능성을 제기했다.

> 출처 : [정부 GPU 프로젝트, 네이버·삼성·엘리스 3파전…목표 물량 확보는 '난제'(ZDNet Korea, 2026.05.13)](https://zdnet.co.kr/view/?no=20260513172238)

국가AI컴퓨팅센터는 별도 사업으로 총사업비 2조 5,000억원 이상이며 삼성SDS 컨소시엄이 단독 참여했다. 2030년까지 GPU 5만장 확보 로드맵을 가지며, 지분구조가 공공 30% 미만과 민간 70% 초과로 개편되고 국산 NPU 도입 의무 조항이 삭제되었다.

> 출처 : [9.9조원의 AI 예산, 2026년 정부 인프라 지원사업 정리(엑스디노드)](https://www.xdnode.co.kr/insight/articles/2026-government-ai-infrastructure-programs)

국산 NPU 의무 조항 삭제는 단기 확보 효율과 장기 국산화 사이의 상충을 보여주는 지점이다.

#### 4.2.3 3대 메가프로젝트

2026년 6월 29일 발표된 3대 메가프로젝트는 향후 10년간 반도체와 피지컬AI, AI데이터센터 3대 축에 1,500조원 이상 투자를 계획한다. 서남권 호남에 800조원 규모 반도체 생산거점 구축과 신규 메모리 팹 건설, AI 로봇 글로벌 3강 도약을 위한 3M 전략 추진이 포함된다.

다만 투자 규모 수치에 편차가 있다. 기업 투자계획으로 삼성 2,655조원과 SK 2,100조원이 거론되나, 정부 발표 기준 집계는 약 1,500조원 수준이며 4,700조원 수치와의 간극은 정부도 명확히 확인하지 않았다.

> 출처 : [Q&A로 보는 '3대 메가프로젝트'(PwC)](https://www.pwc.com/kr/ko/insights/issue-brief/mega-projects.html)
>
> 출처 : [3대 메가 프로젝트 환호 속에 던지는 다섯 개 질문(민들레)](https://www.mindlenews.com/news/articleView.html?idxno=21180)

#### 4.2.4 미국 수출통제 노출도 — VEU 폐지

2025년 9월 BIS는 삼성과 SK하이닉스의 중국 팹을 VEU 프로그램에서 제거했다. Intel Dalian과 TSMC Nanjing도 포함되었으며 2025년 12월 31일 발효되었다. 이후 연간 라이선스 체제로 전환되어 2026년분은 2025년 12월 30일 승인되었다.

기존 시설 운영은 허용되지만 증설과 기술 업그레이드 라이선스는 불허 방침이어서, 중국 내 경쟁사인 YMTC 등에 대응할 여지가 제약된다. 삼성 시안 팹은 삼성 자사 NAND 생산량의 약 40%를 담당하는 유일한 해외 NAND 거점이다. 세계 NAND의 40%가 아니라는 점에 유의해야 한다.

> 출처 : [US Policy Shift Complicates South Korean Semiconductor Operations in China(The Diplomat)](https://thediplomat.com/2025/09/us-policy-shift-complicates-south-korean-semiconductor-operations-in-china/)
>
> 출처 : [U.S. Export Controls and China: Advanced Semiconductors(Congress.gov CRS R48642)](https://www.congress.gov/crs-product/R48642)

#### 4.2.5 Stanford AI Index 2026 기준 한국 좌표

강점은 세 가지다. 주목모델 5개로 세계 3위이며 미국 50개, 중국 30개 다음이고 전년 4위에서 상승했다. 5개 중 4개가 LG AI연구원의 EXAONE 등 산출물이다. 인구 10만명당 AI 특허는 14.31개로 2년 연속 세계 1위이며 룩셈부르크 12.25, 중국 6.95, 미국 4.68을 앞선다. AI 도입률 증가폭도 세계 1위로, 2025년 상반기 25위에서 하반기 18위로 4.8%p 상승했다. G20 중 2016년부터 2025년까지 AI 입법은 2위다.

약점은 민간 AI 투자 취약과 AI 인재 순유출이다. 인재 순유출은 OECD 38개국 중 35위다.

> 출처 : [Korea ranks 3rd globally in key AI models, securing top spot for patents(The Korea Times, 2026.04.14)](https://www.koreatimes.co.kr/southkorea/others/20260414/korea-ranks-3rd-globally-in-key-ai-models-securing-top-spot-for-patents)
>
> 출처 : [South Korea ranks third in notable AI models, tops patents(MLex)](https://www.mlex.com/mlex/artificial-intelligence/articles/2464910/)

#### 4.2.6 인프라 계층별 국산화 — 비대칭 구조

한국은 HBM에서 세계적 우위를 보유하나 나머지 계층은 취약하다. AI 가속기와 클라우드 소프트웨어, 프론티어 모델 계층은 미국·중국에 의존한다. EXAONE, HyperCLOVA X, Solar Pro, A.X, VARCO 5개 소버린 모델은 약 300억 파라미터급으로 규모보다 비용효율과 한국어 특화로 경쟁한다. 메모리 상류는 강하지만 GPU와 SW, 프론티어 모델 하류는 의존하는 비대칭 구조다.

> 출처 : [Patent Leader, Talent Rank 35th — K-AI's Paradox(Pebblous)](https://blog.pebblous.ai/report/hai-ai-index-2026-part2/en/)

### 4.3 격차·공백 지점 식별

위 비교를 통해 도출되는 격차와 공백은 다섯 가지다.

**첫째, 모델 접근권 단절 리스크에 대한 제도적 대비가 부재하다.** 2026년 6월 사건처럼 미국 프론티어 모델 접근이 차단될 경우, 한국 정부와 기업 차원의 대응 절차나 백업 체계가 확인되지 않는다.

**둘째, 오픈웨이트 관련 정책 논의가 부재하다.** 미국은 통제 여부를 논쟁 중이고 중국은 전략적으로 활용하고 있으나, 한국은 오픈웨이트에 대한 정책 입장이 정립되지 않았다.

**셋째, 규제 기준의 국제 정합성이 미확보 상태다.** 10^26 FLOPs와 5억 달러 기준이 사실표준화되는 중이나 AI 기본법에 대응 개념이 없어, 국내 기업의 이중 규제 부담과 규범 논의 참여 자격 문제가 발생한다.

**넷째, 인프라 확보의 단가 리스크 관리가 부재하다.** GPU 확보 목표가 물량 기준으로만 설정되어 HBM 가격 변동에 대한 예산 탄력성이 확보되지 않았다.

**다섯째, 인재 순유출이 지속가능성을 위협한다.** 특허 1위와 모델 3위의 산출 역량에도 인재 순유출이 OECD 35위라는 것은, 현재 성과가 축적된 자산에 의존하며 지속가능성이 취약함을 시사한다.

---

---

title: 미중 AI 패권경쟁 대응방안·실행계획 (5~6장 개정본) publish: false type:

- report tags:
- AI패권경쟁
- 오픈웨이트
- 수출통제
- GPU조달
- AI인프라 source: '' created: 2026-07-30 modified: 2026-07-30

---

# 5. 대응방안

## 5.0 전개 방향 전제

대응방안 설계 전에 향후 전개 가능성을 3안으로 압축하여 전제로 둔다.

|구분|① 통제 강화·블록화|② 통제 실효성 저하|③ 부분적 규범 합의|
|---|---|---|---|
|핵심 전개|미국 통제 상설화, 미중 병렬 생태계 고착|오픈웨이트 확산으로 통제 무력화|임계치·안전기준 국제 수렴|
|지지 근거|반도체 통제는 희토류 무기보다 오래갈 것, NDRC 2,950억 달러 국산화 그리드|중국 오픈웨이트 61% 점유, Kimi K3 근프론티어 개방|EU 10^25와 미국 10^26 수렴, 동맹 상호의존이 완전 블록화 억제|
|대표 견해|War on the Rocks 병렬 생태계론|David Sacks 규제반대론, MIT Tech Review|AI Frontiers 중견국 협력론|
|한국 영향|모델 접근권 후순위, VEU 추가 제약|중국 스택 의존 심화 리스크|규범 참여 기회, 기준 정합화 필요|

> 출처 : [The Burn and the Choke: Why Semiconductor Controls Will Outlast China's Rare Earth Weapon(War on the Rocks)](https://warontherocks.com/the-burn-and-the-choke-why-semiconductor-controls-will-outlast-chinas-rare-earth-weapon/) 출처 : [What Export Controls on Anthropic's Most Advanced Models Mean for Europe(AI Frontiers)](https://ai-frontiers.org/articles/what-export-controls-on-anthropics-most-advanced-models-mean-for-europe)

전개 방향 태그는 정책 제안 계층에만 적용한다. 기반 작업 계층은 어느 전개가 실현되어도 필요하므로 태그를 부여하지 않는다. 세 전개 중 어느 것이 실현될지 미확정이며, 특히 통제 강화론과 실효성 저하론이 미국 내에서 동시에 유효한 상태다.

제3국 파급효과도 전제에 포함한다. 미국의 프론티어 모델 통제는 부품과 인재, 테스트 인프라, 매출, 데이터를 제공하는 동맹국에 직접 타격을 준다. Anthropic Fable 5의 글로벌 중단 후 오스트리아는 2026년 6월 28일 EU 집행위에 Anthropic의 역내 유치 검토를 촉구했다. 미국이 동맹의 자원에 의존하면서 동맹을 향해 모델을 수출통제하는 전략은 유효기간이 제한적이라는 분석이 제기된다.

> 출처 : [What Export Controls on Anthropic's Most Advanced Models Mean for Europe(AI Frontiers)](https://ai-frontiers.org/articles/what-export-controls-on-anthropics-most-advanced-models-mean-for-europe)

## 5.1 대응방안 구성 원칙

대응방안을 권한 귀속에 따라 두 계층으로 구분한다. 이는 실행 주체와 산출물의 성격이 계층별로 근본적으로 다르기 때문이다.

각 대응안은 효과성, 실행가능성, 적합성 3축으로 평가한다. 효과성은 식별된 리스크를 실제로 완화하는 정도, 실행가능성은 권한·예산·시점·정보 접근의 확보 여부, 적합성은 문제 진단에 대한 답의 정확성과 수행 주체 역할과의 부합도를 뜻한다.

## 5.2 계층 A — 실행 과제

### 5.2.1 미국 규제 상시 감시 체계 가동

효과성 중 / 실행가능성 상 / 적합성 상

감시 대상은 네 가지다. BIS 대체 규칙의 오픈웨이트 통제 포함 여부, ECCN 4E091 재활성화 동향, GAAIA 정식 발의 경과, 주법 선점 조항의 적용 범위다. ECCN 4E091은 2025년 5월 규칙 철회 후에도 CFR에 잔존하며 GAO가 2026년 5월 비집행의 적법성에 의문을 제기한 상태이므로, 언제든 재활성화될 수 있는 잠재적 통제 수단으로 다룬다.

> 출처 : [BIS Rescinds AI Diffusion Rule(Freshfields)](https://www.freshfields.com/en/our-thinking/blogs/a-fresh-take/bis-rescinds-ai-diffusion-rule-issues-notice-of-high-probability-enforcement-r-102kp9j) 출처 : [Frontier AI Goes Federal: How the Great American AI Act Compares to State Laws(Future of Privacy Forum)](https://fpf.org/blog/frontier-ai-goes-federal-how-the-great-american-ai-act-compares-to-state-laws/)

감시 자체는 리스크를 완화하지 않으므로 효과성은 중으로 평가한다. 그러나 나머지 모든 판단의 선행조건이며, 산출물이 정보 정리와 분류체계 형태라 본부의 간접 지원 역할에 가장 부합한다.

### 5.2.2 수출통제 영향 추적 — GPU·HBM 조달 범위 한정

효과성 중 / 실행가능성 상 / 적합성 중

삼성과 SK하이닉스 중국 팹의 VEU 폐지 후속으로 연간 라이선스 갱신 상황을 분기별 추적한다. 2026년분은 2025년 12월 30일 승인되었으나 증설과 기술 업그레이드 라이선스는 불허 방침이 유지되고 있다.

> 출처 : [US Policy Shift Complicates South Korean Semiconductor Operations in China(The Diplomat)](https://thediplomat.com/2025/09/us-policy-shift-complicates-south-korean-semiconductor-operations-in-china/) 출처 : [U.S. Export Controls and China: Advanced Semiconductors(Congress.gov CRS R48642)](https://www.congress.gov/crs-product/R48642)

적합성을 중으로 평가한 이유는 반도체 수출통제가 산업통상부 소관이어서 AI인프라본부 업무와 직접 연결이 약하기 때문이다. 추적 범위를 GPU·HBM 조달 단가와 공급 시점에 미치는 영향으로 한정하면 적합성이 회복된다. 삼성 시안 팹이 자사 NAND 생산량의 약 40%를 담당하는 만큼 라이선스 불승인 시나리오의 파급 범위도 함께 검토한다.

### 5.2.3 차기 GPU 사업 단계 발주 설계

효과성 상 / 실행가능성 중 / 적합성 상

HBM 가격 급등으로 동일 예산에서 확보 가능한 GPU 물량이 크게 줄었고, 유력 3사 제안 물량을 합쳐도 1만 5,000장 목표에 미달할 가능성이 제기되었다.

> 출처 : [정부 GPU 프로젝트, 네이버·삼성·엘리스 3파전…목표 물량 확보는 '난제'(ZDNet Korea, 2026.05.13)](https://zdnet.co.kr/view/?no=20260513172238)

총액 고정과 물량 변동 방식에서 단계 발주와 물량 재조정 조항으로 전환하는 설계안을 마련한다. 다만 2026년 사업은 6월 초 최종 협상 단계에 진입했으므로 협약이 이미 체결된 경우 적용이 불가하다. 따라서 **적용 대상을 국가AI컴퓨팅센터(2030년까지 GPU 5만장 로드맵)와 2027년 이후 신규 사업으로 이동**한다. 실행가능성을 중으로 평가한 것은 이 시점 제약 때문이다.

> 출처 : [9.9조원의 AI 예산, 2026년 정부 인프라 지원사업 정리(엑스디노드)](https://www.xdnode.co.kr/insight/articles/2026-government-ai-infrastructure-programs)

### 5.2.4 활용률 기반 성과지표 도입

효과성 중 / 실행가능성 상 / 적합성 상

중국 동수서산 프로젝트는 과잉건설과 저활용, 전송 병목으로 다수 데이터센터가 유휴 상태다. 물리적 용량 확보와 실제 활용은 별개 과제이며 수요 연계 없는 건설은 유휴자산을 낳는다.

> 출처 : [Abundant electricity isn't enough: China's overbuilt AI computing power is underused(ASPI)](https://www.aspistrategist.org.au/abundant-electricity-isnt-enough-chinas-overbuilt-ai-computing-power-is-underused/)

AI데이터센터와 GPU 사업 성과지표에 확보 물량과 함께 실사용률, 대기시간, 유휴 시간대 분포를 병행 설정한다. 다만 기존 사업 협약에 유사 지표가 이미 포함되어 있을 가능성이 있어 중복 여부 확인이 선행되어야 한다.

### 5.2.5 모델 접근권 단절 자체진단

효과성 상 / 실행가능성 중 / 적합성 상

2026년 6월 12일 상무부 수출통제 지시로 Anthropic이 Claude Fable 5·Mythos 5를 전 고객 대상 중단했고, 6월 26일 복원은 미국 조직 우선으로 진행된 후 6월 30일 통제 해제와 7월 1일 일반 복원으로 이어졌다. 통제 국면에서 국적에 따른 접근 계층화가 즉시 발생하며 한국 사용자가 후순위에 놓일 수 있음을 보여준다.

> 출처 : [White House Frontier AI Model Access, July 2026(Vorp Labs)](https://vorplabs.com/ai-regulatory-updates/reports/2026-07-frontier-model-access)

공공 부문 전반은 권한 범위를 넘으므로 **본부 업무 범위 내 외부 모델 의존도 목록화로 한정**한다. 각 업무별로 사용 모델, 대체 가능성, 단절 시 업무 중단 여부를 정리한다.

### 5.2.6 소버린 모델 대체 가능성 실측

효과성 중 / 실행가능성 상 / 적합성 상

국내 5개 소버린 모델(EXAONE, HyperCLOVA X, Solar Pro, A.X, VARCO)은 약 300억 파라미터급으로 프론티어 경쟁이 아닌 비용효율과 한국어 특화 위치에 있다.

> 출처 : [Patent Leader, Talent Rank 35th — K-AI's Paradox(Pebblous)](https://blog.pebblous.ai/report/hai-ai-index-2026-part2/en/)

이를 주권 자산으로 재정의한다는 서술만으로는 실행 내용이 없으므로, **실제 업무 몇 건을 국내 모델로 전환해 성능 저하폭과 프롬프트·워크플로우 재작성 비용을 측정**한다. 측정 결과가 5.2.5의 자체진단과 결합되어 백업 체계 설계의 정량 근거가 된다.

### 5.2.7 EU·일본 대응 사례 정리

효과성 중 / 실행가능성 상 / 적합성 상

EU는 AI Act에서 10^25 FLOPs 이상을 systemic risk GPAI로 분류하고 Mistral AI 등 자국 프론티어 랩 보유와 소버린 컴퓨팅 투자를 병행한다. 다만 AI 가속기는 여전히 NVIDIA와 TSMC에 의존한다는 한계가 한국과 동일하다. 일본은 23개 품목 수출통제 지정 방식으로 미국 통제에 정렬했다.

> 출처 : [Europe AI Landscape 2026(explainx.ai)](https://explainx.ai/blog/europe-ai-landscape-sovereign-compute-eu-act-2026) 출처 : [Understanding U.S. Allies' Current Legal Authority to Implement AI and Semiconductor Export Controls(CSIS)](https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export)

## 5.3 계층 B — 정책 제안 과제

### 5.3.1 컴퓨팅 임계치 정합화

효과성 중 / 실행가능성 중 / 적합성 상 · 소관 과기정통부 · 유효 전개 ③ 필수, ① 유효

미국 연방·주 입법이 10^26 FLOPs와 매출 5억 달러로 수렴하고 EU가 10^25 FLOPs를 채택한 상황에서, AI 기본법 고영향 AI 기준에 컴퓨팅 임계치 개념 도입을 검토한다.

> 출처 : [California Enacts SB 53(Mayer Brown)](https://www.mayerbrown.com/en/insights/publications/2025/10/california-enacts-sb-53) 출처 : [Illinois Frontier AI Safety Law(Davis Wright Tremaine)](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/07/illinois-frontier-ai-safety-law)

목적은 규제 강화가 아니라 국내 기업의 이중 규제 부담 완화와 국제 규범 논의 참여 자격 확보다. 법률 개정보다 **시행령·고시 수준에서 먼저 검토**하면 실행가능성이 올라간다. 과태료 계도기간이 1년 이상 운영되어 실제 부과가 2027년 이후로 전망되므로 그 전까지가 검토 기한이 된다.

### 5.3.2 오픈웨이트 규정 공백 해소

효과성 중 / 실행가능성 중 / 적합성 상 · 소관 과기정통부 · 유효 전개 ②③ 필수

미국은 오픈웨이트를 EAR99로 분류해 통제 공백 상태에 두면서 잠재적 통제 수단을 보유하고 있고, 중국은 오픈웨이트를 대외 배포 전략으로 적극 활용한다. 한국 AI 기본법에는 오픈웨이트 모델 관련 별도 규정이 확인되지 않는다.

> 출처 : [BIS Issues Long Awaited Export Controls on AI(WilmerHale)](https://www.wilmerhale.com/en/insights/publications/20250205-bis-issues-long-awaited-export-controls-on-ai)

최소한 공개 가중치 모델의 안전성 평가 기준과 배포 책임 소재에 대한 해석 지침 마련이 필요하다.

### 5.3.3 공공 부문 모델 접근권 이중화 정책

효과성 상 / 실행가능성 중 / 적합성 상 · 소관 과기정통부·행정안전부 · 유효 전개 ① 필수, ②③ 유효

5.2.5의 자체진단과 5.2.6의 실측 결과를 근거로 공공 부문 전반의 이중화 정책을 제기한다. 공공과 국가 핵심 업무에 미국 프론티어 모델 단독 의존을 피하고 국내 소버린 모델을 최소 기능 백업으로 지정하는 방식이다. 백업 모델은 성능 동등성이 아니라 차단 시 업무 지속이 가능한 최소 수준을 기준으로 설계하며, 그 기준선은 5.2.6 실측치로 확정한다.

### 5.3.4 오픈웨이트 활용 가이드라인

효과성 상 / 실행가능성 중 / 적합성 상 · 소관 과기정통부·국가정보원 · 유효 전개 ②③ 필수

중국 오픈웨이트 모델이 OpenRouter 토큰 소비 기준 약 61%를 점유하고 Hugging Face 신규 파생모델의 약 40%가 Qwen 기반인 현실에서, 사용하지 않는다는 선택은 비현실적이다. 그러나 무제한 채택은 데이터 레지던시와 보안 리스크를 낳는다.

> 출처 : [China's Open-Weight Takeover(Chris Zeoli / Datagravity)](https://www.datagravity.dev/p/chinas-open-weight-takeover) 출처 : [What's next for Chinese open-source AI(MIT Technology Review, 2026.02.12)](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/)

비민감 개발·연구와 공공·민감 데이터를 구분하는 용도별 허용 구간 가이드라인이 필요하다.

### 5.3.5 중견국 연대 참여

효과성 중 / 실행가능성 중 / 적합성 상 · 소관 외교부·과기정통부 · 유효 전개 ③ 필수, ① 유효

EU, 일본, 대만, 네덜란드와 함께 미국 수출통제의 동맹국 예외 협상 및 국제 규범 임계치 표준화 논의에 공동 대응한다. 목표는 한국의 좌표를 통제 대상국에서 통제 설계 참여국으로 이동시키는 것이다. 효과가 장기에 걸쳐 나타나는 점이 효과성을 중으로 제약한다.

> 출처 : [Understanding U.S. Allies' Current Legal Authority to Implement AI and Semiconductor Export Controls(CSIS)](https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export)

### 5.3.6 피지컬AI 공급망 노출 점검

효과성 중 / 실행가능성 중 / 적합성 중 · 소관 산업통상부 · 유효 전개 ① 필수

중국은 2026년 6월 22일 미국 희토류 기업 MP Materials와 USA Rare Earth를 수출통제 목록에 추가하며 자립화 시도 자체를 표적으로 삼았다. IEA 2024년 데이터 기준 중국은 자석용 희토류 정제 91%, 영구자석 제조 94%를 점유한다.

> 출처 : [China Targets the U.S. Rare Earth Comeback(FDD, 2026.06.24)](https://www.fdd.org/analysis/2026/06/24/china-targets-the-u-s-rare-earth-comeback/) 출처 : [Rare Earth Export Restrictions One Year Later(CSIS)](https://www.csis.org/analysis/rare-earth-export-restrictions-one-year-later)

다만 희토류는 주로 자석·모터용이고 GPU 병목은 HBM과 CoWoS, 전력이므로 AI 인프라와의 직접 연결은 약하다. **점검 범위를 3대 메가프로젝트 2축인 피지컬AI·로봇으로 한정**하면 적합성이 회복된다. 로봇 구동계에 영구자석이 직접 사용되기 때문이다.

### 5.3.7 AI 인재 유출 대응

효과성 중 / 실행가능성 중 / 적합성 중 · 소관 범정부 · 유효 전개 ①②③ 공통

한국은 인구 10만명당 AI 특허 14.31개로 2년 연속 세계 1위이고 주목모델 5개로 3위이나, AI 인재 순유출은 OECD 38개국 중 35위다. 산출 성과와 인재 지표의 병존은 현재 성과가 축적 자산에 의존하며 지속가능성이 취약함을 시사한다.

> 출처 : [Korea ranks 3rd globally in key AI models, securing top spot for patents(The Korea Times, 2026.04.14)](https://www.koreatimes.co.kr/southkorea/others/20260414/korea-ranks-3rd-globally-in-key-ai-models-securing-top-spot-for-patents) 출처 : [Patent Leader, Talent Rank 35th — K-AI's Paradox(Pebblous)](https://blog.pebblous.ai/report/hai-ai-index-2026-part2/en/)

유출 원인은 급여와 연구환경, 커리어 경로에 있으므로 인프라 정책 단독으로 대응할 수 없다. 범정부 인재정책 과제로 이관하고, 본부 차원에서는 GPU·데이터센터 배분의 연구자 접근성 개선에만 한정한다.


---

# 6. 실행계획

## 6.1 단기 (3개월, 2026년 10월까지)

| 계층  | 과제                 | 산출물                 | 선행조건    |
| --- | ------------------ | ------------------- | ------- |
| A   | 미국 규제 상시 감시 체계 가동  | 월간 모니터링 양식 및 1차 보고  | 없음      |
| A   | 모델 접근권 단절 자체진단     | 본부 업무 외부 모델 의존도 목록  | 없음      |
| A   | 소버린 모델 대체 가능성 실측   | 성능 저하폭·재작성 비용 측정 결과 | 자체진단 완료 |
| A   | GPU 확보사업 협약 상태 확인  | 5.2.3 적용 대상 확정      | 없음      |
| A   | HBM 가격 전망 조달 반영 체계 | 가격 시나리오별 확보 물량 추정   | 없음      |
| A   | 수출통제 영향 추적 체계 수립   | 분기 추적 양식            | 없음      |

단기 과제는 모두 계층 A로 구성했다. 계층 B 제안은 근거 자료 없이 제기하면 설득력이 없으므로, A의 산출물이 B의 입력이 되는 순서를 따른다.

## 6.2 중기 (1년, 2027년 7월까지)

| 계층  | 과제                 | 산출물              | 선행조건         |
| --- | ------------------ | ---------------- | ------------ |
| A   | 차기 GPU 사업 단계 발주 설계 | 협약 조항 개선안        | 협약 상태 확인     |
| A   | 활용률 기반 성과지표 도입     | 실사용률·대기시간 KPI 정의 | 기존 지표 중복 확인  |
| A   | EU·일본 대응 사례 정리     | 비교 분석 자료         | 없음           |
| B   | 컴퓨팅 임계치 정합화 제안     | 시행령·고시 검토 의견서    | 규제 감시 3개월 축적 |
| B   | 오픈웨이트 규정 공백 해소 제안  | 해석 지침 필요사항 정리    | 규제 감시 3개월 축적 |
| B   | 공공 부문 이중화 정책 제안    | 정책 제안서           | 자체진단·실측 완료   |
| B   | 오픈웨이트 활용 가이드라인 제안  | 용도별 허용 구간 초안     | 실측 완료        |
| B   | 중견국 연대 참여 방안       | 참여 채널 검토 자료      | EU·일본 사례 정리  |
| B   | 피지컬AI 공급망 노출 점검 제안 | 산업부 제기용 자료       | 없음           |

계층 B의 컴퓨팅 임계치 정합화는 AI 기본법 계도기간이 2027년에 종료되므로 그 전까지 완료되어야 한다.

## 6.3 우선순위 판단 기준

아래 신호가 관측되면 해당 과제의 우선순위를 상향한다. 각 트리거는 외부에서 관측 가능한 사실로만 구성했다.

**트리거 1 — BIS 대체 규칙 공표.** 오픈웨이트 가중치 통제 또는 한국의 티어 강등이 포함되면 5.3.3 공공 부문 이중화 정책을 즉시 최우선으로 상향하고, 5.2.5 자체진단을 전 부처 범위로 확대 제기한다.

**트리거 2 — 미국 기업의 서비스 조건 변경.** 모델 카드 개정, 지역별 접근 조건 변경, 신뢰 파트너 제도 확대 등 공개 관측 가능한 변화가 나타나면 5.2.6 실측 범위를 확대한다. 당초 검토했던 "NSA 벤치마크 임계치 확인"은 트리거로 사용하지 않는다. 해당 임계치는 기밀 절차로 설정되어 사전 확인이 불가능하므로 관측 불가능한 조건이며, 대신 그 적용 결과인 기업 대응을 관측 지표로 삼는다.

**트리거 3 — HBM 현물가격 추가 급등.** GPU 확보 단가가 예산 대비 임계를 초과하면 5.2.3 단계 발주 설계를 즉시 차기 사업 협상에 반영하고 5.4.2 가격 전망 반영 주기를 단축한다.

**트리거 4 — 프론티어 모델 접근 차단 재발.** 5.3.3 이중화 정책을 제안 단계에서 시행 요구 단계로 전환한다.

**트리거 5 — GAAIA 정식 발의.** 주법 선점 조항이 포함된 상태로 발의되면 5.3.1 임계치 정합화의 시급성이 올라간다. 연방 기준이 단일화되면 국내 정합화 대상이 명확해지기 때문이다.

## 6.4 리스크 및 한계

**정보 비대칭이 구조적으로 존재한다.** 행정명령 14409호의 프론티어 모델 임계치가 NSA 기밀 절차로 설정되므로 한국은 자국 모델이 통제 대상인지 사전에 확인할 수 없다. 6.3의 트리거를 관측 가능한 지표로 재구성한 것은 이 한계에 대한 대응이지, 한계 자체의 해소는 아니다.

**계층 B의 실행은 본부 권한 밖이다.** 계층 B 7건은 소관부처가 채택하지 않으면 실행되지 않는다. 본부의 산출물은 근거 자료와 문제 제기이며, 정책 채택 여부는 통제 범위를 벗어난다. 따라서 계층 B의 성과는 정책 반영이 아니라 자료 제출과 협의 개시 여부로 측정해야 한다.

**시점 리스크가 남아 있다.** 5.2.3의 적용 대상은 2026년 GPU 사업 협약 체결 여부에 따라 달라진다. 협약이 이미 체결된 경우 2027년 이후 사업과 국가AI컴퓨팅센터에만 적용되며, 본 계획은 이 경우를 기본 전제로 작성했다.

**전개 방향이 미확정이다.** 5.0의 3안 중 어느 것이 실현될지 알 수 없으며, 통제 강화론과 실효성 저하론이 미국 내에서 동시에 유효하다. 계층 A는 전개와 무관하게 필요한 기반 작업으로 구성했으나, 계층 B는 전개별 우선순위가 달라지므로 트리거 관측에 따른 재조정이 필요하다.

**오픈웨이트 대응은 양면성을 갖는다.** 중국 오픈웨이트 활용은 미국 접근권 리스크를 줄이지만 다른 종류의 의존을 만든다. 5.3.4에서 용도 구분을 제안했으나 구분 기준 자체는 보안 소관 부처와의 별도 검토가 필요하다.


---
## 관련근거 및 출처

### 산업동향·시장·투자

> 출처 : [The 2026 AI Index Report(Stanford HAI, 2026.04.13)](https://hai.stanford.edu/ai-index/2026-ai-index-report)
>
> 출처 : [Stanford's AI Index for 2026 Shows the State of AI(IEEE Spectrum)](https://spectrum.ieee.org/state-of-ai-index-2026)
>
> 출처 : [Artificial Intelligence Market Size & Share Report, 2026-2033(Grand View Research)](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market)
>
> 출처 : [Artificial Intelligence (AI) Market Report 2026-2033(MarketsandMarkets)](https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-market-74851580.html)
>
> 출처 : [Google, Microsoft, Meta, and Amazon capex spending to hit $725 billion in 2026(Tom's Hardware)](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)
>
> 출처 : [Big Tech earnings slam into a market in revolt over AI spending(Fortune, 2026.07.26)](https://fortune.com/2026/07/26/big-tech-earnings-meta-microsoft-apple-amazon-market-revolt-ai-spending/)
>
> 출처 : [Best Open Source LLM 2026: DeepSeek, Kimi, Qwen Ranked(Tech Insider)](https://tech-insider.org/best-open-source-llm-2026/)

### 미국 정책·규제

> 출처 : [FACT SHEET: NTIA AI Report Calls for Monitoring, But Not Mandating Restrictions of Open AI Models(NTIA)](https://www.ntia.gov/other-publication/2024/fact-sheet-ntia-ai-report-calls-monitoring-not-mandating-restrictions-open-ai-models)
>
> 출처 : [BIS Issues Long Awaited Export Controls on AI(WilmerHale)](https://www.wilmerhale.com/en/insights/publications/20250205-bis-issues-long-awaited-export-controls-on-ai)
>
> 출처 : [BIS Rescinds AI Diffusion Rule(Freshfields)](https://www.freshfields.com/en/our-thinking/blogs/a-fresh-take/bis-rescinds-ai-diffusion-rule-issues-notice-of-high-probability-enforcement-r-102kp9j)
>
> 출처 : [Department of Commerce Announces Rescission of AI Diffusion Rule(BIS)](https://www.bis.gov/press-release/department-commerce-rescinds-biden-era-artificial-intelligence-diffusion-rule-strengthens-chip-related)
>
> 출처 : [New Executive Order Addressing Early Government Access to Frontier AI Models(WilmerHale, 2026.06.02)](https://www.wilmerhale.com/en/insights/client-alerts/20260602-new-executive-order-addressing-early-government-access-to-frontier-ai-models)
>
> 출처 : [White House Frontier AI Model Access, July 2026(Vorp Labs)](https://vorplabs.com/ai-regulatory-updates/reports/2026-07-frontier-model-access)
>
> 출처 : [Frontier AI Goes Federal: How the Great American AI Act Compares to State Laws(Future of Privacy Forum)](https://fpf.org/blog/frontier-ai-goes-federal-how-the-great-american-ai-act-compares-to-state-laws/)
>
> 출처 : [California Enacts SB 53(Mayer Brown)](https://www.mayerbrown.com/en/insights/publications/2025/10/california-enacts-sb-53)
>
> 출처 : [Illinois Frontier AI Safety Law(Davis Wright Tremaine)](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/07/illinois-frontier-ai-safety-law)
>
> 출처 : [NY Overhauls Frontier AI Transparency Law(Davis Wright Tremaine)](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/04/ny-overhauls-frontier-ai-transparency-law)
>
> 출처 : [AI: The Washington Report — July 2026 Edition(Mintz)](https://www.mintz.com/insights-center/viewpoints/54941/2026-07-08-ai-washington-report-july-2026-edition)
>
> 출처 : [2026 AI export controls: chip rules and model choice(eCorpIT)](https://ecorpit.com/ai-regulation-export-controls-enterprise-models-2026/)
>
> 출처 : [U.S. Export Controls and China: Advanced Semiconductors(Congress.gov CRS R48642)](https://www.congress.gov/crs-product/R48642)

### 중국 동향

> 출처 : [China Targets the U.S. Rare Earth Comeback(FDD, 2026.06.24)](https://www.fdd.org/analysis/2026/06/24/china-targets-the-u-s-rare-earth-comeback/)
>
> 출처 : [Rare Earth Export Restrictions One Year Later(CSIS)](https://www.csis.org/analysis/rare-earth-export-restrictions-one-year-later)
>
> 출처 : [Chinese AI Chips Landscape 2026(Presenc AI)](https://presenc.ai/research/chinese-ai-chips-landscape-2026)
>
> 출처 : [China's Open-Weight Takeover(Chris Zeoli / Datagravity)](https://www.datagravity.dev/p/chinas-open-weight-takeover)
>
> 출처 : [What's next for Chinese open-source AI(MIT Technology Review, 2026.02.12)](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/)
>
> 출처 : [Huawei to double output of Ascend AI chips(RCR Wireless)](https://www.rcrwireless.com/20250930/ai-infrastructure/huawei-ai-chips-2)
>
> 출처 : [Cambricon targets 500,000 AI chips in 2026(Tom's Hardware)](https://www.tomshardware.com/tech-industry/semiconductors/cambricon-targets-500000-ai-chips-in-2026-as-china-accelerates-domestic-hardware-push)
>
> 출처 : [Huawei Ascend Production Ramp(SemiAnalysis)](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
>
> 출처 : [China plans $295 billion AI data center buildout with domestic chips(Yahoo Finance/Bloomberg)](https://finance.yahoo.com/sectors/technology/articles/china-plans-295-billion-ai-125238341.html)
>
> 출처 : [Abundant electricity isn't enough: China's overbuilt AI computing power is underused(ASPI)](https://www.aspistrategist.org.au/abundant-electricity-isnt-enough-chinas-overbuilt-ai-computing-power-is-underused/)

### 한국 현황

> 출처 : [2026년 1월 시행 앞둔 'AI 기본법'(MS TODAY)](https://www.mstoday.co.kr/news/articleView.html?idxno=99963)
>
> 출처 : [인공지능기본법 완벽 가이드(상상력집단)](https://edu.imaginationgroup.co.kr/korea-ai-basic-law-guide-2026/)
>
> 출처 : [2조원 규모 국가 GPU 확충 닻 올렸다(ZDNet Korea, 2026.03.12)](https://zdnet.co.kr/view/?no=20260312182846)
>
> 출처 : [정부 GPU 프로젝트, 네이버·삼성·엘리스 3파전…목표 물량 확보는 '난제'(ZDNet Korea, 2026.05.13)](https://zdnet.co.kr/view/?no=20260513172238)
>
> 출처 : [9.9조원의 AI 예산, 2026년 정부 인프라 지원사업 정리(엑스디노드)](https://www.xdnode.co.kr/insight/articles/2026-government-ai-infrastructure-programs)
>
> 출처 : [Q&A로 보는 '3대 메가프로젝트'(PwC)](https://www.pwc.com/kr/ko/insights/issue-brief/mega-projects.html)
>
> 출처 : [3대 메가 프로젝트 환호 속에 던지는 다섯 개 질문(민들레)](https://www.mindlenews.com/news/articleView.html?idxno=21180)
>
> 출처 : [US Policy Shift Complicates South Korean Semiconductor Operations in China(The Diplomat)](https://thediplomat.com/2025/09/us-policy-shift-complicates-south-korean-semiconductor-operations-in-china/)
>
> 출처 : [Korea ranks 3rd globally in key AI models, securing top spot for patents(The Korea Times, 2026.04.14)](https://www.koreatimes.co.kr/southkorea/others/20260414/korea-ranks-3rd-globally-in-key-ai-models-securing-top-spot-for-patents)
>
> 출처 : [South Korea ranks third in notable AI models, tops patents(MLex)](https://www.mlex.com/mlex/artificial-intelligence/articles/2464910/)
>
> 출처 : [Patent Leader, Talent Rank 35th — K-AI's Paradox(Pebblous)](https://blog.pebblous.ai/report/hai-ai-index-2026-part2/en/)

### 전망·제3국 대응

> 출처 : [What Export Controls on Anthropic's Most Advanced Models Mean for Europe(AI Frontiers)](https://ai-frontiers.org/articles/what-export-controls-on-anthropics-most-advanced-models-mean-for-europe)
>
> 출처 : [The Burn and the Choke: Why Semiconductor Controls Will Outlast China's Rare Earth Weapon(War on the Rocks)](https://warontherocks.com/the-burn-and-the-choke-why-semiconductor-controls-will-outlast-chinas-rare-earth-weapon/)
>
> 출처 : [Europe AI Landscape 2026(explainx.ai)](https://explainx.ai/blog/europe-ai-landscape-sovereign-compute-eu-act-2026)
>
> 출처 : [Understanding U.S. Allies' Current Legal Authority to Implement AI and Semiconductor Export Controls(CSIS)](https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export)

---

## 부록 — 수치 사용 시 유의사항

본 보고서에 인용된 수치 중 출처 간 불일치가 있거나 확정되지 않은 항목을 정리한다. 발표자료로 전용할 경우 반드시 확인이 필요하다.

**시장규모**는 기관별 정의 차이로 2026년 추정치가 5,400억 달러에서 9,000억 달러까지 벌어진다. 단일 수치 인용은 피해야 하며, 정책 근거로는 Stanford AI Index의 기업투자액 5,817억 달러가 더 적절하다.

**주목모델 집계**에서 미국 50개·중국 30개와 미국 59개·중국 35개는 Epoch AI 등 집계 기준과 시점 차이에서 비롯된다. 한국 3위, 5개는 일관되게 확인된다.

**3대 메가프로젝트 투자규모**는 약 4,700조원이라는 기업 자체 집계와 약 1,500조원이라는 정부 발표 기준이 병존한다. 집계 기준과 집행 기간 차이로 정부도 명확히 확인하지 않았다. SK AI데이터센터 1,000조원은 미확보 외부조달분을 포함한 수치다.

**중국 칩 생산량**에서 Huawei 60만개와 Cambricon 50만개는 Bloomberg와 JPMorgan 추정치다. SMIC 수율과 HBM 공급 상한에 따라 실제 양산량은 이를 하회할 수 있다.

**삼성 시안 팹 40%**는 세계 NAND가 아니라 삼성 자사 NAND 생산량 기준이다. 혼용에 주의해야 한다.

**백악관 상시 접근승인 주장**과 관련해, 백악관이 프론티어 모델 접근을 상시 결정한다는 2026년 7월 17일 CNBC 보도는 익명 2개 출처에 기반하며 백악관이 공식 부인했고 독립 확증이 없다. 본 보고서는 이를 인용하지 않고, 문서와 기업성명으로 확인된 사실인 EO 14409, 6월 차단·복원 사건, GPT-5.6 프리뷰 정부 관여만 사용했다.

**GAAIA 임계치**는 269페이지 법안 원문의 직접 확인이 아닌 법률·정책 분석 2차 출처에 기반한다. 토론초안 단계로 정식 발의 전이다.