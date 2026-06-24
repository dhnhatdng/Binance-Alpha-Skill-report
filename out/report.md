# BEAT (Audiera) — On-chain Decision Briefing


## 🎯 One-screen verdict

> This section is deterministically derived from on-chain detector outputs and is not buy/sell advice. Full evidence is in the sections below.

| Dimension | Conclusion | Key evidence |
|---|---|---|
| **Current phase** | 🟢 Accumulation / watch — no significant trigger | None of the 5 main signal tiers triggered |
| **Chip structure** | 🟣 Highly operator-controlled | Operator/project-controlled chips 78.8% / CEX relay pool 17.1% / verifiable non-operator sell-pressure 4.1% |
| **Insider / operator spot realization** | 🔴 Heavily realized | Confirmed insider realization 22.7% of circ + net CEX-withdrawal distribution 0.0% of circ |
| **Volume quality** | 🔴 24h volume untrustworthy — wash bots dominate | 2,524,236 on-chain matches; single bot 15.2% |
| **Supply risk** | 🔴 Active mint / bridge supply source | 10 mint-authority contracts; cumulative mint = 98.8% of total supply |
| **Market-cap stage** | 🟠 Mid mcap + thin absorption / pumping | mcap $729M; 5% depth $17,900; LP/mcap 0.004; vol/LP 10.7×; 24h +49.1% |
| **Monitoring focus** | Maintain baseline monitoring | Mint-authority contracts, High-frequency liquidation wallets |

**One-liner**: Accumulation / watch + Highly operator-controlled + volume inflated by wash.

## 🎯 Quick-read summary

> This section is for quick retail reading / AI re-interpretation. Detailed forensic detection is in the sections below (with English terms). Everything here is derived from on-chain data and contains no buy/sell advice.

