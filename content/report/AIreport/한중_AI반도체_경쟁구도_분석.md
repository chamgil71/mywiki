---
created: 2026-08-10
modified: 2026-08-10
publish: true
source: 본문출처, claude
tags:
- AI
- AI반도체
title: 한중 AI반도체 경쟁구도
type:
- report
---

```toc  
minLevel: 2
maxLevel: 2
```

---

# 한국-중국 AI반도체(NPU/AI가속기) 경쟁구도 

## ■ 전체 내용 요약 (작성일자: 2026.08.11)

**시장·기술 구도**
- AI반도체 시장은 GPU(2033년까지 81% 유지 전망)가 절대 규모를 유지하는 가운데, 워크로드가 학습에서 추론으로 전환되며 커스텀 ASIC·NPU가 CAGR 27%로 GPU(16%)보다 두 배 가까이 빠르게 성장하는 구조적 전환기에 있다.
- 이 전환은 'NPU가 GPU를 대체한다'는 단순 구도가 아니라, 엔비디아 자신도 토큰당 비용 절감형 아키텍처(Blackwell)로 추론에 대응하는 가운데, NPU·ASIC·TPU가 전력효율이라는 좁은 우위 지점을 파고드는 경쟁이다.

**데이터센터 vs 엣지, 중국 vs 한국**
- 데이터센터용 가속기에서 중국은 화웨이·캠브리콘을 축으로 정부 조달 화이트리스트와 대규모 자본(대기금 3기 475억 달러)을 앞세워 내수 자립을 가속(2025년 자국 점유율 41%→2030년 76% 전망)하는 반면, 한국은 리벨리온·퓨리오사AI가 국내 HBM·파운드리 연계와 전력효율로 차별화하며 2026년 양산·프리IPO 단계에 진입했다.
- 엣지·피지컬AI에서는 호라이즌 로보틱스(중국)가 완성차 1,000만 대 누적 출하로 압도적 규모를 확보한 반면, 딥엑스·모빌린트(한국)는 글로벌 다변화(해외매출 67%+)를 무기로 반복매출 전환의 초기 단계에 있다.

**결정적 승부처**
- 소프트웨어 생태계는 반도체 성능 자체보다 결정적인 경쟁축이다. 화웨이는 CANN 오픈소스화로 CUDA 추격 속도를 높이고 있는 반면, 한국은 4개 팹리스의 SDK 파편화로 집단 대응력이 화웨이 한 개 기업보다도 약하다.
- 제조·공급망(HBM·파운드리)은 한국의 가장 확실한 구조적 우위이나, MSIT 기술수준평가상 한중 AI반도체 기본역량 격차가 2년 새 2배 가까이 벌어진 것으로 나타나 안주할 수 없는 상황이다.
- 정책 측면에서 중국은 '규모와 강제력'(대기금·조달의무화)으로, 한국은 '실증과 자율참여'(K-클라우드·국민성장펀드)로 대응하고 있어 예산 규모·집행 강도에서 격차가 크다.

---

## 1. 서론: 풀스택 AI 생태계 속 AI가속기의 전략적 위치

### 1-1. 가트너 「Top AI Trends From China, 2026」 요지

- 가트너는 중국 AI를 저가형 대안이 아닌 반도체·모델·에이전트·로봇을 아우르는 '풀스택 자립' 생태계로 평가한다.
    - 2030년까지 중국 민간 AI인프라의 50% 이상이 국산 AI가속기로 채워질 것으로 전망하며, 중국 AI모델의 글로벌 기업 채택률도 2025년 5%에서 2027년 50%로 급증할 것으로 예측한다.
