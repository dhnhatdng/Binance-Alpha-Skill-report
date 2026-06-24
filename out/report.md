# ARX (Arcium) — On-chain Decision Briefing


## 🎯 One-screen verdict

> This section is deterministically derived from on-chain detector outputs and is not buy/sell advice. Full evidence is in the sections below.

| Dimension | Conclusion | Key evidence |
|---|---|---|
| **Current phase** | 🟢 Accumulation / watch — no significant trigger | None of the 5 main signal tiers triggered |
| **Chip structure** | 🟠 Moderately controlled | Operator/project-controlled chips 45.8% / CEX relay pool 39.1% / verifiable non-operator sell-pressure 15.1% |
| **Insider / operator spot realization** | 🟠 Partially realized | Confirmed insider realization 16.1% of circ + net CEX-withdrawal distribution 0.0% of circ |
| **Volume quality** | 🔴 24h volume untrustworthy — wash bots dominate | 217,053 on-chain matches; single bot 2.2% |
| **Supply risk** | 🟠 Supply source present — limited magnitude | 5 mint authorities; cumulative 3.3% of total supply |
| **Market-cap stage** | 🟢 Low mcap / sharp drop | mcap $69.5M; 5% depth $15,685; LP/mcap 0.029; vol/LP 15.0×; 24h -22.8% |
| **Monitoring focus** | Maintain baseline monitoring | Mint-authority contracts |

**One-liner**: Accumulation / watch + Moderately controlled + volume inflated by wash.

## 🎯 Quick-read summary

> This section is for quick retail reading / AI re-interpretation. Detailed forensic detection is in the sections below (with English terms). Everything here is derived from on-chain data and contains no buy/sell advice.

