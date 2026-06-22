# AIO (OLAXBT) — On-chain Decision Briefing


## 🎯 One-screen verdict

> This section is deterministically derived from on-chain detector outputs and is not buy/sell advice. Full evidence is in the sections below.

| Dimension | Conclusion | Key evidence |
|---|---|---|
| **Current phase** | 🟢 Accumulation / watch — no significant trigger | None of the 5 main signal tiers triggered |
| **Chip structure** | 🟠 Moderately controlled | Operator/project-controlled chips 65.8% / CEX relay pool 26.8% / verifiable non-operator sell-pressure 7.4% |
| **Insider / operator spot realization** | 🔴 Heavily realized | Confirmed insider realization 36.5% of circ + net CEX-withdrawal distribution 0.0% of circ |
| **Volume quality** | 🔴 24h volume untrustworthy — wash bots dominate | 750,998 on-chain matches; single bot 14.0% |
| **Supply risk** | 🔴 Active mint / bridge supply source | 1 mint-authority contracts; cumulative mint = 100.0% of total supply |
| **Market-cap stage** | 🟢 Low mcap | mcap $41.4M; 5% depth $30; LP/mcap 0.052; vol/LP 0.0×; 24h +9.1% |
| **Monitoring focus** | Maintain baseline monitoring | Mint-authority contracts, High-frequency liquidation wallets |

**One-liner**: Accumulation / watch + Moderately controlled + volume inflated by wash.

## 🎯 Quick-read summary

> This section is for quick retail reading / AI re-interpretation. Detailed forensic detection is in the sections below (with English terms). Everything here is derived from on-chain data and contains no buy/sell advice.

