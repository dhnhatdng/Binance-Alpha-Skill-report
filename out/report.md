# O (o1.exchange) — On-chain Decision Briefing


## 🎯 One-screen verdict

> This section is deterministically derived from on-chain detector outputs and is not buy/sell advice. Full evidence is in the sections below.

| Dimension | Conclusion | Key evidence |
|---|---|---|
| **Current phase** | 🟢 Accumulation / watch — no significant trigger | None of the 5 main signal tiers triggered |
| **Chip structure** | 🟠 Moderately controlled | Operator/project-controlled chips 55.4% / CEX relay pool 15.4% / verifiable non-operator sell-pressure 29.2% |
| **Insider / operator spot realization** | 🟠 Partially realized | Confirmed insider realization 13.4% of circ + net CEX-withdrawal distribution 0.0% of circ |
| **Volume quality** | 🔴 24h volume untrustworthy — wash bots dominate | 145,937 on-chain matches; single bot 14.3% |
| **Supply risk** | 🟠 Supply source present — limited magnitude | 1 mint authorities; cumulative 3.4% of total supply |
| **Market-cap stage** | 🟢 Mid mcap | mcap $108M; 5% depth $7,812; LP/mcap 0.028; vol/LP 5.0×; 24h +5.8% |
| **Monitoring focus** | Maintain baseline monitoring | Mint-authority contracts |

**One-liner**: Accumulation / watch + Moderately controlled + volume inflated by wash.

## 🎯 Quick-read summary

> This section is for quick retail reading / AI re-interpretation. Detailed forensic detection is in the sections below (with English terms). Everything here is derived from on-chain data and contains no buy/sell advice.