> 출처 : [Half of China's AI Accelerators Will Be Homegrown by 2030: Gartner Forecasts 'AI Full-Stack' Self-Reliance(BigGo Finance, 2026.08.09)](https://finance.biggo.com/news/813d32c3-af15-4bd8-8c1e-3a9604808118)

- 중국 기업의 54%가 이미 국산 AI모델을 에이전트 개발에 활용 중이며, 34%는 로봇 등 피지컬 AI를 적극 검토하고 있다.
    - 이는 AI가속기 수요가 단순 클라우드 추론을 넘어 에이전트·로봇 워크로드로 확장되고 있음을 시사한다.
> 출처 : [Half of China's AI Accelerators Will Be Homegrown by 2030(BigGo Finance, 2026.08.09)](https://finance.biggo.com/news/813d32c3-af15-4bd8-8c1e-3a9604808118)

### 1-2. 풀스택 AI 생태계에서 AI반도체의 역할과 비중

- 풀스택 AI 생태계는 하드웨어(반도체)를 최하단 기반층으로, 그 위에 파운데이션 모델, 에이전트 프레임워크, 로봇·피지컬AI 응용층이 쌓이는 구조다.
    - 반도체 계층이 나머지 세 계층의 연산·전력·비용 구조를 물리적으로 규정하기 때문에, 어떤 국가가 모델·에이전트 경쟁에서 앞서더라도 반도체 자립이 없으면 궁극적으로 외부 공급망에 종속된다는 것이 가트너 풀스택론의 핵심 함의다.
- 2026년 기준 전 세계 반도체 매출은 1.3조 달러를 넘어서고 이 중 AI반도체가 약 30%를 차지할 것으로 전망되는데, 이는 AI 생태계 전체 투자에서 하드웨어(반도체)가 차지하는 비중이 구조적으로 크다는 것을 보여준다.
> 출처 : [Gartner Forecasts Worldwide Semiconductor Revenue to Exceed $1.3 Trillion in 2026(Gartner, 2026.04.08)](https://www.gartner.com/en/newsroom/press-releases/2026-04-08-gartner-forecasts-worldwide-semiconductor-revenue-to-exceed-us-dollars-one-point-3-trillion-in-2026)

- 본 보고서는 풀스택 4개 계층 중 반도체(그중에서도 GPU를 제외한 AI가속기) 계층에 한정해 심층분석하며, 모델·에이전트·로봇 계층은 반도체 수요를 설명하는 배경으로만 다룬다.

### 1-3. 글로벌 AI반도체 경쟁 지형의 배경

- 엔비디아는 여전히 AI가속기 시장의 절대 강자로, 2033년까지도 GPU가 시장의 81%(약 4,860억 달러)를 점유할 전망이다.
    - 그러나 이 지배력의 이면에서 하이퍼스케일러(구글·아마존·MS·메타)가 자체 칩 개발로 GPU 의존을 낮추는 움직임이 본격화되고 있다.
> 출처 : [Bloomberg Intelligence: AI Accelerator Chips 2026 Outlook(Bloomberg LP, 2026.01.14)](https://www.bloomberg.com)

- 미국은 구글 TPU v7·아마존 Trainium3·MS Maia 200 등 자체 AI가속기로 엔비디아 종속을 낮추고 있다.
    - 구글 TPU v7(Ironwood)은 FP8 기준 4.6 PFLOPS로 엔비디아 B200(4.5 PFLOPS)을 근소하게 상회하며, 이미 제미나이 API 트래픽의 상당 부분을 자체 칩으로 처리한다.
> 출처 : [TPU v7, Google's answer to Nvidia's Blackwell is nearly here(The Register, 2025.11.06)](https://www.theregister.com/2025/11/06/googles_ironwood_tpus_ai/)

- 중국은 미국의 대중 수출통제를 계기로 국산화를 가속했고, 그 결과 화웨이·캠브리콘이 정부 조달 화이트리스트에 등재되며 내수 수요를 흡수하고 있다.
> 출처 : [Ball game's over—the US is out of the AI chip market in China(Brookings, 2026)](https://www.brookings.edu/articles/ball-games-over-the-us-is-out-of-the-ai-chip-market-in-china/)

- 한국은 리벨리온·퓨리오사AI·딥엑스·모빌린트 4개 팹리스가 각자 시장에서 유의미한 고객사를 확보했으나, 내수 수요 기반과 정부 지원 규모는 중국 대비 절대적으로 작다.
    - 국민성장펀드의 'K-엔비디아' 프로젝트가 2026년 리벨리온에 첫 직접투자(2,500억원)를 단행하며 국가 차원의 후원이 본격화된 단계다.
> 출처 : [국민성장펀드, AI 반도체 리벨리온에 2500억 쏜다(서울경제, 2026.03.30)](https://www.sedaily.com/article/20017612)

**국가별 AI가속기 경쟁 포지션 요약**

| 구분 | 미국 | 중국 | 한국 |
|---|---|---|---|
| 시장 지위 | GPU 절대우위 + 자체칩 병행 | 국산화 드라이브, 내수 중심 급성장 | 유니콘급 팹리스 4개, 추격 단계 |
| 대표 플레이어 | 엔비디아·구글TPU·아마존Trainium·MS Maia | 화웨이·캠브리콘·바이렌 등 | 리벨리온·퓨리오사AI·딥엑스·모빌린트 |
| 핵심 동력 | 하이퍼스케일러 자체 수요 | 정부 조달+수출통제 반사이익 | 국민성장펀드+민간 고객사 확보 |
| 약점 | 없음(구조적 우위) | 소프트웨어 생태계·첨단공정 | 내수 규모·정책 예산 절대량 |

### 1-4. 분석 대상: 풀스택 중 AI가속기(반도체) 계층

- 본 보고서는 가트너가 제시한 풀스택 AI 생태계 중 최하단 인프라 계층인 AI가속기(반도체)에 한정해 심층 분석하며, 그중에서도 GPU를 제외한 NPU·ASIC 계열에 초점을 둔다.

### 1-5. 분석 범위 및 방법론

- 분석 범위는 GPU를 제외한 NPU·ASIC 계열 AI가속기로 하되, 시장 규모 전망에서는 비교 기준점으로 GPU 수치를 병기한다.
- 기업 비교는 첨부 자료의 그룹핑(리벨리온·퓨리오사AI/딥엑스·모빌린트 vs 화웨이·캠브리콘·하이곤·바이렌·무어스레드·메타엑스/호라이즌·바이두쿤룬·알리바바T-Head)을 기준으로 한다.

---

## 2. 글로벌 AI반도체 시장 규모 및 세부그룹 전망

### 2-1. 시장 규모 계층구조 정의 — 용어 혼선 방지

시장 조사기관마다 "AI 시장"·"AI반도체 시장"·"AI가속기 시장"의 정의 범위가 달라 수치가 뒤섞이면 혼선이 생긴다. 본 보고서는 아래 4단계 계층으로 구분해 사용한다.

| 계층                            | 정의                      | 포함 범위                                  | 2026년 규모(대표치)                             |
| ----------------------------- | ----------------------- | -------------------------------------- | ----------------------------------------- |
| ① 전체 AI 시장                    | AI 관련 소프트웨어·서비스·하드웨어 총합 | SW·클라우드서비스·컨설팅·하드웨어 전체                 | 5,395억 달러(2033년 3조 4,973억 달러, CAGR 30.6%) |
| ② 전체 반도체 시장 중 AI반도체(광의)       | AI 워크로드용 반도체 전반         | CPU·GPU·가속기·네트워킹·메모리 등 데이터센터 AI 인프라 전체 | 전체 반도체(1.3조 달러)의 약 30% ≈ 3,900억 달러        |
| ③ AI가속기(협의, GPU+ASIC+NPU 연산칩) | 연산 가속기 칩 자체만            | GPU·TPU·NPU·ASIC 등 순수 연산칩              | 1,070~1,200억 달러(기관별 편차)                   |
| ④ 가속기 내 세부구분                  | GPU vs 커스텀 ASIC/NPU     | ③의 하위 구분                               | GPU 약 80%, 커스텀ASIC/NPU 약 20%              |

> 출처 : [Artificial Intelligence Market Size & Share Report(Grand View Research, 2026.06.18)](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market)
> 출처 : [Gartner Forecasts Worldwide Semiconductor Revenue to Exceed $1.3 Trillion in 2026(Gartner, 2026.04.08)](https://www.gartner.com/en/newsroom/press-releases/2026-04-08-gartner-forecasts-worldwide-semiconductor-revenue-to-exceed-us-dollars-one-point-3-trillion-in-2026)
> 출처 : [AI Chips Market Size, Share and Forecast, 2026-2033(Coherent Market Insights, 2026)](https://www.coherentmarketinsights.com/industry-reports/ai-chips-market)

**한계 및 주의사항**
- ②(광의 AI반도체)와 ③(협의 AI가속기)은 조사기관에 따라 경계가 다르다. IDC는 "지능형 데이터센터" 세그먼트(CPU+가속기+네트워킹 포함)를 2,810억 달러로 별도 집계하는데, 이는 ②와 ③ 사이 어딘가에 위치한 독자적 정의다.
> 출처 : [AI Chip Market Share 2026(Axis Intelligence, 2026)](https://axis-intelligence.com/ai-chip-market-share/)

- Precedence Research의 "AI in Semiconductor" 시장(2025년 650억 달러→2035년 2,506억 달러)은 ②·③ 어느 쪽과도 정확히 일치하지 않는 독자 정의이므로, 본 보고서에서는 참고치로만 사용한다.
> 출처 : [Artificial Intelligence in Semiconductor Market Size to Hit USD 250.63 Bn by 2035(Precedence Research, 2026.07.15)](https://www.precedenceresearch.com/artificial-intelligence-in-semiconductor-market)

### 2-2. AI가속기(협의) 시장 규모·성장률 및 GPU vs NPU·ASIC 전망

- 코히런트마켓인사이츠는 AI가속기(협의) 시장이 2026년 1,070억 달러에서 2033년 5,926억 달러로 성장할 것으로 전망한다.
    - 블룸버그 인텔리전스는 유사한 범위에서 2024년 1,160억 달러→2033년 6,040억 달러(CAGR 16%)로 전망하되, 이 중 커스텀 ASIC 세그먼트만 CAGR 27%로 GPU보다 훨씬 빠르게 성장한다고 명시한다.
> 출처 : [AI Chips Market Size, Share and Forecast, 2026-2033(Coherent Market Insights, 2026)](https://www.coherentmarketinsights.com/industry-reports/ai-chips-market)
> 출처 : [Bloomberg Intelligence: AI Accelerator Chips 2026 Outlook(Bloomberg LP, 2026.01.14)](https://www.bloomberg.com)

- GPU는 2033년까지도 시장의 81%(약 4,860억 달러)를 유지하는 반면, 커스텀 ASIC·NPU는 2024년 8%에서 2033년 19%(1,180억 달러)로 비중이 두 배 이상 확대된다.
> 출처 : [Bloomberg Intelligence: AI Accelerator Chips 2026 Outlook(Bloomberg LP, 2026.01.14)](https://www.bloomberg.com)

- 카운터포인트 리서치는 하이퍼스케일러의 커스텀 AI ASIC 출하량이 2024년 대비 2027년 3배로 증가하고, 2028년에는 GPU 출하량을 추월할 것으로 전망한다.
> 출처 : [Counterpoint Research: Custom AI ASIC Shipment Forecast(Counterpoint Research, 2026.01)](https://www.counterpointresearch.com)

**AI가속기(협의) 세부그룹별 시장 규모 전망 비교**

| 조사기관 | 2026년 규모 | 2030~2033년 전망 | CAGR | 비고 |
|---|---|---|---|---|
| Bloomberg Intelligence | (2024년 1,160억 달러) | 6,040억 달러(2033) | 16% | 커스텀ASIC CAGR 27% 별도 명시 |
| Coherent Market Insights | 1,070억 달러 | 5,926억 달러(2033) | - | GPU·TPU·NPU 포괄 |
| Mordor Intelligence | (2024년 1,405.5억 달러) | 4,403억 달러(2030) | 25% | ASIC 최고 성장 세그먼트로 명시 |
| MarketsandMarkets(데이터센터가속기 한정) | - | - | 16.9% | ASIC 세그먼트만 29.2% |

> 출처 : [AI Accelerators Market Size, Share & 2030 Trends Report(Mordor Intelligence, 2026)](https://www.mordorintelligence.com/industry-reports/ai-accelerators-market)
> 출처 : [Data Center Accelerator Market Size, Share, Latest Trends & Growth Analysis(MarketsandMarkets, 2026)](https://www.marketsandmarkets.com/Market-Reports/data-center-accelerator-market-48984803.html)

### 2-3. 데이터센터용 vs 엣지용 시장 규모 구분

- 데이터센터·클라우드가 2024년 가속기(협의) 매출의 75%를 차지하나, 엣지 세그먼트가 CAGR 27%로 더 빠르게 성장하고 있다.
    - 엣지 성장은 중국 EV(전기차)와 한국 팹리스(딥엑스·모빌린트)의 산업·자동차용 AI가속기 수요가 견인하고 있다.
> 출처 : [Hardware Acceleration Market Outlook 2025-2032(AI2Work, 2026)](https://ai2.work/blog/ai-business-hardware-acceleration-market-2025)

### 2-4. 지역별(미·중·한) 점유율 및 투자 동향

- 엔비디아는 2024년 중국 지능형컴퓨팅 칩 시장의 76%(범용 GPU 세그먼트는 98%)를 점유했으나, 중국 국산 제조사가 2025년 약 165만 장을 출하하며 국내 AI서버 시장의 41%까지 확대했다.
    - 중국 지능형컴퓨팅 칩 시장 자체는 2024년 301억 달러에서 2029년 2,012억 달러로 CAGR 46%의 초고속 성장이 예상된다.
> 출처 : [Biren Technology 투자설명서(2025)](https://siliconangle.com/2025/12/31/chinese-graphics-card-maker-biren-raises-717m-ipo/)

- 한국 AI칩 시장은 2024년 24.9억 달러에서 2032년 146.8억 달러로 성장(CAGR 19.4%)할 것으로 전망되며, 이는 중국 시장 성장률(46%)의 절반 이하 수준이다.
> 출처 : [South Korea AI Chip Market(MarketsandMarkets, 2026)](https://www.marketsandmarkets.com/Market-Reports/south-korea-ai-chip-market-87237882.html)

---

## 3. 학습에서 추론으로 — AI가속기 경쟁구도의 전환

### 3-1. 워크로드 전환: 학습(Training) 중심에서 추론(Inference) 중심으로

- AI 산업의 무게중심이 대규모 모델 학습에서 상시 가동되는 추론 서비스로 이동하고 있다.
    - 학습은 대규모 병렬 GPU가 유리하지만, 추론은 토큰당 비용·지연시간·전력이 핵심 변수이며 이 지점에서 워크로드 특화 칩의 경제성이 부각된다.
> 출처 : [The Next Battlefield for AI Chips: From Training to Inference(TSPA Semiconductor, 2026.04.07)](https://tspasemiconductor.substack.com/p/the-next-battlefield-for-ai-chips)

### 3-2. GPU 대응 AI가속기가 부각되는 이유 — GPU도 추론을 겨냥한다는 점을 포함해

- 추론 전환이 곧 "NPU가 GPU를 대체한다"는 의미는 아니다. 엔비디아 자신도 토큰당 비용 절감과 처리량 극대화를 목표로 하는 풀스택 추론 아키텍처(Blackwell)로 진화하고 있으며, 2026년 데이터센터 매출 기준 엔비디아는 여전히 병합 시장의 87.4%를 점유한다.
    - 엔비디아가 추론 특화 스타트업 Groq를 인수한 것도 "추론에는 학습과 다른 실리콘이 필요하다"는 것을 인정한 방어적 행보로 해석된다.
> 출처 : [The Next Battlefield for AI Chips(TSPA Semiconductor, 2026.04.07)](https://tspasemiconductor.substack.com/p/the-next-battlefield-for-ai-chips)
> 출처 : [GPU vs LPU vs NPU: Infrastructure for the AI Inference Era(ModulEdge, 2026.04.06)](https://www.moduledge.com/blog/gpu-vs-lpu-vs-npu-ai-chip-infrastructure)

- 그럼에도 TPU·NPU·전용 ASIC이 특정 영역에서 부각되는 이유는 명확하다. GPU는 다양한 워크로드에 대응하는 "스위스 군용 칼"인 반면, ASIC/NPU는 특정 연산(트랜스포머 추론 등)에만 특화된 "단일 목적 도구"로서, 동일 성능 기준 전력소비를 절반 이하로 낮출 수 있다.
> 출처 : [Comparing AI chips: GPU, ASIC, and NPU(4sysops, 2026.03.20)](https://4sysops.com/archives/comparing-ai-chips-gpu-asic-and-npu/)

- 정리하면, 추론 전환은 GPU와 NPU·ASIC 모두에게 "추론 최적화"라는 같은 방향의 경쟁압력을 가하고 있으나, NPU·ASIC·TPU는 워크로드를 좁혀 전력효율에서 구조적 우위를 갖는 반면, GPU는 범용성과 성숙한 소프트웨어 생태계(CUDA)로 대응하는 것이 핵심 구도다.

**GPU vs TPU/NPU/ASIC 추론 경쟁 구도 요약**

| 구분 | GPU(엔비디아 Blackwell 등) | TPU/NPU/ASIC |
|---|---|---|
| 추론 대응 전략 | 토큰당 비용 절감형 아키텍처 개선(Blackwell), 추론 전문기업 인수(Groq) | 처음부터 특정 연산에 최적화된 전용 설계 |
| 강점 | 범용성, 성숙한 CUDA 생태계, 프레임워크 호환성 | 동일 처리량 기준 전력효율(성능/와트) 우위 |
| 약점 | 범용 설계로 인한 상대적 전력 비효율 | 워크로드 변화 시 유연성 부족, 소프트웨어 생태계 미성숙 |
| 대표 사례 | 메타·오픈AI의 여전한 주력 인프라 | 구글(TPU, 자사 추론 대체), 아마존(Trainium) |

### 3-3. 배치 위치(데이터센터/엣지)와 설계 방식(GPU/ASIC/NPU)은 별개의 두 축이다

**설계 방식 축**: ASIC(주문형 반도체)은 신경망 연산에 특화된 하위개념으로 NPU를 포함하며, TPU도 넓은 의미에서 ASIC의 한 종류다.

**배치 위치 축**: 이와 별개로, "칩이 어디에 놓이는가"는 완전히 다른 제약 조건에서 결정된다.

- **전력·발열 예산**: 데이터센터용 칩은 300~700W까지 허용되나(예: H100 700W), 엣지용 칩은 5~25W 수준으로 제한된다.
    - 화웨이 Ascend 310B1(엣지 NPU)은 8W TDP에서 동작하며, 동일 SoC 내 NPU가 GPU 대비 전력당 처리량에서 6.8배 우위를 보인다는 벤치마크 결과가 있다.
> 출처 : [The AI Chip Wars: NVIDIA, AMD, and Custom Silicon Explained 2026(Hakia, 2026)](https://hakia.com/tech-insights/ai-chip-wars/)
> 출처 : [AI-RAN on NPUs: Baseband Processing Without Baseband Chips(arXiv, 2026)](https://arxiv.org/pdf/2607.04224)

- **지연시간 요구**: 학습·클라우드 추론은 수백 밀리초의 네트워크 왕복을 허용하지만, 자율주행·산업로봇 등 실시간 엣지 애플리케이션은 한 자릿수 밀리초 응답이 필요해 연산을 물리적으로 데이터 발생지(공장, 차량, 카메라)에 배치해야 한다.
> 출처 : [AI Inference Infrastructure: Power & Cooling for Edge Racks(ModulEdge, 2026.03.03)](https://www.moduledge.com/blog/edge-ai-infrastructure-for-inference-translating-ai-servers-into-rack-power-cooling-and-module-design)

- **폼팩터·벤치마크 방법론**: 데이터센터용은 랙 마운트 서버·PCIe 카드 형태로 대규모 배치를 전제하는 반면, 엣지용은 M.2 모듈·SoC·스마트카메라 등 소형 폼팩터를 전제한다. MLPerf도 이 차이를 반영해 서버·엣지 시나리오를 별도로 평가한다.
> 출처 : [Edge AI Chip Benchmark Metrics That Matter(Troy Lendman, 2026)](https://troylendman.com/edge-ai-chip-benchmark-metrics-that-matter/)

- **결론**: 데이터센터용 ASIC(화웨이 Ascend, 캠브리콘 시위안)과 엣지용 ASIC(호라이즌, 딥엑스)이 모두 존재하는 것은 당연하며, ASIC을 엣지 카테고리로 한정하는 것은 부정확하다. 본 보고서는 이 두 축을 명시적으로 분리해 5~7장(데이터센터)과 8~10장(엣지)으로 장을 구성한다.

---

## 4. 비교 분석 프레임 설정

### 4-1. 데이터센터용 AI가속기 개요 및 중요성

- 데이터센터용 AI가속기는 클라우드·초거대 데이터센터에서 대규모 병렬 학습·추론을 처리하는 핵심 인프라로, AI가속기(협의) 시장 매출의 75%를 차지하는 최대 세그먼트다(2-3).
    - 이 영역의 경쟁력은 개별 기업의 기술력을 넘어 **국가 AI 주권(소버린 AI)**과 직결된다. 자국 데이터센터가 외국산 칩에 의존하면 모델 학습·서비스 운영 비용과 공급 안정성이 타국 정책·수출통제에 좌우되기 때문이다.
    - 중국이 정부 조달 화이트리스트와 80% 국산조달 의무화(13-1)를 데이터센터에 우선 적용하는 이유, 한국이 K-클라우드로 국산 AI칩의 데이터센터 점유율 80%를 목표(13-2)로 하는 이유가 여기에 있다.
- 경쟁의 승부처는 ①단일 칩 성능(TFLOPS/HBM대역폭), ②시스템 규모(SuperPoD·클러스터 단위 연산능력), ③소프트웨어 생태계(11장) 세 가지가 결합된 '시스템 경쟁'이라는 점이 5~7장 전체를 관통하는 전제다.

### 4-2. 엣지·피지컬AI용 AI가속기 개요 및 중요성

- 엣지용 AI가속기는 자동차·로봇·카메라·산업설비 등 온디바이스 환경에서 저전력·실시간 추론을 수행하며, 시장 규모는 데이터센터보다 작지만(25%) CAGR 27%로 더 빠르게 성장하는 영역이다(2-3).
    - 이 영역의 전략적 중요성은 **완성차·로봇 OEM의 대량양산 채택 여부**에 달려 있다. 데이터센터용이 소수의 하이퍼스케일러·정부기관을 고객으로 하는 반면, 엣지용은 자동차·가전·산업설비 제조사라는 훨씬 넓고 반복적인 고객군을 상대해, 한 번 설계 채택(design-win)되면 해당 모델의 생산주기(통상 5~7년) 동안 안정적 매출이 보장되는 구조다.
    - 가트너의 '피지컬AI' 전망(1-1)—중국 기업 34%가 로봇 등 피지컬AI를 적극 검토—이 시사하듯, 엣지 AI가속기는 다음 성장축인 휴머노이드 로봇 산업의 '두뇌'로서 향후 승부처가 될 잠재력이 크다(10-3).
- 데이터센터용이 정책·자본으로 견인되는 영역이라면, 엣지용은 완성차·로봇 제조사의 실제 채택 결정이 더 큰 변수로 작용해 시장 논리가 상대적으로 강하게 작동하는 영역이라는 차이가 8~10장의 분석 틀이 된다.

### 4-3. 배치 위치 기준: 데이터센터용 vs 엣지용

- ASIC·NPU 설계방식은 두 영역 모두에 존재하므로(3-3), 본 보고서는 5~7장(데이터센터)과 8~10장(엣지)으로 배치 위치 기준에 따라 장을 분리했다.

### 4-4. 한국-중국 대응 기업군 매핑

**데이터센터용**

| 한국 기업 | 중국 대응군 | 비교 성격 |
|---|---|---|
| 리벨리온 | 화웨이 하이실리콘, 캠브리콘, 하이곤 | 서버·클라우드 추론 NPU/가속기 |
| 퓨리오사AI | 캠브리콘, 화웨이, 바이렌 | 고성능·저전력 생성AI 추론 가속기 |
| 리벨리온·퓨리오사AI 공동 | 바이렌·무어스레드·메타엑스 | GPU형 범용 AI가속기(참고 비교군) |

**엣지·피지컬AI용**

| 한국 기업 | 중국 대응군 | 비교 성격 |
|---|---|---|
| 딥엑스 | 호라이즌 로보틱스, 화웨이 Ascend310, 바이두쿤룬, 알리바바 T-Head | 카메라·로봇·차량·스마트팩토리 |
| 모빌린트 | 호라이즌 로보틱스, 바이두쿤룬, T-Head | 산업자동화·로봇·엣지서버 |

### 4-5. 비교 평가축 정의

- 본 보고서는 5개 평가축(제품성능, 공급규모, 소프트웨어생태계, 양산능력, 고객확보)으로 기업별 경쟁력을 비교하며, 각 평가축은 5~10장의 기업별 심층분석과 종합비교 섹션에서 정량·정성 지표로 반복 적용된다.

---

## 5. 데이터센터용 AI가속기 — 중국 기업

### 5-1. 화웨이 하이실리콘(Huawei HiSilicon)

- 화웨이는 중국 AI GPU 시장에서 점유율 63%로 압도적 1위를 차지하는 국산 진영의 리더다.
    - 캠브리콘(10%)·핑터우거(8%)·쿤룬신(7%)을 합쳐도 화웨이 한 곳에 못 미치며, 4개사 합산 점유율이 약 88%에 달해 중국 AI가속기 시장은 사실상 소수 기업 과점 구조다.
> 출처 : [모건스탠리 중국 AI GPU 시장 전망(뉴스핌 GAM, 2026.08.04)](https://gam.newspim.com/news/view/20260804001128)

- 주력 제품 Ascend 910C는 SMIC 7nm 공정에 두 개 다이를 결합한 구조로, FP16 성능이 엔비디아 H100의 약 80% 수준으로 추정된다.
    - 2026년 생산 목표는 약 60만 장으로 전년 대비 두 배이며, Ascend 라인업 전체로는 최대 160만 다이 생산을 계획하고 있다.
> 출처 : [Huawei to double output of Ascend AI chips(RCR Wireless News, 2025.09.30)](https://www.rcrwireless.com/20250930/ai-infrastructure/huawei-ai-chips-2)

- 2025년 9월 화웨이커넥트에서 3년 로드맵을 공개했는데, 950PR(2026년 1분기, 프리필·추천 특화)과 950DT(2026년 4분기, 디코드·학습 특화)가 핵심이다.
    - 950DT는 910C 대비 약 2.5배 성능이며, 후속 960(2027년 4분기)·970(2028년)으로 엔비디아 블랙웰 세대를 추격하는 단계별 계획이다.
> 출처 : [Huawei Unveils Ambitious Three-Year AI Chip Roadmap with Self-Built HBM Technology(BigGo, 2025.09.18)](https://biggo.com/news/202509181252_Huawei_Reveals_AI_Chip_Roadmap_with_In-House_HBM)

- SMIC 7nm 공정의 실제 수율은 소식통에 따라 20%~60%로 편차가 크며, HBM 조달이 화웨이 어센드 생산의 최대 병목으로 지목된다.
    - SemiAnalysis는 SMIC가 다이 자체는 연 100만 개 이상 생산할 수 있으나 외국산 HBM 부족으로 실제 완성품 전환량이 제한된다고 분석했으며, TechInsights는 상당수 910B/910C 다이가 실제로는 TSMC 7nm 공정을 우회 활용한 것으로 확인해 TSMC가 10억 달러 벌금을 부과받았다고 보도했다.
> 출처 : [Huawei Ascend Production Ramp: HBM is The Bottleneck(SemiAnalysis)](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
> 출처 : [Huawei/HiSilicon Spotlight(SemiconductorX)](https://semiconductorx.com/spotlight-huawei-hisilicon.html)

- 화웨이는 캠브리콘과 함께 중국 정부 승인 AI 하드웨어 조달 리스트에 오른 단 2개 기업 중 하나로, 정책 수혜를 독점하고 있다(13장에서 상술).
> 출처 : [China drafts $295 billion plan to build a national AI data center grid running on 80% domestic silicon(Tom's Hardware)](https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips)

### 5-2. 캠브리콘(Cambricon, 688256.SH)

- 캠브리콘은 2026년 1분기 매출 28.85억 위안(약 4.23억 달러, +159.6% YoY)을 기록하며 '중국의 리틀 엔비디아'로 불리는 극적 반등을 보였다.
    - 2025년 연매출은 64.97억 위안(+453.2%)으로 2020년 상장 이후 첫 연간 흑자(순이익 20.59억 위안)를 달성했다.
> 출처 : [Chinese GPU maker Cambricon's Q1 revenue hits $423 million(Tom's Hardware/Yahoo Finance)](https://finance.yahoo.com/sectors/technology/articles/chinese-gpu-maker-cambricons-q1-103000723.html)
> 출처 : [Cambricon's Profit Soars 185% in Q1(MarketScreener)](https://www.marketscreener.com/news/cambricon-s-profit-soars-185-in-q1-revenue-jumps-160-on-ai-boom-ce7f58d8d080f020)

- 2025년 상반기 상위 5개 고객이 매출의 94%, 최대 단일고객이 약 80%를 차지하는 극단적인 고객 집중 구조를 보인다.
    - 중국 언론은 바이트댄스를 지배적 구매자로 지목했으며, Siyuan 590 약 20만 개를 선주문했다고 보도했다.
> 출처 : [China's Cambricon Shares Surge 14% After Q1 Revenue More Than Doubles(BigGo Finance)](https://finance.biggo.com/news/Yppf4Z0BDXrLZJaADbAR)

- 2026년 출하 목표는 50만 개(2025년 추정 11.6만 개)이며, SMIC 7nm 수율 약 20%가 최대 병목 변수로 지목된다.
    - PER 368배 고평가 논란으로 2일간 시가총액 1,400억 위안이 증발한 바 있어 밸류에이션 변동성이 크다.
> 출처 : [Cambricon's Trillion-Yuan Market Cap 'Day Trip'(BigGo Finance)](https://finance.biggo.com/news/98bc1a60-279a-4c01-9464-05c0a704b4fa)

### 5-3. 하이곤(Hygon, 688041.SH)

- 하이곤은 2025년 매출 143.77억 위안(+56.9%), 2026년 1분기 매출 40.34억 위안(+68.1%)으로 꾸준한 고성장을 이어가고 있다.
    - AMD Zen 아키텍처 라이선스 기반 x86 CPU와 DCU(8000 시리즈)를 결합한 'CPU+DCU 통합 컴퓨팅' 전략이 차별점으로, 2026년 시가총액은 약 1,010억 달러(P/E 약 190배)에 달한다.
> 출처 : [Inside Hygon's CPU-DCU Compute Stack(Leon Liao Substack)](https://leonliao.substack.com/p/inside-hygons-cpu-dcu-compute-stack)

- 2025년 5월 발표된 Sugon 116억 위안 규모 흡수합병이 2025년 12월 무산됐으나 양사는 공급망 협력을 유지하기로 했다.
> 출처 : [China's US$16.4B Chip Megamerger Collapses(TrendForce, 2025.12.11)](https://www.trendforce.com/news/2025/12/11/news-chinas-us16-4b-chip-megamerger-collapses-as-hygon-and-sugon-call-off-deal/)

### 5-4. 신흥 IPO 3사 — 무어스레드·메타엑스·바이렌

- 2025~2026년 중국 GPU 스타트업 IPO 러시가 폭발했으나, 3사 모두 여전히 대규모 적자 상태다.

**신흥 IPO 3사 비교**

| 기업 | 상장 시기·규모 | 2025년 손실 | 특이사항 |
|---|---|---|---|
| 무어스레드 | 2025.12.05 상하이 STAR마켓, 약 11억 달러, 첫날 +400%+ | 3분기 누적 약 59억 위안 | IPO 자금 약 90%를 은행상품에 예치 |
| 메타엑스 | 2025.12 STAR마켓, 청약률 무어스레드 상회 | 1~9월 3.46억 위안 | 前AMD 엔지니어 창업, C600 개발 중 |
| 바이렌 | 2026.01.02 홍콩 상장, 최대 6.24억 달러 | 상반기 약 90억 위안(+32.3%) | 중국 본토 최초 GPU 홍콩 상장사 |

> 출처 : ['China's Nvidia' Moore Threads surges over 400% on trading debut(CNBC, 2025.12.05)](https://www.cnbc.com/2025/12/05/china-nvidia-moore-threads-trading-debut-1-billion-listing-ipo-shanghai-gpu-enflame-biren.html)
> 출처 : [China's GPU IPO Wave Intensifies(TrendForce, 2025.12.11)](https://www.trendforce.com/news/2025/12/11/news-chinas-gpu-ipo-wave-intensifies-metax-surpasses-moore-threads-in-retail-investor-interest/)
> 출처 : [China's premier GPU maker Biren kicks off Hong Kong IPO(Tom's Hardware)](https://www.tomshardware.com/tech-industry/biren-kicks-off-hong-kong-ipo)

- 무어스레드는 IPO 자금 대부분을 R&D가 아닌 은행 상품에 예치해 '기술 자신감 부족' 논란이 일었으며, 신흥 3사의 밸류에이션은 정책·기대 주도의 투자 광풍(FOMO) 성격이 강하다는 지적이 나온다.
> 출처 : [Biren's $300M IPO: China's AI Chip Wave Hits Peak FOMO(byteiota)](https://byteiota.com/birens-300m-ipo-chinas-ai-chip-wave-hits-peak-fomo/)

---

## 6. 데이터센터용 AI가속기 — 한국 기업

### 6-1. 리벨리온(Rebellions)

- 2024년 SK텔레콤 자회사 사피온코리아와 합병하며 한국 첫 AI칩 유니콘으로 등극했고, 2026년 3월 국민성장펀드 'K-엔비디아' 직접투자 1호로 6,400억원 규모 프리IPO를 유치해 기업가치 3.4조원을 달성했다.
    - 2026년 8월 코스피 상장예비심사 청구를 앞두고 있으며, 2027년 상장 시 목표 기업가치는 5조원이다.
> 출처 : [리벨리온 뉴스룸(2026.03.30)](https://kr.rebellions.ai/newsroom/)
> 출처 : [리벨리온 비즈니스모델 분석(demoday.co.kr)](https://demoday.co.kr/bm-analysis/167)

- 2세대 제품 REBEL-Quad는 삼성 파운드리 4nm급(SF4X) 공정에 NPU 다이 4개를 결합한 칩렛 구조로, HBM3E 144GB·4.8TB/s를 탑재해 세계 최초로 UCIe-Advanced 인터커넥트를 적용했다.
    - FP16 기준 1페타플롭스 성능으로 엔비디아 H200 동등 이상을 주장하며, Hot Chips 2025와 ISSCC 2026에서 공개됐다.
> 출처 : [Rebellions AI Puts Together An HBM And Arm Alliance(The Next Platform, 2025.12.23)](https://www.nextplatform.com/2025/12/23/rebellions-ai-puts-together-an-hbm-and-arm-alliance-to-take-on-nvidia/)
> 출처 : [ISSCC 2026: Rebellions details industry's first quad-chiplet AI solution(Tom's Hardware)](https://www.tomshardware.com/tech-industry/semiconductors/isscc-2026-rebellions-ucie-rebel-100)

- 1세대 ATOM/ATOM-Max는 KT클라우드·SKT·Konan 등 국내 고객사에 이미 양산·배포되고 있다.
    - 매출은 2023년 27억원에서 2025년 350억원으로 늘었고 2026년 목표는 900억원으로, 일본·말레이시아·미국·유럽으로 시장을 확대할 계획이다.
> 출처 : [ZDNet Korea(2026.02.20)](https://zdnet.co.kr/)

### 6-2. 퓨리오사AI(FuriosaAI)

- 2세대 추론 칩 RNGD(레니게이드)를 2026년 1월 TSMC 공정으로 양산 개시했으며, 초도 물량 4,000장을 확보해 2026년 2만 장 양산을 목표로 한다.
    - 칩당 TDP 약 180W로 엔비디아(700~1,000W) 대비 저전력이며, 데이터센터 총소유비용(TCO)을 약 40% 절감하는 것으로 검증됐다.
> 출처 : [FuriosaAI RNGD Lands in Europe(Tech Times, 2026.07.11)](https://www.techtimes.com/articles/320154/20260711/furiosaai-rngd-lands-europe-koreas-power-efficient-inference-chip-reaches-equinix-lisbon.htm)

- 2025년 메타의 약 8억 달러 인수 제안을 거절하고 독자노선을 선택했으며, 프리머니 기업가치 약 20억 달러(약 3조원) 기준 최대 7,500억원 규모 프리IPO를 추진 중이다.
    - 자문사는 모건스탠리·미래에셋증권이며, LG AI연구원·삼성SDS·메가존클라우드 등을 고객·파트너로 확보했다.
> 출처 : [FuriosaAI Rejects Big Tech Path, Builds Independent Road to 2027 IPO(KoreaTechDesk)](https://koreatechdesk.com/furiosaai-pre-ipo-funding-meta-rejection-2027-korea-ai-chip)

---

## 7. 데이터센터용 한중 비교 종합

### 7-1. 영역별 자립 수준 비교 매트릭스

| 영역 | 중국 | 한국 |
|---|---|---|
| 가속기 설계 | 중상 — 30개+사, 화웨이·캠브리콘·하이곤 검증 | 중 — 리벨리온·퓨리오사 2개사, 설계력 인정 |
| 중저가·추론용 제품 | 상 — 대량양산·정책수요·낮은 TCO | 중상 — 추론 특화·전력효율 우위(TCO 40%↓) |
| 대규모 학습용 최고성능칩 | 중 — 950DT 등, 엔비디아 대비 약 2년 격차 | 하 — 학습칩 부재, 추론 집중 전략 |
| 첨단 파운드리 | 하 — SMIC 7nm, 수율 병목(20~60%) | 중 — 삼성 4nm 활용, 자체 파운드리 보유 |
| HBM | 하 — 화웨이 자체 HBM 초기 단계 | 최상 — SK하이닉스·삼성 세계 지배 |
| 첨단 패키징 | 중 — 칩렛·하이브리드본딩 자체개발 | 중상 — 삼성 I-Cube, OSAT 확대 중 |
| 개발 소프트웨어 | 중 — CANN 오픈소스화, CUDA 대비 열위 | 중 — 자체 SDK, vLLM/PyTorch 호환 |
| 데이터센터 시스템통합 | 상 — Atlas SuperPoD, 국가 컴퓨팅 그리드 | 중 — KT·삼성SDS 등 초기 배치 |

### 7-2. 2030년 한중 격차 시나리오

- 낙관 시나리오는 한국이 추론 중심 수요 전환과 HBM·첨단패키징 수직계열화로 글로벌 추론 시장 입지를 확보하는 경우다. 중국은 미국 수출규제 지속과 HBM 병목으로 자급 목표(76%)에 미달할 가능성을 전제한다.
- 현실 시나리오는 중국이 내수 자립 70%대를 달성하되 첨단 학습칩은 엔비디아 대비 약 2년 격차를 유지하고, 한국은 메모리·전력효율 우위를 지키되 시스템반도체(로직 설계) 격차가 구조적으로 지속되는 '분리 병존' 구도다.
- 비관 시나리오는 중국이 AI반도체 기본역량에서 한국을 지속 추월하고 CXMT의 D램·HBM 양산(2028~2030)이 한국 메모리 해자를 잠식하는 경우다.

### 7-3. 한국에 대한 시사점

- 삼성·SK하이닉스는 2024년 글로벌 HBM 시장을 합산 약 90%대 장악했으나, 2025년 경쟁 심화로 2분기 기준 합산 약 79%(SK하이닉스 62%+삼성 17%)로 조정됐다.
    - UBS는 엔비디아 차세대 Rubin 플랫폼용 HBM4에서 SK하이닉스가 약 70% 점유를 예상하는 반면, Counterpoint의 공식 전망은 54%로 더 보수적이어서 분석기관별 편차(54~70%)가 있다.
> 출처 : [SK hynix has won two-thirds of Nvidia's next-gen HBM orders(Korea JoongAng Daily)](https://www.koreajoongangdaily.com/business/sk-hynix-has-won-two-thirds-of-nvidias-next-gen-high-bandwidth-memory-orders-industry-sources/12030483)

- MSIT '2024 기술수준평가'에서 한국의 전체 기술수준은 미국(100%) 대비 82.7%인 반면 중국은 91.3%로, 한중 격차가 2022년 4.8%p에서 2024년 8.6%p로 확대됐다.
> 출처 : [中-韓 기술 격차, 2년 새 80% 더 벌어졌다(한국경제, 2026.02.22)](https://www.hankyung.com/article/2026022264921)
> 출처 : [KISTEP "中, 韓 반도체 기술 수준 추월"(글로벌이코노믹, 2025.02.23)](https://www.g-enews.com/article/Industry/2025/02/202502231842524392056c162803_1)

- 중국의 국산화 가속(외국산 의존 90%→60%→25% 전망)은 한국 팹리스의 대중 가속기 수출 기회를 구조적으로 축소시키는 반면, 한국 HBM은 중국이 아직 자립하지 못한 영역이라 협상력을 유지한다.
> 출처 : [China's AI Chip Self-Sufficiency Hits 41%, Korea Slips to 5th in Semiconductors(Seoul Economic Daily, 2026.04.17)](https://en.sedaily.com/finance/2026/04/17/chinas-ai-chip-self-sufficiency-hits-41-percent-korea-slips)

---

## 8. 엣지·피지컬AI 가속기 — 중국 기업

### 8-1. 호라이즌 로보틱스(Horizon Robotics, 9660.HK)

- 호라이즌은 2025년 매출 37.58억 위안(약 5.45억 달러, +57.7~59% YoY)을 기록했으나 R&D 투자 급증으로 순손실이 100억 위안을 넘어섰다.
    - 전환사채·우선주의 비현금성 공정가치 변동을 반영한 순손실은 105억 위안이며, 이를 제외한 조정영업손실은 24억 위안이다. 매출총이익률은 2024년 77.3%에서 2025년 64.5%로 하락했는데, 도메인 컨트롤러를 저마진에 공급하며 점유율과 이익률을 맞바꾼 결과다.
> 출처 : [Horizon Robotics' 2025 Revenue Soars Nearly 60%(BigGo Finance, 2026.03.23)](https://finance.biggo.com/news/OCQGGp0BZk7xib5fgFLX)

- Journey 시리즈 누적 출하량은 2025년 8월 1,000만 대를 돌파했으며, Journey 6 포트폴리오는 25개 이상 완성차·100개 이상 모델의 설계 채택을 확보했다.
    - 최상위 지능형주행 시장에서 화웨이(15.2%)에 근접한 14.4% 점유율로 격차를 0.8%p까지 좁혔고, 2026년 4월 폭스바겐 합작사 카리즌(Carizon)이 첫 대량양산 모델(위중06·07)을 출시했다.
> 출처 : [Horizon Robotics Partners with Volkswagen(Horizon Robotics)](https://www.horizon.auto/en/news/horizon-news/478)
> 출처 : [Horizon Robotics 2025 Financial Report(BigGo Finance, 2026.03.20)](https://finance.biggo.com/news/M8xIC50BvbjfYyetKZ3w)

- 2026년 하반기 로보택시 파일럿을 준비 중이며, 후속 Journey 7은 테슬라 차세대 칩을 목표 성능으로 2027년 출시 예정이다.
> 출처 : [Research insight: Horizon Robotics leads China's push for autonomous driving independence(Digitimes, 2025.11.19)](https://www.digitimes.com/news/a20251119PD232/market-horizon-robotics-autonomous-driving-automakers-adas.html)

### 8-2. 화웨이 Ascend 310 계열(엣지)

- Ascend 310은 12nm 공정 기반 AI SoC로, INT8 기준 최대 16~20 TOPS 성능을 8W 이하 전력에서 구현해 차량·산업설비 등 엣지 환경에 최적화됐다.
    - 차량·사람·장애물·교통표지 등 최대 200종의 객체를 동시 인식하고 초당 수천 장의 이미지를 처리할 수 있으며, 스마트시티·자율주행·신유통(뉴리테일)·로보틱스·산업제조·클라우드컴퓨팅 등 폭넓은 영역에 적용된다.
> 출처 : [HUAWEI Ascend(Baidu Baike)](https://baike.baidu.com/en/item/HUAWEI%20Ascend/1453477)
> 출처 : [Huawei | TechInsights](https://www.techinsights.com/vendor/huawei)

- 화웨이의 자율주행 도메인 컨트롤러 플랫폼(MDC)은 Ascend 310 NPU·타이산 코어·쿤펑 CPU·기린 SoC를 결합한 완결형 컴퓨팅 스택으로, 다빈치(DaVinci) 아키텍처 기반 CANN 소프트웨어가 TensorFlow·PyTorch 대비 학습곡선을 크게 낮췄다고 소개된다.
> 출처 : [Comprehensive Analysis of Huawei's Autonomous Driving Computing and Domain Control Platform Technology(Oreate AI Blog, 2026.01.07)](https://www.oreateai.com/blog/comprehensive-analysis-of-huaweis-autonomous-driving-computing-and-domain-control-platform-technology/a52d9a7adbeebc41b4ed40f9f387a12f)

- 2026년 WAIC(세계인공지능대회)에서 오렌지파이(Xunlong)와 화웨이가 협력해 Ascend Atlas 310B 기반 로봇 전용 컴퓨팅 모듈 'Orange Pi Robot 2'(20 TOPS, 12/24GB LPDDR4X)를 공개하는 등, 서드파티 하드웨어 생태계와의 협업을 통해 엣지 저변을 확대하고 있다.
> 출처 : [Orange Pi Maker Xunlong & Huawei Launch Edge AI at WAIC 2026(androidpimp.com, 2026)](https://www.androidpimp.com/product-news/orange-pi-xunlong-huawei-edge-ai-waic-2026)

### 8-3. 바이두 쿤룬신(Kunlunxin)

- 바이두는 2018년 중국 최초로 클라우드 기반 AI칩 쿤룬을 자체 개발했으며, 2020년부터 삼성전자와 합작해 14nm 공정으로 1세대 칩을 양산한 이력이 있다.
    - 자율주행 플랫폼 '아폴로'(2017년 공개, 오픈소스 생태계 전략)와 쿤룬 칩 개발을 연계해 엣지·자율주행 AI 자립을 추진해왔으며, 2024년 1월 기준 아폴로 누적 시험주행 거리는 약 9,000만km, 로보택시 호출 건수는 500만 건을 돌파했다.
> 출처 : [바이두(위키백과)](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%9D%B4%EB%91%90)
> 출처 : [자율주행, 새로운 지평을 열다(KDI 경제교육·정보센터)](https://eiec.kdi.re.kr/publish/reviewView.do?ridx=17&idx=179&fcode=000020003600003)

- 2026년 1월 바이두그룹은 AI칩 사업부 쿤룬신을 분사해 A주+홍콩 동시 상장(A+H)을 추진한다고 발표했다. A주 상장은 비교적 순조롭게 진행 중이나 홍콩 상장은 2026년 8월 기준 비공개 신청서 제출 단계에 머물러 있다.
    - 주력 상용 제품은 3세대 P800 칩이며, 순수 자체 개발 칩만으로 3만 2,000장 규모의 초대형 지능형 연산 클러스터를 구축한 바 있다. 2025년 바이두 AI사업 매출은 400억 위안, 이 중 쿤룬신 기반 스마트클라우드 인프라 매출이 198억 위안(2026년 1분기 88억 위안, +79% YoY)을 차지했다.
> 출처 : [[中 하드테크 IPO 빅뱅] ⑱쿤룬신, '바이두 AI제국' 성장엔진 A+H 상장(뉴스핌, 2026.08.04)](https://www.newspim.com/news/view/20260804001134)
> 출처 : [[中 하드테크 IPO 빅뱅] ⑳쿤룬신, 독자 AI 생태계로 '엔비디아 도전장'(뉴스핌, 2026.08.04)](https://gam.newspim.com/news/view/20260804001128)

### 8-4. 알리바바 T-Head(핑터우거)

- 알리바바는 2026년 1월 AI 반도체 설계 자회사 핑터우거(T-Head)를 직원 지분이 일부 포함된 별도 사업체로 재편한 뒤 기업공개를 검토 중이라고 블룸버그가 보도했다.
    - 다만 상장 시점과 구체적 일정은 2026년 8월 기준 확정되지 않았다. 에디 우 알리바바 CEO는 AI·인프라 확충에 530억 달러 이상을 투자하겠다고 밝혔으며, 투자 규모는 시간이 지나며 더 늘어날 수 있다고 언급했다.
> 출처 : [中 알리바바, AI 반도체 자회사 핑터우거 상장 검토(글로벌이코노믹, 2026.01.22)](https://www.g-enews.com/article/Global-Biz/2026/01/2026012221581784029a1f309431_1)

- 남중국모닝포스트(SCMP)는 알리바바·바이두 양사가 반도체 설계 부문 상장을 준비하면서, 엔비디아를 대체할 중국 내 고성능 AI칩 주요 공급업체 지위를 놓고 국내 다른 AI칩 개발사들과의 경쟁이 심화될 것으로 분석했다.
    - 엣지 응용은 알리바바 클라우드·IoT 생태계와 연계된 형태로 전개되며, 데이터센터용(2장·5장의 PPU·Hanguang 800) 대비 엣지 전용 비중은 상대적으로 작다.
> 출처 : [알리바바-바이두, AI 칩 설계 자회사 상장으로 중국 반도체 자립 가속(헬로티, 2026.01.26)](https://www.hellot.net/news/article.html?no=109661)

**소결(8장)**: 중국 엣지 AI가속기 진영은 자동차(호라이즌·화웨이)가 압도적으로 앞서 있고, 플랫폼 기업(바이두·알리바바)은 자사 클라우드·자율주행 생태계 내 수직계열화와 자본시장 상장을 동시에 추진하는 구조다. 자동차 엣지 시장은 상위 2개사(화웨이·호라이즌) 합산 약 30%를 점유하는 과점화 단계에 진입했으며, 바이두·알리바바의 반도체 부문 분사·상장은 엔비디아 대체 공급자 지위를 둘러싼 경쟁을 한층 심화시키고 있다.

---

## 9. 엣지·피지컬AI 가속기 — 한국 기업

### 9-1. 딥엑스(DeepX)

- 딥엑스의 시리즈D 프리머니 밸류는 3개월 만에 1조 8,000억원(2026.03)에서 2조 6,500억원(2026.06)으로 47% 급등했다.
    - 6,000억원을 민간에서 조달 중이며, 나스닥 상장을 검토했으나 저매출 대비 고밸류 우려로 코스닥 상장으로 방향을 바꿔 모건스탠리를 주관사로 확정했다.
> 출처 : [매출 터진 딥엑스…기업가치 2조6500억(딜사이트, 2026.06.24)](https://dealsite.co.kr/articles/164141)

- 삼성 5nm 기반 DX-M1(1~5W, 최대 25TOPS)을 양산 중이며, 양산 개시 8개월 만에 8개국에서 48건의 구매주문(PO)을 확보했다.
    - 매출의 67% 이상이 해외에서 발생하는 반복 가능한 상업 매출 구조를 완성했으며, 2026년 5월 한 달 신규 수주가 2025년 전체 매출(33억원)에 도달했다.
> 출처 : ["한 달 수주가 연매출 돌파"…딥엑스, '컴퓨텍스 2026'서 양산 협력 발표(아시아경제 CORE, 2026.05.29)](https://core.asiae.co.kr/article/2026052916063021955)

- 업계 최초로 삼성 파운드리 2nm 공정을 적용한 차세대 칩 DX-M2를 2027년 양산 목표로 개발 중이다(목표 성능 최대 80TOPS). 현대차·바이두가 개념검증(POC)을 진행한 것으로 알려져 있다.
> 출처 : [딥엑스 비즈니스모델 분석(demoday.co.kr, 2026.04.14)](https://demoday.co.kr/bm-analysis/175)

### 9-2. 모빌린트(Mobilint)

- 온프레미스 가속기 ARIES(MLA100·MLX-A1)와 온디바이스 SoC REGULUS가 핵심 라인업으로, ARIES는 산업통상자원부 신기술(NET) 인증을 획득했다.
> 출처 : [[ISEC 2026 미리보기] 모빌린트, 온프레미스 AI 추론 최적화 NPU 솔루션 공개(보안뉴스)](https://m.boannews.com/html/detail.html?idx=144445)

- 2026년 6월 컴퓨텍스 타이베이에서 대만 기업들과 협력을 확대하며 글로벌 산업용 AI 시장 공략에 속도를 내고 있다.
    - 롯데이노베이트와 휴머노이드·스마트인프라 등 피지컬AI 실증을, 포스코DX와 산업용 제어 분야 협력을 추진 중이다.
> 출처 : [모빌린트(AI 반도체) 기업정보(THE VC, 2026.05.22)](https://thevc.kr/mobilint)

**소결(9장)**: 한국 엣지 팹리스 2사는 2026년을 기점으로 '기술 검증'에서 '반복 가능한 상업 매출'로 전환하는 변곡점에 있다. 다만 딥엑스의 2025년 매출(33억원)은 호라이즌(약 7,700억원)의 0.4% 수준에 불과해, 기술력 인정과 실제 매출 규모 사이의 간극이 여전히 크다.

---

## 10. 엣지·피지컬AI 한중 비교 종합

### 10-1. 영역별 비교 매트릭스(엣지 특화 재구성)

| 영역 | 중국(호라이즌·화웨이 등) | 한국(딥엑스·모빌린트) |
|---|---|---|
| 가속기 설계 | 상 — 자율주행 특화 검증 완료, Journey6 560TOPS급 | 중상 — 초저전력(1~5W) 특화 |
| 온칩메모리·저전력 공정 | 중상 — 완성차 규격 충족 | 상 — 삼성 5nm 25TOPS, 2nm 로드맵 확보 |
| 완성차·로봇 OEM 채택 | 최상 — 25개+ 완성차, 1,000만대 누적출하 | 하~중 — 현대차·바이두 POC 단계 |
| 대량양산 검증 | 상 — 연 400만대+ 출하 규모 | 중 — 양산 8개월차, 48건 PO |
| 소프트웨어·SDK | 중상 — HSD 통합 솔루션 | 중 — 자체 SDK, 글로벌 트라이얼 진행형 |
| 시스템통합(자동차향) | 최상 — 폭스바겐 합작사(Carizon) 양산 | 하 — 완성차 합작사 부재 |
| 글로벌 매출 다변화 | 중 — 중국 내수 중심 | 상 — 매출 67%+ 해외 |
| 로봇(피지컬AI) 확장 | 상 — 로보택시 파일럿, 정부 주도 대량투입 | 중 — 롯데이노베이트·포스코DX 실증 단계 |

### 10-2. 완성차·로봇 OEM 채택 격차

- 호라이즌은 200,000위안(약 3,900만원) 이하 주류 차급에서 고급 솔루션 44.2% 점유율로 선도적 지위를 확보했으며, J6 시리즈만으로 400개에 가까운 모델 설계 채택을 확보했다.
    - 딥엑스·모빌린트는 아직 완성차 대량양산 채택 사례가 공개되지 않고 POC 단계에 머물러 있는데, 이는 기술력보다 내수 완성차 생태계 규모의 차이에서 비롯된다.
> 출처 : [Horizon Robotics 2025 Financial Report(BigGo Finance, 2026.03.20)](https://finance.biggo.com/news/M8xIC50BvbjfYyetKZ3w)

- 한국은 완성차가 현대차그룹으로 집중돼 있고, 현대차그룹은 로봇 부문에서 이미 엔비디아 블랙웰(5만 장 확보)·퀄컴 등과 협력 중이라 국산 엣지 NPU의 진입 여지가 상대적으로 좁다.
> 출처 : [2026 하반기 로보틱스 산업 전망(신한금융투자, 2026.05.22)](https://www.shinhangroup.com/kr/archive/insight/extend/detail/32871)

### 10-3. 중국 로봇산업 성장과 엣지 AI칩 수요

- 중국 시장조사업체 36Kr은 중국 임바디드 AI(체화지능) 시장이 2026년 1조 위안(약 230조원)을 돌파할 것으로 전망하며, MIIT는 2026년 자국 휴머노이드 생산량이 10만 대를 넘어설 것으로 전망했다.
> 출처 : [[더테크] 중국 휴머노이드 로봇, 실전 투입으로 진화 가속(THE TECH, 2026.06.11)](https://www.the-tech.co.kr/news/article.html?no=41605)

- 다만 '생산'과 '현장 가동'은 다른 개념이라는 지적이 있다. 유니트리 매출의 70% 이상이 여전히 연구·교육용에서 나오는 등 실제 산업현장 적용 비중은 약 9%에 그친다는 평가도 존재한다.
    - 2026년 6월 MIIT·SASAC는 휴머노이드의 '공연 모드'에서 '작업 모드' 전환을 위한 실전 훈련·배치 특별행동을 공동 발표했다.
> 출처 : [중국 제조업 AI 자동화, 어디까지 왔나(Korea Business Review, 2026.08.10)](https://www.koreabizreview.com/articles/global-radar-ai-tech-ai-robot-20260810-tm8r)

### 10-4. 2030년 시나리오

| 시나리오 | 내용 |
|---|---|
| 낙관(한국 우위 확대) | 딥엑스·모빌린트가 2nm 초저전력·글로벌 트라이얼로 비자동차 엣지에서 틈새 리더십 확보, 현대차그룹 로봇 밸류체인과 연계 |
| 현실(격차 지속) | 중국은 자동차 엣지 규모의 경제 유지, 한국은 초저전력·글로벌 다변화 틈새에서 안정적 성장하며 세그먼트별 공존 |
| 비관(한국 열위) | 중국의 국가주도 휴머노이드 대량투입이 성공하며 임바디드AI 표준 선점, 한국은 소규모 틈새시장에 머무름 |

### 10-5. 한국에 대한 시사점

- 현대차그룹은 2026년 8월부터 미국 조지아주 '로봇 메타플랜트 응용센터(RMAC)'를 가동하지만, 로봇 온디바이스 AI칩은 현재 엔비디아 블랙웰에 의존하고 있어 국산 엣지 NPU와의 연계는 아직 이뤄지지 않았다.
> 출처 : [2026 하반기 로보틱스 산업 전망(신한금융투자, 2026.05.22)](https://www.shinhangroup.com/kr/archive/insight/extend/detail/32871)

- 딥엑스가 매출의 67% 이상을 해외에서 창출한 것은 중국이 정부·내수 시장에 크게 의존하는 것과 대비되는 한국의 구조적 장점으로, 지정학적 리스크에서 상대적으로 유연한 포지션을 제공한다.

---

## 11. 소프트웨어 생태계 비교

### 11-0. 왜 소프트웨어 생태계가 반도체 경쟁의 핵심 승부처인가

- AI가속기 시장에서 하드웨어 스펙보다 소프트웨어 전환비용(switching cost)이 실질적인 경쟁 장벽으로 작용한다.
    - 단순 추론 워크로드를 표준 PyTorch로 이전하는 데는 수 주~수개월이 걸리지만, 커스텀 CUDA 커널과 NCCL 통신에 의존하는 대규모 학습 스택을 이전하려면 6~12개월이 소요된다.
> 출처 : [CUDA Lock-in Unpacked(SoftwareSeni, 2026.04.27)](https://www.softwareseni.com/cuda-lock-in-unpacked-the-software-moat-the-real-switching-costs-and-how-they-are-changing/)

- 엔비디아는 2026년 2월 기준 시가총액 약 4.45조 달러를 기록했으며, 2026 회계연도 4분기 데이터센터 매출은 623억 달러로 전체 매출의 약 91.5%를 차지했다.
    - 반도체 시장 점유율 격차의 상당 부분은 실리콘이 아니라 소프트웨어 전환비용에서 비롯된다.
> 출처 : [Nvidia's CUDA Lock-In and Supply Scarcity(Alphastreet, 2026.03.27)](https://news.alphastreet.com/nvidias-cuda-lock-in-and-supply-scarcity-make-its-ai-chip-moat-harder-to-break-than-it-looks/)

- AMD ROCm이 2025~2026년 성능 격차를 좁혔고, OpenAI의 Triton·MLIR 같은 하드웨어 중립적 컴파일러가 코드 재작성 없이 여러 하드웨어에서 고성능을 내는 경로를 열고 있다. "칩 대 칩" 경쟁이 아니라 "생태계 대 생태계" 경쟁이 본질이라는 것이 11장의 핵심 전제다.
> 출처 : [The Next Wave of AI Infrastructure Must Target NVIDIA's CUDA Moat(Built In, 2026.01.28)](https://builtin.com/articles/nvidias-cuda-future-ai-infrastructure)

### 11-1. 컴파일러·드라이버·툴체인 스택

- 화웨이는 2025년 8월 어센드 컴퓨팅 산업 발전 서밋에서 CANN 전면 오픈소스화를 최초 발표했고, 9월 화웨이커넥트 2025에서 CANN 기술운영위원회를 공식 출범시켰다.
    - 2025년 9월 말까지 모든 CANN 연산자를 GitCode에 오픈소스화하고, 12월까지 도메인 특화 라이브러리·GE·Ascend C·MindIE 등 핵심 구성요소 전체를 오픈소스화하겠다는 로드맵을 제시했다.
> 출처 : [Ascend: Open for All to Build a Vibrant Ecosystem(Huawei, 2025.09.20)](https://www.huawei.com/en/news/2025/9/hc-shengten-opensource)

- 2026년 3월 MWC 바르셀로나에서 화웨이는 Atlas 950 SuperPoD를 공개하며 CANN이 PyTorch·vLLM·SGLang·xLLM·verl·Triton·TileLang 등을 지원한다고 밝혀, 2025년 로드맵의 실제 이행을 확인했다.
> 출처 : [Huawei Unveiled the Latest SuperPoD(Huawei, 2026.03.02)](https://www.huawei.com/en/news/2026/3/mwc-superpod-ai)

- 한국은 리벨리온의 rebel-compiler, 모빌린트의 'qb' SDK, 딥엑스의 DXNN이 각자 독자 컴파일러·툴체인을 운영해, 화웨이 단일기업의 통일된 거버넌스와 달리 개발자 학습곡선이 4배로 분산되는 구조적 약점이 있다.

### 11-2. 프레임워크 호환성(PyTorch·TensorFlow·ONNX 대응)

- CANN 8.0은 PyTorch·MindSpore·TensorFlow·PaddlePaddle·ONNX·Jittor·OpenCV·OpenMMLab 등을 지원하며, 커뮤니티·상용 버전이 병행 제공된다(8.2.RC1 기준 12개 OS 지원).
    - 업계는 "부분적 PyTorch 호환성이 특정 연산에서 우회를 요구하거나 성능 저하를 유발할 수 있어, 통합의 완성도가 실제 채택을 좌우할 것"이라 경계한다.
> 출처 : [Huawei Version of CUDA Fully Open-Sourced(36Kr, 2025.08.06)](https://eu.36kr.com/en/p/3411091131567747)

- 리벨리온은 vLLM RBLN 플러그인으로 기존 코드 수정 없이 NPU 최적화를 활용할 수 있도록 지원하며, PyTorch Foundation에도 참여해 PyTorch 2.x·Triton 네이티브 지원을 공식화했다. ATOM-Max는 300개 이상의 모델 호환성을 강조한다.
> 출처 : [RBLN NPU용 vLLM 플러그인(리벨리온 공식문서)](https://docs.rbln.ai/latest/ko/software/model_serving/vllm_support/vllm-rbln.html)

### 11-3. CUDA 대응체계: 화웨이 CANN vs 한국 NPU SDK 생태계 성숙도

- CUDA의 진짜 해자는 소프트웨어·프레임워크 계층과 네트워킹·집단통신 계층(NCCL·NVLink)으로 나뉜다.
    - 모델 코드를 ROCm 등으로 이전해도 노드 간 분산학습에서 NCCL을 계속 쓰면 네트워킹 계층은 여전히 종속돼 있는 것이다. 이 계층의 유일한 대안(HetCCL)은 2026년 1월 발표된 연구 단계 수준이라, 화웨이·한국 모두 이 계층에서는 CUDA·NVLink에 준하는 대안이 없다.
> 출처 : [CUDA Lock-in Unpacked(SoftwareSeni, 2026.04.27)](https://www.softwareseni.com/cuda-lock-in-unpacked-the-software-moat-the-real-switching-costs-and-how-they-are-changing/)

- 화웨이는 openEuler·BoostKit·MindSpore와의 협업으로 8,192개 칩에 걸친 모델 샤딩을 자동화하는 등, 단일 기업이지만 다층적 파트너 생태계를 구축하고 있어 한국의 개별 기업 단위 SDK보다 집단적 대응력이 앞선다.
> 출처 : [MWC 2026 Takeaway 2(Jeffrey Towson, 2026.03.13)](https://jefftowson.com/membership_content/mwc-2026-takeaway-2-huaweis-ai-infrastructure-depends-on-people-not-just-processors-2-of-4/)

### 11-4. 개발자 생태계·오픈소스 커뮤니티 규모

- ZDNet Korea는 "빅테크는 자체 ASIC, 범용 시장은 엔비디아가 독점"하는 구도 속에서 한국 NPU의 입지가 좁아지고 있다고 진단한다.
    - 자체 서비스가 없는 한국 NPU 업체는 고객사 장기 로드맵을 알 수 없어 범용 시장을 겨냥할 수밖에 없는데, 범용 AI 칩 시장은 이미 엔비디아가 지배하고 있어 개발자 유입 자체가 구조적으로 불리하다.
> 출처 : [빅테크는 ASIC, 범용은 엔비디아…좁아지는 K-NPU 입지(ZDNet Korea, 2026.08.07)](https://zdnet.co.kr/view/?no=20260807154129)

### 11-5. 벤치마크 성능 비교

- MLPerf Inference v5.1(2025.09, 27개사 참여)과 v6.0(2026.04.01)에 엔비디아·AMD·인텔·구글 등이 참여하지만, 화웨이·캠브리콘 등 중국 국산 AI가속기는 공개 MLPerf 제출 목록에서 사실상 확인되지 않는다.
    - 예측시장 Manifold(2026년 8월 기준)는 "2026년 말까지 중국산 AI칩이 공개 벤치마크에서 H100 성능의 80% 이상을 달성할 것인가"라는 질문에 확률 18%를 부여하고 있어, 벤더 마케팅이 아닌 독립 검증 기준으로는 중국산 칩 성능이 아직 불투명하다는 시장 인식을 보여준다.
> 출처 : [Will any China-domestic AI chip reach ≥80% of NVIDIA H100 perf on a public benchmark before 2026-12-31?(Manifold, 2026)](https://manifold.markets/ChristopherBerzins/will-any-chinadomestic-ai-chip-reac)

- 한국의 퓨리오사AI는 furiosa-mlperf 도구로 결과를 제3자가 재현 가능한 형태로 공개하며, GPU와 동등한 토큰 생성 속도에 72.4% 높은 전력효율을 자체 보고했다. 다만 MLPerf 공식 폐쇄부문 제출을 통한 교차검증은 아직 이뤄지지 않았다.
> 출처 : [Furiosa RNGD NPU에서 LLM 모델 서빙하기(Dudaji Tech Blog, 2025.12.26)](https://blog.dudaji.com/furiosa-rngd-npueseo-llm-model-seobinghagi/)

**소결(11장)**: 화웨이는 오픈소스화(2025.08 발표→2025.09 거버넌스 출범→2025.12 1차 완료→2026.03 SuperPoD 통합 확인)라는 명확한 로드맵으로 CUDA 프레임워크 계층 우위를 빠르게 잠식하고 있으나, 네트워킹 계층에서는 화웨이·한국 모두 대안이 없다. 한국은 SDK 파편화로 화웨이 한 개 기업보다도 생태계 통합력이 약하며, 독립 검증 벤치마크 참여에서도 중국·한국 모두 엔비디아·AMD 수준의 투명성을 아직 갖추지 못했다.

---

## 12. 제조·공급망 연계 비교

### 12-1. 삼성·SK하이닉스와의 파운드리·HBM 연계 잠재력

- SK하이닉스와 삼성전자는 2024년 글로벌 HBM 시장을 합산 약 90%대까지 장악했으나, 2025년 경쟁 심화로 2분기 기준 합산 약 79%로 조정됐다.
    - UBS는 엔비디아 차세대 Rubin 플랫폼용 HBM4에서 SK하이닉스가 약 70% 점유를 예상하는 반면, Counterpoint의 공식 전망은 54%로 더 보수적이다.
> 출처 : [SK hynix has won two-thirds of Nvidia's next-gen HBM orders(Korea JoongAng Daily)](https://www.koreajoongangdaily.com/business/sk-hynix-has-won-two-thirds-of-nvidias-next-gen-high-bandwidth-memory-orders-industry-sources/12030483)

- 리벨리온 REBEL-Quad는 삼성 파운드리 4nm급(SF4X) 공정과 HBM3E를 결합했고, 딥엑스 DX-M2는 업계 최초로 삼성 2nm 공정을 적용할 예정이다. 국내 팹리스가 국내 파운드리·메모리와 수직 연계된 '원스톱' 공급망을 구축하고 있다는 점은 중국에는 없는 한국 고유의 구조적 이점이다.
> 출처 : ["한 달 수주가 연매출 돌파"…딥엑스(아시아경제 CORE, 2026.05.29)](https://core.asiae.co.kr/article/2026052916063021955)

### 12-2. 중국의 파운드리·패키징 내재화 추진 현황

- 중국은 SMIC의 7nm 공정에 의존하고 있으나 수율이 소식통에 따라 20~60%로 편차가 크며, 첨단 미세공정(14nm 이하)·EUV 노광장비는 여전히 확보하지 못한 상태다.
    - 화웨이는 HBM 조달 제약을 우회하기 위해 자체 HBM(HiBL 1.0·HiZQ 2.0)을 개발해 950 시리즈에 탑재하는 등 첨단패키징 내재화를 추진하고 있다.
> 출처 : [Huawei Unveils Ambitious Three-Year AI Chip Roadmap with Self-Built HBM Technology(BigGo, 2025.09.18)](https://biggo.com/news/202509181252_Huawei_Reveals_AI_Chip_Roadmap_with_In-House_HBM)

- CXMT(창신메모리)는 D램 양산 규모를 확대 중이며 HBM 자립을 2028~2030년 목표로 추진하고 있어, 한국 메모리 우위에 대한 중장기 위협 요인이다.

**소결(12장)**: 제조·공급망은 한국이 확실한 우위를 갖는 영역이다. 그러나 이 우위는 '현재 시점'의 스냅샷이며, 중국의 국가 자본이 SMIC 수율 개선과 CXMT HBM 양산에 집중 투입되고 있어 격차가 좁혀질 수 있다.

---

## 13. 정책지원 비교

### 13-1. 중국의 자립화·국산화 지원정책

- 중국은 2024년 5월 반도체 대기금 3기(3,440억 위안, 약 475억 달러)를 설립했으며, 이는 역대 최대 규모로 미국 CHIPS법(527억 달러)에 대응하는 성격이다.
    - 향후 5년간 데이터센터에 약 2조 위안(약 450조원)을 배정하고 핵심 기술의 최소 80%를 국산으로 조달한다는 방침이며, 2025년 11월에는 국가지원 프로젝트에서 외국산 가속기를 배제하는 조치까지 나왔다.
> 출처 : [China's $47.5bn 'Big Fund III' Fuels Semiconductor Self-Sufficiency(Quantum Zeitgeist)](https://quantumzeitgeist.com/chinas-47-5bn-big-fund-iii-fuels-semiconductor-self-sufficiency-amid-us-tech-war/)
> 출처 : [China drafts $295 billion plan(Tom's Hardware)](https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips)

- 화웨이·캠브리콘만 정부 조달 화이트리스트에 등재돼 정책 수혜를 사실상 독점하고 있으며, 이는 캠브리콘의 2025년 흑자전환(고객 집중도 94%)을 뒷받침한 핵심 동력이다.

### 13-2. 한국의 AI반도체 지원정책

- 정부는 2026년 AI 관련 예산을 전년 대비 3배 수준인 총 9.9조원(41개 부처, 738개 사업)으로 편성했으며, 이 중 AI반도체 소관 과학기술정보통신부가 5.1조원(51%)으로 가장 큰 비중을 차지한다.
> 출처 : [AI 예산사업 통합 설명자료(국가인공지능전략위원회, 2026)](https://aikorea.go.kr/web/board/brdDetail.do?currentPage=1&menu_cd=000011&num=359)

- K-클라우드 프로젝트는 2023~2030년 총 8,262억원을 투입해 데이터센터의 국산 AI칩 점유율을 80%까지 끌어올리는 것이 목표다.
    - 광주는 국가 AI데이터센터를 활용해 퓨리오사AI·리벨리온·사피온 제품의 성능을 검증하고 있으며, 국산 NPU 전환 실증 과제는 2025년 4개에서 2026년 8개로 두 배 확대됐다.
> 출처 : [2026년도 AI 예산(AI반도체과)(광주광역시의회, 2026)](https://council.gwangju.go.kr/attach/544/a7d4a1b90fd2a7d6cbe72e297f2f652c.pdf)

- 국민성장펀드의 'K-엔비디아' 프로젝트는 리벨리온·퓨리오사AI·딥엑스·모빌린트·하이퍼엑셀 5개사를 대상으로 하며, 2025년 12월에는 12개사가 참여하는 K-Perf(공동성능지표) 협의체가 출범했다.

### 13-3. 정책 실행 격차 평가 — 제도 설계 vs 실행 실적

- 중국은 대기금(475억 달러)·정부조달 화이트리스트·80% 국산조달 의무화라는 '규모와 강제력을 갖춘 정책'으로 즉각적인 수요를 창출한 반면, 한국은 예산 규모가 절대적으로 작고(K-클라우드 총 8,262억원은 대기금의 1% 미만) 조달 의무화 대신 실증사업 중심으로 설계돼 있다.
    - 실증 과제가 2025년 4개에서 2026년 8개로 늘어난 것은 확대 신호이지만, 여전히 '의무 조달'이 아닌 '자율 참여형 실증'이라 정책 설계와 실제 시장 파급력 사이에 간극이 존재한다.
> 출처 : [9.9조원의 AI 예산, 2026년 정부 인프라 지원사업 정리(effettoblog, 2026)](https://effettoblog.com/blog/2026%EB%85%84-%EC%A0%95%EB%B6%80-ai-%EC%98%88%EC%82%B0-9-9%EC%A1%B0%EC%9B%90-%EC%8B%9C%EB%8C%80-%EA%B3%B5%EA%B3%B5-ai-%EC%9D%B8%ED%94%84%EB%9D%BC-%EC%82%AC%EC%97%85-%EC%99%84%EB%B2%BD-%EC%A0%95/)

**소결(13장)**: 중국의 정책은 '규모와 강제력'으로 즉각적인 내수 수요를 만들어내는 방식이고, 한국의 정책은 '실증과 자율 참여'를 통해 점진적으로 시장을 형성하는 방식이다. 예산 규모의 절대적 차이를 감안하면, 한국은 조달 의무화 등 수요 견인 정책의 강도를 높이는 것이 실행 격차를 줄이는 핵심 과제다.

---

## 14. 종합 평가: 한국 AI반도체 산업의 위치

### 14-1. SWOT 분석

**강점(Strengths)**
- 세계 최고 수준의 HBM·파운드리 공급망을 국내에 보유(SK하이닉스·삼성 합산 약 90%대, 리벨리온·딥엑스의 삼성 4nm~2nm 활용).
- 리벨리온·퓨리오사AI(데이터센터 추론)·딥엑스·모빌린트(엣지)가 각각 '전력효율' 차별화 축을 확보, 2026년 양산·매출 실현 단계 진입.

**약점(Weaknesses)**
- 소프트웨어 생태계가 4개 팹리스 단위로 파편화돼 단일기업 화웨이의 CANN보다도 생태계 통합력이 약함(11장).
- 내수 시장 규모가 절대적으로 작음(딥엑스 2025년 매출 33억원은 호라이즌의 0.4%), 정책 예산도 중국 대기금의 1% 미만.

**기회(Opportunities)**
- 추론 중심 워크로드 전환이 전력효율에 강점을 가진 한국 NPU에 유리한 방향으로 시장구조를 재편 중(3장).
- 딥엑스의 해외매출 67%+처럼, 중국의 정부·내수 의존형 성장과 대비되는 글로벌 다변화가 지정학적 리스크 국면에서 강점으로 작용 가능.

**위협(Threats)**
- CXMT의 D램·HBM 양산(2028~2030)이 한국 메모리 해자를 중장기 잠식할 가능성.
- 한중 기술격차가 2022년 4.8%p→2024년 8.6%p로 확대(MSIT), 기본역량에서부터 추월당할 위험.

### 14-2. 풀스택 생태계 관점에서 본 가속기 계층의 함의

- 한국의 강점(HBM·파운드리)은 풀스택 중 '반도체 계층 내부'에 머물러 있고, 모델·에이전트·로봇 계층과의 연계가 상대적으로 약하다.
    - 중국은 반도체(화웨이·캠브리콘)-모델(DeepSeek·Qwen)-에이전트-로봇(휴머노이드)을 국가 차원에서 동시에 밀어붙이는 수직 통합 전략을 구사한다(1-1, 10-3).
- 한국의 과제는 반도체 계층의 상대적 강점을 국내 모델(LG EXAONE)·로봇(현대차그룹) 계층과 연결하는 '국내 풀스택 고리'를 만드는 것이다(9-1, 10-5의 연계 미흡 문제와 직결).

---

## 15. 결론 및 시사점

### 15-1. 장별 핵심 키포인트 종합

**시장 구조(1~4장)**
- 가트너의 풀스택 AI 생태계론에서 반도체는 모델·에이전트·로봇 위층을 물리적으로 규정하는 기반층이며, 2026년 AI반도체는 전체 반도체 매출의 약 30%(약 3,900억 달러)를 차지하는 핵심 산업이다.
- AI가속기 시장은 GPU가 절대 규모(2033년 81%)를 유지하는 가운데 커스텀 ASIC·NPU가 CAGR 27%로 GPU(16%)를 앞질러 성장하는 구조적 전환기에 있다. 이는 학습에서 추론으로의 워크로드 전환이 만든 결과이나, 엔비디아 역시 추론 대응(Blackwell, Groq 인수)에 나서고 있어 'NPU가 GPU를 대체'하는 단순 구도가 아니라 '워크로드별 최적 실리콘 경쟁'으로 이해해야 한다.
- 데이터센터용(시장의 75%, 정책·자본이 견인하는 시스템 경쟁)과 엣지용(25%지만 CAGR 27%, 완성차·로봇 OEM의 실채택이 결정하는 시장경쟁)은 서로 다른 경쟁 논리를 가진 별개 영역이다.

**데이터센터용 한중 경쟁(5~7장)**
- 중국은 화웨이(시스템 규모·정책수혜 독점)·캠브리콘(2025년 흑자전환, 그러나 고객집중도 94%)·하이곤(CPU+DCU 통합)의 '검증된 3강'과, IPO로 자금은 확보했으나 전원 적자인 신흥 3사(무어스레드·메타엑스·바이렌)로 층위가 나뉜다.
- 한국은 리벨리온(REBEL-Quad, 국민성장펀드 1호 투자, 3.4조원 밸류)·퓨리오사AI(RNGD 양산, 프리IPO 추진)가 삼성 파운드리·SK하이닉스 HBM과 수직 연계된 전력효율 특화 전략으로 대응하고 있으나, 학습용 최고성능칩·내수 수요 규모에서는 열위다.
- 2030년 격차는 '분리 병존'(현실 시나리오)이 가장 가능성 높은 경로이며, 중국의 HBM·수출규제 리스크와 한국의 시스템반도체 격차가 각각의 상방·하방 요인이다.

**엣지·피지컬AI 한중 경쟁(8~10장)**
- 중국은 호라이즌 로보틱스(자동차 엣지 1,000만 대 누적출하, 25개+ 완성차 채택)·화웨이(Ascend 310, MDC 플랫폼)가 자동차·산업 영역에서 실사용 규모를 확보했고, 바이두 쿤룬신·알리바바 T-Head는 자사 생태계 수직계열화와 자본시장 상장(A+H)을 동시 추진 중이다.
- 한국은 딥엑스(해외매출 67%+, 8개국 48건 PO)·모빌린트(산업용·글로벌 파트너십 확대)가 '기술검증→반복매출' 전환의 초기 단계이나, 완성차 대량채택 사례는 아직 없다.
- 중국의 국가주도 휴머노이드 로봇 확산(2026년 생산 10만 대 목표, 임바디드AI 시장 230조원 전망)이 다음 승부처이나, '생산'과 '실제 현장가동률'(유니트리 9%)의 간극도 함께 고려해야 한다.

**소프트웨어 생태계(11장)**
- 반도체 경쟁의 본질은 '칩 성능'이 아니라 '소프트웨어 전환비용'이다. 엔비디아의 4조 달러대 시가총액은 20년간 축적된 CUDA 생태계(소프트웨어 계층+네트워킹 계층)가 만든 결과다.
- 화웨이는 CANN을 2025년 8월 발표 이후 단계적으로 오픈소스화(2026년 3월 MWC에서 PyTorch·vLLM·Triton 통합 확인)하며 추격 속도를 높이는 반면, 한국은 4개 팹리스의 SDK 파편화로 화웨이 한 개 기업보다도 생태계 통합력이 약하다. 독립 벤치마크(MLPerf) 참여 투명성에서도 중국·한국 모두 아직 과제가 남아있다.

**제조·공급망 및 정책(12~13장)**
- 제조·공급망은 한국의 가장 확실한 우위(HBM 합산 약 79~90%대, 삼성 4nm~2nm 파운드리 수직연계)이나, 중국의 SMIC 수율 개선과 CXMT의 HBM 자립 추진(2028~2030)으로 중장기적으로 좁혀질 수 있는 '현재 시점의 스냅샷'이다.
- 정책은 중국(대기금 475억 달러·조달 의무화 80%)과 한국(9.9조원 AI예산 중 반도체 관련 실증사업 확대) 사이에 규모와 강제력 모두에서 현격한 차이가 있으며, 이 격차가 5~10장에서 확인된 내수 수요·매출 규모 차이의 근본 원인이다.

**종합(14장)**
- 한국의 SWOT을 관통하는 하나의 문장은 "반도체 계층 내부에서는 강하지만, 모델·로봇 등 인접 계층과의 국내 연계가 약하다"는 것이다. 중국의 수직통합 전략(반도체-모델-에이전트-로봇)과 대비되는 이 약점이, 개별 장에서 확인된 격차들(내수 수요 부족, SDK 파편화, 완성차·로봇 채택 부진)의 공통 뿌리다.

### 15-2. 정책 시사점(파트별 요약)

| 파트 | 정책 시사점 |
|---|---|
| 시장구조(1~4장) | 추론 전환이라는 구조적 순풍을 국내 팹리스 지원의 논리적 근거로 명확히 활용해야 한다. |
| 데이터센터용(5~7장) | HBM·파운드리 수직연계를 국가전략자산화하고, 정부·공공 데이터센터에 국산 NPU 우선조달 비중을 설정해야 한다. |
| 엣지·피지컬AI(8~10장) | 현대차그룹 등 국내 완성차·로봇 대기업과 국산 엣지 NPU 팹리스를 연결하는 '국내 앵커 고객' 확보를 정책적으로 유인해야 한다. |
| 소프트웨어 생태계(11장) | 4개 팹리스의 SDK를 화웨이 CANN처럼 통합된 오픈소스 런타임·컴파일러로 묶는 '공동 컴파일러 이니셔티브'가 시급하다. |
| 제조·공급망(12장) | 국산 NPU-국산 HBM-국산 파운드리 '풀턴키' 패키지를 국가 전략자산으로 육성해 중국에 없는 강점을 지렛대화해야 한다. |
| 정책지원(13장) | 예산 규모 확대보다 우선, 조달 의무화 등 '실증'을 넘어선 강제력 있는 수요 견인 정책의 도입을 검토해야 한다. |
| 종합(14장) | 반도체-모델-로봇을 잇는 '국내 풀스택 고리' 구축이 중장기 국가전략의 최우선 과제여야 한다. |

### 15-3. 전략 변경 임계치(모니터링 지표)

- 중국 국산 AI가속기 내수 점유율이 41%(2025)에서 60%를 초과할 경우 → 한국의 대중 수출 기회 소멸을 가정하고 내수·비중국 시장 집중으로 전환한다.
- 엔비디아 H200/B30A의 대중 수출이 전면 허용될 경우 → 중국 팹리스 성장 둔화가 예상되므로 한국은 '비엔비디아 대안' 포지션을 재점검한다.
- SMIC 7nm 수율이 20%에서 40%를 돌파할 경우 → 중국의 공급 병목이 완화되므로 한국 파운드리 우위 축소에 대비한다.
- 중국 휴머노이드 로봇의 실제 현장가동률이 유니트리 수준(9%)에서 유의미하게 상승할 경우 → 임바디드AI 엣지칩 수요가 실질화되므로 한국도 로봇용 엣지 NPU 투자를 확대한다.

---

## Caveats (전체 종합)

- **가트너 원문 미확보**: 「2026 Top Trends in China AI」 핵심 수치(2030년 50% 국산화 등)는 2차 인용 기반으로, 가트너 정식 보고서로 직접 교차검증이 필요하다.
- **시장 규모 전망의 정의 차이**: AI반도체/AI가속기 시장 규모는 조사기관별 정의(GPU 포함 여부, 데이터센터 한정 여부 등)가 달라 절대값 편차가 크다(2장 참조).
- **중국 기업 수율·출하량 데이터**: SMIC 수율(20~60%), 화웨이·캠브리콘 출하량 등 상당수가 '소식통' 기반 추정치이며 공식 확인이 제한적이다.
- **모건스탠리 자급률 전망치 편차**: 보도별로 76%/82%/85%/86%로 갈리는데, 이는 지표 정의(출하량 vs 매출액 vs 수요충당) 차이에 기인한다.
- **HBM 점유율 편차**: 집계기관(TrendForce vs Counterpoint)·기준(매출 vs 생산능력)에 따라 2024년 90%대~2025년 79%까지 편차가 있다.
- **리벨리온·퓨리오사 스펙 표기 불일치**: REBEL-Quad 공정(4nm급 vs 2nm 로드맵 혼재), 소비전력(300W vs 최대 600W) 등 자료마다 편차가 있어 최종 사양 확인이 필요하다.
- **딥엑스 시리즈D 밸류(2조 6,500억원)**: 확정 라운드가 아닌 준비 중인 프리머니 기준으로, 마감 시 조건이 달라질 수 있다.
- **중국 신흥 IPO 3사 밸류에이션**: 정책·기대 주도 성격이 강하며 펀더멘털(전원 적자) 대비 과열 지적이 있다.
- **중국 휴머노이드 로봇 시장 전망**: 정부·업계의 낙관적 전망치이며, 실제 현장가동률은 유니트리 사례(9%)처럼 현저히 낮을 수 있다는 반박 자료가 병존한다.
- **완성차·로봇 OEM향 국산 엣지 NPU 채택**: 현대차·바이두의 POC 단계 정보에 근거한 전망으로, 실제 대량양산 계약은 아직 공개 확정되지 않았다.
- **알리바바 T-Head·바이두 쿤룬신 엣지 전용 매출**: 데이터센터용과 분리 공시되지 않아 엣지 부문 정량 비교에 한계가 있다.
- **성능효율 벤치마크**: '추론 ASIC이 GPU 대비 3~10배 전력효율'은 워크로드·정밀도·비교 대상에 따라 편차가 크며, 다수는 벤더 자체 측정치로 MLPerf 등 독립 검증을 거치지 않았다.

---

## 관련근거 및 출처 (전체 통합)

**1장 — 서론**
- [Half of China's AI Accelerators Will Be Homegrown by 2030: Gartner Forecasts 'AI Full-Stack' Self-Reliance(BigGo Finance, 2026.08.09)](https://finance.biggo.com/news/813d32c3-af15-4bd8-8c1e-3a9604808118)
- [Gartner Forecasts Worldwide Semiconductor Revenue to Exceed $1.3 Trillion in 2026(Gartner, 2026.04.08)](https://www.gartner.com/en/newsroom/press-releases/2026-04-08-gartner-forecasts-worldwide-semiconductor-revenue-to-exceed-us-dollars-one-point-3-trillion-in-2026)
- [Bloomberg Intelligence: AI Accelerator Chips 2026 Outlook(Bloomberg LP, 2026.01.14)](https://www.bloomberg.com)
- [TPU v7, Google's answer to Nvidia's Blackwell is nearly here(The Register, 2025.11.06)](https://www.theregister.com/2025/11/06/googles_ironwood_tpus_ai/)
- [Ball game's over—the US is out of the AI chip market in China(Brookings, 2026)](https://www.brookings.edu/articles/ball-games-over-the-us-is-out-of-the-ai-chip-market-in-china/)
- [국민성장펀드, AI 반도체 리벨리온에 2500억 쏜다(서울경제, 2026.03.30)](https://www.sedaily.com/article/20017612)

**2장 — 시장 규모**
- [Artificial Intelligence Market Size & Share Report(Grand View Research, 2026.06.18)](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market)
- [AI Chips Market Size, Share and Forecast, 2026-2033(Coherent Market Insights, 2026)](https://www.coherentmarketinsights.com/industry-reports/ai-chips-market)
- [AI Chip Market Share 2026(Axis Intelligence, 2026)](https://axis-intelligence.com/ai-chip-market-share/)
- [Artificial Intelligence in Semiconductor Market Size to Hit USD 250.63 Bn by 2035(Precedence Research, 2026.07.15)](https://www.precedenceresearch.com/artificial-intelligence-in-semiconductor-market)
- [AI Accelerators Market Size, Share & 2030 Trends Report(Mordor Intelligence, 2026)](https://www.mordorintelligence.com/industry-reports/ai-accelerators-market)
- [Data Center Accelerator Market Size, Share, Latest Trends & Growth Analysis(MarketsandMarkets, 2026)](https://www.marketsandmarkets.com/Market-Reports/data-center-accelerator-market-48984803.html)
- [Hardware Acceleration Market Outlook 2025-2032(AI2Work, 2026)](https://ai2.work/blog/ai-business-hardware-acceleration-market-2025)
- [South Korea AI Chip Market(MarketsandMarkets, 2026)](https://www.marketsandmarkets.com/Market-Reports/south-korea-ai-chip-market-87237882.html)
- [Biren Technology 투자설명서(2025)](https://siliconangle.com/2025/12/31/chinese-graphics-card-maker-biren-raises-717m-ipo/)

**3장 — 학습→추론 전환**
- [The Next Battlefield for AI Chips: From Training to Inference(TSPA Semiconductor, 2026.04.07)](https://tspasemiconductor.substack.com/p/the-next-battlefield-for-ai-chips)
- [GPU vs LPU vs NPU: Infrastructure for the AI Inference Era(ModulEdge, 2026.04.06)](https://www.moduledge.com/blog/gpu-vs-lpu-vs-npu-ai-chip-infrastructure)
- [Comparing AI chips: GPU, ASIC, and NPU(4sysops, 2026.03.20)](https://4sysops.com/archives/comparing-ai-chips-gpu-asic-and-npu/)
- [The AI Chip Wars: NVIDIA, AMD, and Custom Silicon Explained 2026(Hakia, 2026)](https://hakia.com/tech-insights/ai-chip-wars/)
- [AI-RAN on NPUs: Baseband Processing Without Baseband Chips(arXiv, 2026)](https://arxiv.org/pdf/2607.04224)
- [AI Inference Infrastructure: Power & Cooling for Edge Racks(ModulEdge, 2026.03.03)](https://www.moduledge.com/blog/edge-ai-infrastructure-for-inference-translating-ai-servers-into-rack-power-cooling-and-module-design)
- [Edge AI Chip Benchmark Metrics That Matter(Troy Lendman, 2026)](https://troylendman.com/edge-ai-chip-benchmark-metrics-that-matter/)

**5장 — 데이터센터용 중국 기업**
- [모건스탠리 중국 AI GPU 시장 전망(뉴스핌 GAM, 2026.08.04)](https://gam.newspim.com/news/view/20260804001128)
- [Huawei to double output of Ascend AI chips(RCR Wireless News, 2025.09.30)](https://www.rcrwireless.com/20250930/ai-infrastructure/huawei-ai-chips-2)
- [Huawei Unveils Ambitious Three-Year AI Chip Roadmap with Self-Built HBM Technology(BigGo, 2025.09.18)](https://biggo.com/news/202509181252_Huawei_Reveals_AI_Chip_Roadmap_with_In-House_HBM)
- [Huawei Ascend Production Ramp: HBM is The Bottleneck(SemiAnalysis)](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- [Huawei/HiSilicon Spotlight(SemiconductorX)](https://semiconductorx.com/spotlight-huawei-hisilicon.html)
- [China drafts $295 billion plan(Tom's Hardware)](https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips)
- [Chinese GPU maker Cambricon's Q1 revenue hits $423 million(Yahoo Finance)](https://finance.yahoo.com/sectors/technology/articles/chinese-gpu-maker-cambricons-q1-103000723.html)
- [Cambricon's Profit Soars 185% in Q1(MarketScreener)](https://www.marketscreener.com/news/cambricon-s-profit-soars-185-in-q1-revenue-jumps-160-on-ai-boom-ce7f58d8d080f020)
- [China's Cambricon Shares Surge 14%(BigGo Finance)](https://finance.biggo.com/news/Yppf4Z0BDXrLZJaADbAR)
- [Cambricon's Trillion-Yuan Market Cap 'Day Trip'(BigGo Finance)](https://finance.biggo.com/news/98bc1a60-279a-4c01-9464-05c0a704b4fa)
- [Inside Hygon's CPU-DCU Compute Stack(Leon Liao Substack)](https://leonliao.substack.com/p/inside-hygons-cpu-dcu-compute-stack)
- [China's US$16.4B Chip Megamerger Collapses(TrendForce, 2025.12.11)](https://www.trendforce.com/news/2025/12/11/news-chinas-us16-4b-chip-megamerger-collapses-as-hygon-and-sugon-call-off-deal/)
- ['China's Nvidia' Moore Threads surges over 400% on trading debut(CNBC, 2025.12.05)](https://www.cnbc.com/2025/12/05/china-nvidia-moore-threads-trading-debut-1-billion-listing-ipo-shanghai-gpu-enflame-biren.html)
- [China's GPU IPO Wave Intensifies(TrendForce, 2025.12.11)](https://www.trendforce.com/news/2025/12/11/news-chinas-gpu-ipo-wave-intensifies-metax-surpasses-moore-threads-in-retail-investor-interest/)
- [China's premier GPU maker Biren kicks off Hong Kong IPO(Tom's Hardware)](https://www.tomshardware.com/tech-industry/biren-kicks-off-hong-kong-ipo)
- [Biren's $300M IPO: China's AI Chip Wave Hits Peak FOMO(byteiota)](https://byteiota.com/birens-300m-ipo-chinas-ai-chip-wave-hits-peak-fomo/)

**6장 — 데이터센터용 한국 기업**
- [리벨리온 뉴스룸(2026.03.30)](https://kr.rebellions.ai/newsroom/)
- [리벨리온 비즈니스모델 분석(demoday.co.kr)](https://demoday.co.kr/bm-analysis/167)
- [Rebellions AI Puts Together An HBM And Arm Alliance(The Next Platform, 2025.12.23)](https://www.nextplatform.com/2025/12/23/rebellions-ai-puts-together-an-hbm-and-arm-alliance-to-take-on-nvidia/)
- [ISSCC 2026: Rebellions details industry's first quad-chiplet AI solution(Tom's Hardware)](https://www.tomshardware.com/tech-industry/semiconductors/isscc-2026-rebellions-ucie-rebel-100)
- [FuriosaAI RNGD Lands in Europe(Tech Times, 2026.07.11)](https://www.techtimes.com/articles/320154/20260711/furiosaai-rngd-lands-europe-koreas-power-efficient-inference-chip-reaches-equinix-lisbon.htm)
- [FuriosaAI Rejects Big Tech Path, Builds Independent Road to 2027 IPO(KoreaTechDesk)](https://koreatechdesk.com/furiosaai-pre-ipo-funding-meta-rejection-2027-korea-ai-chip)

**7장 — 데이터센터 한중 비교**
- [SK hynix has won two-thirds of Nvidia's next-gen HBM orders(Korea JoongAng Daily)](https://www.koreajoongangdaily.com/business/sk-hynix-has-won-two-thirds-of-nvidias-next-gen-high-bandwidth-memory-orders-industry-sources/12030483)
- [中-韓 기술 격차, 2년 새 80% 더 벌어졌다(한국경제, 2026.02.22)](https://www.hankyung.com/article/2026022264921)
- [KISTEP "中, 韓 반도체 기술 수준 추월"(글로벌이코노믹, 2025.02.23)](https://www.g-enews.com/article/Industry/2025/02/202502231842524392056c162803_1)
- [China's AI Chip Self-Sufficiency Hits 41%, Korea Slips to 5th in Semiconductors(Seoul Economic Daily, 2026.04.17)](https://en.sedaily.com/finance/2026/04/17/chinas-ai-chip-self-sufficiency-hits-41-percent-korea-slips)

**8장 — 엣지 중국 기업**
- [Horizon Robotics' 2025 Revenue Soars Nearly 60%(BigGo Finance, 2026.03.23)](https://finance.biggo.com/news/OCQGGp0BZk7xib5fgFLX)
- [Horizon Robotics Partners with Volkswagen(Horizon Robotics)](https://www.horizon.auto/en/news/horizon-news/478)
- [Horizon Robotics 2025 Financial Report(BigGo Finance, 2026.03.20)](https://finance.biggo.com/news/M8xIC50BvbjfYyetKZ3w)
- [Research insight: Horizon Robotics leads China's push for autonomous driving independence(Digitimes, 2025.11.19)](https://www.digitimes.com/news/a20251119PD232/market-horizon-robotics-autonomous-driving-automakers-adas.html)
- [HUAWEI Ascend(Baidu Baike)](https://baike.baidu.com/en/item/HUAWEI%20Ascend/1453477)
- [Huawei | TechInsights](https://www.techinsights.com/vendor/huawei)
- [Comprehensive Analysis of Huawei's Autonomous Driving Computing and Domain Control Platform Technology(Oreate AI Blog, 2026.01.07)](https://www.oreateai.com/blog/comprehensive-analysis-of-huaweis-autonomous-driving-computing-and-domain-control-platform-technology/a52d9a7adbeebc41b4ed40f9f387a12f)
- [Orange Pi Maker Xunlong & Huawei Launch Edge AI at WAIC 2026(androidpimp.com, 2026)](https://www.androidpimp.com/product-news/orange-pi-xunlong-huawei-edge-ai-waic-2026)
- [바이두(위키백과)](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%9D%B4%EB%91%90)
- [자율주행, 새로운 지평을 열다(KDI 경제교육·정보센터)](https://eiec.kdi.re.kr/publish/reviewView.do?ridx=17&idx=179&fcode=000020003600003)
- [[中 하드테크 IPO 빅뱅] ⑱쿤룬신, '바이두 AI제국' 성장엔진 A+H 상장(뉴스핌, 2026.08.04)](https://www.newspim.com/news/view/20260804001134)
- [[中 하드테크 IPO 빅뱅] ⑳쿤룬신, 독자 AI 생태계로 '엔비디아 도전장'(뉴스핌, 2026.08.04)](https://gam.newspim.com/news/view/20260804001128)
- [中 알리바바, AI 반도체 자회사 핑터우거 상장 검토(글로벌이코노믹, 2026.01.22)](https://www.g-enews.com/article/Global-Biz/2026/01/2026012221581784029a1f309431_1)
- [알리바바-바이두, AI 칩 설계 자회사 상장으로 중국 반도체 자립 가속(헬로티, 2026.01.26)](https://www.hellot.net/news/article.html?no=109661)

**9장 — 엣지 한국 기업**
- [매출 터진 딥엑스…기업가치 2조6500억(딜사이트, 2026.06.24)](https://dealsite.co.kr/articles/164141)
- [딥엑스 투자 가이드(bullstory.io, 2026.07.09)](https://bullstory.io/blog/%EB%94%A5%EC%97%91%EC%8A%A4-%ED%88%AC%EC%9E%90-%EA%B0%80%EC%9D%B4%EB%93%9C-%EA%B8%B0%EC%97%85%EA%B0%80%EC%B9%98-7000%EC%96%B526%EC%A1%B0-%EA%B8%89%EB%93%B1%ED%95%9C-%EC%9D%B4%EC%9C%A0%EC%99%80-ipo-%EB%A1%9C%EB%93%9C%EB%A7%B5)
- ["한 달 수주가 연매출 돌파"…딥엑스(아시아경제 CORE, 2026.05.29)](https://core.asiae.co.kr/article/2026052916063021955)
- [딥엑스 비즈니스모델 분석(demoday.co.kr, 2026.04.14)](https://demoday.co.kr/bm-analysis/175)
- [[ISEC 2026 미리보기] 모빌린트, 온프레미스 AI 추론 최적화 NPU 솔루션 공개(보안뉴스)](https://m.boannews.com/html/detail.html?idx=144445)
- [모빌린트(AI 반도체) 기업정보(THE VC, 2026.05.22)](https://thevc.kr/mobilint)

**10장 — 엣지 한중 비교**
- [2026 하반기 로보틱스 산업 전망(신한금융투자, 2026.05.22)](https://www.shinhangroup.com/kr/archive/insight/extend/detail/32871)
- [[더테크] 중국 휴머노이드 로봇, 실전 투입으로 진화 가속(THE TECH, 2026.06.11)](https://www.the-tech.co.kr/news/article.html?no=41605)
- [중국 제조업 AI 자동화, 어디까지 왔나(Korea Business Review, 2026.08.10)](https://www.koreabizreview.com/articles/global-radar-ai-tech-ai-robot-20260810-tm8r)
- [AI 휴머노이드 진화 특성: 美-中 비교를 중심으로(ETRI ICT정책 이슈&트렌드, 2025-01)](https://ksp.etri.re.kr/ksp/plan-report/file/1450.pdf)

**11장 — 소프트웨어 생태계**
- [CUDA Lock-in Unpacked(SoftwareSeni, 2026.04.27)](https://www.softwareseni.com/cuda-lock-in-unpacked-the-software-moat-the-real-switching-costs-and-how-they-are-changing/)
- [Nvidia's CUDA Lock-In and Supply Scarcity(Alphastreet, 2026.03.27)](https://news.alphastreet.com/nvidias-cuda-lock-in-and-supply-scarcity-make-its-ai-chip-moat-harder-to-break-than-it-looks/)
- [The Next Wave of AI Infrastructure Must Target NVIDIA's CUDA Moat(Built In, 2026.01.28)](https://builtin.com/articles/nvidias-cuda-future-ai-infrastructure)
- [Ascend: Open for All to Build a Vibrant Ecosystem(Huawei, 2025.09.20)](https://www.huawei.com/en/news/2025/9/hc-shengten-opensource)
- [Huawei Unveiled the Latest SuperPoD(Huawei, 2026.03.02)](https://www.huawei.com/en/news/2026/3/mwc-superpod-ai)
- [Huawei Version of CUDA Fully Open-Sourced(36Kr, 2025.08.06)](https://eu.36kr.com/en/p/3411091131567747)
- [RBLN NPU용 vLLM 플러그인(리벨리온 공식문서)](https://docs.rbln.ai/latest/ko/software/model_serving/vllm_support/vllm-rbln.html)
- ['K-엔비디아'는 가능한가…딥엑스·퓨리오사AI·리벨리온의 성공조건(eFactoryNews, 2026.04.14)](https://www.efactorynews.com/sub_view.asp?ch=31&t=0&idx=22370)
- [MWC 2026 Takeaway 2(Jeffrey Towson, 2026.03.13)](https://jefftowson.com/membership_content/mwc-2026-takeaway-2-huaweis-ai-infrastructure-depends-on-people-not-just-processors-2-of-4/)
- [빅테크는 ASIC, 범용은 엔비디아…좁아지는 K-NPU 입지(ZDNet Korea, 2026.08.07)](https://zdnet.co.kr/view/?no=20260807154129)
- [Will any China-domestic AI chip reach ≥80% of NVIDIA H100 perf on a public benchmark before 2026-12-31?(Manifold, 2026)](https://manifold.markets/ChristopherBerzins/will-any-chinadomestic-ai-chip-reac)
- [Furiosa RNGD NPU에서 LLM 모델 서빙하기(Dudaji Tech Blog, 2025.12.26)](https://blog.dudaji.com/furiosa-rngd-npueseo-llm-model-seobinghagi/)

**12장 — 제조·공급망**
- (7장·11장 출처와 중복되는 SK하이닉스·삼성 관련 출처 참조)

**13장 — 정책지원**
- [China's $47.5bn 'Big Fund III' Fuels Semiconductor Self-Sufficiency(Quantum Zeitgeist)](https://quantumzeitgeist.com/chinas-47-5bn-big-fund-iii-fuels-semiconductor-self-sufficiency-amid-us-tech-war/)
- [AI 예산사업 통합 설명자료(국가인공지능전략위원회, 2026)](https://aikorea.go.kr/web/board/brdDetail.do?currentPage=1&menu_cd=000011&num=359)
- [2026년도 AI 예산(AI반도체과)(광주광역시의회, 2026)](https://council.gwangju.go.kr/attach/544/a7d4a1b90fd2a7d6cbe72e297f2f652c.pdf)
- [9.9조원의 AI 예산, 2026년 정부 인프라 지원사업 정리(effettoblog, 2026)](https://effettoblog.com/blog/2026%EB%85%84-%EC%A0%95%EB%B6%80-ai-%EC%98%88%EC%82%B0-9-9%EC%A1%B0%EC%9B%90-%EC%8B%9C%EB%8C%80-%EA%B3%B5%EA%B3%B5-ai-%EC%9D%B8%ED%94%84%EB%9D%BC-%EC%82%AC%EC%97%85-%EC%99%84%EB%B2%BD-%EC%A0%95/)