- **Project**: Audiera (BEAT), main contract [`0xcf3232b8…`](https://bscscan.com/address/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36)
- **Listing**: Binance Alpha S2 (Spot + Perp) · primary chain BSC

- **Confirmed insider on-chain realization**: **65,457,028 tokens (22.73% of circulating)** ≈ **$48,215,531 USD** — a lower bound on what insider wallets have realized themselves via (a) deposits to centralized-exchange deposit addresses + (b) their own direct on-chain matches; actual sell-out is most likely higher (see 📊 Confirmed sell-out section)
- **Historical high-throughput operators surfaced**: 100 wallets ran cumulative **throughput** (token in/out flow, NOT sell volume, includes wash double-counting) of **1,512,472,963 tokens** over 365 days then zeroed out — already exited

- **Report-completeness note**: only on-chain-verifiable wallet → DEX/CEX flows are included. Off-chain behaviour (distribution after a CEX withdrawal / OTC transfers / bridges not in the surf index, etc.) is not on-chain-detectable, so real sell-out may exceed the figures here. See the 🟡 completeness note below.

- **How to use this report**: read it alongside the **Monitored wallets** section below; add the core wallets to Binance Wallet / OKX monitoring (monitoring_paste.json supports one-click import). Make entry/exit decisions according to your own risk tolerance.


> ⚠️ **Read first — on-chain detection limits / data caveats**
>
> - 🚨 **24h volume / on-chain matches dominated by a wash bot**: 200 counterparty addresses / 2,524,236 on-chain matches, with a single wash bot doing up to 383,389 wash matches (single wash bot share 15.2%). **Do not use 24h volume to judge real absorption** — see "absorption cap (5% depth)" below. Detail → 📊 Confirmed sell-out section.
> - 🟡 **Several dump paths are structurally out of coverage**: ⛓️ cross-chain dumps (other chains invisible) / 🌉 bridge mint-authority self-dumps (mint source selling itself) / 🏦 the CEX-withdrawal phase (off-chain, not on-chain-detectable) / ⏰ 60d+ historical high-throughput dumps. **Real sell-out may be 5-50× the figures here**. v0.7.24 backlog: mint-authority + multi-chain + high-throughput detectors added (see 🌉 / 🌊 / 🔗 sections at the end).
_Tool version 1.0.4 · Main chain BSC · Alpha listed 2025-12-23_

_Total supply 1,000,000,000 · Circulating 288,016,666 (28.8%) · Type VC_LIKELY_
_Tier S2 · S1 2025-12-23 · S2 2025-11-12_
## 💹 Token market (real-time)

| Item | Value |
|---|---|
| **Project name** | **Audiera** (BEAT) |
| Ticker | `BEAT` |
| Primary chain | BSC |
| Listing | S2 (Alpha + Binance Perps) · Alpha listed 2025-12-23 · Perp listed 2025-11-12 |
| **Current price** | **$2.49** (🟢 +46.86% 24H) |
| **Network 24H volume (CEX+DEX)** | **$67,411,523** |
| Current LP (DEX main pool) | $3,219,178 |
| Market cap (mcap / FDV) | $734,195,758 / $2,549,143,312 |
| Data source | surf+Alpha API (real-time) · 143,619 holders · 24H 122,510 txns |

## 📋 Decision summary

| Item | Value |
|---|---|
| **🎯 Risk score** | **🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ (2/10)** |
| **On-chain state label** | **No significant trigger** — No significant on-chain detection trigger |
| Primary chain | binance-smart-chain (this chain's current LP $992,520) |
| **Entry cap (LP 5% depth)** | **$17,899** |
| Near-term catalysts | None |
| Blind spots you must cross-check yourself | None |

> 🎯 **Meaning of the 5 on-chain-state labels** (deterministically derived at render time, describing on-chain detection state only, not trading advice):
> - **No significant trigger** — no significant on-chain detection signal (risk 0-2)
> - **Watching** — some activity but no primary signal triggered (risk 2-5)
> - **Distributed and exited** — historical operator already distributed; on-chain historical sell-pressure released (risk 4-7)
> - **Dormant insider, undistributed** — dormant insider wallets have not distributed; timing unpredictable (risk 6-9)
> - **Recent distribution** — large on-chain activity in the last 72h (risk 7-10)

> Based on the analysis of BEAT, the trade sizing is restricted to a max of $17899 due to shallow depth.



## 🎯 On-chain state: No significant trigger (risk score 2/10)

**No significant on-chain detection trigger**


| Decision anchor | Value | Status |
|---|---|---|
| Alpha 5% slippage cap | $17,899 | 🟡 Medium |
| DEX main pool USD liquidity | $15,837 | 🔴 |
| Pool token 24h net throughput (NOT LP add/remove) | — | 🟢 |


## 🧠 Current on-chain behaviour profile

> This section translates 10 detector outputs into 4 categories of "what the operator might be doing." Multi-label by design — one token can hit several categories at once (e.g. A1 accumulation + B1 wash volume + C3 recent activity). Order: severity (🔴 STRONG / 🟠 MEDIUM / 🟡 WEAK) → category → label ID. Describes on-chain facts only, not trading advice.

| Severity | Label | Category | Trigger metric | On-chain fact |
|:-:|---|---|---|---|
| 🔴 **STRONG** | `A3` Mint / bridge / mining supply source | A Chip preparation | `mint_authorities=10, mint_pct_supply_max=40.0, mint_pct_supply_sum=98.8` | 10 mint-authority contracts present (cumulative mint = 98.8% of circulating supply), an ongoing supply source — future mint → dump is possible |
| 🔴 **STRONG** | `B1` Wash-trade volume inflation (24h vol untrustworthy) | B Volume fabrication | `wash_swap_count=2524236, wash_top_bot_share=0.152, wash_n_dex_addrs=200` | 2,524,236 on-chain matches in 24h across 200 on-chain trading addresses, a single wash bot accounting for 15.2% — the 24h volume contains heavy wash trading and does not equal real absorption |
| 🔴 **STRONG** | `C1` On-chain confirmed outflow (CEX deposit + DEX swap) | C Dump behavior | `net_sellout_usd=48215531.0, sell_pct_circ=22.727` | On-chain confirmed outflow $48,215,531 (22.73% of circulating) — real insider realization observed via CEX deposit + on-chain match paths |
| 🔴 **STRONG** | `C2` Historical high-frequency operator liquidation | C Dump behavior | `ht_operator_count=100, ht_throughput_pct_supply=151.25` | 100 high-frequency operator wallets (cumulative **throughput** = 151% of total supply; throughput = token in/out flow, NOT sell volume) — already exited historically, balance near 0 |
| 🟠 **MEDIUM** | `B2` Fake depth (LP/mcap mismatch or high vol/LP) | B Volume fabrication | `vol_lp_ratio=10.68, lp_mcap_ratio=0.0044, lp_usd=3219177.782437822` | Volume/liquidity ratio = 10.7× / liquidity/mcap ratio = 0.0044 — surface liquidity is low and a single trade has large price impact |

> **Behaviour profile is not the verdict**: the 🎯 on-chain state label above is a composite of 5 tiers (No significant trigger / Watching / Distributed and exited / Dormant insider / Recent distribution); the behaviour profile here is the finer-grained 10-class on-chain detection signals. A token can be "Recent distribution" while also hitting multiple labels like A1+A2+A3+B1+C2+C3.


## 🔴 Confirmed sell-out (insider lower bound)

### 🎯 Pump counterparty check

> **⚡ Quick read**: circulating 192.1M tokens · **non-operator sell-pressure 4.1%** (7,900,695 tokens = verifiable within top 100 holders 4.1%) · operator ammo 78.8% (⚠️ Alpha API reports 288M circulating, on-chain dumpable 192M = 0.67x, Alpha overstates (includes mint authority / vesting lockup)) · exchange transit pool (retail vs project custody indistinguishable) 17.1% (7 exchange wallets) · insider confirmed realization $48,215,531 (22.7% of circulating).

> When the operator wants to pump, **the potential sellers = the held chips that don't belong to the operator**. The smaller this is, the more confident the operator is to pump (less fear of being dumped on); the larger, the more cautious.

| Chip bucket | Tokens | % of current circulating | Interpretation |
|---|---:|---:|---|
| 🟣 **Operator / project-controlled chips** | **151,362,188** | **78.8%** | **High control** — low theoretical pump resistance, but also strong active-distribution capacity |
| 🔥 **Verifiable non-operator sell-pressure** | **7,900,695** | **4.1%** | **Very light external counterparty** — low risk of being dumped on during a pump (includes retail whales + protocol contracts + bridge transit) |
| 🟦 **Exchange transit pool (neutral, indistinguishable)** | **32,863,454** | **17.1%** | 7 exchange hot/cold/deposit wallets. On-chain it is **impossible to distinguish** retail deposit aggregation vs project custody reserve. During a pump it may flow out from either side |

### Key judgment

**High control + light external counterparty** — the operator has active-distribution capacity and low pump resistance, but the distribution pace determines the one-sided move.
**Raw bucket total 701% (expand for detail)** — wallet-level overlap across buckets is a debug caveat and does not affect the quick-read 78.8% operator-ammo conclusion.

<details>
<summary>🔍 Expand: operator-ammo 11-sub-bucket detail (with raw total + overlap note)</summary>

| Sub-bucket | Tokens | % of circulating | Note |
|---|---:|---:|---|
| ①a Public lockup / treasury / airdrop contract outside m6 lineage | 0 | 0.0% | Sablier / Hedgey / custom lockups. Public release schedule, **won't dump immediately during a pump**. Lower bound after subtracting the 711,983,334 unminted reserve |
| ①b Movable multisig outside m6 lineage | 0 | 0.0% | Gnosis Safe Proxy etc. The operator can transfer today with one signature |
| ② m6 lineage portion in circulation | 0 | 0.0% | m6 lineage total holdings -18,511,897 minus lockup 0. Includes pure insiders (-18,511,897) |
| ⚠️ ③ Exchange-withdrawal distribution (net control not computable) | — | — | Gross inflow; phase-2 SQL truncated; net fan-out cannot be computed.  |
| ④ DEX pool token-side holdings | 398,602 | 0.2% | DEX pools are 99% provided by the project / market maker |
| ⑤ Other detector hits | 833,296 | 0.4% | 34 wallets — flow operators / cross-token whales / high-throughput exit operators |
| ⑥ Mint-contract unreleased reserve | 711,983,334 | 370.6% | Mining / bridge mint contract current balance; operator-controlled unreleased supply |
| ⑥' Minted to operator cluster (net holdings) | 275,330,952 | 143.3% | Cumulative mint - contract reserve - realized = still in the fake-mining cluster |
| ⑥'' Heuristic hidden ammo (top-100 unclassified ≥ 3%) | 357,996,717 | 186.3% | 6 wallets. **The 3% threshold risks false positives** — cross-check via monitoring_paste |
| 📌 Unminted operator-controlled reserve | 711,983,334 | _71.2% of total supply_ | **Not in the circulating denominator — but operator-controlled**. Adds sell-pressure once lockup / mint cadence releases it into circulation |
| ━━━━━ | ━━━━━ | ━━━━━ | ━━━━━ |
| Operator ammo raw total | 1,346,542,901 | 700.9% | ⚠️ > 100% = wallet-level overlap across sub-buckets (an in-m6 multisig counted in both ①b + ②). The quick-read 78.8% is a strictly de-duplicated wallet-level back-calculation |

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
| 1 | [`0x384c7472cd6b`](https://bscscan.com/address/0x384c7472cd6bb2767a86705e636ba0234ab095a0) | 7,900,695 | 4.11% | Unclassified | — |
| ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━━━━━━━━━ | ━━━━━━━━━ | ━━━━━━━ | ━━━━━━━━━ | ━━━━━━━━━ |
| **Total verifiable non-operator sell-pressure (within top 100 holders)** | 1 wallets | **7,900,695** | **4.1%** | — | — |

> ⚠️ **Nature of non-operator sell-pressure**: mainly true retail whales + protocol contracts like Wormhole / veVELVET (user-deposited) + bridge transit. Large bare addresses (no Arkham label + > 1% circulating) are suspect as either operator aliases or true retail whales — cross-check wallet activity via monitoring_paste below.

---

| Item | Value |
|---|---|
| Tracked wallets | **137** (127 standard insiders + **10 mint authorities**; mining / bridge token, no pre-launch m6 lineage) |
| **Pure insider current holdings (the true dormant sell-pressure the verdict references)** | **69.3471% of supply** (693,471,437 tokens, **excluding** vesting / multisig / treasury / CEX custody / DEX routing; includes mint-authority contract current balance) · 🌉 mint authority still sits on 711,983,334 tokens (can keep mint→dumping at any time) |
| Insider-tree current holdings (incl. lockup, conservation anchor) | 69.3471% of supply (693,471,437 tokens, in mining mode the tree = standard insiders + mining-fed set + mint-authority contracts (no vesting/lockup separation)) |
| (a) Confirmed sell-out — CEX deposit | 50,216,749 → Gate, Binance Wallet, Gate Deposit, Cold Wallet |
> _💡 Note: off-chain CEX withdrawals (CEX → wallet) are not in row (a) — (a) only tracks on-chain wallet → CEX deposits. A project that withdraws from a CEX first and then dumps (e.g. the H case Eleve described) does so off-chain and cannot be on-chain-detected; any subsequent on-chain transfer that dumps via a DEX router is already captured in row (b)._
| (b) Confirmed sell-out — DEX swap (own wallet) | 15,240,278 (216,951 swaps all via DEX router) |
| **Confirmed gross sell-out, a+b** | **≥ 65,457,028 = 22.7% of circulating**, USD ≈ $42,690,521 |
| **Confirmed net sell-out** | **$48,215,531** — insider **self-sell DEX TWAP** $0.7366 (rejects wash-quote contamination); DEX real ≈ $11,225,962 (on-chain SUM amount_usd, 100% provable) + CEX estimate ≈ $36,989,568 (cex_tokens × TWAP) · ⚠️ Net > Gross +13% (the apparatus traded above the wash price — not a cap breach but high-price realization) |



> **📅 Time-window split** — reconcile against short-term events (Twitter sudden-dump alerts / large moves); the relationship is **last 7d ≤ last 30d ≤ cumulative**.

| Window | Confirmed gross sell-out (tokens) | % of circulating | Confirmed net sell-out (USD) | DEX real volume (USD) | CEX route (tokens) |
|---|---:|---:|---:|---:|---:|
| **Last 7 days** | 831,427 | 0.29% | **$618,135** | $30,391 | 797,917 |
| Last 30 days | 6,297,975 | 2.19% | $5,860,689 | $3,156,237 | 3,671,542 |
| Cumulative (~364 days) | 65,457,028 | 22.73% | $48,215,531 | $11,225,962 | 50,216,749 |

> Interpretation: **last 7 days** shows current heat (reconcile directly with EmberCN-style sudden alarms); **last 30 days** shows the month's pace; **cumulative** = everything within the surf query window. A single-day burst may not show in the 7d average but is already in the cumulative. CEX route = tokens that went into exchange deposit/hot wallets (sold off-chain on the CEX side, not at the wash price).


> 🕵️ **Hidden operator ammo has shown realization activity**: the tracked **27 hidden-ammo wallets** (heuristic catches / fake-mining mint cluster) have, via (a) deposits to exchange deposit addresses of **685,714 tokens** (1 exchanges: Binance Wallet) + (b) their own on-chain matches of **0 tokens** (0 swaps), totalled **685,714 tokens** = 0.24% of circulating. **These wallets are outside the algorithm's 5 buckets** and may add on top of "confirmed gross sell-out" to view real distribution; but **you must subtract any wallet overlap with the m6 insider / mining-fed sets** (v0.8.4 backlog: add disjoint dedupe). Time window: from 2025-12-23.> ⚠️ **This token's on-chain dump is dominated by a wash bot**: 200 counterparty addresses with 2,524,236 on-chain matches total, a single wash bot doing up to 383,389 wash matches. Many insiders route tokens to relays / bots before selling (this portion is **unattributable** and not counted in the confirmed lower bound above — so real sell-out is most likely higher than the lower bound). Massive wash = dumping while inflating surface activity to lure buyers.


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

**On-chain transfer rhythm for BEAT.**



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

**Interpretation**: The token BEAT is deployed as a single-chain asset on BSC with no cross-chain bridge activity.

## Entry-price anchor (TGE)

| Time anchor | UTC | Price | vs current |
|---|---|---|---|
| LP creation first tx (DEX start) | — | — | — |
| Alpha first tx | 2025-12-23 13:00 UTC | — | — |
| **Current price** | 2026-06-24 | **$2.4200** | 1.00× |

**Interpretation**: The token was first listed on Binance Alpha on 2025-12-23 UTC. The current price is $2.5296.

<a id="section-alloc"></a>
## Project allocation power (ALLOC)

| Item | Value | Source |
|---|---|---|
| Alpha quota (officially disclosed) | **Not disclosed** | Binance Alpha API does not expose this field |
| Deployer wallet `—` current balance | Unknown | Deployer distribution trace |
| Pre-launch insider recipients 0 cumulative balance | 0 tokens (= 0.00% of supply) | Insider wallet sum |
| Quiet wallets 0 holding (core future risk) | **0 tokens (= 0.00% of supply / $0)** | Insiders that never distributed |
| Fully-distributed insiders 0 (distribution complete) | 100% distributed, 0 remaining | Insiders with ≥95% distributed |
| **Burned (permanently out of circulation)** | **13,897,092 tokens (= 1.39% total supply / $33,630,962)** | 0x...dead / 0x...0 burn-address balance (burned at deploy, never circulating) |

**Interpretation**: No verified early insider distributions were detected on-chain, indicating supply remains inside reserve clusters.

## Near-term CEX catalyst (CEX-TRACE)

| Exchange | Status | Time | Since |
|---|---|---|---|
| Binance | Listed | 2025-11-12 | ~7 months ago |
| Aster | Unverified | — | — |
| Bitget | Unverified | — | — |

No new catalyst within 14 days. Current S2 (Alpha + Binance Perps).

**Interpretation**: The token is currently listed on Binance with perps active since 2025-11-12, representing S2 classification.

<a id="section-liq"></a>
## Entry ceiling (LIQ)

| Anchor | Value | Note |
|---|---|---|
| **Max single buy under 5% slippage (estimated)** | $17,899 | Derived from Alpha 24h vol (vol_24h / 96 × 0.05 heuristic estimate) |
| DEX main pool liquidity | $15,837 | surf 0x5760ebda… |
| DEX main pool 24h volume | $67,411,523 | surf project-detail (cross-chain CEX+DEX realtime aggregation) |
| Pool token 24h net throughput (NOT LP add/remove) | — | surf agent.bsc_transfers |
| DEX main pool address | `0x5760ebda06cd880dc01aa108c57e820ec1205a39` | FDV $2,549,143,312 |

**Interpretation**: DEX liquidity is $15,836.53 but estimated 5% depth is extremely low at $17899, limiting trade sizing.

<a id="section-holdings"></a>
## Holdings distribution by role

**Distribution table**:

| Role | Wallet # | Current balance | % of supply | Top wallet |
|---|---|---|---|---|
| DEX main pool | 0 | 0 | —% | — |
| Deployer wallet | 0 | 0 | —% | — |
| Project / infra / distribution pool (vesting / multisig / treasury / DEX infra / CEX custody / 3rd-party distribution platform / retail claim pool, Arkham-verified) | 3 | 130,777,273 | 13.0777% | [`0xc6ff829c…`](https://bscscan.com/address/0xc6ff829cde48848b02c19b3af54b1de73c40a669) |
| Quiet wallet (insider, never distributed) | 0 | 0 | —% | — |
| Other (retail + unclassified) | 46 | 813,897,805 | 81.3898% | [`0x75552f8f…`](https://bscscan.com/address/0x75552f8f6785946172527cbfef84a08086a4ede7) |

**Key takeaways**:
- Insider tracking: **137** wallets hold **-1.9%** of supply cumulatively, incl. 10 mint authorities  (mining / bridge token, no pre-launch m6 lineage).
- Insiders have on-chain-confirmed outflow of **48.2M USD** = **22.73%** of circulating, priced at the insider self-sell TWAP (not the wash quote).

<details>
<summary>📂 <strong>Backward trace (Deployer → insider lineage)</strong> — 0 insider wallets: 0 fully distributed / 0 distributing / 0 quiet (click to expand the full lineage + wallet balances + distribution rate)</summary>

**Insider wallet list (deployer distribution trace)**:

| ID | Address | Received from deployer | Current balance | Dumped % |
|---|---|---|---|---|
_Stats (full m6 lineage, **0** wallets): 0 near-zero holdings / public-lockup custody · 0 distributing · 0 fully distributed_

**m4_notes (pre-LP allocation interpretation)**:
- The pre-launch phase for BEAT shows no early wallet deployments or allocations.
- No pre-launch OTC seeding was detected on BSC for BEAT, which means there are zero verified early insider recipients.
- Without any pre-launch deployment trace, the initial allocation remains highly concentrated in the creator/unlabeled reserves.



</details>

## 💰 High-Value Address Funding Source (mint / DEX / P2P)

Below are the high-value addresses already surfaced by the wash setup / flow operator / m6 insider / Top-30 holder sections, classified by how they ACQUIRED their tokens over the past 365 days: mint (received directly from 0x0 — covers mining contracts, bridge mint authorities, airdrop mint contracts), DEX buy (received from a known DEX main pool), or P2P (any other EOA transfer, including unidentified CEX withdrawals). Use this to distinguish: ⛏️ high mint% = mining-token operator or sockpuppet airdrop farmer; 🟢 high DEX% = real retail buyer; 🔵 high P2P% = operator aggregation hub or OTC recipient.

> Queried 200 high-value addresses; 8 have real incoming activity in the past 365 days — ⛏️ Mint-fed 0 / 🟢 DEX-fed 4 / 🔵 P2P-fed 4.


| Address | Primary Source | Total Received | Mint % | DEX buy % | P2P % |
|---|---|---:|---:|---:|---:|
| [`0x9999b0cd…`](https://bscscan.com/address/0x9999b0cdd35d7f3b281ba02efc0d228486940515) | 🟢 DEX-buy-fed | 114,981,830 | 0.0% | 92.0% | 8.0% |
| [`0x12d2b8ac…`](https://bscscan.com/address/0x12d2b8ac38c59758a062a9f757f2740461779439) | 🟢 DEX-buy-fed | 1,726,298 | 0.0% | 60.5% | 39.5% |
| [`0x63186b34…`](https://bscscan.com/address/0x63186b34c809cca9f3825a3592082e1f1549fa5b) | 🔵 P2P-fed | 1,694,807 | 0.0% | 31.2% | 68.8% |
| [`0xfea18be5…`](https://bscscan.com/address/0xfea18be59b326917572fbb999410749b22f335bf) | 🔵 P2P-fed | 1,645,572 | 0.0% | 0.0% | 100.0% |
| [`0x28aee52c…`](https://bscscan.com/address/0x28aee52c2dfd391fb5028615c930a9a7b43ca19b) | 🔵 P2P-fed | 858,570 | 0.0% | 0.0% | 100.0% |
| [`0xda9442b6…`](https://bscscan.com/address/0xda9442b6871f74d1af4af85ee940602f547453f3) | 🔵 P2P-fed | 216,864 | 0.0% | 0.0% | 100.0% |
| [`0xe2228e89…`](https://bscscan.com/address/0xe2228e892aae78fffd5f27d158074e888b72b5b9) | 🟢 DEX-buy-fed | 13 | 0.0% | 100.0% | 0.0% |
| [`0xfeed0014…`](https://bscscan.com/address/0xfeed001448bed378402ed4b73c2a4ce98ffd0ba9) | 🟢 DEX-buy-fed | 4 | 0.0% | 100.0% | 0.0% |

> _Scan cap: the pipeline collected 230 high-value candidates, max_addrs cap = 200, actually queried 200 (ordered by detector priority: wash → flow → m6 → dump-sellers → Top-30 holders). Truncated 30 — common on PLAY-class tokens with many (60+) flow_operators._

> _The CEX-withdrawal column is not yet separately identified (a v0.7.24 candidate) and is currently grouped under P2P. When a real CEX hot-wallet transfer cannot be distinguished from a plain EOA transfer, both count as P2P._



<a id="section-bridge-mint"></a>
### 🌉 Bridge / mint-authority self-sell detail (v0.7.24a)

> Detected **10 mint-authority contracts** (receive mint from 0x0, excluding the deployer + wallets already covered in the mining-fed section). They are bridge / staking / airdrop contracts that may **themselves** DEX swap. This is a dump path the v0.7.23.x series missed entirely.

| Authority address | Arkham label | 365d Mint amount | % of supply | Own DEX sell | USD ≈ |
|---|---|---:|---:|---|---:|
| [`0x75552f8f6785…`](https://bscscan.com/address/0x75552f8f6785946172527cbfef84a08086a4ede7) | _Unlabeled (new contract, not in Arkham) | 400,000,000 | 40.00% | — (no direct DEX self-sell) | — |
| [`0x1830834fe374…`](https://bscscan.com/address/0x1830834fe3742b7e0988968dd50f321250157561) | _Unlabeled (new contract, not in Arkham) | 150,000,000 | 15.00% | — (no direct DEX self-sell) | — |
| [`0x8c84616281bb…`](https://bscscan.com/address/0x8c84616281bb4686600090a1aad58543a0e11be1) | _Unlabeled (new contract, not in Arkham) | 100,000,000 | 10.00% | — (no direct DEX self-sell) | — |
| [`0x05b7721d66e8…`](https://bscscan.com/address/0x05b7721d66e83f8fb236d2ace995f710fd59e718) | _Unlabeled (new contract, not in Arkham) | 80,000,000 | 8.00% | — (no direct DEX self-sell) | — |
| [`0x34d5d4c15ff9…`](https://bscscan.com/address/0x34d5d4c15ff9a1417411787c1eb26f4c3c35149f) | _Unlabeled (new contract, not in Arkham) | 74,000,000 | 7.40% | — (no direct DEX self-sell) | — |
| [`0xcaf2023e3721…`](https://bscscan.com/address/0xcaf2023e372169b89318888f3c6fecea7197c891) | _Unlabeled (new contract, not in Arkham) | 68,000,000 | 6.80% | — (no direct DEX self-sell) | — |
| [`0x0793b14b0beb…`](https://bscscan.com/address/0x0793b14b0beb04caf55c5fd48e0e3e7358bf6bb2) | _Unlabeled (new contract, not in Arkham) | 60,000,000 | 6.00% | — (no direct DEX self-sell) | — |
| [`0x73237e12c419…`](https://bscscan.com/address/0x73237e12c419d582121de95e8abd2cf9ec42821a) | _Unlabeled (new contract, not in Arkham) | 36,000,000 | 3.60% | — (no direct DEX self-sell) | — |
| [`0x9a493cf4fc3f…`](https://bscscan.com/address/0x9a493cf4fc3f9effd9c148a2db5e5a2a16721eaa) | _Unlabeled (new contract, not in Arkham) | 10,000,000 | 1.00% | — (no direct DEX self-sell) | — |
| [`0x11ae7e0345d6…`](https://bscscan.com/address/0x11ae7e0345d69d370728418f357fe7fb2e53fd78) | _Unlabeled (new contract, not in Arkham) | 10,000,000 | 1.00% | — (no direct DEX self-sell) | — |





<a id="section-high-throughput"></a>
### 🌊 High-throughput dump wallets (v0.7.24b)

> Detected **100 operator wallets** with a high-throughput clear-out pattern (large token flow-through + balance ≈ 0 + high-frequency tx). Thresholds: throughput 1M ~ 5% of supply, balance < 5% of throughput, n_tx ≥ 1000. Already filtered out infra labels like DEX routers / CEX deposits / aggregators (not operators). These are operators that finished dumping and left before the 60d window — missed by flow_operators (60d window) + mining-fed (balance > threshold).

| Operator address | Primary role | Arkham label | 365d inflow (= received mint/p2p) | Outflow (= sold / transferred out) | Residual balance | tx count |
|---|---|---|---:|---:|---:|---:|
| [`0xaa86268030aa…`](https://bscscan.com/address/0xaa86268030aae432ac471f220080ba3e46b52b43) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 48,365,924 | 48,366,427 | -503 | 480,040 |
| [`0x286da9568057…`](https://bscscan.com/address/0x286da9568057420df90c5489e51cbb82b29f0301) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 47,011,729 | 47,021,080 | -9,352 | 357,055 |
| [`0x3a1008024ff1…`](https://bscscan.com/address/0x3a1008024ff1653d78170c18afbef8bf92eefa2f) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 45,871,899 | 45,879,172 | -7,273 | 111,828 |
| [`0x097fd934ce91…`](https://bscscan.com/address/0x097fd934ce9124fe6aec6dd325108b34986770d1) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 40,609,255 | 40,610,933 | -1,678 | 325,150 |
| [`0x2e8fc72e46d1…`](https://bscscan.com/address/0x2e8fc72e46d1c6584bf7c66b673c99cbfa3a882c) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 40,322,042 | 40,322,042 | 0 | 180,526 |
| [`0xd060a0193a72…`](https://bscscan.com/address/0xd060a0193a72ba809149476cec1ca865a887ec91) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 40,149,829 | 40,149,829 | 0 | 141,478 |
| [`0xa5aa69f4a9f4…`](https://bscscan.com/address/0xa5aa69f4a9f403ea32611b4da4da3f5afa985a0c) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 39,461,336 | 39,461,336 | -0 | 402,404 |
| [`0x5c9450ad619c…`](https://bscscan.com/address/0x5c9450ad619cf7e8a123c0f4af8f92044c1c66cf) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 37,516,463 | 37,516,463 | 0 | 192,508 |
| [`0x5bfc6f954cb0…`](https://bscscan.com/address/0x5bfc6f954cb05de01f2cd2847f4f948231113b1e) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 35,845,486 | 35,845,486 | 0 | 49,158 |
| [`0x53f78a071d04…`](https://bscscan.com/address/0x53f78a071d04224b8e254e243fffc6d9f2f3fa23) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 35,245,511 | 35,515,841 | -270,331 | 6,683 |
| [`0xc30ac7ab7fbb…`](https://bscscan.com/address/0xc30ac7ab7fbb2f0cb82c6d49b65df362b5ac1769) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 34,329,198 | 34,329,092 | 107 | 240,948 |
| [`0x278d858f05b9…`](https://bscscan.com/address/0x278d858f05b94576c1e6f73285886876ff6ef8d2) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 34,220,442 | 34,217,023 | 3,420 | 1,254,747 |
| [`0x031942f26a09…`](https://bscscan.com/address/0x031942f26a094be40414f442a2f1295e3a5c1680) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 32,611,295 | 32,625,526 | -14,231 | 241,039 |
| [`0x9999b0cdd35d…`](https://bscscan.com/address/0x9999b0cdd35d7f3b281ba02efc0d228486940515) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 32,354,119 | 32,354,319 | -200 | 937,884 |
| [`0xc5a1350019fa…`](https://bscscan.com/address/0xc5a1350019fabafe58cb2c3576672b6f7e1fd562) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 31,833,896 | 31,836,479 | -2,583 | 211,529 |
| [`0xbd97306a087e…`](https://bscscan.com/address/0xbd97306a087ed0c46b783cfbfdcdc6c12c7a2866) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 31,327,855 | 31,318,672 | 9,182 | 951,269 |
| [`0x238a35880837…`](https://bscscan.com/address/0x238a358808379702088667322f80ac48bad5e6c4) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 28,660,254 | 28,788,543 | -128,289 | 365,152 |
| [`0xe6123111637c…`](https://bscscan.com/address/0xe6123111637c59e662b69f83511ccc184e2ff77d) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 28,232,513 | 28,243,794 | -11,281 | 120,656 |
| [`0xe50e106e8ad8…`](https://bscscan.com/address/0xe50e106e8ad8530fbb3246e4b36f61098d9a4581) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 26,614,849 | 26,614,849 | -0 | 81,056 |
| [`0xca852767b43a…`](https://bscscan.com/address/0xca852767b43a395ac1dd54737193eba5e20c78bd) | 🌊 HT operator (primary) | _Unlabeled (EOA / not indexed) | 25,601,401 | 25,601,401 | 0 | 62,010 |

> _Showing top 20; 100 high-throughput operator wallets detected in total (sorted by throughput; throughput = token in/out flow, NOT sell volume). Full list in skeleton.json `funding_attribution.high_throughput_dumpers.dumpers`._

> 🌊 These wallets passed **1,512,472,963 tokens** through over 365d then cleared out — operators that have finished dumping. They've already sold, but **if the project mints another batch and distributes it to similar-pattern wallets in future**, they become the next dump-risk source.





<a id="section-wallet-cluster-graph"></a>
## 🌐 Wallet-graph clusters (v0.8.6.5)

> **Wallet ↔ wallet direct-transfer graph clusters** — operator clusters that bypass CEX, mint, and the m6 lineage. Bubblemaps-style algorithm: high-value transfers between candidate wallets (≥0.5% supply per edge) form connected components ≥ 3 nodes. Uses undirected 2-core pruning to exclude single-edge false positives.| Metric | Value |
|---|---|
| Clusters detected | **1** |
| Total cluster wallets | **17** |
| Candidate wallets input | 127 |
| Excluded by L1 Arkham filter | 0 |
| Total graph edges | 95 |
| Newly discovered (not master_cluster) | 0 |
| SQL chunks run | 1 |

#### 🌐 Cluster 1: 17 wallets

| Field | Value |
|---|---|
| cluster wallets | 17 |
| edge count | 27 |
| Total transfer weight | 478,788,611 tokens |
| Max edge weight | 47,011,729 tokens |
| Cluster current total holdings | 846,325 tokens |
| Arkham UNLABELED % | 100% |
| Source distribution | master_cluster: 17 |

**Cluster wallets (sorted by transfer weight)**:

| # | Recipient wallet | Current balance (tokens) |
|---:|---|---:|
| 1 | [`0x238a35880837`](https://bscscan.com/address/0x238a358808379702088667322f80ac48bad5e6c4) | 533,564 |
| 2 | [`0x286da9568057`](https://bscscan.com/address/0x286da9568057420df90c5489e51cbb82b29f0301) | -9,352 |
| 3 | [`0x2e8fc72e46d1`](https://bscscan.com/address/0x2e8fc72e46d1c6584bf7c66b673c99cbfa3a882c) | -0 |
| 4 | [`0x031942f26a09`](https://bscscan.com/address/0x031942f26a094be40414f442a2f1295e3a5c1680) | -14,231 |
| 5 | [`0x3a1008024ff1`](https://bscscan.com/address/0x3a1008024ff1653d78170c18afbef8bf92eefa2f) | -7,273 |
| 6 | [`0x5bfc6f954cb0`](https://bscscan.com/address/0x5bfc6f954cb05de01f2cd2847f4f948231113b1e) | -0 |
| 7 | [`0xe50e106e8ad8`](https://bscscan.com/address/0xe50e106e8ad8530fbb3246e4b36f61098d9a4581) | 0 |
| 8 | [`0xab02ed426457`](https://bscscan.com/address/0xab02ed42645769874738941405e6891505c009f7) | -0 |
| 9 | [`0x144d395b5562`](https://bscscan.com/address/0x144d395b5562c742259932d2ee6e1d8d092a21b8) | 2 |
| 10 | [`0x507b7c70752e`](https://bscscan.com/address/0x507b7c70752e2fa98dc5360f844fa289f6177c93) | -620 |
| 11 | [`0x452244f592ef`](https://bscscan.com/address/0x452244f592eff4cde9deaeb8907bca9b64c44947) | -0 |
| 12 | [`0x92f843555e73`](https://bscscan.com/address/0x92f843555e7394620af82ed1d717b9cb72bf1949) | 0 |
| 13 | [`0x823934c4916a`](https://bscscan.com/address/0x823934c4916a1ff5ab60a28548c90321a920e174) | -0 |
| 14 | [`0x3087b907c070`](https://bscscan.com/address/0x3087b907c07089a74047d5a841cd306466eeeae0) | -0 |
| 15 | [`0x055a3b37957b`](https://bscscan.com/address/0x055a3b37957bfbd3345bed9968e7e8dd56d67066) | -98 |
| 16 | [`0x2add4ea65c91`](https://bscscan.com/address/0x2add4ea65c917a166d8b379c80d354205c44240d) | 4 |
| 17 | [`0x4982085c9e2f`](https://bscscan.com/address/0x4982085c9e2f89f2ecb8131eca71afad896e89cb) | 344,327 |

<a id="section-monitoring"></a>
## Monitored wallets + real-time alerts


> 📊 **Monitoring priority (v0.7.27 deterministic ranker)**: 🚨 9 CRITICAL · 🔥 18 HIGH · 👀 0 NORMAL>
> Wallets in paste.json are sorted by level, 🚨 first. Prioritize CRITICAL+HIGH (27) — when these wallets move, the on-chain detection picture changes. NORMAL (0) is for bulk cross-checking, no push notification needed. 💤 NOT_TRACKED are DEX routers / public CEX hot wallets whose flow noise drowns the real signal, removed from paste.

_(the report shows only the top 10; for all 27 wallets use `monitoring/monitoring_paste.json` to one-click paste into Binance Wallet / OKX monitoring)_

| # | Level | Wallet | Role | primary role section | Trigger condition | Status |
|---|:-:|---|---|---|---|---|
| 1 | 🔥 HIGH | [`0x6f8a2e8f`](https://bscscan.com/address/0x6f8a2e8fe3dc9867ab3ff3351fc5b2ab7fe93a7e) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 2 | 🚨 CRITICAL | [`0x9a493cf4`](https://bscscan.com/address/0x9a493cf4fc3f9effd9c148a2db5e5a2a16721eaa) | Fake-mining mint-cluster member | [🌉 Bridge / mint-authority contract self-sell detail](#section-bridge-mint) | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 3 | 🔥 HIGH | [`0x56705ec6`](https://bscscan.com/address/0x56705ec68deb49f49daa6c6dee1eab4b1c9b2830) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 4 | 🔥 HIGH | [`0x3069bdd3`](https://bscscan.com/address/0x3069bdd3cb1768719aa382e9540e80162a25d684) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 5 | 🔥 HIGH | [`0xc6ff829c`](https://bscscan.com/address/0xc6ff829cde48848b02c19b3af54b1de73c40a669) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 6 | 🔥 HIGH | [`0x5b4d5dc3`](https://bscscan.com/address/0x5b4d5dc3be070fc7c3dc79338d21e71bc668deee) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 7 | 🔥 HIGH | [`0x5b2b2c70`](https://bscscan.com/address/0x5b2b2c70b9e3651f282a86a65d0c12c3cff9ca12) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 8 | 🔥 HIGH | [`0x14cf359c`](https://bscscan.com/address/0x14cf359ca3e04dec329e39d023c041b81cbd65f3) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 9 | 🔥 HIGH | [`0x051edb1b`](https://bscscan.com/address/0x051edb1b6561d3c83410d278d5980b2c10e9af63) | Fake-mining mint-cluster member | — | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |
| 10 | 🚨 CRITICAL | [`0x11ae7e03`](https://bscscan.com/address/0x11ae7e0345d69d370728418f357fe7fb2e53fd78) | Fake-mining mint-cluster member | [🌉 Bridge / mint-authority contract self-sell detail](#section-bridge-mint) | Tag type: fake-mining mint-cluster member (mint-authority contract → a few large accounts). The user can watch whether / when these three on-chain behaviours occur: (1) transferring into an exchange deposit address after receiving tokens, (2) on-chain matching, (3) splitting across downstream sub-accounts. If (1)(2) appear, combine with this report's confirmed sell-out section to estimate the actual realization of the minted allocation. | 🟡 |

Monitoring these 27 wallets helps track active operator reserves and potential sell-out actions for BEAT.

## Machine-readable JSON (compact)

```json
{
  "schema_version": "1.0.4",
  "symbol": "BEAT",
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
    "monitoring_wallets": 27,
    "lineage_flowchart_nodes": 1,
    "lineage_flowchart_edges": 0,
    "m6_rows": 0,
    "decision_anchors": 3,
    "decision_re_entry_conditions": 1
  },
  "address_role_index": {
    "0xf2a69b94d3c7f2d2c35e8f44a94b42e5bf486ed8": {
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
    "0x77519fa2324078e75b43c1bf2f8681069100c6c0": {
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
    "0x9b1aeab10ba1bccd7ec6a4416771a815f65412e1": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x73237e12c419d582121de95e8abd2cf9ec42821a": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x9021069ce6842ac73d824941f841810e7d73f4c5": {
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
    "0x73b96044b171ef12107283ad082e85de64593a56": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x9bbab50219e5ab3fb66c5561d64b6ddd518ae24f": {
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
    "0x3087b907c07089a74047d5a841cd306466eeeae0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xbc0be9e090224983eb9bff63eb9504dd55994e17": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x144d395b5562c742259932d2ee6e1d8d092a21b8": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2e8fc72e46d1c6584bf7c66b673c99cbfa3a882c": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x7caef3b35af09aa8a8eda9cd48a936d507ca97b1": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x3a1008024ff1653d78170c18afbef8bf92eefa2f": {
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
    "0x7aac35c41fa2508dc0cb6246c2a5141a15e4a5f6": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x92f843555e7394620af82ed1d717b9cb72bf1949": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6984e749baf0faf6a2f6bffd940806abb495cb1c": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4cc9bd8b985e7a98cac939113081b2801b644066": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x9a493cf4fc3f9effd9c148a2db5e5a2a16721eaa": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x1b5be83a2101b93d206faf09cc67a6aba754eb7a": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x75552f8f6785946172527cbfef84a08086a4ede7": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0xbeb2c2171e3d9086aca86c785a69bb5bfdd5c5a5": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x8c48143d1d589c39b0a7fe1a305c0ba1a7cf58f8": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe50e106e8ad8530fbb3246e4b36f61098d9a4581": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe5f1395efce39a2ac238b63f79dbc5d524c85dcc": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xb61825e2d098711fd3a31c894ab6ee2bb95f8eff": {
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
    "0x452244f592eff4cde9deaeb8907bca9b64c44947": {
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
    "0xe0881cc50de6a472cd340111e80d70b79d807ac1": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe6451016f095835a0d5ef98a5c0092e47ddf0a93": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x32631223a3b8f7bb28dc3c067d5f880902730dfa": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x0127f38424f01a1ad13d16a377ef8fc1a97cc58b": {
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
    "0x055a3b37957bfbd3345bed9968e7e8dd56d67066": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x33c37cd8b78c521d21b17db4d52a016e963c0e41": {
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
    "0xcaf2023e372169b89318888f3c6fecea7197c891": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x507b7c70752e2fa98dc5360f844fa289f6177c93": {
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
    "0x3b4945745608768f37de52f39874cb48ddfed762": {
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
    "0xb85b098448b2aac4af96f5bdd9c6c02373a08975": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xf6aef9c57491019fbc94e2caeb3fd98d8152dd5d": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4a4915a02ebfd6e05132ff9f622646d157b719bb": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x1830834fe3742b7e0988968dd50f321250157561": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0xa5aa69f4a9f403ea32611b4da4da3f5afa985a0c": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x24a0d9928a3b6cd13a6210d0ff6d450a080fc266": {
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
    "0x5c9450ad619cf7e8a123c0f4af8f92044c1c66cf": {
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
    "0x238a358808379702088667322f80ac48bad5e6c4": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x3156020dff8d99af1ddc523ebdfb1ad2018554a0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xc30ac7ab7fbb2f0cb82c6d49b65df362b5ac1769": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x05b7721d66e83f8fb236d2ace995f710fd59e718": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0xd5da17a84314194e348649c89a65143a061f7190": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x1567faa2e8643f6bfde1790e36aa6b0c3a9b156f": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xc83e1167989f3bb499fb78b8e121b979ca8d0f44": {
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
    "0xb9d374d544fd7da42b102e1e0293b56ab2199d7c": {
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
    "0x5bfc6f954cb05de01f2cd2847f4f948231113b1e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6ec512ccdf675364a27e6117d413bb71eeaaf098": {
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
    "0x60b97709d633dd4e0f0f44f6102fd50341c0afa6": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x561a3a8f7c97b66248c8a343a2649301740ce7c5": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x71d98d3db374f2b865eb7da5f85d0079ea2f78f0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4982085c9e2f89f2ecb8131eca71afad896e89cb": {
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
    "0x11ae7e0345d69d370728418f357fe7fb2e53fd78": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x9999b0cdd35d7f3b281ba02efc0d228486940515": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x8d17fbfb03a6b7e8fdcfd60f1f9e6c08578ba5d7": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x4efe47293d511c5b343134b7ffb000a638ea4fe0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x34d5d4c15ff9a1417411787c1eb26f4c3c35149f": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x0793b14b0beb04caf55c5fd48e0e3e7358bf6bb2": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x75f838dbf3be0a79d6e5904ab5c364d5418a5f66": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2b6fe32c240ef9f54d93d8febab3d8303e1d9f86": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xab02ed42645769874738941405e6891505c009f7": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x823934c4916a1ff5ab60a28548c90321a920e174": {
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
    "0x8f6fbb791a1920a236c5be0184ddcc942dcbe611": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xcc6f6216d8fe4d17758a2bc436e01386a710e89e": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x6f3817ec9329ffe10081d86edf9350b02e8515b0": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2add4ea65c917a166d8b379c80d354205c44240d": {
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
    "0x1231deb6f5749ef6ce6943a275a1d3e7486f4eae": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x155cfd8dc72d83ee8fab0748c181e19a5ef4662e": {
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
    "0x0b79102476747751b82d551dfc43d06ff74bb000": {
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
    "0xcf12035273f337f744c320b221a837d77ca6dff3": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xca852767b43a395ac1dd54737193eba5e20c78bd": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xfd650452002e818956489c76fdf57fe6c6e48d6b": {
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
    "0x134247cef23dec6080d97ec50df7a9632fe67ce1": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x5b5a202fa3e9a21eaf9a0d6f02b54a002ccbda02": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2671702729a934538589dc818f212a7f53d03db3": {
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
    "0x8c84616281bb4686600090a1aad58543a0e11be1": {
      "primary_role": "mint_authority",
      "all_roles": \[
        "mint_authority"
      \],
      "primary_section_anchor": "section-bridge-mint"
    },
    "0x4b1b2ea60cc20a171cb7eed8fe0de988f79651d2": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xad689857b97723b2f16c92e0336e06cc0e115262": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x9e229b12cc9081d6a510b29ccbd6311743e277ed": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0x2480faeb931272cd1f7375d8f4c104a4db5fff63": {
      "primary_role": "high_throughput_operator",
      "all_roles": \[
        "high_throughput_operator"
      \],
      "primary_section_anchor": "section-high-throughput"
    },
    "0xe6123111637c59e662b69f83511ccc184e2ff77d": {
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
    "0x2ad99fcfe69248561bf5f0eb788af5217afaaa29": {
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
