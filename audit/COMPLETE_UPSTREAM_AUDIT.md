# First Proof Batch 2 — Complete Repository Audit

**Audit date:** 2026-08-09  
**Audited archive:** `batch-2-main.zip`  
**Archive SHA-256:** `bd4268a439c69ab2121d6a94867ea7211f4e264809201582f4ffe83667900ac9`  
**Archive size:** 435,679,876 bytes  
**ZIP entries:** 7,767  
**Uncompressed payload:** 767,856,206 bytes

This audit was performed **after** the ten local ATTICUS-vs-Sol trials and their scores were locked. It was therefore not used by either solver condition during generation.

## Executive findings

1. The repository is internally coherent and contains benchmark design files, human solutions, standardized AI solutions, raw model/harness outputs, detailed human reviews, three submitter source trees, and a separate model-testing harness.
2. The official Batch 2 protocol is **not closed-book**. It permits outbound HTTPS/public web search and requires detailed logging. Official results therefore measure agentic research systems under retrieval/tooling and large compute budgets, not one-shot parametric reasoning.
3. The de-anonymized solution letters map unambiguously by raw-content matching: **A = IMProofBench, B = UCLA, C = OpenAI direct, D = Princeton**.
4. Human full/publishable solutions cluster strongly on P1, P2, P6, P7, and P9. P3 has publishable partial progress but the exact characterization remains open. P4, P5, P8, and P10 expose substantial proof-completion/verification failures.
5. Self-verification quality differs sharply across harnesses. UCLA was conservative; Princeton had multiple false-positive “solved” signals; IMProofBench had two major-gap false positives among its positive solve signals; OpenAI direct was explicitly prompted to keep working until a complete proof was achieved and presented several major-gap arguments as complete.
6. The local blind P01–P10 scores were left unchanged. The repository audit strongly supports the qualitative gap diagnoses, particularly on P03, P05, P08, and P10.
7. **Training-data contamination remains unresolved.** No-retrieval local testing prevents live lookup but cannot prove the public benchmark was absent from model pretraining.
8. Archive hygiene was good in the performed checks: CRC verification passed; no traversal paths, absolute paths, ZIP symlinks, or obvious committed private/API-key patterns were found in the targeted scan.

## Scope and evidence hierarchy

The audit covered ZIP integrity/path safety, repository inventory, benchmark protocol, human solutions/referee reports, raw outputs for all four submitters, available source/configuration trees, token/cost/runtime records, internal solve/verification signals, standardization fidelity, and comparison against the locked local grading.

For forensic claims the preferred evidence order was:

1. raw outputs/logs;
2. run metadata/source configuration;
3. human reviewer source and human solutions;
4. standardized AI-solution files for presentation/content matching.

The distinction matters because the standardized AI-solution files are described upstream as standardized rather than verbatim model transcripts.

## Archive integrity and hygiene

- ZIP CRC test: **pass**.
- Entries: **7,767**.
- Compressed member payload: **432,756,938 bytes**.
- Uncompressed payload: **767,856,206 bytes**.
- Path traversal entries: **0**.
- Absolute-path entries: **0**.
- ZIP symlink entries: **0**.
- Targeted common-secret-pattern hits: **0**.
- Unique content SHA-256 values: **4,486**.
- Duplicate-hash groups: **952**.

The secret scan was targeted, not a formal proof that no credential appears anywhere.

## Repository inventory

| Area | Entries | Files | Uncompressed bytes | Purpose |
|---|---:|---:|---:|---|
| `batch-2-raw-outputs` | 7,031 | 6,577 | 714,135,888 | model/harness outputs, logs, papers, verification artifacts |
| `batch-2-submissions` | 344 | 288 | 6,061,988 | source/configs for submitted harnesses |
| `batch-2-reviews` | 232 | 182 | 37,691,417 | referee reports and combined PDFs |
| `batch-2-AI-solutions` | 92 | 81 | 7,348,440 | standardized A–D solutions |
| `batch-2-human-solution` | 34 | 23 | 2,577,289 | human/reference solutions |
| `batch-2-design` | 21 | 14 | 31,656 | protocol/runner/common input |
| `batch-2-modeltesting` | 11 | 8 | 9,460 | separate simple OpenAI model-test harness |

Raw-output file counts:
- OpenAI direct: 22 files / 4,193,712 bytes.
- UCLA: 596 / 246,543,281 bytes.
- Princeton: 535 / 163,221,880 bytes.
- IMProofBench: 5,423 / 300,164,445 bytes.

## Protocol finding: retrieval was allowed

The official design permits outbound HTTPS, including LLM APIs, unauthenticated public websites, and web search. Submitters were expected to provide comprehensive logs of model input/output, intermediate reasoning/thinking, and significant state transitions. Runs generally had a 24-hour wall-clock cap unless an approved override applied.