- **Project**: OLAXBT (AIO), main contract [`0x81a7da40…`](https://bscscan.com/address/0x81a7da4074b8e0ed51bea40f9dcbdf4d9d4832b4)
- **Listing**: Binance Alpha S2 (Spot + Perp) · primary chain BSC

- **Confirmed insider on-chain realization**: **129,031,593 tokens (36.48% of circulating)** ≈ **$15,713,734 USD** — a lower bound on what insider wallets have realized themselves via (a) deposits to centralized-exchange deposit addresses + (b) their own direct on-chain matches; actual sell-out is most likely higher (see 📊 Confirmed sell-out section)
- **Historical high-throughput operators surfaced**: 100 wallets ran cumulative **throughput** (token in/out flow, NOT sell volume, includes wash double-counting) of **1,762,628,288 tokens** over 365 days then zeroed out — already exited

- **Report-completeness note**: only on-chain-verifiable wallet → DEX/CEX flows are included. Off-chain behaviour (distribution after a CEX withdrawal / OTC transfers / bridges not in the surf index, etc.) is not on-chain-detectable, so real sell-out may exceed the figures here. See the 🟡 completeness note below.

- **How to use this report**: read it alongside the **Monitored wallets** section below; add the core wallets to Binance Wallet / OKX monitoring (monitoring_paste.json supports one-click import). Make entry/exit decisions according to your own risk tolerance.


> ⚠️ **Read first — on-chain detection limits / data caveats**
>
> - 🚨 **24h volume / on-chain matches dominated by a wash bot**: 200 counterparty addresses / 750,998 on-chain matches, with a single wash bot doing up to 105,318 wash matches (single wash bot share 14.0%). **Do not use 24h volume to judge real absorption** — see "absorption cap (5% depth)" below. Detail → 📊 Confirmed sell-out section.
> - 🟡 **Several dump paths are structurally out of coverage**: ⛓️ cross-chain dumps (other chains invisible) / 🌉 bridge mint-authority self-dumps (mint source selling itself) / 🏦 the CEX-withdrawal phase (off-chain, not on-chain-detectable) / ⏰ 60d+ historical high-throughput dumps. **Real sell-out may be 5-50× the figures here**. v0.7.24 backlog: mint-authority + multi-chain + high-throughput detectors added (see 🌉 / 🌊 / 🔗 sections at the end).
_Tool version 1.0.4 · Main chain BSC · Alpha listed 2025-10-26_

_Total supply 1,000,000,000 · Circulating 353,750,000 (35.4%) · Type VC_LIKELY_
_Tier S2 · S1 2025-10-26 · S2 2025-08-13_
## 💹 Token market (real-time)

| Item | Value |
|---|---|
| **Project name** | **OLAXBT** (AIO) |
| Ticker | `AIO` |
| Primary chain | BSC |
| Listing | S2 (Alpha + Binance Perps) · Alpha listed 2025-10-26 · Perp listed 2025-08-13 |
| **Current price** | **$0.1161** (🟢 +8.28% 24H) |
| **Network 24H volume (CEX+DEX)** | **$1,694,901** |
| Current LP (DEX main pool) | $2,150,036 |
| Market cap (mcap / FDV) | $26,799,731 / $116,394,055 |
| Data source | surf+Alpha API (real-time) · 59,538 holders · 24H 5,418 txns |

## 📋 Decision summary

| Item | Value |
|---|---|
| **🎯 Risk score** | **🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ (2/10)** |
| **On-chain state label** | **No significant trigger** — No significant on-chain detection trigger |
| Primary chain | binance-smart-chain (this chain's current LP $3,558) |
| **Entry cap (LP 5% depth)** | **$30** |
| Near-term catalysts | None |
| Blind spots you must cross-check yourself | None |

> 🎯 **Meaning of the 5 on-chain-state labels** (deterministically derived at render time, describing on-chain detection state only, not trading advice):
> - **No significant trigger** — no significant on-chain detection signal (risk 0-2)
> - **Watching** — some activity but no primary signal triggered (risk 2-5)
> - **Distributed and exited** — historical operator already distributed; on-chain historical sell-pressure released (risk 4-7)
> - **Dormant insider, undistributed** — dormant insider wallets have not distributed; timing unpredictable (risk 6-9)
> - **Recent distribution** — large on-chain activity in the last 72h (risk 7-10)

> Based on the analysis of AIO, the trade sizing is restricted to a max of $30 due to shallow depth.



## 🎯 On-chain state: No significant trigger (risk score 2/10)

**No significant on-chain detection trigger**


| Decision anchor | Value | Status |
|---|---|---|
| Alpha 5% slippage cap | $30 | 🔴 Very thin |
| DEX main pool USD liquidity | $2,125,958 | 🟢 |
| Pool token 24h net throughput (NOT LP add/remove) | — | 🟢 |


## 🧠 Current on-chain behaviour profile

> This section translates 10 detector outputs into 4 categories of "what the operator might be doing." Multi-label by design — one token can hit several categories at once (e.g. A1 accumulation + B1 wash volume + C3 recent activity). Order: severity (🔴 STRONG / 🟠 MEDIUM / 🟡 WEAK) → category → label ID. Describes on-chain facts only, not trading advice.

| Severity | Label | Category | Trigger metric | On-chain fact |
|:-:|---|---|---|---|
| 🔴 **STRONG** | `A3` Mint / bridge / mining supply source | A Chip preparation | `mint_authorities=1, mint_pct_supply_max=100.0, mint_pct_supply_sum=100.0` | 1 mint-authority contracts present (cumulative mint = 100.0% of circulating supply), an ongoing supply source — future mint → dump is possible |
| 🔴 **STRONG** | `B1` Wash-trade volume inflation (24h vol untrustworthy) | B Volume fabrication | `wash_swap_count=750998, wash_top_bot_share=0.14, wash_n_dex_addrs=200` | 750,998 on-chain matches in 24h across 200 on-chain trading addresses, a single wash bot accounting for 14.0% — the 24h volume contains heavy wash trading and does not equal real absorption |
| 🔴 **STRONG** | `C1` On-chain confirmed outflow (CEX deposit + DEX swap) | C Dump behavior | `net_sellout_usd=15713734.0, sell_pct_circ=36.475` | On-chain confirmed outflow $15,713,734 (36.48% of circulating) — real insider realization observed via CEX deposit + on-chain match paths |
| 🔴 **STRONG** | `C2` Historical high-frequency operator liquidation | C Dump behavior | `ht_operator_count=100, ht_throughput_pct_supply=176.26` | 100 high-frequency operator wallets (cumulative **throughput** = 176% of total supply; throughput = token in/out flow, NOT sell volume) — already exited historically, balance near 0 |

> **Behaviour profile is not the verdict**: the 🎯 on-chain state label above is a composite of 5 tiers (No significant trigger / Watching / Distributed and exited / Dormant insider / Recent distribution); the behaviour profile here is the finer-grained 10-class on-chain detection signals. A token can be "Recent distribution" while also hitting multiple labels like A1+A2+A3+B1+C2+C3.


## 🔴 Confirmed sell-out (insider lower bound)

### 🎯 Pump counterparty check

> **⚡ Quick read**: circulating 208.6M tokens · **non-operator sell-pressure 7.4%** (15,337,497 tokens = verifiable within top 100 holders 7.4%) · operator ammo 65.8% (⚠️ Alpha API reports 354M circulating, on-chain dumpable 209M = 0.59x, Alpha overstates (includes mint authority / vesting lockup)) · exchange transit pool (retail vs project custody indistinguishable) 26.8% (10 exchange wallets) · insider confirmed realization $15,713,734 (36.5% of circulating).

> When the operator wants to pump, **the potential sellers = the held chips that don't belong to the operator**. The smaller this is, the more confident the operator is to pump (less fear of being dumped on); the larger, the more cautious.

| Chip bucket | Tokens | % of current circulating | Interpretation |
|---|---:|---:|---|
| 🟣 **Operator / project-controlled chips** | **137,253,345** | **65.8%** | **Moderate control** |
| 🔥 **Verifiable non-operator sell-pressure** | **15,337,497** | **7.4%** | **Moderate external sell-pressure** (includes retail whales + protocol contracts + bridge transit) |
| 🟦 **Exchange transit pool (neutral, indistinguishable)** | **55,994,327** | **26.8%** | 10 exchange hot/cold/deposit wallets. On-chain it is **impossible to distinguish** retail deposit aggregation vs project custody reserve. During a pump it may flow out from either side |

### Key judgment

**Project-controlled chips ≥ 50%** — the operator has the conditions to control the book. Read with "insider confirmed realization" below to see whether it is in the active-distribution phase.
**Raw bucket total 896% (expand for detail)** — wallet-level overlap across buckets is a debug caveat and does not affect the quick-read 65.8% operator-ammo conclusion.

<details>
<summary>🔍 Expand: operator-ammo 11-sub-bucket detail (with raw total + overlap note)</summary>

| Sub-bucket | Tokens | % of circulating | Note |
|---|---:|---:|---|
| ①a Public lockup / treasury / airdrop contract outside m6 lineage | 0 | 0.0% | Sablier / Hedgey / custom lockups. Public release schedule, **won't dump immediately during a pump**. Lower bound after subtracting the 646,250,000 unminted reserve |
| ①b Movable multisig outside m6 lineage | 0 | 0.0% | Gnosis Safe Proxy etc. The operator can transfer today with one signature |
| ② m6 lineage portion in circulation | 0 | 0.0% | m6 lineage total holdings 4,496,369 minus lockup 0. Includes pure insiders (4,496,369) |
| ⚠️ ③ Exchange-withdrawal distribution (net control not computable) | — | — | Gross inflow; phase-2 SQL truncated; net fan-out cannot be computed.  |
| ④ DEX pool token-side holdings | 30,648 | 0.0% | DEX pools are 99% provided by the project / market maker |
| ⑤ Other detector hits | 1,018,667 | 0.5% | 33 wallets — flow operators / cross-token whales / high-throughput exit operators |
| ⑥ Mint-contract unreleased reserve | 757,743,057 | 363.3% | Mining / bridge mint contract current balance; operator-controlled unreleased supply |
| ⑥' Minted to operator cluster (net holdings) | 219,516,530 | 105.2% | Cumulative mint - contract reserve - realized = still in the fake-mining cluster |
| ⑥'' Heuristic hidden ammo (top-100 unclassified ≥ 3%) | 890,412,746 | 426.9% | 6 wallets. **The 3% threshold risks false positives** — cross-check via monitoring_paste |
| 📌 Unminted operator-controlled reserve | 646,250,000 | _64.6% of total supply_ | **Not in the circulating denominator — but operator-controlled**. Adds sell-pressure once lockup / mint cadence releases it into circulation |
| ━━━━━ | ━━━━━ | ━━━━━ | ━━━━━ |
| Operator ammo raw total | 1,868,721,649 | 895.9% | ⚠️ > 100% = wallet-level overlap across sub-buckets (an in-m6 multisig counted in both ①b + ②). The quick-read 65.8% is a strictly de-duplicated wallet-level back-calculation |

**Notes**:
- The quick-read "operator ammo" is a **wallet-level back-calculation**: iterate the top 100 and de-dup-sum those in the operator set. Different from the raw total — raw is per-bucket upper bound (with overlap), quick-read is strictly de-duplicated.
- The quick-read "non-operator sell-pressure" includes **retail whales + protocol contracts (Wormhole / veVELVET etc.)**, not all of which is true retail. It is an upper bound.
- ①a vesting / ⑥ mint reserve → **won't dump immediately** during a pump; enters circulation only over the medium term.
- ①b multisig / ⑥' cluster → **transferable today**, different in nature from "lockup".
- Algorithm version: operator-ammo / non-operator-sell-pressure reverse algorithm v0.8.4.8.

</details>

#### 🔍 Verifiable non-operator sell-pressure wallet detail (reverse calc)

> Top-100 holders that are **neither in the operator set nor the exchange pool**. Operator set: m6 lineage + multisig / public lockup / treasury / airdrop contract / DEX pool + heuristic catches + detector hits. **All exchange wallets are excluded** (placed in the neutral "exchange transit pool", retail deposits vs project custody indistinguishable). Non-operator sell-pressure mainly comprises true retail whales + bridge protocol contracts + DeFi protocol contracts.

| # | Wallet | Current balance | % circulating | Type | Arkham label |
|---:|---|---:|---:|---|---|
| 1 | [`0x3c6953b84076`](https://bscscan.com/address/0x3c6953b8407652d5f4b2634b22739a1752a2521e) | 7,373,965 | 3.54% | Unclassified | — |
| 2 | [`0x2a78eb7f9358`](https://bscscan.com/address/0x2a78eb7f935875277a2199eb7c8605cd67075386) | 3,200,000 | 1.53% | Unclassified | — |
| 3 | [`0xa6f2434b63ed`](https://bscscan.com/address/0xa6f2434b63ed85838ccc0f7255b030447d57fccb) | 2,421,719 | 1.16% | Unclassified | — |
| 4 | [`0xd860312ec79e`](https://bscscan.com/address/0xd860312ec79e5692dfa75d9af291910c8cbf4490) | 2,341,813 | 1.12% | Unclassified | — |
| ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━ | ━━━━━━━ | ━━━━━━━━━ | ━━━━━━━━━ |
| **Total verifiable non-operator sell-pressure (within top 100 holders)** | 4 wallets | **15,337,497** | **7.4%** | — | — |

> ⚠️ **Nature of non-operator sell-pressure**: mainly true retail whales + protocol contracts like Wormhole / veVELVET (user-deposited) + bridge transit. Large bare addresses (no Arkham label + > 1% circulating) are suspect as either operator aliases or true retail whales — cross-check wallet activity via monitoring_paste below.

---

| Item | Value |
|---|---|
| Tracked wallets | **106** (105 standard insiders + **1 mint authorities**; mining / bridge token, no pre-launch m6 lineage) |
| **Pure insider current holdings (the true dormant sell-pressure the verdict references)** | **76.2239% of supply** (762,239,426 tokens, **excluding** vesting / multisig / treasury / CEX custody / DEX routing; includes mint-authority contract current balance) · 🌉 mint authority still sits on 757,743,057 tokens (can keep mint→dumping at any time) |
| Insider-tree current holdings (incl. lockup, conservation anchor) | 76.2239% of supply (762,239,426 tokens, in mining mode the tree = standard insiders + mining-fed set + mint-authority contracts (no vesting/lockup separation)) |
| (a) Confirmed sell-out — CEX deposit | 43,580,981 → Bitget, Gate Deposit, MEXC, Cold Wallet, MEXC Deposit |
> _💡 Note: off-chain CEX withdrawals (CEX → wallet) are not in row (a) — (a) only tracks on-chain wallet → CEX deposits. A project that withdraws from a CEX first and then dumps (e.g. the H case Eleve described) does so off-chain and cannot be on-chain-detected; any subsequent on-chain transfer that dumps via a DEX router is already captured in row (b)._
| (b) Confirmed sell-out — DEX swap (own wallet) | 85,450,611 (56,932 swaps all via DEX router) |
| **Confirmed gross sell-out, a+b** | **≥ 129,031,593 = 36.5% of circulating**, USD ≈ $15,261,674 |
| **Confirmed net sell-out** | **$15,713,734** — insider **self-sell DEX TWAP** $0.1218 (rejects wash-quote contamination); DEX real ≈ $10,406,352 (on-chain SUM amount_usd, 100% provable) + CEX estimate ≈ $5,307,382 (cex_tokens × TWAP) |



> **📅 Time-window split** — reconcile against short-term events (Twitter sudden-dump alerts / large moves); the relationship is **last 7d ≤ last 30d ≤ cumulative**.

| Window | Confirmed gross sell-out (tokens) | % of circulating | Confirmed net sell-out (USD) | DEX real volume (USD) | CEX route (tokens) |
|---|---:|---:|---:|---:|---:|
| **Last 7 days** | 83,626 | 0.02% | **$8,105** | $3,586 | 37,113 |
| Last 30 days | 1,037,565 | 0.29% | $121,452 | $33,696 | 720,597 |
| Cumulative (~364 days) | 129,031,593 | 36.48% | $15,713,734 | $10,406,352 | 43,580,981 |

> Interpretation: **last 7 days** shows current heat (reconcile directly with EmberCN-style sudden alarms); **last 30 days** shows the month's pace; **cumulative** = everything within the surf query window. A single-day burst may not show in the 7d average but is already in the cumulative. CEX route = tokens that went into exchange deposit/hot wallets (sold off-chain on the CEX side, not at the wash price).


> 🕵️ **Hidden operator ammo has shown realization activity**: the tracked **10 hidden-ammo wallets** (heuristic catches / fake-mining mint cluster) have, via (a) deposits to exchange deposit addresses of **22,740,413 tokens** (4 exchanges: Binance Wallet, Bitget Deposit, KuCoin Deposit, MEXC Deposit) + (b) their own on-chain matches of **0 tokens** (0 swaps), totalled **22,740,413 tokens** = 6.43% of circulating. **These wallets are outside the algorithm's 5 buckets** and may add on top of "confirmed gross sell-out" to view real distribution; but **you must subtract any wallet overlap with the m6 insider / mining-fed sets** (v0.8.4 backlog: add disjoint dedupe). Time window: from 2025-10-26.> ⚠️ **This token's on-chain dump is dominated by a wash bot**: 200 counterparty addresses with 750,998 on-chain matches total, a single wash bot doing up to 105,318 wash matches. Many insiders route tokens to relays / bots before selling (this portion is **unattributable** and not counted in the confirmed lower bound above — so real sell-out is most likely higher than the lower bound). Massive wash = dumping while inflating surface activity to lure buyers.


<a id="section-recent-anomaly"></a>
## 📊 Risk-signal aggregation (detectors + rhythm)

### Detector summary

| emoji | Category | Count | Interpretation |
|---|---|---|---|
| ⚪ | Pre-launch insider distribution | 0 | No pre-launch distribution to early wallets was identified on BSC. |
| ⚪ | Fully-distributed insider wallets | 0 | No fully-distributed insider wallets were recorded on BSC. |
| ⚪ | Quiet wallets (never distributed) | 0 | No quiet insider wallets holding supply were identified on BSC. |
| ⚪ | Recent 72h anomaly large transfers | 0 | No anomalous large transfers were observed in the past 72 hours on BSC. |

### Rhythm recognition

**On-chain transfer rhythm for AIO.**



<details>
<summary>📂 <strong>📊 Full anomaly event list (raw detail, grouped by distribution wave, UTC)</strong> — 0 distribution waves, 0 events total (click to expand the full timeline + wallet flows)</summary>


</details>


## Primary chain (MULTI-CHAIN)

| Item | Value |
|---|---|
| **Primary chain** | **BSC** (BNB Chain) |
| Mint chain (supply_chain) | BSC, totalSupply 1,000,000,000 |
| Trading chain (trading_venue_chain) | BSC (Alpha + DEX main pool) |
| Cross-chain distribution | **Single chain, no cross-chain bridge found** (v0.6 phase B.3 minimal — BSC only) |
| Report coverage | **Full coverage** |

✅ No non-BSC chain data required.

**Interpretation**: The token AIO is deployed as a single-chain asset on BSC with no cross-chain bridge activity.

## Entry-price anchor (TGE)

| Time anchor | UTC | Price | vs current |
|---|---|---|---|
| LP creation first tx (DEX start) | — | — | — |
| Alpha first tx | 2025-10-26 08:00 UTC | — | — |
| **Current price** | 2026-06-22 | **$0.1182** | 1.00× |

**Interpretation**: The token was first listed on Binance Alpha on 2025-10-26 UTC. The current price is $0.1171.

<a id="section-alloc"></a>
## Project allocation power (ALLOC)

| Item | Value | Source |
|---|---|---|
| Alpha quota (officially disclosed) | **Not disclosed** | Binance Alpha API does not expose this field |
| Deployer wallet `—` current balance | Unknown | Deployer distribution trace |
| Pre-launch insider recipients 0 cumulative balance | 0 tokens (= 0.00% of supply) | Insider wallet sum |
| Quiet wallets 0 holding (core future risk) | **0 tokens (= 0.00% of supply / $0)** | Insiders that never distributed |
| Fully-distributed insiders 0 (distribution complete) | 100% distributed, 0 remaining | Insiders with ≥95% distributed |

**Interpretation**: No verified early insider distributions were detected on-chain, indicating supply remains inside reserve clusters.

## Near-term CEX catalyst (CEX-TRACE)

| Exchange | Status | Time | Since |
|---|---|---|---|
| Binance | Listed | 2025-08-13 | ~10 months ago |
| Aster | Unverified | — | — |
| Bitget | Unverified | — | — |

No new catalyst within 14 days. Current S2 (Alpha + Binance Perps).

**Interpretation**: The token is currently listed on Binance with perps active since 2025-08-13, representing S2 classification.

<a id="section-liq"></a>
## Entry ceiling (LIQ)

| Anchor | Value | Note |
|---|---|---|
| **Max single buy under 5% slippage (estimated)** | $30 | Derived from Alpha 24h vol (vol_24h / 96 × 0.05 heuristic estimate) |
| DEX main pool liquidity | $2,125,958 | surf 0x97620e00… |
| DEX main pool 24h volume | $1,694,901 | surf project-detail (cross-chain CEX+DEX realtime aggregation) |
| Pool token 24h net throughput (NOT LP add/remove) | — | surf agent.bsc_transfers |
| DEX main pool address | `0x97620e003c03381eacbde7135f28d94303bb5672` | FDV $116,394,055 |

**Interpretation**: DEX liquidity is $2,125,958.01 but estimated 5% depth is extremely low at $30, limiting trade sizing.

<a id="section-holdings"></a>
## Holdings distribution by role

**Distribution table**:

| Role | Wallet # | Current balance | % of supply | Top wallet |
|---|---|---|---|---|
| DEX main pool | 1 | 12,069,966 | 1.2070% | [`0x97620e00…`](https://bscscan.com/address/0x97620e003c03381eacbde7135f28d94303bb5672) |
| Deployer wallet | 0 | 0 | —% | — |
| Project / infra / distribution pool (vesting / multisig / treasury / DEX infra / CEX custody / 3rd-party distribution platform / retail claim pool, Arkham-verified) | 3 | 761,079,773 | 76.1080% | [`0x78818ee5…`](https://bscscan.com/address/0x78818ee5d3899176f99d79dda24d3d626b958bb6) |
| Quiet wallet (insider, never distributed) | 0 | 0 | —% | — |
| Other (retail + unclassified) | 46 | 222,349,651 | 22.2350% | [`0x207d87cd…`](https://bscscan.com/address/0x207d87cd5710ad33c00615c423093ec89d273f51) |

**Key takeaways**:
- Insider tracking: **106** wallets hold **0.4%** of supply cumulatively, incl. 1 mint authorities  (mining / bridge token, no pre-launch m6 lineage).
- Insiders have on-chain-confirmed outflow of **15.7M USD** = **36.48%** of circulating, priced at the insider self-sell TWAP (not the wash quote).

<details>
<summary>📂 <strong>Backward trace (Deployer → insider lineage)</strong> — 0 insider wallets: 0 fully distributed / 0 distributing / 0 quiet (click to expand the full lineage + wallet balances + distribution rate)</summary>

**Insider wallet list (deployer distribution trace)**:

| ID | Address | Received from deployer | Current balance | Dumped % |
|---|---|---|---|---|
_Stats (full m6 lineage, **0** wallets): 0 near-zero holdings / public-lockup custody · 0 distributing · 0 fully distributed_

**m4_notes (pre-LP allocation interpretation)**:
- The pre-launch phase for AIO shows no early wallet deployments or allocations.
- No pre-launch OTC seeding was detected on BSC for AIO, which means there are zero verified early insider recipients.
- Without any pre-launch deployment trace, the initial allocation remains highly concentrated in the creator/unlabeled reserves.



</details>

## 💰 High-Value Address Funding Source (mint / DEX / P2P)

Below are the high-value addresses already surfaced by the wash setup / flow operator / m6 insider / Top-30 holder sections, classified by how they ACQUIRED their tokens over the past 365 days: mint (received directly from 0x0 — covers mining contracts, bridge mint authorities, airdrop mint contracts), DEX buy (received from a known DEX main pool), or P2P (any other EOA transfer, including unidentified CEX withdrawals). Use this to distinguish: ⛏️ high mint% = mining-token operator or sockpuppet airdrop farmer; 🟢 high DEX% = real retail buyer; 🔵 high P2P% = operator aggregation hub or OTC recipient.

> Queried 200 high-value addresses; 12 have real incoming activity in the past 365 days — ⛏️ Mint-fed 0 / 🟢 DEX-fed 0 / 🔵 P2P-fed 12.


| Address | Primary Source | Total Received | Mint % | DEX buy % | P2P % |
|---|---|---:|---:|---:|---:|
| [`0x9999b0cd…`](https://bscscan.com/address/0x9999b0cdd35d7f3b281ba02efc0d228486940515) | 🔵 P2P-fed | 224,998,441 | 0.0% | 28.9% | 71.1% |
| [`0xfc098099…`](https://bscscan.com/address/0xfc0980992ab0d7ef1e7359a868f2870c92a9e13b) | 🔵 P2P-fed | 44,046,632 | 0.0% | 0.0% | 100.0% |
| [`0x5a5867b4…`](https://bscscan.com/address/0x5a5867b4e3a1cd7afe8686f252459b4de424225b) | 🔵 P2P-fed | 13,948,303 | 0.0% | 0.0% | 100.0% |
| [`0xfb4165e2…`](https://bscscan.com/address/0xfb4165e2f32b2e942dfcc3dcf420954237b523e0) | 🔵 P2P-fed | 10,251,140 | 0.0% | 0.0% | 100.0% |
| [`0x0f0067cd…`](https://bscscan.com/address/0x0f0067cd819cb8f20bda62046daff7a2b5c88280) | 🔵 P2P-fed | 7,421,196 | 0.0% | 0.4% | 99.6% |
| [`0x0a6ed58e…`](https://bscscan.com/address/0x0a6ed58ed2c1849b281f6b379c2764e17d57a7e8) | 🔵 P2P-fed | 5,414,892 | 0.0% | 0.0% | 100.0% |
| [`0x286b9604…`](https://bscscan.com/address/0x286b960493f8dc81c5d6626eba53547f4a7d8175) | 🔵 P2P-fed | 5,051,000 | 0.0% | 0.0% | 100.0% |
| [`0x2230345e…`](https://bscscan.com/address/0x2230345ea2f77709a91447d1a6862212f59c6879) | 🔵 P2P-fed | 4,072,801 | 0.0% | 0.0% | 100.0% |
| [`0x4788cecf…`](https://bscscan.com/address/0x4788cecfbed4a2cbc3e006368a54f4c5174a3cd8) | 🔵 P2P-fed | 2,497,721 | 0.0% | 0.0% | 100.0% |
| [`0x0e91e407…`](https://bscscan.com/address/0x0e91e407a3c8887b0713d9abf7695cb6efdc385c) | 🔵 P2P-fed | 1,402,473 | 0.0% | 0.0% | 100.0% |
| [`0xc408d39f…`](https://bscscan.com/address/0xc408d39f1c009a95d31861b094b100dbb196b5cd) | 🔵 P2P-fed | 468,838 | 0.0% | 0.0% | 100.0% |
| [`0x666ae865…`](https://bscscan.com/address/0x666ae8654992cf7260c08f076a8a727a91f1e733) | 🔵 P2P-fed | 394,350 | 0.0% | 0.0% | 100.0% |

> _Scan cap: the pipeline collected 230 high-value candidates, max_addrs cap = 200, actually queried 200 (ordered by detector priority: wash → flow → m6 → dump-sellers → Top-30 holders). Truncated 30 — common on PLAY-class tokens with many (60+) flow_operators._

> _The CEX-withdrawal column is not yet separately identified (a v0.7.24 candidate) and is currently grouped under P2P. When a real CEX hot-wallet transfer cannot be distinguished from a plain EOA transfer, both count as P2P._



<a id="section-bridge-mint"></a>
### 🌉 Bridge / mint-authority self-sell detail (v0.7.24a)

> Detected **1 mint-authority contracts** (receive mint from 0x0, excluding the deployer + wallets already covered in the mining-fed section). They are bridge / staking / airdrop contracts that may **themselves** DEX swap. This is a dump path the v0.7.23.x series missed entirely.

| Authority address | Arkham label | 365d Mint amount | % of supply | Own DEX sell | USD ≈ |
|---|---|---:|---:|---|---:|
| [`0x78818ee5d389…`](https://bscscan.com/address/0x78818ee5d3899176f99d79dda24d3d626b958bb6) | _Unlabeled (new contract, not in Arkham) | 1,000,000,000 | 100.00% | — (no direct DEX self-sell) | — |





<a id="section-high-throughput"></a>
### 🌊 High-throughput dump wallets (v0.7.24b)

> Detected **100 operator wallets** with a high-throughput clear-out pattern (large token flow-through + balance ≈ 0 + high-frequency tx). Thresholds: throughput 1M ~ 5% of supply, balance < 5% of throughput, n_tx ≥ 1000. Already filtered out infra labels like DEX routers / CEX deposits / aggregators (not operators). These are operators that finished dumping and left before the 60d window — missed by flow_operators (60d window) + mining-fed (balance > threshold).

| Operator address | Primary role | Arkham label | 365d inflow (= received mint/p2p) | Outflow (= sold / transferred out) | Residual balance | tx count |
|---|---|---|---:|---:|---:|---:|
| [`0xe97b1f053c91…`](https://bscscan.com/address/0xe97b1f053c9118041c9016d83c86deffbf398095) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 49,903,783 | 49,903,783 | 0 | 5,763 |
| [`0x3d6035e23ce3…`](https://bscscan.com/address/0x3d6035e23ce306a0b3dd23977f6aa904c9bd3154) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 47,965,412 | 47,913,265 | 52,147 | 12,942 |
| [`0x6aba0315493b…`](https://bscscan.com/address/0x6aba0315493b7e6989041c91181337b662fb1b90) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 47,342,047 | 47,342,111 | -63 | 61,190 |
| [`0xd547eafde241…`](https://bscscan.com/address/0xd547eafde2410e63300fc5308ccea0b356e7b5d8) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 45,848,404 | 45,848,404 | 0 | 69,602 |
| [`0x53f78a071d04…`](https://bscscan.com/address/0x53f78a071d04224b8e254e243fffc6d9f2f3fa23) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 45,076,065 | 44,722,387 | 353,678 | 6,567 |
| [`0xdfc1db4904dc…`](https://bscscan.com/address/0xdfc1db4904dc1e7718d4783bd4be02ac1967ae86) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 44,622,595 | 44,612,172 | 10,423 | 12,138 |
| [`0x971435fc38ee…`](https://bscscan.com/address/0x971435fc38eed5e0aaff0dd717d0d16a02a4110e) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 44,298,637 | 44,310,603 | -11,965 | 241,692 |
| [`0xfc0980992ab0…`](https://bscscan.com/address/0xfc0980992ab0d7ef1e7359a868f2870c92a9e13b) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 44,046,632 | 44,046,632 | 0 | 49,324 |
| [`0xb94741fb3240…`](https://bscscan.com/address/0xb94741fb32409f914c67d161efa718815c038b3f) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 43,890,895 | 43,898,531 | -7,636 | 12,050 |
| [`0x5ddf9200ca81…`](https://bscscan.com/address/0x5ddf9200ca8163585d1d9b05022adc14c32a71f1) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 42,932,826 | 42,920,480 | 12,346 | 11,856 |
| [`0x45a2e455b2f7…`](https://bscscan.com/address/0x45a2e455b2f7054f02317533057ed60196c90f73) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 42,699,222 | 42,699,026 | 196 | 11,796 |
| [`0x6e1b2a5bc882…`](https://bscscan.com/address/0x6e1b2a5bc88227d7067b4d02ef82dd1b8c4fcd7b) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 42,497,571 | 42,452,856 | 44,715 | 11,742 |
| [`0x802b65b5d901…`](https://bscscan.com/address/0x802b65b5d9016621e66003aed0b16615093f328b) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 42,493,168 | 42,494,055 | -888 | 167,064 |
| [`0xac30203cb479…`](https://bscscan.com/address/0xac30203cb479ee89696d9e7ec98dca08fd538065) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 42,172,889 | 42,162,882 | 10,007 | 11,685 |
| [`0xb6e27c34a794…`](https://bscscan.com/address/0xb6e27c34a794d04e8e078b46cb38093be26f0516) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 41,272,079 | 41,260,189 | 11,891 | 11,486 |
| [`0x1906c1d672b8…`](https://bscscan.com/address/0x1906c1d672b88cd1b9ac7593301ca990f94eae07) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 40,203,664 | 40,203,664 | 0 | 64,313 |
| [`0xde9e4fe32b04…`](https://bscscan.com/address/0xde9e4fe32b049f821c7f3e9802381aa470ffca73) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 39,661,186 | 39,661,186 | -0 | 30,222 |
| [`0xda728a2e3c41…`](https://bscscan.com/address/0xda728a2e3c413b905b90d626e7d942435f80fc38) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 39,653,779 | 39,602,117 | 51,662 | 11,247 |
| [`0x87866aa14c37…`](https://bscscan.com/address/0x87866aa14c37306ef3ee49468f79f4e0e1cc52f6) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 39,331,507 | 39,320,569 | 10,939 | 11,132 |
| [`0xbce729580490…`](https://bscscan.com/address/0xbce729580490534fdaa5a4306c49c019418e2823) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 36,156,737 | 36,156,721 | 15 | 35,706 |

> _Showing top 20; 100 high-throughput operator wallets detected in total (sorted by throughput; throughput = token in/out flow, NOT sell volume). Full list in skeleton.json `funding_attribution.high_throughput_dumpers.dumpers`._

> 🌊 These wallets passed **1,762,628,288 tokens** through over 365d then cleared out — operators that have finished dumping. They've already sold, but **if the project mints another batch and distributes it to similar-pattern wallets in future**, they become the next dump-risk source.





<a id="section-wallet-cluster-graph"></a>
## 🌐 Wallet-graph clusters (v0.8.6.5)

> **Wallet ↔ wallet direct-transfer graph clusters** — operator clusters that bypass CEX, mint, and the m6 lineage. Bubblemaps-style algorithm: high-value transfers between candidate wallets (≥0.5% supply per edge) form connected components ≥ 3 nodes. Uses undirected 2-core pruning to exclude single-edge false positives.| Metric | Value |
|---|---|
| Clusters detected | **1** |
| Total cluster wallets | **3** |
| Candidate wallets input | 105 |
| Excluded by L1 Arkham filter | 0 |
| Total graph edges | 36 |
| Newly discovered (not master_cluster) | 0 |
| SQL chunks run | 1 |

#### 🌐 Cluster 1: 3 wallets

| Field | Value |
|---|---|
| cluster wallets | 3 |
| edge count | 3 |
| Total transfer weight | 19,234,065 tokens |
| Max edge weight | 7,081,665 tokens |
| Cluster current total holdings | 7,364,688 tokens |
| Arkham UNLABELED % | 100% |
| Source distribution | master_cluster: 3 |

**Cluster wallets (sorted by transfer weight)**:

| # | Recipient wallet | Current balance (tokens) |
|---:|---|---:|
| 1 | [`0x73d8bd54f7cf`](https://bscscan.com/address/0x73d8bd54f7cf5fab43fe4ef40a62d390644946db) | 7,356,764 |
| 2 | [`0xbd97306a087e`](https://bscscan.com/address/0xbd97306a087ed0c46b783cfbfdcdc6c12c7a2866) | 7,924 |
| 3 | [`0x653dd7677aea`](https://bscscan.com/address/0x653dd7677aea3030eab68c97ed3594bacf560158) | -0 |

<a id="section-monitoring"></a>
## Monitored wallets + real-time alerts


> 📊 **Monitoring priority (v0.7.27 deterministic ranker)**: 🚨 6 CRITICAL · 🔥 4 HIGH · 👀 0 NORMAL>
> Wallets in paste.json are sorted by level, 🚨 first. Prioritize CRITICAL+HIGH (10) — when these wallets move, the on-chain detection picture changes. NORMAL (0) is for bulk cross-checking, no push notification needed. 💤 NOT_TRACKED are DEX routers / public CEX hot wallets whose flow noise drowns the real signal, removed from paste.


| # | Level | Wallet | Role | primary role section | Trigger condition | Status |
|---|:-:|---|---|---|---|---|
| 1 | 🔥 HIGH | [`0x3dd3f1af`](https://bscscan.com/address/0x3dd3f1af52b820a6ef8e72f67d02b3c3848dd63c) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 2 | 🔥 HIGH | [`0x216ef93e`](https://bscscan.com/address/0x216ef93e51bd6d1498bed395cebd72bef6cc9e83) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 3 | 🔥 HIGH | [`0xa0d6d194`](https://bscscan.com/address/0xa0d6d1942c2e4790234601544e7afe6431b193e5) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 4 | 🔥 HIGH | [`0xe0559a26`](https://bscscan.com/address/0xe0559a26532d244dec36cab758eeff1eacefb37b) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 5 | 🚨 CRITICAL | [`0x78818ee5`](https://bscscan.com/address/0x78818ee5d3899176f99d79dda24d3d626b958bb6) | Heuristically-flagged hidden operator ammo (reserve) | [🌉 Bridge / mint-authority contract self-sell detail](#section-bridge-mint) | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 6 | 🚨 CRITICAL | [`0x207d87cd`](https://bscscan.com/address/0x207d87cd5710ad33c00615c423093ec89d273f51) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 7 | 🚨 CRITICAL | [`0xdf788c54`](https://bscscan.com/address/0xdf788c546cb62fca5f346a02a856ede993a310fb) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 8 | 🚨 CRITICAL | [`0x79431d98`](https://bscscan.com/address/0x79431d989ad051ce4b8e9a75987b867c92a09627) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 9 | 🚨 CRITICAL | [`0x7313e2be`](https://bscscan.com/address/0x7313e2be11d843482e7d10fe3b04d2abf72e8839) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 10 | 🚨 CRITICAL | [`0x97620e00`](https://bscscan.com/address/0x97620e003c03381eacbde7135f28d94303bb5672) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |

Monitoring these 10 wallets helps track active operator reserves and potential sell-out actions for AIO.

## Machine-readable JSON (compact)

```json
{
  "schema_version": "1.0.4",
  "symbol": "AIO",
  "verdict": "ADVISORY",
  "verdict_zh": "Observe",
  "verdict_downgrade_applied": 0,
  "chain_state": "CLEAN",
  "chain_state_label": "No significant on-chain detection trigger",
  "chain_state_risk_score": 2,
  "alpha_listing_tier": "S2",
  "any_anomaly_firing": false,
  "render_provenance": {
    "rendered_by": "render_report.py (v0.6, jinja2)",
    "data_source": "report_data.json (LLM-filled, Python-validated)",
    "deterministic": true
  },
  "structural_counts": {
    "anomaly_waves": 0,
    "evidence_graph_entries": 1,
    "holdings_role_rows": 5,
    "holdings_progress_bars": 5,
    "monitoring_wallets": 10,
    "lineage_flowchart_nodes": 1,
    "lineage_flowchart_edges": 0,
    "m6_rows": 0,
    "decision_anchors": 3,
    "decision_re_entry_conditions": 1
  },
  "address_role_index": {
    "0x7817dbf38e9d1c95671625f0052c147864692fe0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x48e6bb7895d5af640bf1072f1e6812bbd76dee6e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x22f8326cf3da32e36d3d2df911def876b7be486f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x286da9568057420df90c5489e51cbb82b29f0301": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x9a773d0749b2e6eba628b471d03485718e533681": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x28e2ea090877bf75740558f6bfb36a5ffee9e9df": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x45a2e455b2f7054f02317533057ed60196c90f73": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x60b97709d633dd4e0f0f44f6102fd50341c0afa6": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2087d8fe927966fee758ba5563fb8f2347180b7c": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb6f51b00739cc60a03f51cd12caa0ec6f1fc057e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x653dd7677aea3030eab68c97ed3594bacf560158": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb6e27c34a794d04e8e078b46cb38093be26f0516": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x111111125421ca6dc452d289314280a0f8842a65": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x5ddf9200ca8163585d1d9b05022adc14c32a71f1": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xfd7ac7e9dfbb78a0ab17b2476bb890f178120d1d": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x87866aa14c37306ef3ee49468f79f4e0e1cc52f6": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x7b7c7245c2070221f3ff1db5b3ac9042e91c4867": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x0f0067cd819cb8f20bda62046daff7a2b5c88280": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xf5c8b2cc7cc44403646f908dbc76b2f4c6317dd5": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xbd97306a087ed0c46b783cfbfdcdc6c12c7a2866": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x80278c216f6e3230e55b00f10710781e810d5b7a": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xbeb2c2171e3d9086aca86c785a69bb5bfdd5c5a5": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4b1b2ea60cc20a171cb7eed8fe0de988f79651d2": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x055a3b37957bfbd3345bed9968e7e8dd56d67066": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xd547eafde2410e63300fc5308ccea0b356e7b5d8": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xdfc1db4904dc1e7718d4783bd4be02ac1967ae86": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xbce729580490534fdaa5a4306c49c019418e2823": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb891cc3b4271e85644c4e871e16c650ecc71d5b0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe25f4ffdf8ae4d95cce75ff8cfd9ec297026aa43": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x78818ee5d3899176f99d79dda24d3d626b958bb6": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x652af6bd6135922a0034fb8c135387896fad5116": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4923d960f84d89e72c78daf82015b519aaafe994": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x1661212c888bb26ba52cee09d295ddd24f722286": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb7d0ec13b7a8bf10d210f937c28817af88f0d401": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x222cf5b76beb49543832e4f044fb1f3407fbb58a": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe6f6fd0413af3aeed1da7dd5020338a0875db0fc": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x208633b825abf7b0c2a1ccea7dbdfc37d0d5a325": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xf8f02694101ad3ec3a07ddf573fff450290abce0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x1578f35d42ce6a9183412264b993093035195aa0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6aba0315493b7e6989041c91181337b662fb1b90": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x00000aad8cc7a34f9c5174a3f1862cd05ad3776b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x031942f26a094be40414f442a2f1295e3a5c1680": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xfc9efe51f84d75ae5ef0355a43c85df84928f13e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x53f78a071d04224b8e254e243fffc6d9f2f3fa23": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x286b960493f8dc81c5d6626eba53547f4a7d8175": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x3d6035e23ce306a0b3dd23977f6aa904c9bd3154": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x0501f595d17dd90ff11a9873692ee3f8d478f4e5": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x278d858f05b94576c1e6f73285886876ff6ef8d2": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe6794da27926ee1333fc96b3a233cf94bc0075d4": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x628683c3c54ec4a22217d0022d0d442b391e9a4f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2ea94a042461940fb59cc7260bb85342891fb5eb": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xa116b5a5552e27dfdfa33dddd4066f10c948d414": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6e1b2a5bc88227d7067b4d02ef82dd1b8c4fcd7b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x353275134153f5291d2070107d9a2779f1de7293": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x5a5867b4e3a1cd7afe8686f252459b4de424225b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x836c8c9daa4ab44a5f53992d727c1babd1b6d89f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xd58b22154423339c8e16b8bebdd244364f58a245": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x70b4ab2d09169eab905dfe0053140eaddd10fa6c": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x8c8b5293795d643d982dcbafc905d0645e9f8efb": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x802b65b5d9016621e66003aed0b16615093f328b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x73d8bd54f7cf5fab43fe4ef40a62d390644946db": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb7697d225fa34bf1ebd3413adfa1c35b1be74729": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x5c9450ad619cf7e8a123c0f4af8f92044c1c66cf": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x8ca175b3514fe5f6ea2ccb179972eb3607f2f53d": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4faf59b2922387554c6226a38426ff2538425f77": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe97b1f053c9118041c9016d83c86deffbf398095": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x0b04d2eb5da34d118d8b5c31cef911b67d806c88": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6993f32bec7edef817be6db869a226572cfb919e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xcc3fc06d4057ad0c28c9ffb32563387d97f0fa61": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xda728a2e3c413b905b90d626e7d942435f80fc38": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x8468b808426df54189964d33365ba778c56125a3": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xde9e4fe32b049f821c7f3e9802381aa470ffca73": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x0a6ed58ed2c1849b281f6b379c2764e17d57a7e8": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xac30203cb479ee89696d9e7ec98dca08fd538065": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x084aeb64cfe9e89d9cfe6f3f82378d63eaa5f430": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x3663658a2db327938a2cefc9119232bb4190f858": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x5b8a8f0f27d19b66363b31477358bccf5812c54a": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xa0d62be88fa3e42b607b8252d828df6dfcd3dbe1": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xccb16263985566e2c508010f70c53e296c526f85": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2a4d7efcb75c10fc56dbee991125262c2a4cb802": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xd543c8553da70879743c5dc462b8b09b0464f92e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xaf7076ff9f05f2653e73aea69cf68e6ffc4ec800": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xfb4165e2f32b2e942dfcc3dcf420954237b523e0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x73b4c818892283e5fc37fee7b91ff7245b236d3c": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x7964315379060f853a3cc0e211b94bc788103a74": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4e7ed91e702ef2ff0c58e251c6e20d1dc1e31a5f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xfc0980992ab0d7ef1e7359a868f2870c92a9e13b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x77519fa2324078e75b43c1bf2f8681069100c6c0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6f3f9630caeeef4ea119c991506b20a5ee9fe4aa": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x7820a963b4a8e5af0c975373059f6dd796278ef3": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x971435fc38eed5e0aaff0dd717d0d16a02a4110e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x3bc367866468d4f80096be899b66ab29d03f2717": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb94741fb32409f914c67d161efa718815c038b3f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xa9b6a8e08f2b413b36484128442da9ef28dd5778": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xd060a0193a72ba809149476cec1ca865a887ec91": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4be50c8ed077edb3dd24cb22f218c7d02680b888": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x0303e4fe3d5a3d4f225e7690f038786648657b2b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6b3affc894b0d2d566e5ff03ad79188f1b65bfff": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xfaa0a5c1a1aec3ee75a9963abc187fdc5455e5af": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x1906c1d672b88cd1b9ac7593301ca990f94eae07": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb5cb055053f4c1a2801a8304015d1dddf3081cdd": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    }
  }
}
```

---

****Data research only, not investment advice. evidence_graph contains 1 stable IDs for provenance tracing.****