- **Project**: Arcium (ARX), main contract [`0xd5f6ef5d…`](https://bscscan.com/address/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715)
- **Listing**: Binance Alpha S2 (Spot + Perp) · primary chain BSC

- **Confirmed insider on-chain realization**: **36,475,244 tokens (16.09% of circulating)** ≈ **$7,685,020 USD** — a lower bound on what insider wallets have realized themselves via (a) deposits to centralized-exchange deposit addresses + (b) their own direct on-chain matches; actual sell-out is most likely higher (see 📊 Confirmed sell-out section)- **TGE-distributed tokens already sold**: **4,850,806 tokens** ≈ **$1,143,837 USD** (~0.49% of total supply) — via mining-fed wallets (3) + bridge / mint-authority self-sells (2 contracts) channels back into the market
- **Historical high-throughput operators surfaced**: 46 wallets ran cumulative **throughput** (token in/out flow, NOT sell volume, includes wash double-counting) of **307,913,995 tokens** over 365 days then zeroed out — already exited

- **Report-completeness note**: only on-chain-verifiable wallet → DEX/CEX flows are included. Off-chain behaviour (distribution after a CEX withdrawal / OTC transfers / bridges not in the surf index, etc.) is not on-chain-detectable, so real sell-out may exceed the figures here. See the 🟡 completeness note below.

- **How to use this report**: read it alongside the **Monitored wallets** section below; add the core wallets to Binance Wallet / OKX monitoring (monitoring_paste.json supports one-click import). Make entry/exit decisions according to your own risk tolerance.


> ⚠️ **Read first — on-chain detection limits / data caveats**
>
> - 🚨 **24h volume / on-chain matches dominated by a wash bot**: 200 counterparty addresses / 217,053 on-chain matches, with a single wash bot doing up to 4,854 wash matches (single wash bot share 2.2%). **Do not use 24h volume to judge real absorption** — see "absorption cap (5% depth)" below. Detail → 📊 Confirmed sell-out section.
> - 🟡 **Several dump paths are structurally out of coverage**: ⛓️ cross-chain dumps (other chains invisible) / 🌉 bridge mint-authority self-dumps (mint source selling itself) / 🏦 the CEX-withdrawal phase (off-chain, not on-chain-detectable) / ⏰ 60d+ historical high-throughput dumps. **Real sell-out may be 5-50× the figures here**. v0.7.24 backlog: mint-authority + multi-chain + high-throughput detectors added (see 🌉 / 🌊 / 🔗 sections at the end).
_Tool version 1.0.4 · Main chain BSC · Alpha listed 2026-06-22_

_Total supply 1,000,000,000 · Circulating 226,725,926 (22.7%) · Type VC_LIKELY_
_Tier S2 · S1 2026-06-22 · S2 2026-06-23_
## 💹 Token market (real-time)

| Item | Value |
|---|---|
| **Project name** | **Arcium** (ARX) |
| Ticker | `ARX` |
| Primary chain | BSC |
| Listing | S2 (Alpha + Binance Perps) · Alpha listed 2026-06-22 · Perp listed 2026-06-23 |
| **Current price** | **$0.3008** (🔴 -22.08% 24H) |
| **Network 24H volume (CEX+DEX)** | **$144,765,056** |
| Current LP (DEX main pool) | $2,005,750 |
| Market cap (mcap / FDV) | $62,826,671 / $300,848,857 |
| Data source | surf+Alpha API (real-time) · 22,831 holders · 24H 290,387 txns |

## 📋 Decision summary

| Item | Value |
|---|---|
| **🎯 Risk score** | **🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ (2/10)** |
| **On-chain state label** | **No significant trigger** — No significant on-chain detection trigger |
| Primary chain | binance-smart-chain (this chain's current LP $264,740) |
| **Entry cap (LP 5% depth)** | **$15,685** |
| Near-term catalysts | None |
| Blind spots you must cross-check yourself | None |

> 🎯 **Meaning of the 5 on-chain-state labels** (deterministically derived at render time, describing on-chain detection state only, not trading advice):
> - **No significant trigger** — no significant on-chain detection signal (risk 0-2)
> - **Watching** — some activity but no primary signal triggered (risk 2-5)
> - **Distributed and exited** — historical operator already distributed; on-chain historical sell-pressure released (risk 4-7)
> - **Dormant insider, undistributed** — dormant insider wallets have not distributed; timing unpredictable (risk 6-9)
> - **Recent distribution** — large on-chain activity in the last 72h (risk 7-10)

> Based on the analysis of ARX, the trade sizing is restricted to a max of $15685 due to shallow depth.



## 🎯 On-chain state: No significant trigger (risk score 2/10)

**No significant on-chain detection trigger**


| Decision anchor | Value | Status |
|---|---|---|
| Alpha 5% slippage cap | $15,685 | 🟡 Medium |
| DEX main pool USD liquidity | $188,798 | 🟡 |
| Pool token 24h net throughput (NOT LP add/remove) | — | 🟢 |


## 🧠 Current on-chain behaviour profile

> This section translates 10 detector outputs into 4 categories of "what the operator might be doing." Multi-label by design — one token can hit several categories at once (e.g. A1 accumulation + B1 wash volume + C3 recent activity). Order: severity (🔴 STRONG / 🟠 MEDIUM / 🟡 WEAK) → category → label ID. Describes on-chain facts only, not trading advice.

| Severity | Label | Category | Trigger metric | On-chain fact |
|:-:|---|---|---|---|
| 🔴 **STRONG** | `C1` On-chain confirmed outflow (CEX deposit + DEX swap) | C Dump behavior | `net_sellout_usd=7685020.0, sell_pct_circ=16.088` | On-chain confirmed outflow $7,685,020 (16.09% of circulating) — real insider realization observed via CEX deposit + on-chain match paths |
| 🔴 **STRONG** | `C2` Historical high-frequency operator liquidation | C Dump behavior | `ht_operator_count=46, ht_throughput_pct_supply=30.79` | 46 high-frequency operator wallets (cumulative **throughput** = 31% of total supply; throughput = token in/out flow, NOT sell volume) — already exited historically, balance near 0 |
| 🟠 **MEDIUM** | `A3` Mint / bridge / mining supply source | A Chip preparation | `mint_authorities=5, mint_pct_supply_max=2.1, mint_pct_supply_sum=3.28` | 5 mint-authority contracts present (cumulative mint = 3.3% of circulating supply), an ongoing supply source — future mint → dump is possible |
| 🟠 **MEDIUM** | `B1` Wash-trade volume inflation (24h vol untrustworthy) | B Volume fabrication | `wash_swap_count=217053, wash_top_bot_share=0.022, wash_n_dex_addrs=200` | 217,053 on-chain matches in 24h across 200 on-chain trading addresses, a single wash bot accounting for 2.2% — the 24h volume contains heavy wash trading and does not equal real absorption |
| 🟠 **MEDIUM** | `B2` Fake depth (LP/mcap mismatch or high vol/LP) | B Volume fabrication | `vol_lp_ratio=15.01, lp_mcap_ratio=0.0289, lp_usd=2005750.1384062439` | Volume/liquidity ratio = 15.0× / liquidity/mcap ratio = 0.0289 — surface liquidity is low and a single trade has large price impact |
| 🟡 **WEAK** | `D2` Cross-chain deployment / coordination | D Coordination structure | `non_primary_chains=0, cg_chains=2` | This token is deployed on 2 chains (0 non-primary chains have independent on-chain hits) — cross-chain dump paths require separate monitoring |

> **Behaviour profile is not the verdict**: the 🎯 on-chain state label above is a composite of 5 tiers (No significant trigger / Watching / Distributed and exited / Dormant insider / Recent distribution); the behaviour profile here is the finer-grained 10-class on-chain detection signals. A token can be "Recent distribution" while also hitting multiple labels like A1+A2+A3+B1+C2+C3.


## 🔴 Confirmed sell-out (insider lower bound)

### 🎯 Pump counterparty check

> **⚡ Quick read**: circulating 21.6M tokens · **non-operator sell-pressure 15.1%** (3,253,811 tokens = verifiable within top 100 holders 15.1%) · operator ammo 45.8% (⚠️ Alpha API reports 227M circulating, on-chain dumpable 22M = 0.10x, Alpha overstates (includes mint authority / vesting lockup)) · exchange transit pool (retail vs project custody indistinguishable) 39.1% (1 exchange wallets) · insider confirmed realization $7,685,020 (16.1% of circulating).

> When the operator wants to pump, **the potential sellers = the held chips that don't belong to the operator**. The smaller this is, the more confident the operator is to pump (less fear of being dumped on); the larger, the more cautious.

| Chip bucket | Tokens | % of current circulating | Interpretation |
|---|---:|---:|---|
| 🟣 **Operator / project-controlled chips** | **9,871,441** | **45.8%** | **Moderate control** |
| 🔥 **Verifiable non-operator sell-pressure** | **3,253,811** | **15.1%** | **Moderate external sell-pressure** (includes retail whales + protocol contracts + bridge transit) |
| 🟦 **Exchange transit pool (neutral, indistinguishable)** | **8,439,527** | **39.1%** | 1 exchange hot/cold/deposit wallets. On-chain it is **impossible to distinguish** retail deposit aggregation vs project custody reserve. During a pump it may flow out from either side |

### Key judgment

**Project-controlled chips < 50%** — control is weak; the external counterparty + CEX pool flow direction decide the book.
**Raw bucket total 4317659893939% (expand for detail)** — wallet-level overlap across buckets is a debug caveat and does not affect the quick-read 45.8% operator-ammo conclusion.

<details>
<summary>🔍 Expand: operator-ammo 11-sub-bucket detail (with raw total + overlap note)</summary>

| Sub-bucket | Tokens | % of circulating | Note |
|---|---:|---:|---|
| ①a Public lockup / treasury / airdrop contract outside m6 lineage | 0 | 0.0% | Sablier / Hedgey / custom lockups. Public release schedule, **won't dump immediately during a pump**. Lower bound after subtracting the 773,274,074 unminted reserve |
| ①b Movable multisig outside m6 lineage | 0 | 0.0% | Gnosis Safe Proxy etc. The operator can transfer today with one signature |
| ② m6 lineage portion in circulation | 0 | 0.0% | m6 lineage total holdings -11,677,137 minus lockup 0. Includes pure insiders (-11,677,137) |
| ⚠️ ③ Exchange-withdrawal distribution (net control not computable) | — | — | Gross inflow; phase-2 SQL truncated; net fan-out cannot be computed.  |
| ④ DEX pool token-side holdings | 880,011 | 4.1% | DEX pools are 99% provided by the project / market maker |
| ⑤ Other detector hits | 694,015 | 3.2% | 19 wallets — flow operators / cross-token whales / high-throughput exit operators |
| ⑥ Mint-contract unreleased reserve | 19,545 | 0.1% | Mining / bridge mint contract current balance; operator-controlled unreleased supply |
| ⑥' Minted to operator cluster (net holdings) | 19,208,027 | 89.1% | Cumulative mint - contract reserve - realized = still in the fake-mining cluster |
| ⑥'' Heuristic hidden ammo (top-100 unclassified ≥ 3%) | 931,093,827,901,250,560 | 4317659893843.0% | 10 wallets. **The 3% threshold risks false positives** — cross-check via monitoring_paste |
| 📌 Unminted operator-controlled reserve | 773,274,074 | _77.3% of total supply_ | **Not in the circulating denominator — but operator-controlled**. Adds sell-pressure once lockup / mint cadence releases it into circulation |
| ━━━━━ | ━━━━━ | ━━━━━ | ━━━━━ |
| Operator ammo raw total | 931,093,827,922,052,096 | 4317659893939.5% | ⚠️ > 100% = wallet-level overlap across sub-buckets (an in-m6 multisig counted in both ①b + ②). The quick-read 45.8% is a strictly de-duplicated wallet-level back-calculation |

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
| 1 | [`0xb4b5bd6a972a`](https://bscscan.com/address/0xb4b5bd6a972ac27f306df2f0a20d7010308b8085) | 907,568 | 4.21% | Unclassified | — |
| 2 | [`0x2ed52850d4c0`](https://bscscan.com/address/0x2ed52850d4c013edbfdd11ae4403233fd818b782) | 873,538 | 4.05% | Unclassified | — |
| 3 | [`0xe0fbf2413b63`](https://bscscan.com/address/0xe0fbf2413b6340654106aa289a22a45f4c6613c3) | 470,098 | 2.18% | Unclassified | — |
| 4 | [`0xecc90d54b10a`](https://bscscan.com/address/0xecc90d54b10add1ab746abe7e83abe178b72aa9e) | 368,422 | 1.71% | Unclassified | — |
| 5 | [`0x76c94a64c094`](https://bscscan.com/address/0x76c94a64c0949e294a4dd219d1c0e911e5f25d4c) | 320,503 | 1.49% | Unclassified | — |
| 6 | [`0x3d59284cdef8`](https://bscscan.com/address/0x3d59284cdef876861157a70f8a3f462d3200d8a8) | 313,683 | 1.45% | Unclassified | — |
| ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━ | ━━━━━━━ | ━━━━━━━━━ | ━━━━━━━━━ |
| **Total verifiable non-operator sell-pressure (within top 100 holders)** | 6 wallets | **3,253,811** | **15.1%** | — | — |

> ⚠️ **Nature of non-operator sell-pressure**: mainly true retail whales + protocol contracts like Wormhole / veVELVET (user-deposited) + bridge transit. Large bare addresses (no Arkham label + > 1% circulating) are suspect as either operator aliases or true retail whales — cross-check wallet activity via monitoring_paste below.

---

| Item | Value |
|---|---|
| Tracked wallets | **73** (65 standard insiders + **3 mining-fed** + **5 mint authorities**; mining / bridge token, no pre-launch m6 lineage) |
| **Pure insider current holdings (the true dormant sell-pressure the verdict references)** | **-1.1588% of supply** (-11,587,670 tokens, **excluding** vesting / multisig / treasury / CEX custody / DEX routing; includes mining-fed operator wallet current balance; includes mint-authority contract current balance) — ⛏️ mining-fed still sits on 69,921 tokens awaiting sell-out · 🌉 mint authority still sits on 19,545 tokens (can keep mint→dumping at any time) |
| Insider-tree current holdings (incl. lockup, conservation anchor) | -1.1588% of supply (-11,587,670 tokens, in mining mode the tree = standard insiders + mining-fed set + mint-authority contracts (no vesting/lockup separation)) |
| (a) Confirmed sell-out — CEX deposit | 17,760,578 → Binance Wallet |
> _💡 Note: off-chain CEX withdrawals (CEX → wallet) are not in row (a) — (a) only tracks on-chain wallet → CEX deposits. A project that withdraws from a CEX first and then dumps (e.g. the H case Eleve described) does so off-chain and cannot be on-chain-detected; any subsequent on-chain transfer that dumps via a DEX router is already captured in row (b)._
| (b) Confirmed sell-out — DEX swap (own wallet) | 23,565,472 (55,231 swaps; mining-fed accounts for 2,767,882 tokens / 3,413 swaps ≈ **$689,414 USD**; 🌉 mint-authority self-sell 2,082,924 tokens / 2,147 swaps ≈ **$454,423 USD** all via DEX router) |
| **Confirmed gross sell-out, a+b** | **≥ 41,326,050 = 16.6% of circulating**, USD ≈ $13,132,154 |
| **Confirmed net sell-out** | **$7,685,020** — insider **self-sell DEX TWAP** $0.2107 (rejects wash-quote contamination); DEX real ≈ $3,943,019 (on-chain SUM amount_usd, 100% provable) + CEX estimate ≈ $3,742,001 (cex_tokens × TWAP) |



> **📅 Time-window split** — reconcile against short-term events (Twitter sudden-dump alerts / large moves); the relationship is **last 7d ≤ last 30d ≤ cumulative**.

| Window | Confirmed gross sell-out (tokens) | % of circulating | Confirmed net sell-out (USD) | DEX real volume (USD) | CEX route (tokens) |
|---|---:|---:|---:|---:|---:|
| **Last 7 days** | 36,475,244 | 16.09% | **$7,685,020** | $3,943,019 | 17,760,578 |
| Last 30 days | 36,475,244 | 16.09% | $7,685,020 | $3,943,019 | 17,760,578 |
| Cumulative (~364 days) | 36,475,244 | 16.09% | $7,685,020 | $3,943,019 | 17,760,578 |

> Interpretation: **last 7 days** shows current heat (reconcile directly with EmberCN-style sudden alarms); **last 30 days** shows the month's pace; **cumulative** = everything within the surf query window. A single-day burst may not show in the 7d average but is already in the cumulative. CEX route = tokens that went into exchange deposit/hot wallets (sold off-chain on the CEX side, not at the wash price).


> 🕵️ **Hidden operator ammo has shown realization activity**: the tracked **19 hidden-ammo wallets** (heuristic catches / fake-mining mint cluster) have, via (a) deposits to exchange deposit addresses of **13,606,374 tokens** (2 exchanges: Binance Wallet, OKX Deposit) + (b) their own on-chain matches of **0 tokens** (0 swaps), totalled **13,606,374 tokens** = 6.00% of circulating. **These wallets are outside the algorithm's 5 buckets** and may add on top of "confirmed gross sell-out" to view real distribution; but **you must subtract any wallet overlap with the m6 insider / mining-fed sets** (v0.8.4 backlog: add disjoint dedupe). Time window: from 2026-06-22.> ⚠️ **This token's on-chain dump is dominated by a wash bot**: 200 counterparty addresses with 217,053 on-chain matches total, a single wash bot doing up to 4,854 wash matches. Many insiders route tokens to relays / bots before selling (this portion is **unattributable** and not counted in the confirmed lower bound above — so real sell-out is most likely higher than the lower bound). Massive wash = dumping while inflating surface activity to lure buyers.


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

**On-chain transfer rhythm for ARX.**



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

**Interpretation**: The token ARX is deployed as a single-chain asset on BSC with no cross-chain bridge activity.

## Entry-price anchor (TGE)

| Time anchor | UTC | Price | vs current |
|---|---|---|---|
| LP creation first tx (DEX start) | — | — | — |
| Alpha first tx | 2026-06-22 10:00 UTC | — | — |
| **Current price** | 2026-06-24 | **$0.3056** | 1.00× |

**Interpretation**: The token was first listed on Binance Alpha on 2026-06-22 UTC. The current price is $0.3065.

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
| Binance | Listed | 2026-06-23 | ~1 days ago |
| Aster | Unverified | — | — |
| Bitget | Unverified | — | — |

Binance Perp listed within last 14 days. Current S2 (Alpha + Binance Perps).

**Interpretation**: The token is currently listed on Binance with perps active since 2026-06-23, representing S2 classification.

<a id="section-liq"></a>
## Entry ceiling (LIQ)

| Anchor | Value | Note |
|---|---|---|
| **Max single buy under 5% slippage (estimated)** | $15,685 | Derived from Alpha 24h vol (vol_24h / 96 × 0.05 heuristic estimate) |
| DEX main pool liquidity | $188,798 | surf 0x56336db9… |
| DEX main pool 24h volume | $144,765,056 | surf project-detail (cross-chain CEX+DEX realtime aggregation) |
| Pool token 24h net throughput (NOT LP add/remove) | — | surf agent.bsc_transfers |
| DEX main pool address | `0x56336db9642763b34b746cf38ca2e7657f243a43` | FDV $300,848,857 |

**Interpretation**: DEX liquidity is $188,798.47 but estimated 5% depth is extremely low at $15685, limiting trade sizing.

<a id="section-holdings"></a>
## Holdings distribution by role

**Distribution table**:

| Role | Wallet # | Current balance | % of supply | Top wallet |
|---|---|---|---|---|
| DEX main pool | 1 | 240,884 | 0.0241% | [`0x56336db9…`](https://bscscan.com/address/0x56336db9642763b34b746cf38ca2e7657f243a43) |
| Deployer wallet | 0 | 0 | —% | — |
| Project / infra / distribution pool (vesting / multisig / treasury / DEX infra / CEX custody / 3rd-party distribution platform / retail claim pool, Arkham-verified) | 1 | 368,422 | 0.0368% | [`0xecc90d54…`](https://bscscan.com/address/0xecc90d54b10add1ab746abe7e83abe178b72aa9e) |
| Quiet wallet (insider, never distributed) | 0 | 0 | —% | — |
| Other (retail + unclassified) | 48 | 23,307,640 | 2.3308% | [`0x73d8bd54…`](https://bscscan.com/address/0x73d8bd54f7cf5fab43fe4ef40a62d390644946db) |

**Key takeaways**:
- Insider tracking: **73** wallets hold **-1.2%** of supply cumulatively, incl. 3 mining-fed operators, incl. 5 mint authorities  (mining / bridge token, no pre-launch m6 lineage).
- Insiders have on-chain-confirmed outflow of **7.7M USD** = **16.09%** of circulating, priced at the insider self-sell TWAP (not the wash quote).

<details>
<summary>📂 <strong>Backward trace (Deployer → insider lineage)</strong> — 0 insider wallets: 0 fully distributed / 0 distributing / 0 quiet (click to expand the full lineage + wallet balances + distribution rate)</summary>

**Insider wallet list (deployer distribution trace)**:

| ID | Address | Received from deployer | Current balance | Dumped % |
|---|---|---|---|---|
_Stats (full m6 lineage, **0** wallets): 0 near-zero holdings / public-lockup custody · 0 distributing · 0 fully distributed_

**m4_notes (pre-LP allocation interpretation)**:
- The pre-launch phase for ARX shows no early wallet deployments or allocations.
- No pre-launch OTC seeding was detected on BSC for ARX, which means there are zero verified early insider recipients.
- Without any pre-launch deployment trace, the initial allocation remains highly concentrated in the creator/unlabeled reserves.



</details>

## 💰 High-Value Address Funding Source (mint / DEX / P2P)

Below are the high-value addresses already surfaced by the wash setup / flow operator / m6 insider / Top-30 holder sections, classified by how they ACQUIRED their tokens over the past 365 days: mint (received directly from 0x0 — covers mining contracts, bridge mint authorities, airdrop mint contracts), DEX buy (received from a known DEX main pool), or P2P (any other EOA transfer, including unidentified CEX withdrawals). Use this to distinguish: ⛏️ high mint% = mining-token operator or sockpuppet airdrop farmer; 🟢 high DEX% = real retail buyer; 🔵 high P2P% = operator aggregation hub or OTC recipient.

> Queried 200 high-value addresses; 77 have real incoming activity in the past 365 days — ⛏️ Mint-fed 4 / 🟢 DEX-fed 66 / 🔵 P2P-fed 7.


| Address | Primary Source | Total Received | Mint % | DEX buy % | P2P % |
|---|---|---:|---:|---:|---:|
| [`0x9999b0cd…`](https://bscscan.com/address/0x9999b0cdd35d7f3b281ba02efc0d228486940515) | 🔵 P2P-fed | 20,988,265 | 0.0% | 49.1% | 50.9% |
| [`0x4c4f0b07…`](https://bscscan.com/address/0x4c4f0b07cee233eebb525162cc81d0cd2a472c51) | ⛏️ Mint-fed | 6,676,217 | 51.4% | 2.4% | 46.2% |
| [`0xf91e8bf4…`](https://bscscan.com/address/0xf91e8bf46b9e90909e53c82353c833bb4a5e3a45) | 🔵 P2P-fed | 2,715,442 | 44.9% | 0.0% | 55.1% |
| [`0xc0fc3da4…`](https://bscscan.com/address/0xc0fc3da4c2e3c0cd76eaa312132f924d3a85d8e5) | 🔵 P2P-fed | 2,025,160 | 45.8% | 0.0% | 54.2% |
| [`0xe2bc399a…`](https://bscscan.com/address/0xe2bc399aafd4c5ed3f43b4bf8f0cec24bcd11bae) | 🟢 DEX-buy-fed | 1,033,733 | 0.0% | 99.3% | 0.7% |
| [`0xf3cd2b71…`](https://bscscan.com/address/0xf3cd2b713be8b13842f5925e57b64df9d44ccf18) | 🟢 DEX-buy-fed | 1,023,916 | 0.0% | 99.3% | 0.7% |
| [`0x7d23606b…`](https://bscscan.com/address/0x7d23606b0e3c6cdab8409010359fcba16ab8667b) | 🟢 DEX-buy-fed | 1,020,135 | 0.0% | 99.3% | 0.7% |
| [`0xde6caede…`](https://bscscan.com/address/0xde6caede07e7003924f3d23126f303466f03f234) | 🟢 DEX-buy-fed | 1,018,586 | 0.0% | 99.3% | 0.7% |
| [`0xa5dd28e6…`](https://bscscan.com/address/0xa5dd28e677a935734fda73b9fe028261057a111d) | 🔵 P2P-fed | 1,012,242 | 0.0% | 0.0% | 100.0% |
| [`0x0687182f…`](https://bscscan.com/address/0x0687182f669d186522277176b4bbf050eb54e7e4) | 🟢 DEX-buy-fed | 1,011,746 | 0.0% | 99.3% | 0.7% |
| [`0xcaddb22c…`](https://bscscan.com/address/0xcaddb22c5a3c140dcd721245b1a5cd76d6537b07) | 🟢 DEX-buy-fed | 1,006,811 | 0.0% | 99.3% | 0.7% |
| [`0x2e17809c…`](https://bscscan.com/address/0x2e17809c9f0e7a6bacf463a43129300cd45f359d) | 🟢 DEX-buy-fed | 995,834 | 0.0% | 99.3% | 0.7% |
| [`0xc7a3537d…`](https://bscscan.com/address/0xc7a3537d9ca1525c9283c5fe132f13cf1656a6f6) | 🟢 DEX-buy-fed | 984,263 | 0.0% | 99.3% | 0.7% |
| [`0x74fe4ed7…`](https://bscscan.com/address/0x74fe4ed7bcecdb7484148e200d1fdcb15ce8c361) | 🟢 DEX-buy-fed | 980,401 | 0.0% | 99.3% | 0.7% |
| [`0x1828cf25…`](https://bscscan.com/address/0x1828cf252df5e24902ce85df26e274a48dad5427) | 🟢 DEX-buy-fed | 967,943 | 0.0% | 99.3% | 0.7% |
| [`0xe02c3489…`](https://bscscan.com/address/0xe02c3489e2f1d2fd49953ab4ad7792415377fde8) | 🟢 DEX-buy-fed | 956,222 | 0.0% | 99.2% | 0.8% |
| [`0xf17f6f40…`](https://bscscan.com/address/0xf17f6f4095f4977d226501adbf953c76ab7eee22) | 🟢 DEX-buy-fed | 954,752 | 0.0% | 99.3% | 0.7% |
| [`0xc9176ae5…`](https://bscscan.com/address/0xc9176ae50abbe6cfe462538f3343c9d0d63092d5) | 🟢 DEX-buy-fed | 951,393 | 0.0% | 99.2% | 0.8% |
| [`0x08334aa8…`](https://bscscan.com/address/0x08334aa8a4c6ee42d9250b20adaed26502c2dc97) | 🟢 DEX-buy-fed | 950,984 | 0.0% | 99.3% | 0.7% |
| [`0xed79a10e…`](https://bscscan.com/address/0xed79a10eea6a7315d964a61000ac720b066ea8ef) | 🟢 DEX-buy-fed | 939,934 | 0.0% | 99.3% | 0.7% |
| [`0x25336dd8…`](https://bscscan.com/address/0x25336dd853cf7024fa757a613acbca5f9dd5e52c) | 🟢 DEX-buy-fed | 913,663 | 0.0% | 99.2% | 0.8% |
| [`0x8962580f…`](https://bscscan.com/address/0x8962580f96f2020808722499d19c246556057bfa) | 🟢 DEX-buy-fed | 890,520 | 0.0% | 99.2% | 0.8% |
| [`0x0e43e387…`](https://bscscan.com/address/0x0e43e38713fb2cf2a6e852a2a0a656d5833ef051) | 🟢 DEX-buy-fed | 882,392 | 0.0% | 99.2% | 0.8% |
| [`0xe7dd9afd…`](https://bscscan.com/address/0xe7dd9afd190a2ae2274670c7ab682bc43e0d661d) | 🟢 DEX-buy-fed | 879,394 | 0.0% | 99.2% | 0.8% |
| [`0xe2456250…`](https://bscscan.com/address/0xe245625073a88b44f295b7fcd731bcbbbbdc9500) | 🟢 DEX-buy-fed | 876,828 | 0.0% | 99.2% | 0.8% |
| [`0x47877c8c…`](https://bscscan.com/address/0x47877c8c2f2b501c7727acf42d3a8404a4a12552) | 🟢 DEX-buy-fed | 874,298 | 0.0% | 99.2% | 0.8% |
| [`0xf2bd5cde…`](https://bscscan.com/address/0xf2bd5cde4dc63a57f7674fdc537daa4c8b499696) | 🟢 DEX-buy-fed | 867,291 | 0.0% | 99.2% | 0.8% |
| [`0x801f8cd6…`](https://bscscan.com/address/0x801f8cd62ad02beca0902835abda75592fe9007b) | 🟢 DEX-buy-fed | 852,714 | 0.0% | 99.2% | 0.8% |
| [`0xde2f4f91…`](https://bscscan.com/address/0xde2f4f91551a5d1e3f2cc22dd2981a95bb3dc78b) | 🟢 DEX-buy-fed | 852,677 | 0.0% | 99.2% | 0.8% |
| [`0xe8991371…`](https://bscscan.com/address/0xe89913719ff5505e4fbc8001ce44d2f8fb9bf34d) | 🟢 DEX-buy-fed | 825,722 | 0.0% | 99.2% | 0.8% |

> _Scan cap: the pipeline collected 229 high-value candidates, max_addrs cap = 200, actually queried 200 (ordered by detector priority: wash → flow → m6 → dump-sellers → Top-30 holders). Truncated 29 — common on PLAY-class tokens with many (60+) flow_operators._

> _The CEX-withdrawal column is not yet separately identified (a v0.7.24 candidate) and is currently grouped under P2P. When a real CEX hot-wallet transfer cannot be distinguished from a plain EOA transfer, both count as P2P._


### ⛏️ Mining-fed wallet sell-out detail (v0.7.23.2)

> Mining-fed wallets (3) sold via DEX over 365 days: **2,767,882 tokens ≈ $689,414 USD**, total on-chain outflow 6,996,673 tokens. **This is the real dump data dump_tracker cannot reach under the mining / bridge-token model** — the path where the operator claims tokens from the mining contract then realizes them.

**[`0x4c4f0b07cee2…`](https://bscscan.com/address/0x4c4f0b07cee233eebb525162cc81d0cd2a472c51)** —
 DEX sold **2,481,925 tokens** (2,618 swaps, ≈ **$640,138 USD**).
 Top outflow:
> - [`0xaa86268030aa…`](https://bscscan.com/address/0xaa86268030aae432ac471f220080ba3e46b52b43) ← 2,808,008 tokens (1989 txns)> - [`0xae4cf2630987…`](https://bscscan.com/address/0xae4cf2630987e1f7ddd12d03075eb1bc48c3d38a) ← 2,017,336 tokens (67 txns)> - [`0x238a35880837…`](https://bscscan.com/address/0x238a358808379702088667322f80ac48bad5e6c4) ← 674,225 tokens (549 txns)> - [`0x7a7ad9aa93cd…`](https://bscscan.com/address/0x7a7ad9aa93cd0a2d0255326e5fb145cec14997ff) ← 540,735 tokens (881 txns)> - [`0xdd3d3c05a672…`](https://bscscan.com/address/0xdd3d3c05a672b8a1112e158cd2fc6f577c2b6e1f) ← 505,642 tokens (2087 txns)
**[`0xc1b2aff52877…`](https://bscscan.com/address/0xc1b2aff52877b4a23422f554f3d240be50ec80cf)** —
 DEX sold **110,005 tokens** (393 swaps, ≈ **$25,295 USD**).
 Top outflow:
> - [`0xaa86268030aa…`](https://bscscan.com/address/0xaa86268030aae432ac471f220080ba3e46b52b43) ← 110,186 tokens (384 txns)> - [`0xdd3d3c05a672…`](https://bscscan.com/address/0xdd3d3c05a672b8a1112e158cd2fc6f577c2b6e1f) ← 10,267 tokens (242 txns)> - [`0x83f5c7b03bbb…`](https://bscscan.com/address/0x83f5c7b03bbbe20fe2e39312b957d86dc7c3dee2) ← 9,992 tokens (2 txns)> - [`0x7a7ad9aa93cd…`](https://bscscan.com/address/0x7a7ad9aa93cd0a2d0255326e5fb145cec14997ff) ← 6,121 tokens (47 txns)
**[`0x791252f51e08…`](https://bscscan.com/address/0x791252f51e081adddee3baf6597cfad1c26b80fb)** —
 DEX sold **175,953 tokens** (402 swaps, ≈ **$23,981 USD**).
 Top outflow:
> - [`0xaa86268030aa…`](https://bscscan.com/address/0xaa86268030aae432ac471f220080ba3e46b52b43) ← 129,003 tokens (294 txns)> - [`0x83f5c7b03bbb…`](https://bscscan.com/address/0x83f5c7b03bbbe20fe2e39312b957d86dc7c3dee2) ← 49,535 tokens (30 txns)> - [`0x56336db96427…`](https://bscscan.com/address/0x56336db9642763b34b746cf38ca2e7657f243a43) ← 45,000 tokens (90 txns)> - [`0x7a7ad9aa93cd…`](https://bscscan.com/address/0x7a7ad9aa93cd0a2d0255326e5fb145cec14997ff) ← 9,998 tokens (62 txns)> - [`0xdd3d3c05a672…`](https://bscscan.com/address/0xdd3d3c05a672b8a1112e158cd2fc6f577c2b6e1f) ← 9,769 tokens (206 txns)


<a id="section-bridge-mint"></a>
### 🌉 Bridge / mint-authority self-sell detail (v0.7.24a)

> Detected **5 mint-authority contracts** (receive mint from 0x0, excluding the deployer + wallets already covered in the mining-fed section). They are bridge / staking / airdrop contracts that may **themselves** DEX swap. This is a dump path the v0.7.23.x series missed entirely.

| Authority address | Arkham label | 365d Mint amount | % of supply | Own DEX sell | USD ≈ |
|---|---|---:|---:|---|---:|
| [`0x56bb8adad99c…`](https://bscscan.com/address/0x56bb8adad99c5fb41cc7516db52ea746abd916b4) | _Unlabeled (new contract, not in Arkham) | 21,028,198 | 2.10% | — (no direct DEX self-sell) | — |
| [`0x79fcf7bfa45d…`](https://bscscan.com/address/0x79fcf7bfa45da0351d9dd99395cd8a9d4793bade) | _Unlabeled (new contract, not in Arkham) | 5,049,800 | 0.50% | — (no direct DEX self-sell) | — |
| [`0x477de773a5ed…`](https://bscscan.com/address/0x477de773a5ed7136e15f3a79742d4040f700c451) | _Unlabeled (new contract, not in Arkham) | 4,000,025 | 0.40% | — (no direct DEX self-sell) | — |
| [`0x5d98f54d8297…`](https://bscscan.com/address/0x5d98f54d829708eeb2aa555badb96bcb5400def1) | _Unlabeled (new contract, not in Arkham) | 1,537,909 | 0.15% | 599,495 tokens (134 swaps) | **$135,661** |
| [`0xf91e8bf46b9e…`](https://bscscan.com/address/0xf91e8bf46b9e90909e53c82353c833bb4a5e3a45) | _Unlabeled (new contract, not in Arkham) | 1,218,015 | 0.12% | 1,483,429 tokens (2,013 swaps) | **$318,762** |


> 🌉 The mint authorities **themselves** sold via DEX over 365d: **2,082,924 tokens ≈ $454,423 USD**. This is the portion the bridge contract swapped out directly — a path independent of the mining-fed operators' dumping; **real total sell-out should be the sum of both**.


**[`0xf91e8bf46b9e…`](https://bscscan.com/address/0xf91e8bf46b9e90909e53c82353c833bb4a5e3a45)** self-DEX-sold $318,762 USD, top outflow:
> - [`0xaa86268030aa…`](https://bscscan.com/address/0xaa86268030aae432ac471f220080ba3e46b52b43) ← 1,784,684 tokens (1982 txns)> - [`0x83f5c7b03bbb…`](https://bscscan.com/address/0x83f5c7b03bbbe20fe2e39312b957d86dc7c3dee2) ← 417,913 tokens (28 txns)> - [`0xdd3d3c05a672…`](https://bscscan.com/address/0xdd3d3c05a672b8a1112e158cd2fc6f577c2b6e1f) ← 255,249 tokens (1986 txns)
**[`0x5d98f54d8297…`](https://bscscan.com/address/0x5d98f54d829708eeb2aa555badb96bcb5400def1)** self-DEX-sold $135,661 USD, top outflow:
> - [`0x04ce218ead72…`](https://bscscan.com/address/0x04ce218ead72401702dd5f3e56cedb7d2d477777) ← 1,494,696 tokens (183 txns)> - [`0x6f0538001f90…`](https://bscscan.com/address/0x6f0538001f90d0a5f0000060d01d34c002030900) ← 13,671 tokens (2 txns)> - [`0x8faa0000c100…`](https://bscscan.com/address/0x8faa0000c10015610005ca010ee000d006e0e820) ← 13,200 tokens (3 txns)

<a id="section-high-throughput"></a>
### 🌊 High-throughput dump wallets (v0.7.24b)

> Detected **46 operator wallets** with a high-throughput clear-out pattern (large token flow-through + balance ≈ 0 + high-frequency tx). Thresholds: throughput 1M ~ 5% of supply, balance < 5% of throughput, n_tx ≥ 1000. Already filtered out infra labels like DEX routers / CEX deposits / aggregators (not operators). These are operators that finished dumping and left before the 60d window — missed by flow_operators (60d window) + mining-fed (balance > threshold).

| Operator address | Primary role | Arkham label | 365d inflow (= received mint/p2p) | Outflow (= sold / transferred out) | Residual balance | tx count |
|---|---|---|---:|---:|---:|---:|
| [`0x56336db96427…`](https://bscscan.com/address/0x56336db9642763b34b746cf38ca2e7657f243a43) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 38,035,421 | 37,813,603 | 221,818 | 103,184 |
| [`0x1905dbf18c91…`](https://bscscan.com/address/0x1905dbf18c916bf8ec659545de0858d9f20eaeab) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 32,641,545 | 32,641,545 | 0 | 156,006 |
| [`0x9999b0cdd35d…`](https://bscscan.com/address/0x9999b0cdd35d7f3b281ba02efc0d228486940515) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 20,988,265 | 20,988,265 | 0 | 136,820 |
| [`0x28e2ea090877…`](https://bscscan.com/address/0x28e2ea090877bf75740558f6bfb36a5ffee9e9df) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 20,054,105 | 19,991,368 | 62,737 | 222,720 |
| [`0xae4cf2630987…`](https://bscscan.com/address/0xae4cf2630987e1f7ddd12d03075eb1bc48c3d38a) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 18,136,299 | 18,136,299 | 0 | 3,144 |
| [`0x62ccef0b4545…`](https://bscscan.com/address/0x62ccef0b4545166f721caa9fee13c1d3767e27dc) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 16,897,654 | 16,897,654 | -0 | 62,345 |
| [`0x507b7c70752e…`](https://bscscan.com/address/0x507b7c70752e2fa98dc5360f844fa289f6177c93) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 14,983,945 | 14,983,945 | -0 | 42,220 |
| [`0xaa86268030aa…`](https://bscscan.com/address/0xaa86268030aae432ac471f220080ba3e46b52b43) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 14,486,948 | 14,486,948 | 0 | 36,572 |
| [`0x83f5c7b03bbb…`](https://bscscan.com/address/0x83f5c7b03bbbe20fe2e39312b957d86dc7c3dee2) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 12,850,498 | 12,850,498 | 0 | 2,884 |
| [`0xf45ecc0b0028…`](https://bscscan.com/address/0xf45ecc0b00283c607f2f6e93425e4b9f8e7488d8) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 12,192,694 | 12,192,694 | -0 | 33,664 |
| [`0x31d6ea082acc…`](https://bscscan.com/address/0x31d6ea082acc3d4e377528a721ac5c4b891726fb) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 11,225,561 | 11,225,561 | 0 | 72,988 |
| [`0xbd97306a087e…`](https://bscscan.com/address/0xbd97306a087ed0c46b783cfbfdcdc6c12c7a2866) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 8,497,880 | 8,497,532 | 348 | 71,349 |
| [`0x031942f26a09…`](https://bscscan.com/address/0x031942f26a094be40414f442a2f1295e3a5c1680) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 7,534,737 | 7,534,737 | -0 | 13,834 |
| [`0x286da9568057…`](https://bscscan.com/address/0x286da9568057420df90c5489e51cbb82b29f0301) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 7,449,625 | 7,449,208 | 417 | 23,360 |
| [`0x8f10b468b06c…`](https://bscscan.com/address/0x8f10b468b06c6fd214b65f87778827f7d113f996) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 6,392,558 | 6,392,558 | -0 | 6,598 |
| [`0x4812bb70890d…`](https://bscscan.com/address/0x4812bb70890de10615b2dab53f1564ac5a07922c) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 5,635,980 | 5,635,980 | -0 | 10,579 |
| [`0xcd8d805a0735…`](https://bscscan.com/address/0xcd8d805a0735d59539abd348e1c9a68eec75737f) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 4,985,473 | 4,985,473 | 0 | 45,792 |
| [`0x2ad99fcfe692…`](https://bscscan.com/address/0x2ad99fcfe69248561bf5f0eb788af5217afaaa29) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 3,825,232 | 3,825,232 | -0 | 7,374 |
| [`0x462e1c9eab62…`](https://bscscan.com/address/0x462e1c9eab620e0bd10be0a30ba2fd3f019d87e4) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 3,776,626 | 3,776,626 | 0 | 6,587 |
| [`0x7a7ad9aa93cd…`](https://bscscan.com/address/0x7a7ad9aa93cd0a2d0255326e5fb145cec14997ff) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 3,618,580 | 3,618,580 | -0 | 12,794 |

> _Showing top 20; 46 high-throughput operator wallets detected in total (sorted by throughput; throughput = token in/out flow, NOT sell volume). Full list in skeleton.json `funding_attribution.high_throughput_dumpers.dumpers`._

> 🌊 These wallets passed **307,913,995 tokens** through over 365d then cleared out — operators that have finished dumping. They've already sold, but **if the project mints another batch and distributes it to similar-pattern wallets in future**, they become the next dump-risk source.





<a id="section-wallet-cluster-graph"></a>
## 🌐 Wallet-graph clusters (v0.8.6.5)

> **Wallet ↔ wallet direct-transfer graph clusters** — operator clusters that bypass CEX, mint, and the m6 lineage. Bubblemaps-style algorithm: high-value transfers between candidate wallets (≥0.5% supply per edge) form connected components ≥ 3 nodes. Uses undirected 2-core pruning to exclude single-edge false positives.| Metric | Value |
|---|---|
| Clusters detected | **1** |
| Total cluster wallets | **4** |
| Candidate wallets input | 65 |
| Excluded by L1 Arkham filter | 0 |
| Total graph edges | 17 |
| Newly discovered (not master_cluster) | 0 |
| SQL chunks run | 1 |

#### 🌐 Cluster 1: 4 wallets

| Field | Value |
|---|---|
| cluster wallets | 4 |
| edge count | 5 |
| Total transfer weight | 44,952,253 tokens |
| Max edge weight | 14,983,945 tokens |
| Cluster current total holdings | 799,371 tokens |
| Arkham UNLABELED % | 100% |
| Source distribution | master_cluster: 4 |

**Cluster wallets (sorted by transfer weight)**:

| # | Recipient wallet | Current balance (tokens) |
|---:|---|---:|
| 1 | [`0x238a35880837`](https://bscscan.com/address/0x238a358808379702088667322f80ac48bad5e6c4) | 798,953 |
| 2 | [`0x507b7c70752e`](https://bscscan.com/address/0x507b7c70752e2fa98dc5360f844fa289f6177c93) | -0 |
| 3 | [`0x031942f26a09`](https://bscscan.com/address/0x031942f26a094be40414f442a2f1295e3a5c1680) | 0 |
| 4 | [`0x286da9568057`](https://bscscan.com/address/0x286da9568057420df90c5489e51cbb82b29f0301) | 417 |

<a id="section-monitoring"></a>
## Monitored wallets + real-time alerts


> 📊 **Monitoring priority (v0.7.27 deterministic ranker)**: 🚨 17 CRITICAL · 🔥 12 HIGH · 👀 0 NORMAL>
> Wallets in paste.json are sorted by level, 🚨 first. Prioritize CRITICAL+HIGH (29) — when these wallets move, the on-chain detection picture changes. NORMAL (0) is for bulk cross-checking, no push notification needed. 💤 NOT_TRACKED are DEX routers / public CEX hot wallets whose flow noise drowns the real signal, removed from paste.

_(the report shows only the top 10; for all 29 wallets use `monitoring/monitoring_paste.json` to one-click paste into Binance Wallet / OKX monitoring)_

| # | Level | Wallet | Role | primary role section | Trigger condition | Status |
|---|:-:|---|---|---|---|---|
| 1 | 🔥 HIGH | [`0x3e5e8c26`](https://bscscan.com/address/0x3e5e8c26cda4d0caa4bfee9cddb283b356aeea74) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 2 | 🔥 HIGH | [`0xa45c45eb`](https://bscscan.com/address/0xa45c45ebe32654566c77be38a6583b8b2f1a3616) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 3 | 🔥 HIGH | [`0xf131c733`](https://bscscan.com/address/0xf131c7335966110528bea9dbefd6c040658d6128) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 4 | 🔥 HIGH | [`0x1e239247`](https://bscscan.com/address/0x1e2392477b413cb023cc7f46fd4a8765cd03bc4c) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 5 | 🔥 HIGH | [`0xae6829bc`](https://bscscan.com/address/0xae6829bc689db546bb88ba13b19321068c7de6d9) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 6 | 🔥 HIGH | [`0x81611558`](https://bscscan.com/address/0x816115587ea5b6fba2dac9c85e375cddf25464fa) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 7 | 🔥 HIGH | [`0xeccbf1ac`](https://bscscan.com/address/0xeccbf1ac6d0407360f0992ff6ea500020d6e1702) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 8 | 🔥 HIGH | [`0xdef7d1a7`](https://bscscan.com/address/0xdef7d1a70b4b57fc2432e431adceb01c404b1eac) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 9 | 🔥 HIGH | [`0x39b57dd9`](https://bscscan.com/address/0x39b57dd9908f8be02cfee283b67ea1303bc29fe1) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 10 | 🚨 CRITICAL | [`0x83f5c7b0`](https://bscscan.com/address/0x83f5c7b03bbbe20fe2e39312b957d86dc7c3dee2) | Fake-mining mint-cluster member | [🌊 High-throughput dump wallet](#section-high-throughput) | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |

Monitoring these 29 wallets helps track active operator reserves and potential sell-out actions for ARX.

## Machine-readable JSON (compact)

```json
{
  "schema_version": "1.0.4",
  "symbol": "ARX",
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
    "monitoring_wallets": 29,
    "lineage_flowchart_nodes": 1,
    "lineage_flowchart_edges": 0,
    "m6_rows": 0,
    "decision_anchors": 3,
    "decision_re_entry_conditions": 1
  },
  "address_role_index": {
    "0x5d98f54d829708eeb2aa555badb96bcb5400def1": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x79fcf7bfa45da0351d9dd99395cd8a9d4793bade": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0xe94753d6e067d25e0dbe90ed782b7ea21475fc48": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4812bb70890de10615b2dab53f1564ac5a07922c": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2ad99fcfe69248561bf5f0eb788af5217afaaa29": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x56336db9642763b34b746cf38ca2e7657f243a43": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xde6caede07e7003924f3d23126f303466f03f234": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xca8d055d625f5fc29d0891ac0b67c687ed450f51": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xc0fc3da4c2e3c0cd76eaa312132f924d3a85d8e5": {
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
    "0x7a7ad9aa93cd0a2d0255326e5fb145cec14997ff": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xf3cd2b713be8b13842f5925e57b64df9d44ccf18": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xcd8d805a0735d59539abd348e1c9a68eec75737f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x04ce218ead72401702dd5f3e56cedb7d2d477777": {
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
    "0x317cd61fa24e2e4068b4c47bd58d5fc9f4e7a12b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xaa86268030aae432ac471f220080ba3e46b52b43": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xae4cf2630987e1f7ddd12d03075eb1bc48c3d38a": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x507b7c70752e2fa98dc5360f844fa289f6177c93": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x462e1c9eab620e0bd10be0a30ba2fd3f019d87e4": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xc383960159d5c5f6ad9bbc6519a9e1937ca58046": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x09ad820aac5779683b481c4674208a4e1b024afa": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xdd3d3c05a672b8a1112e158cd2fc6f577c2b6e1f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xcaddb22c5a3c140dcd721245b1a5cd76d6537b07": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x83f5c7b03bbbe20fe2e39312b957d86dc7c3dee2": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xdfd97c55f95e8c1bf652b3b43b4facaf8ad53489": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x1231deb6f5749ef6ce6943a275a1d3e7486f4eae": {
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
    "0xf91e8bf46b9e90909e53c82353c833bb4a5e3a45": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x31d6ea082acc3d4e377528a721ac5c4b891726fb": {
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
    "0x9999b0cdd35d7f3b281ba02efc0d228486940515": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe2bc399aafd4c5ed3f43b4bf8f0cec24bcd11bae": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x42275a2e3123e1ed0a7bddccb8900cd8cabe9e83": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xf45ecc0b00283c607f2f6e93425e4b9f8e7488d8": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x477de773a5ed7136e15f3a79742d4040f700c451": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0xc1faf39ecd3dd4149a04474797f61695da23f93d": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x11eacd2bedd700a5e21ff70dea4086305100e5e0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x1905dbf18c916bf8ec659545de0858d9f20eaeab": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xeaeb8acd87cbef7b50ded7558e603b0d0b37eb42": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x62ccef0b4545166f721caa9fee13c1d3767e27dc": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x0687182f669d186522277176b4bbf050eb54e7e4": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x7d23606b0e3c6cdab8409010359fcba16ab8667b": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xa5dd28e677a935734fda73b9fe028261057a111d": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x56bb8adad99c5fb41cc7516db52ea746abd916b4": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0xc2eff1f1ce35d395408a34ad881dbcd978f40b89": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x8f10b468b06c6fd214b65f87778827f7d113f996": {
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
    "0xb92fe925dc43a0ecde6c8b1a2709c170ec4fff4f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6b9017cf3e4e9a01667a8cb242a9451e5022d05d": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4c1079f1c260da4444a002aaabcecc7fdc2b2b73": {
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