Therefore the official systems are best treated as **research-agent systems**. Their human pass counts are useful context for problem difficulty but are not apples-to-apples controls for the local one-shot/no-retrieval experiment.

## Identity reconstruction and standardization fidelity

The referenced anonymized hash table is absent from the supplied ZIP, but the institutional mapping is independently recoverable from raw content:

| Submission | Raw submitter | Mean raw 8-token-shingle containment |
|---|---|---:|
| A | IMProofBench | 99.54% over 9 substantive outputs; P06 empty |
| B | UCLA | 99.44% |
| C | OpenAI direct | 98.62% |
| D | Princeton | 98.07% |

Wrong cross-mappings had only very low overlap. The per-problem figures are versioned in `standardization_fidelity.csv`.

## Reproducibility/provenance gaps

Present in the archive:
- UCLA source tree/configuration;
- Princeton source tree/configuration;
- IMProofBench source tree/configuration;
- recorded source commit IDs for those three.

Limits:
- no `batch-2-submissions/openai/` source tree and no OpenAI run-metadata JSON were present;
- the ZIP contains no `.git` history, so recorded commit IDs cannot be authenticated solely from the archive;
- the anonymized-solution hash table referenced upstream is missing;
- Princeton token accounting differs materially between `solutions.json` and the complete raw token log.

Princeton discrepancy: `solutions.json` reports **94,457,462** total tokens while the 4,726-record raw token log sums to **115,284,209**, a difference of **20,826,747** (~22.1% of the smaller number). Different accounting/snapshot scope is a plausible explanation, but the archive does not contain one explicit reconciliation.

## Resource-use audit

| System | Main configuration | Calls | Total tokens | Recorded cost | Runtime/elapsed |
|---|---|---:|---:|---:|---:|
| IMProofBench | mixed GPT-5.5 Pro / Claude Opus 4.7 / Gemini 3.1 Pro, author-critic multi-round | 491 | 308,157,035 | $3,185.64 | 82,502 s |
| UCLA | GPT-5.5 Pro xhigh, literature search + advisor/solver + verifier/refiner | 992 | 59,553,109 | $4,799.20 | 83,188 s |
| OpenAI direct | `openai/gpt-5.5-pro-20260423`, direct research prompt + built-in web search | 10 | 1,513,119 | $116.60 | ~20,832 s recorded |
| Princeton | Gemini 3.1 Pro Preview, multi-agent W=9 D=6 + graders/literature verification | 4,726 raw token records | 115,284,209 raw-log total | not normalized | 27,948 s |

OpenAI direct recorded **144 built-in web searches**. Its prompt also told the system to work very hard and **not return until a complete proof was achieved**, an anti-calibration pressure relevant to interpreting false-complete behavior.

UCLA and IMProofBench contained extensive literature/retrieval artifacts. Princeton's top-level solver metadata can say `search=false`, but its overall raw output includes substantial librarian/fetch-and-distill/PDF material; this must not be read as “no external retrieval occurred.”

The detailed table is in `resource_usage.csv`.

## Human-review consensus

The machine-readable 40-cell table is in `review_consensus.csv`. Aggregate pattern:

- **P1:** A/B/C pass; D reject.
- **P2:** A/B/C pass; D reject.
- **P3:** A publishable partial; B/C/D reject.
- **P4:** A major-revision/partial; B/C/D reject.
- **P5:** A pass; B/C/D reject.
- **P6:** A empty; B/C pass; D reject.
- **P7:** all four pass.
- **P8:** A/B major; C/D reject.
- **P9:** A/B/C pass; D reject.
- **P10:** A/C major; B/D reject.

This makes P3/P4/P5/P8/P10 especially useful as calibration/proof-gap stress tests.

## Verification/calibration audit

The full per-problem signal table is in `self_verification.csv`.

Descriptively:
- UCLA's strongest “verified and not a relaxation” signals aligned well with human acceptance in this batch, with P02 appearing as a conservative false negative.
- IMProofBench declared seven problems solved; five became full human passes, while P8/P10 retained major gaps.
- Princeton declared four solved; only P7 received full human acceptance among those four.
- OpenAI direct was structurally pressured to output complete proofs; human review accepted P1/P2/P6/P7/P9 and rejected or marked major the others.

These results show why **self-certification is not a substitute for external proof review**.

## Problem-level cross-check of the local experiment

The audit was conducted after local scores were locked. After final unblinding, Sample A was ATTICUS and Sample B was raw Sol.