- **Project**: o1.exchange (O), main contract [`0x500a02a2…`](https://bscscan.com/address/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4)
- **Listing**: Binance Alpha S1 (Alpha only) · primary chain BSC

- **Confirmed insider on-chain realization**: **21,496,076 tokens (13.44% of circulating)** ≈ **$8,218,160 USD** — a lower bound on what insider wallets have realized themselves via (a) deposits to centralized-exchange deposit addresses + (b) their own direct on-chain matches; actual sell-out is most likely higher (see 📊 Confirmed sell-out section)
- **Historical high-throughput operators surfaced**: 27 wallets ran cumulative **throughput** (token in/out flow, NOT sell volume, includes wash double-counting) of **178,630,989 tokens** over 365 days then zeroed out — already exited

- **Report-completeness note**: only on-chain-verifiable wallet → DEX/CEX flows are included. Off-chain behaviour (distribution after a CEX withdrawal / OTC transfers / bridges not in the surf index, etc.) is not on-chain-detectable, so real sell-out may exceed the figures here. See the 🟡 completeness note below.

- **How to use this report**: read it alongside the **Monitored wallets** section below; add the core wallets to Binance Wallet / OKX monitoring (monitoring_paste.json supports one-click import). Make entry/exit decisions according to your own risk tolerance.


> ⚠️ **Read first — on-chain detection limits / data caveats**
>
> - 🚨 **24h volume / on-chain matches dominated by a wash bot**: 200 counterparty addresses / 145,937 on-chain matches, with a single wash bot doing up to 20,805 wash matches (single wash bot share 14.3%). **Do not use 24h volume to judge real absorption** — see "absorption cap (5% depth)" below. Detail → 📊 Confirmed sell-out section.
> - 🟡 **Several dump paths are structurally out of coverage**: ⛓️ cross-chain dumps (other chains invisible) / 🌉 bridge mint-authority self-dumps (mint source selling itself) / 🏦 the CEX-withdrawal phase (off-chain, not on-chain-detectable) / ⏰ 60d+ historical high-throughput dumps. **Real sell-out may be 5-50× the figures here**. v0.7.24 backlog: mint-authority + multi-chain + high-throughput detectors added (see 🌉 / 🌊 / 🔗 sections at the end).
_Tool version 1.0.4 · Main chain BSC · Alpha listed 2026-06-17_

_Total supply 1,000,000,000 · Circulating 160,000,000 (16.0%) · Type VC_LIKELY_
_Tier S1 · S1 2026-06-17_

## 💹 Token market (real-time)

| Item | Value |
|---|---|
| **Project name** | **o1.exchange** (O) |
| Ticker | `O` |
| Primary chain | BSC |
| Listing | S1 (Alpha only) · Alpha listed 2026-06-17 |
| **Current price** | **$0.6887** (🟢 +7.48% 24H) |
| **Network 24H volume (CEX+DEX)** | **$22,625,912** |
| Current LP (DEX main pool) | $2,991,846 |
| Market cap (mcap / FDV) | $109,821,513 / $686,384,458 |
| Data source | surf+Alpha API (real-time) · 34,196 holders · 24H 68,692 txns |

## 📋 Decision summary

| Item | Value |
|---|---|
| **🎯 Risk score** | **🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ (2/10)** |
| **On-chain state label** | **No significant trigger** — No significant on-chain detection trigger |
| Primary chain | binance-smart-chain |
| **Entry cap (LP 5% depth)** | **$7,812** |
| Near-term catalysts | None |
| Blind spots you must cross-check yourself | None |

> 🎯 **Meaning of the 5 on-chain-state labels** (deterministically derived at render time, describing on-chain detection state only, not trading advice):
> - **No significant trigger** — no significant on-chain detection signal (risk 0-2)
> - **Watching** — some activity but no primary signal triggered (risk 2-5)
> - **Distributed and exited** — historical operator already distributed; on-chain historical sell-pressure released (risk 4-7)
> - **Dormant insider, undistributed** — dormant insider wallets have not distributed; timing unpredictable (risk 6-9)
> - **Recent distribution** — large on-chain activity in the last 72h (risk 7-10)

> Based on the analysis of O, the trade sizing is restricted to a max of $7812 due to shallow depth.



## 🎯 On-chain state: No significant trigger (risk score 2/10)

**No significant on-chain detection trigger**


| Decision anchor | Value | Status |
|---|---|---|
| Alpha 5% slippage cap | $7,812 | 🟡 Medium |
| DEX main pool USD liquidity | $2,895,108 | 🟢 |
| Pool token 24h net throughput (NOT LP add/remove) | — | 🟢 |


## 🧠 Current on-chain behaviour profile

> This section translates 10 detector outputs into 4 categories of "what the operator might be doing." Multi-label by design — one token can hit several categories at once (e.g. A1 accumulation + B1 wash volume + C3 recent activity). Order: severity (🔴 STRONG / 🟠 MEDIUM / 🟡 WEAK) → category → label ID. Describes on-chain facts only, not trading advice.

| Severity | Label | Category | Trigger metric | On-chain fact |
|:-:|---|---|---|---|
| 🔴 **STRONG** | `B1` Wash-trade volume inflation (24h vol untrustworthy) | B Volume fabrication | `wash_swap_count=145937, wash_top_bot_share=0.143, wash_n_dex_addrs=200` | 145,937 on-chain matches in 24h across 200 on-chain trading addresses, a single wash bot accounting for 14.3% — the 24h volume contains heavy wash trading and does not equal real absorption |
| 🔴 **STRONG** | `C1` On-chain confirmed outflow (CEX deposit + DEX swap) | C Dump behavior | `net_sellout_usd=8218160.0, sell_pct_circ=13.435` | On-chain confirmed outflow $8,218,160 (13.44% of circulating) — real insider realization observed via CEX deposit + on-chain match paths |
| 🔴 **STRONG** | `C2` Historical high-frequency operator liquidation | C Dump behavior | `ht_operator_count=27, ht_throughput_pct_supply=17.86` | 27 high-frequency operator wallets (cumulative **throughput** = 18% of total supply; throughput = token in/out flow, NOT sell volume) — already exited historically, balance near 0 |
| 🟠 **MEDIUM** | `A3` Mint / bridge / mining supply source | A Chip preparation | `mint_authorities=1, mint_pct_supply_max=3.4, mint_pct_supply_sum=3.4` | 1 mint-authority contracts present (cumulative mint = 3.4% of circulating supply), an ongoing supply source — future mint → dump is possible |
| 🟠 **MEDIUM** | `D2` Cross-chain deployment / coordination | D Coordination structure | `non_primary_chains=1, cg_chains=2` | This token is deployed on 2 chains (1 non-primary chains have independent on-chain hits) — cross-chain dump paths require separate monitoring |
| 🟡 **WEAK** | `B2` Fake depth (LP/mcap mismatch or high vol/LP) | B Volume fabrication | `vol_lp_ratio=5.01, lp_mcap_ratio=0.0277, lp_usd=2991846.3855196363` | Volume/liquidity ratio = 5.0× / liquidity/mcap ratio = 0.0277 — surface liquidity is low and a single trade has large price impact |

> **Behaviour profile is not the verdict**: the 🎯 on-chain state label above is a composite of 5 tiers (No significant trigger / Watching / Distributed and exited / Dormant insider / Recent distribution); the behaviour profile here is the finer-grained 10-class on-chain detection signals. A token can be "Recent distribution" while also hitting multiple labels like A1+A2+A3+B1+C2+C3.


## 🔴 Confirmed sell-out (insider lower bound)

### 🎯 Pump counterparty check

> **⚡ Quick read**: circulating 27.8M tokens · **non-operator sell-pressure 29.2%** (8,120,627 tokens = verifiable within top 100 holders 29.2%) · operator ammo 55.4% (⚠️ Alpha API reports 160M circulating, on-chain dumpable 28M = 0.17x, Alpha overstates (includes mint authority / vesting lockup)) · exchange transit pool (retail vs project custody indistinguishable) 15.4% (1 exchange wallets) · insider confirmed realization $8,218,160 (13.4% of circulating).

> When the operator wants to pump, **the potential sellers = the held chips that don't belong to the operator**. The smaller this is, the more confident the operator is to pump (less fear of being dumped on); the larger, the more cautious.

| Chip bucket | Tokens | % of current circulating | Interpretation |
|---|---:|---:|---|
| 🟣 **Operator / project-controlled chips** | **15,375,569** | **55.4%** | **Moderate control** |
| 🔥 **Verifiable non-operator sell-pressure** | **8,120,627** | **29.2%** | **Heavy external sell-pressure** (includes retail whales + protocol contracts + bridge transit) |
| 🟦 **Exchange transit pool (neutral, indistinguishable)** | **4,274,547** | **15.4%** | 1 exchange hot/cold/deposit wallets. On-chain it is **impossible to distinguish** retail deposit aggregation vs project custody reserve. During a pump it may flow out from either side |

### Key judgment

**Project-controlled chips ≥ 50%** — the operator has the conditions to control the book. Read with "insider confirmed realization" below to see whether it is in the active-distribution phase.
**Raw bucket total 1809% (expand for detail)** — wallet-level overlap across buckets is a debug caveat and does not affect the quick-read 55.4% operator-ammo conclusion.

<details>
<summary>🔍 Expand: operator-ammo 11-sub-bucket detail (with raw total + overlap note)</summary>

| Sub-bucket | Tokens | % of circulating | Note |
|---|---:|---:|---|
| ①a Public lockup / treasury / airdrop contract outside m6 lineage | 0 | 0.0% | Sablier / Hedgey / custom lockups. Public release schedule, **won't dump immediately during a pump**. Lower bound after subtracting the 840,000,000 unminted reserve |
| ①b Movable multisig outside m6 lineage | 0 | 0.0% | Gnosis Safe Proxy etc. The operator can transfer today with one signature |
| ② m6 lineage portion in circulation | 0 | 0.0% | m6 lineage total holdings -21,599,176 minus lockup 0. Includes pure insiders (-21,599,176) |
| ⚠️ ③ Exchange-withdrawal distribution (net control not computable) | — | — | Gross inflow; phase-2 SQL truncated; net fan-out cannot be computed.  |
| ④ DEX pool token-side holdings | 2,214,027 | 8.0% | DEX pools are 99% provided by the project / market maker |
| ⑤ Other detector hits | 294,852 | 1.1% | 17 wallets — flow operators / cross-token whales / high-throughput exit operators |
| ⑥ Mint-contract unreleased reserve | 1 | 0.0% | Mining / bridge mint contract current balance; operator-controlled unreleased supply |
| ⑥' Minted to operator cluster (net holdings) | 24,000,001 | 86.4% | Cumulative mint - contract reserve - realized = still in the fake-mining cluster |
| ⑥'' Heuristic hidden ammo (top-100 unclassified ≥ 3%) | 475,849,063 | 1713.5% | 5 wallets. **The 3% threshold risks false positives** — cross-check via monitoring_paste |
| 📌 Unminted operator-controlled reserve | 840,000,000 | _84.0% of total supply_ | **Not in the circulating denominator — but operator-controlled**. Adds sell-pressure once lockup / mint cadence releases it into circulation |
| ━━━━━ | ━━━━━ | ━━━━━ | ━━━━━ |
| Operator ammo raw total | 502,357,944 | 1808.9% | ⚠️ > 100% = wallet-level overlap across sub-buckets (an in-m6 multisig counted in both ①b + ②). The quick-read 55.4% is a strictly de-duplicated wallet-level back-calculation |

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
| 1 | [`0xc26e7056ef21`](https://bscscan.com/address/0xc26e7056ef210597812a837c2610f5f38a4544ed) | 3,107,283 | 11.19% | Unclassified | — |
| 2 | [`0x1a9b68ca1dca`](https://bscscan.com/address/0x1a9b68ca1dcacb106c4b853e2d9c915f0cfe2e56) | 2,380,774 | 8.57% | Unclassified | — |
| 3 | [`0x07321f149c4e`](https://bscscan.com/address/0x07321f149c4e0a6d57d4c97250c768e6dae6aaee) | 745,595 | 2.68% | Unclassified | — |
| 4 | [`0xe269f955c745`](https://bscscan.com/address/0xe269f955c74558ef40929e693a4ec93c42636879) | 551,356 | 1.99% | Unclassified | — |
| 5 | [`0x9ba87c84a7cc`](https://bscscan.com/address/0x9ba87c84a7cc2a22717ccc01347bcb46b9c208c4) | 490,993 | 1.77% | Unclassified | — |
| 6 | [`0x7c0f3a9eb040`](https://bscscan.com/address/0x7c0f3a9eb040c3a87e911f85b9f8187585d9ecd2) | 487,836 | 1.76% | Unclassified | — |
| 7 | [`0x747ae5e4f89d`](https://bscscan.com/address/0x747ae5e4f89d19eb4bd56e4afa1deccf67a72016) | 356,791 | 1.28% | Unclassified | — |
| ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━ | ━━━━━━━ | ━━━━━━━━━ | ━━━━━━━━━ |
| **Total verifiable non-operator sell-pressure (within top 100 holders)** | 7 wallets | **8,120,627** | **29.2%** | — | — |

> ⚠️ **Nature of non-operator sell-pressure**: mainly true retail whales + protocol contracts like Wormhole / veVELVET (user-deposited) + bridge transit. Large bare addresses (no Arkham label + > 1% circulating) are suspect as either operator aliases or true retail whales — cross-check wallet activity via monitoring_paste below.

---

| Item | Value |
|---|---|
| Tracked wallets | **33** (32 standard insiders + **1 mint authorities**; mining / bridge token, no pre-launch m6 lineage) |
| **Pure insider current holdings (the true dormant sell-pressure the verdict references)** | **-2.1599% of supply** (-21,599,175 tokens, **excluding** vesting / multisig / treasury / CEX custody / DEX routing; includes mint-authority contract current balance) · 🌉 mint authority still sits on 1 tokens (can keep mint→dumping at any time) |
| Insider-tree current holdings (incl. lockup, conservation anchor) | -2.1599% of supply (-21,599,175 tokens, in mining mode the tree = standard insiders + mining-fed set + mint-authority contracts (no vesting/lockup separation)) |
| (a) Confirmed sell-out — CEX deposit | 10,432,409 → Binance Wallet |
> _💡 Note: off-chain CEX withdrawals (CEX → wallet) are not in row (a) — (a) only tracks on-chain wallet → CEX deposits. A project that withdraws from a CEX first and then dumps (e.g. the H case Eleve described) does so off-chain and cannot be on-chain-detected; any subsequent on-chain transfer that dumps via a DEX router is already captured in row (b)._
| (b) Confirmed sell-out — DEX swap (own wallet) | 11,063,667 (41,409 swaps all via DEX router) |
| **Confirmed gross sell-out, a+b** | **≥ 21,496,076 = 13.4% of circulating**, USD ≈ $8,626,242 |
| **Confirmed net sell-out** | **$8,218,160** — insider **self-sell DEX TWAP** $0.3823 (rejects wash-quote contamination); DEX real ≈ $4,229,748 (on-chain SUM amount_usd, 100% provable) + CEX estimate ≈ $3,988,412 (cex_tokens × TWAP) |



> **📅 Time-window split** — reconcile against short-term events (Twitter sudden-dump alerts / large moves); the relationship is **last 7d ≤ last 30d ≤ cumulative**.

| Window | Confirmed gross sell-out (tokens) | % of circulating | Confirmed net sell-out (USD) | DEX real volume (USD) | CEX route (tokens) |
|---|---:|---:|---:|---:|---:|
| **Last 7 days** | 21,496,076 | 13.44% | **$8,218,160** | $4,229,748 | 10,432,409 |
| Last 30 days | 21,496,076 | 13.44% | $8,218,160 | $4,229,748 | 10,432,409 |
| Cumulative (~364 days) | 21,496,076 | 13.44% | $8,218,160 | $4,229,748 | 10,432,409 |

> Interpretation: **last 7 days** shows current heat (reconcile directly with EmberCN-style sudden alarms); **last 30 days** shows the month's pace; **cumulative** = everything within the surf query window. A single-day burst may not show in the 7d average but is already in the cumulative. CEX route = tokens that went into exchange deposit/hot wallets (sold off-chain on the CEX side, not at the wash price).


> 🕵️ **Hidden operator ammo has shown realization activity**: the tracked **9 hidden-ammo wallets** (heuristic catches / fake-mining mint cluster) have, via (a) deposits to exchange deposit addresses of **10,000,000 tokens** (1 exchanges: Binance Wallet) + (b) their own on-chain matches of **0 tokens** (0 swaps), totalled **10,000,000 tokens** = 6.25% of circulating. **These wallets are outside the algorithm's 5 buckets** and may add on top of "confirmed gross sell-out" to view real distribution; but **you must subtract any wallet overlap with the m6 insider / mining-fed sets** (v0.8.4 backlog: add disjoint dedupe). Time window: from 2026-06-17.> ⚠️ **This token's on-chain dump is dominated by a wash bot**: 200 counterparty addresses with 145,937 on-chain matches total, a single wash bot doing up to 20,805 wash matches. Many insiders route tokens to relays / bots before selling (this portion is **unattributable** and not counted in the confirmed lower bound above — so real sell-out is most likely higher than the lower bound). Massive wash = dumping while inflating surface activity to lure buyers.


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

**On-chain transfer rhythm for O.**



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

**Interpretation**: The token O is deployed as a single-chain asset on BSC with no cross-chain bridge activity.

## Entry-price anchor (TGE)

| Time anchor | UTC | Price | vs current |
|---|---|---|---|
| LP creation first tx (DEX start) | — | — | — |
| Alpha first tx | 2026-06-17 14:00 UTC | — | — |
| **Current price** | 2026-06-22 | **$0.6726** | 1.00× |

**Interpretation**: The token was first listed on Binance Alpha on 2026-06-17 UTC. The current price is $0.6757.

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
| Binance | Not listed | — | — |
| Aster | Unverified | — | — |
| Bitget | Unverified | — | — |

No new catalyst within 14 days. Current S1 (Alpha only).

**Interpretation**: The token has no active CEX perpetual listings on Binance, Aster, or Bitget, keeping it in S1 classification.

<a id="section-liq"></a>
## Entry ceiling (LIQ)

| Anchor | Value | Note |
|---|---|---|
| **Max single buy under 5% slippage (estimated)** | $7,812 | Derived from Alpha 24h vol (vol_24h / 96 × 0.05 heuristic estimate) |
| DEX main pool liquidity | $2,895,108 | surf 0x1a9b68ca… |
| DEX main pool 24h volume | $22,625,912 | surf project-detail (cross-chain CEX+DEX realtime aggregation) |
| Pool token 24h net throughput (NOT LP add/remove) | — | surf agent.bsc_transfers |
| DEX main pool address | `0x1a9b68ca1dcacb106c4b853e2d9c915f0cfe2e56` | FDV $686,384,458 |

**Interpretation**: DEX liquidity is $2,895,107.50 but estimated 5% depth is extremely low at $7812, limiting trade sizing.

<a id="section-holdings"></a>
## Holdings distribution by role

**Distribution table**:

| Role | Wallet # | Current balance | % of supply | Top wallet |
|---|---|---|---|---|
| DEX main pool | 1 | 2,382,053 | 0.2382% | [`0x1a9b68ca…`](https://bscscan.com/address/0x1a9b68ca1dcacb106c4b853e2d9c915f0cfe2e56) |
| Deployer wallet | 0 | 0 | —% | — |
| Quiet wallet (insider, never distributed) | 0 | 0 | —% | — |
| Other (retail + unclassified) | 49 | 27,490,411 | 2.7490% | [`0x35aac8fc…`](https://bscscan.com/address/0x35aac8fc62dbf6d6601bd1e38fc7e049a1333b76) |

**Key takeaways**:
- Insider tracking: **33** wallets hold **-2.2%** of supply cumulatively, incl. 1 mint authorities  (mining / bridge token, no pre-launch m6 lineage).
- Insiders have on-chain-confirmed outflow of **8.2M USD** = **13.44%** of circulating, priced at the insider self-sell TWAP (not the wash quote).

<details>
<summary>📂 <strong>Backward trace (Deployer → insider lineage)</strong> — 0 insider wallets: 0 fully distributed / 0 distributing / 0 quiet (click to expand the full lineage + wallet balances + distribution rate)</summary>

**Insider wallet list (deployer distribution trace)**:

| ID | Address | Received from deployer | Current balance | Dumped % |
|---|---|---|---|---|
_Stats (full m6 lineage, **0** wallets): 0 near-zero holdings / public-lockup custody · 0 distributing · 0 fully distributed_

**m4_notes (pre-LP allocation interpretation)**:
- The pre-launch phase for O shows no early wallet deployments or allocations.
- No pre-launch OTC seeding was detected on BSC for O, which means there are zero verified early insider recipients.
- Without any pre-launch deployment trace, the initial allocation remains highly concentrated in the creator/unlabeled reserves.



</details>

## 💰 High-Value Address Funding Source (mint / DEX / P2P)

Below are the high-value addresses already surfaced by the wash setup / flow operator / m6 insider / Top-30 holder sections, classified by how they ACQUIRED their tokens over the past 365 days: mint (received directly from 0x0 — covers mining contracts, bridge mint authorities, airdrop mint contracts), DEX buy (received from a known DEX main pool), or P2P (any other EOA transfer, including unidentified CEX withdrawals). Use this to distinguish: ⛏️ high mint% = mining-token operator or sockpuppet airdrop farmer; 🟢 high DEX% = real retail buyer; 🔵 high P2P% = operator aggregation hub or OTC recipient.

> Queried 200 high-value addresses; 21 have real incoming activity in the past 365 days — ⛏️ Mint-fed 0 / 🟢 DEX-fed 0 / 🔵 P2P-fed 21.


| Address | Primary Source | Total Received | Mint % | DEX buy % | P2P % |
|---|---|---:|---:|---:|---:|
| [`0x9999b0cd…`](https://bscscan.com/address/0x9999b0cdd35d7f3b281ba02efc0d228486940515) | 🔵 P2P-fed | 6,236,005 | 0.0% | 0.0% | 100.0% |
| [`0xe6dc69e0…`](https://bscscan.com/address/0xe6dc69e04e6075b7b23b41943adce246b86416b4) | 🔵 P2P-fed | 1,800,225 | 22.4% | 0.0% | 77.6% |
| [`0x3e19a7b6…`](https://bscscan.com/address/0x3e19a7b6f216daf2fdafe03335812cb400de9064) | 🔵 P2P-fed | 1,775,405 | 0.0% | 0.0% | 100.0% |
| [`0x8678f58a…`](https://bscscan.com/address/0x8678f58ac6c4748b5289d0db70e627eef395dead) | 🔵 P2P-fed | 1,290,303 | 45.7% | 0.0% | 54.3% |
| [`0x324e559d…`](https://bscscan.com/address/0x324e559d0f7507c4782f54662b09b984b1874094) | 🔵 P2P-fed | 1,266,344 | 8.6% | 0.0% | 91.4% |
| [`0x18d3d1be…`](https://bscscan.com/address/0x18d3d1beb50bb1e0f7edd1a1189622a34ca7bb63) | 🔵 P2P-fed | 1,169,568 | 8.5% | 0.0% | 91.5% |
| [`0x865166dc…`](https://bscscan.com/address/0x865166dca4519a0aee3fe30db27dd5de799d7c5c) | 🔵 P2P-fed | 1,104,962 | 0.0% | 0.0% | 100.0% |
| [`0x93b996f9…`](https://bscscan.com/address/0x93b996f91e60502af0c9a4d7d94a8668257d4800) | 🔵 P2P-fed | 920,347 | 0.0% | 0.0% | 100.0% |
| [`0x3a16e0d5…`](https://bscscan.com/address/0x3a16e0d5a27dad1f28b44b973684ed68f6f22c90) | 🔵 P2P-fed | 707,266 | 0.0% | 0.0% | 100.0% |
| [`0x11fc12b9…`](https://bscscan.com/address/0x11fc12b988933966688d33b70651b5f2f450963c) | 🔵 P2P-fed | 660,790 | 0.0% | 0.0% | 100.0% |
| [`0x930200f7…`](https://bscscan.com/address/0x930200f76ffd57703d8ad5ed9d71261d3e3859db) | 🔵 P2P-fed | 630,901 | 0.0% | 0.0% | 100.0% |
| [`0xe0881cc5…`](https://bscscan.com/address/0xe0881cc50de6a472cd340111e80d70b79d807ac1) | 🔵 P2P-fed | 613,355 | 0.0% | 0.0% | 100.0% |
| [`0x86963e1d…`](https://bscscan.com/address/0x86963e1d6aeafff2868f3c6c7dc4176dc5e81b26) | 🔵 P2P-fed | 595,181 | 0.0% | 0.0% | 100.0% |
| [`0x36f95aaa…`](https://bscscan.com/address/0x36f95aaa9e283e73857c844de40bfcfffb88bf04) | 🔵 P2P-fed | 582,539 | 0.0% | 0.0% | 100.0% |
| [`0xb46c4026…`](https://bscscan.com/address/0xb46c4026303ec47fb9f29bf31bffc0b958a359f3) | 🔵 P2P-fed | 362,131 | 0.0% | 0.0% | 100.0% |
| [`0xc16b14a4…`](https://bscscan.com/address/0xc16b14a4df90c04c7d28a96fd01efd6df3fc9b95) | 🔵 P2P-fed | 247,937 | 0.0% | 0.0% | 100.0% |
| [`0x5d26b4f7…`](https://bscscan.com/address/0x5d26b4f7d08d90dd2f33e41c807710926248819e) | 🔵 P2P-fed | 236,106 | 0.0% | 0.0% | 100.0% |
| [`0xaa4ea716…`](https://bscscan.com/address/0xaa4ea7166e18c596804c76d21f11a99d79775fc1) | 🔵 P2P-fed | 111,625 | 0.0% | 0.0% | 100.0% |
| [`0xd7a3afa5…`](https://bscscan.com/address/0xd7a3afa5461d114521bb6542400900b52a6399eb) | 🔵 P2P-fed | 22,135 | 0.0% | 0.0% | 100.0% |
| [`0x65e107c3…`](https://bscscan.com/address/0x65e107c3b1cf6375cb0bb15e16c2e4eb841de3de) | 🔵 P2P-fed | 20,846 | 0.0% | 0.0% | 100.0% |
| [`0x00326070…`](https://bscscan.com/address/0x00326070c5593b44b1323e112069f8a1c93afbfb) | 🔵 P2P-fed | 18,252 | 0.0% | 0.0% | 100.0% |

> _Scan cap: the pipeline collected 226 high-value candidates, max_addrs cap = 200, actually queried 200 (ordered by detector priority: wash → flow → m6 → dump-sellers → Top-30 holders). Truncated 26 — common on PLAY-class tokens with many (60+) flow_operators._

> _The CEX-withdrawal column is not yet separately identified (a v0.7.24 candidate) and is currently grouped under P2P. When a real CEX hot-wallet transfer cannot be distinguished from a plain EOA transfer, both count as P2P._



<a id="section-bridge-mint"></a>
### 🌉 Bridge / mint-authority self-sell detail (v0.7.24a)

> Detected **1 mint-authority contracts** (receive mint from 0x0, excluding the deployer + wallets already covered in the mining-fed section). They are bridge / staking / airdrop contracts that may **themselves** DEX swap. This is a dump path the v0.7.23.x series missed entirely.

| Authority address | Arkham label | 365d Mint amount | % of supply | Own DEX sell | USD ≈ |
|---|---|---:|---:|---|---:|
| [`0x66f0306baca1…`](https://bscscan.com/address/0x66f0306baca1543f5be385699b5b1df5c2a72f6c) | _Unlabeled (new contract, not in Arkham) | 34,000,002 | 3.40% | — (no direct DEX self-sell) | — |





<a id="section-high-throughput"></a>
### 🌊 High-throughput dump wallets (v0.7.24b)

> Detected **27 operator wallets** with a high-throughput clear-out pattern (large token flow-through + balance ≈ 0 + high-frequency tx). Thresholds: throughput 1M ~ 5% of supply, balance < 5% of throughput, n_tx ≥ 1000. Already filtered out infra labels like DEX routers / CEX deposits / aggregators (not operators). These are operators that finished dumping and left before the 60d window — missed by flow_operators (60d window) + mining-fed (balance > threshold).

| Operator address | Primary role | Arkham label | 365d inflow (= received mint/p2p) | Outflow (= sold / transferred out) | Residual balance | tx count |
|---|---|---|---:|---:|---:|---:|
| [`0x0501f595d17d…`](https://bscscan.com/address/0x0501f595d17dd90ff11a9873692ee3f8d478f4e5) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 36,521,966 | 36,521,966 | 0 | 118,076 |
| [`0x7a7ad9aa93cd…`](https://bscscan.com/address/0x7a7ad9aa93cd0a2d0255326e5fb145cec14997ff) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 20,574,826 | 20,574,826 | 0 | 98,406 |
| [`0xbd97306a087e…`](https://bscscan.com/address/0xbd97306a087ed0c46b783cfbfdcdc6c12c7a2866) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 17,500,778 | 17,462,688 | 38,090 | 147,662 |
| [`0x62ccef0b4545…`](https://bscscan.com/address/0x62ccef0b4545166f721caa9fee13c1d3767e27dc) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 16,658,112 | 16,658,112 | -0 | 89,313 |
| [`0x031942f26a09…`](https://bscscan.com/address/0x031942f26a094be40414f442a2f1295e3a5c1680) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 12,467,058 | 12,452,735 | 14,323 | 20,404 |
| [`0xb40e80acfec7…`](https://bscscan.com/address/0xb40e80acfec7c38ae0f7595cc01d68e98ed31ad6) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 9,720,056 | 9,685,639 | 34,417 | 88,961 |
| [`0x097fd934ce91…`](https://bscscan.com/address/0x097fd934ce9124fe6aec6dd325108b34986770d1) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 9,521,955 | 9,521,955 | 0 | 19,741 |
| [`0xc5a1350019fa…`](https://bscscan.com/address/0xc5a1350019fabafe58cb2c3576672b6f7e1fd562) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 7,735,744 | 7,735,744 | 0 | 13,967 |
| [`0x286da9568057…`](https://bscscan.com/address/0x286da9568057420df90c5489e51cbb82b29f0301) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 6,308,624 | 6,304,637 | 3,987 | 20,439 |
| [`0x9999b0cdd35d…`](https://bscscan.com/address/0x9999b0cdd35d7f3b281ba02efc0d228486940515) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 6,236,005 | 6,236,005 | 0 | 80,160 |
| [`0xca8d055d625f…`](https://bscscan.com/address/0xca8d055d625f5fc29d0891ac0b67c687ed450f51) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 5,541,464 | 5,533,137 | 8,327 | 12,239 |
| [`0xf45ecc0b0028…`](https://bscscan.com/address/0xf45ecc0b00283c607f2f6e93425e4b9f8e7488d8) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 3,969,387 | 3,969,387 | 0 | 19,134 |
| [`0x31d6ea082acc…`](https://bscscan.com/address/0x31d6ea082acc3d4e377528a721ac5c4b891726fb) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 2,859,018 | 2,859,018 | -0 | 34,718 |
| [`0xc1faf39ecd3d…`](https://bscscan.com/address/0xc1faf39ecd3dd4149a04474797f61695da23f93d) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 2,421,548 | 2,406,916 | 14,632 | 8,843 |
| [`0x98bf43f409e1…`](https://bscscan.com/address/0x98bf43f409e1c35e243b9e249575990a6f10dc69) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 2,283,750 | 2,283,705 | 45 | 14,387 |
| [`0xc383960159d5…`](https://bscscan.com/address/0xc383960159d5c5f6ad9bbc6519a9e1937ca58046) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 2,218,994 | 2,217,148 | 1,847 | 13,170 |
| [`0x4c1079f1c260…`](https://bscscan.com/address/0x4c1079f1c260da4444a002aaabcecc7fdc2b2b73) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 1,930,278 | 1,929,887 | 391 | 7,705 |
| [`0xe6dc69e04e60…`](https://bscscan.com/address/0xe6dc69e04e6075b7b23b41943adce246b86416b4) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 1,800,225 | 1,729,740 | 70,485 | 9,130 |
| [`0x3e19a7b6f216…`](https://bscscan.com/address/0x3e19a7b6f216daf2fdafe03335812cb400de9064) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 1,775,405 | 1,741,393 | 34,011 | 5,572 |
| [`0x28e2ea090877…`](https://bscscan.com/address/0x28e2ea090877bf75740558f6bfb36a5ffee9e9df) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 1,679,820 | 1,678,820 | 1,000 | 48,571 |

> _Showing top 20; 27 high-throughput operator wallets detected in total (sorted by throughput; throughput = token in/out flow, NOT sell volume). Full list in skeleton.json `funding_attribution.high_throughput_dumpers.dumpers`._

> 🌊 These wallets passed **178,630,989 tokens** through over 365d then cleared out — operators that have finished dumping. They've already sold, but **if the project mints another batch and distributes it to similar-pattern wallets in future**, they become the next dump-risk source.




### 🔗 Cross-chain dump trace (v0.7.24c)

> Detected that this token is deployed on multiple chains. The primary chain's (BSC) dump activity already surfaced in earlier sections; here we show **other chains'** dump activity. The earlier v0.7.23.x single-chain forensic missed cross-chain entirely.


#### 🔗 BASE (CA: [`0x182fa643e5f2…`](https://bscscan.com/address/0x182fa643e5f29d5eca75e7b9cf9336a3fe4620b2))

> ⏭️ **base skipped** — 0 DEX pools on this chain — no market to forensic.



> _💡 This section only surfaces what the current detectors could fetch cross-chain. For the real cross-chain dump magnitude, combine with on-chain explorers like Etherscan / Bscscan / Arbiscan._


<a id="section-monitoring"></a>
## Monitored wallets + real-time alerts


> 📊 **Monitoring priority (v0.7.27 deterministic ranker)**: 🚨 4 CRITICAL · 🔥 5 HIGH · 👀 0 NORMAL>
> Wallets in paste.json are sorted by level, 🚨 first. Prioritize CRITICAL+HIGH (9) — when these wallets move, the on-chain detection picture changes. NORMAL (0) is for bulk cross-checking, no push notification needed. 💤 NOT_TRACKED are DEX routers / public CEX hot wallets whose flow noise drowns the real signal, removed from paste.


| # | Level | Wallet | Role | primary role section | Trigger condition | Status |
|---|:-:|---|---|---|---|---|
| 1 | 🔥 HIGH | [`0x8f816c7c`](https://bscscan.com/address/0x8f816c7c57638b6c2e0eb8d405dac465f7789466) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 2 | 🔥 HIGH | [`0x08113b2d`](https://bscscan.com/address/0x08113b2d9b8be48e0a533ee753cc063c472598be) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 3 | 🔥 HIGH | [`0x35aac8fc`](https://bscscan.com/address/0x35aac8fc62dbf6d6601bd1e38fc7e049a1333b76) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 4 | 🔥 HIGH | [`0x84c6b83a`](https://bscscan.com/address/0x84c6b83a0ff505e55ad2067555ac2fc405ed9f90) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 5 | 🚨 CRITICAL | [`0xc8662486`](https://bscscan.com/address/0xc8662486e8141a05c38f09f29a8ff47463224685) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 6 | 🚨 CRITICAL | [`0x7022c09e`](https://bscscan.com/address/0x7022c09e1a7fb3823a3ec26585bc7a2b00df8fe5) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 7 | 🚨 CRITICAL | [`0x86b50b10`](https://bscscan.com/address/0x86b50b10561163bee543cb7abe4e4c1564697eb3) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 8 | 🚨 CRITICAL | [`0x500a02a2`](https://bscscan.com/address/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |
| 9 | 🔥 HIGH | [`0xbd1dbe28`](https://bscscan.com/address/0xbd1dbe28fa5eaebf6498be090b78f81a5aa8c652) | Heuristically-flagged hidden operator ammo (reserve) | — | Tag type: heuristically-flagged hidden operator ammo (≥ 10% circulating + no Arkham label). The user can watch whether / when these three on-chain behaviours occur: (1) splitting across multiple downstream accounts, (2) transferring into an Arkham-labeled exchange deposit address, (3) on-chain matching (direct transfer-out against USDT/BNB/WBNB etc.). If (2)(3) appear, combine with this report's confirmed sell-out section insider self-sell TWAP to estimate the actual realized USD. | 🟡 |

Monitoring these 9 wallets helps track active operator reserves and potential sell-out actions for O.

## Machine-readable JSON (compact)

```json
{
  "schema_version": "1.0.4",
  "symbol": "O",
  "verdict": "ADVISORY",
  "verdict_zh": "Observe",
  "verdict_downgrade_applied": 0,
  "chain_state": "CLEAN",
  "chain_state_label": "No significant on-chain detection trigger",
  "chain_state_risk_score": 2,
  "alpha_listing_tier": "S1",
  "any_anomaly_firing": false,
  "render_provenance": {
    "rendered_by": "render_report.py (v0.6, jinja2)",
    "data_source": "report_data.json (LLM-filled, Python-validated)",
    "deterministic": true
  },
  "structural_counts": {
    "anomaly_waves": 0,
    "evidence_graph_entries": 1,
    "holdings_role_rows": 4,
    "holdings_progress_bars": 4,
    "monitoring_wallets": 9,
    "lineage_flowchart_nodes": 1,
    "lineage_flowchart_edges": 0,
    "m6_rows": 0,
    "decision_anchors": 3,
    "decision_re_entry_conditions": 1
  },
  "address_role_index": {
    "0x66f0306baca1543f5be385699b5b1df5c2a72f6c": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x031942f26a094be40414f442a2f1295e3a5c1680": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x31d6ea082acc3d4e377528a721ac5c4b891726fb": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x865166dca4519a0aee3fe30db27dd5de799d7c5c": {
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
    "0x9999b0cdd35d7f3b281ba02efc0d228486940515": {
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
    "0xf45ecc0b00283c607f2f6e93425e4b9f8e7488d8": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe1f7f56d942292eed2e961a809a1043a5e9ce473": {
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
    "0xb40e80acfec7c38ae0f7595cc01d68e98ed31ad6": {
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
    },
    "0x097fd934ce9124fe6aec6dd325108b34986770d1": {
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
    "0xe6dc69e04e6075b7b23b41943adce246b86416b4": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x3e19a7b6f216daf2fdafe03335812cb400de9064": {
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
    "0x62ccef0b4545166f721caa9fee13c1d3767e27dc": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4ac2621d59659ba77e22301c246fc4a4bb174537": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x98bf43f409e1c35e243b9e249575990a6f10dc69": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xc5a1350019fabafe58cb2c3576672b6f7e1fd562": {
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
    "0x18d3d1beb50bb1e0f7edd1a1189622a34ca7bb63": {
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
    "0xc1faf39ecd3dd4149a04474797f61695da23f93d": {
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
    "0x8678f58ac6c4748b5289d0db70e627eef395dead": {
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
    }
  }
}
```

---

****Data research only, not investment advice. evidence_graph contains 1 stable IDs for provenance tracing.****