| P | ATTICUS / Sol | Local judgment | Audit effect |
|---|---|---|---|
| P01 | 97 / 94 | both complete | supported; three official full passes |
| P02 | 86 / 98 | raw stronger; ATTICUS construction gap | supported; complete construction details separate passes from gaps |
| P03 | 89 / 88 | both incomplete, calibrated | strongly supported; exact classification remains open in reference material |
| P04 | 87 / 82 | both incomplete | supported; no official full pass |
| P05 | 91 / 94 | both incomplete at singular-invariant obstruction | strongly supported; human route needs deeper coupling/ASF machinery |
| P06 | 99 / 90 | ATTICUS complete; raw incomplete | strongly supported by complete rooted/capacity-style branch arguments upstream |
| P07 | 99 / 98 | both complete | strongly supported; all official submissions passed |
| P08 | 79 / 85 | both false-complete; modular-duality theorem gap | strongly supported; official reviews identify same failure class |
| P09 | 98 / 76 | ATTICUS complete; raw formula right but derivation omitted | supported; correct hook formulas require the missing bridge |
| P10 | 79 / 68 | both false-complete; central proper-proximality machinery unsupported | strongly supported; human proof needs nontrivial relative-boundary machinery |

**No locked numeric score was changed after unblinding or repository audit.**

## Cross-system difficulty pattern

OpenAI direct and UCLA both received full human acceptance on **P1, P2, P6, P7, P9**. The strongest local solutions also cluster around those problems. P3/P4/P5/P8/P10 more often expose the difference between a plausible architecture and a fully discharged proof obligation.

This is descriptive evidence, not a universal hardness ordering.

## Contamination and benchmark comparability

Official retrieval was extensive, whereas the local A/B experiment was one-shot with retrieval disabled. They are different experimental conditions.

Because Batch 2 was public before the August 2026 local GPT-5.6 tests, prior training exposure cannot be excluded. Conceptual overlap with human/official solutions does not itself prove memorization because many of the constructions are mathematically natural and independently recur across systems.

**Status: CONTAMINATION RISK — UNRESOLVED.**

A stronger future design would use private/newly authored problems or delayed-release holdouts that could not plausibly have entered training.

## Difficult-problem forensic observations

### P03 — calibration stress test
The reference material itself leaves the small-p classification unresolved beyond partial theorems. A system can derive correct special cases and exclusions while hallucinating a universal sufficiency theorem. The local conditions correctly stopped; some official systems did not.

### P05 — singular invariant-measure gap
Constructing the natural Gibbs invariant measure is not enough to prove uniqueness against arbitrary singular invariant measures. The human route requires further smoothing/coupling machinery. This matches the local diagnosis.

### P08 — right construction, hard theorem hidden inside
The polarity/flat-duality construction is the natural object. Proving preservation of valuated Plücker/incidence relations is the theorem-sized obligation. Several systems find the architecture and then compress the hard part.

### P10 — theorem provenance/definition stress test
The correct proof requires domain-specific relative proper-proximality machinery and a nontrivial boundary-piece intersection/upgrade. Superficially plausible shortcuts can conceal an unsupported theorem. This was visible in both local outputs and official referee reports.

## What this repo does and does not support

The upstream repository supports a narrower claim than “one raw AI solved ten impossible problems.” It demonstrates that sophisticated AI research systems can produce publishable mathematics on several genuinely research-level problems, often with retrieval, multi-agent iteration, verification, code, and large token budgets. Human refereeing remains important because polished false-complete arguments occur.

## Audit limitations

1. The audit was primarily archive-derived; it did not rely on outside claims to fill missing files.
2. Git history is absent from the ZIP.
3. OpenAI direct runner/source metadata is incomplete relative to the other submitters.
4. Human-review consensus is a categorical synthesis, not a calibrated scalar score.
5. Token/reasoning accounting is not perfectly comparable across providers.
6. Costs are not apples-to-apples because models, tools, parallelism, retrieval, and stopping rules differ.
7. Training contamination of the later local GPT-5.6 test cannot be resolved from the archive.

## Bottom line

- **Repository integrity:** good under the performed checks.
- **Official reproducibility:** strong for UCLA/Princeton/IMProofBench; incomplete for OpenAI direct.
- **Official condition:** retrieval/tool-enabled research-agent evaluation, not closed-book reasoning.
- **Human-review signal:** essential; it exposes substantial false-complete behavior.
- **Local blind-grading audit:** qualitatively validated; locked scores unchanged.
- **Local condition mapping after unblinding:** A = ATTICUS, B = raw Sol.
- **Training contamination:** unresolved.

### Companion files in this repository

- `review_consensus.csv`
- `resource_usage.csv`
- `self_verification.csv`
- `standardization_fidelity.csv`
- `local_locked_scores.csv`
- `ARCHIVE_INTEGRITY.md`

The full upstream repository itself is not vendored here. It is linked from the project README.
