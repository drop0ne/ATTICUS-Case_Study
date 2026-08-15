# ATTICUS Case Study — First Proof Batch 2

This repository publishes the data, scoring record, statistical analysis, and post-hoc audit for a **paired, blinded-before-scoring comparison of GPT-5.6 Sol + ATTICUS vs GPT-5.6 Sol raw** on ten research-mathematics problems from First Proof Batch 2.

> **Independent case study.** This is not an official First Proof, OpenAI, Princeton, UCLA, or IMProofBench result, and it has not yet been independently peer reviewed.

## Headline result

| Measure | GPT-5.6 Sol + ATTICUS | GPT-5.6 Sol raw |
|---|---:|---:|
| Total rubric score | 904 / 1000 | 873 / 1000 |
| Mean score | 90.4 | 87.3 |
| Problem wins | 7 | 3 |
| Judged-complete proofs | 4 / 10 | 3 / 10 |
| False-complete declarations | 3 | 3 |

Mean paired difference: +3.1 points/problem for ATTICUS.

The category decomposition is the more important result: mathematical correctness was effectively unchanged (**38.6/40 vs 38.5/40**), while completeness rose from **13.8/20 to 15.8/20**. Completeness accounted for **20 of the 31 net points (64.5%)** of the observed ATTICUS advantage.

The sample is small. The paired statistical tests do **not** establish significance. P09 is a large positive outlier; removing it reduces the mean advantage to about **+1.0 point/problem**. The appropriate interpretation is **preliminary evidence of a proof-completion effect that requires independent replication**.

## Experimental controls

- Same underlying model: **GPT-5.6 Sol**.
- Ten First Proof Batch 2 research-level problems.
- Separate chats/conditions.
- One attempt per problem.
- No web browsing or external retrieval during generation.
- No human hints, corrections, or follow-up assistance during the attempt.
- No reference solutions or referee reports available to the solver during generation.
- Fixed 100-point rubric.
- The 100-point rubric was authored by GPT-5.6 Sol operating under
  ATTICUS — i.e. by the intervention under test. See Limitation 9.
- Scoring was blind to condition identity but was performed by the
  author of the intervention. Blinding and grader independence are
  separate properties; only the first was satisfied.
- Trials were run with multiple cases in flight concurrently and
  encountered platform rate/capacity limits during execution. See
  Limitation 11.
- Samples labeled only A/B during evaluation.
- Scores and qualitative statuses locked before condition identities were revealed.
- After all ten scores were locked, the mapping was disclosed: **all Sample A = ATTICUS; all Sample B = Sol raw**.

## ATTICUS disclosure boundary

**The ATTICUS framework itself is intentionally not published in this repository.** Its proprietary instructions, internal modules, hidden prompt text, and operational procedures remain restricted/request-only. The repository contains the experimental outcomes and analysis, not the framework implementation.

This is also a reproducibility limitation: an independent team cannot reproduce the ATTICUS condition exactly from this public repository alone. A qualified reviewer seeking controlled access should contact the repository owner.

See [`NOTICE.md`](NOTICE.md) and [`methodology/CONDITION_DISCLOSURE.md`](methodology/CONDITION_DISCLOSURE.md).

## Repository map

- [`CASE_STUDY.md`](CASE_STUDY.md) — full case-study analysis.
- [`data/problem_scores.csv`](data/problem_scores.csv) — problem-level paired scores and claimed/actual completion status.
- [`data/rubric_scores_by_problem.csv`](data/rubric_scores_by_problem.csv) — all six rubric dimensions for both conditions on every problem.
- [`data/category_summary.csv`](data/category_summary.csv) — aggregate category means and contribution to the net difference.
- [`data/statistical_summary.csv`](data/statistical_summary.csv) — inferential and robustness statistics.
- [`data/experiment_metadata.json`](data/experiment_metadata.json) — machine-readable design/provenance metadata.
- [`figures/`](figures/) — score-delta and category-contribution figures.
- [`methodology/`](methodology/) — design, scoring, disclosure boundary, limitations, and replication requirements.
- [`analysis/reproduce_analysis.py`](analysis/reproduce_analysis.py) — reproduces core statistics and figures from the public CSV data.
- [`audit/`](audit/) — post-hoc audit of the complete upstream Batch 2 repository, including review consensus, resource-use comparisons, self-verification analysis, standardization fidelity, and a SHA-256 manifest of the supplied upstream archive.
- [`public/FACEBOOK_PUBLIC_REPORT.md`](public/FACEBOOK_PUBLIC_REPORT.md) — long-form public report written for non-specialist/public review.
- [`raw_outputs/README.md`](raw_outputs/README.md) — disclosure of the current raw-transcript availability gap.

## Upstream benchmark

The problems, human solutions, institutional submissions, and official Batch 2 repository belong to their respective authors/project. This repository does **not** vendor the 416 MB upstream archive or republish the human-solution/submission PDFs. Use the public upstream project directly:

- First Proof Batch 2: https://github.com/1stproof/batch-2

The post-hoc audit was conducted against a full repository download supplied for this study. The audit's archive manifest is included so the exact audited file set can be checked.

## Core limitations

1. **N = 10.** Statistical uncertainty is large.
2. **One run per condition/problem.** Within-condition stochastic variance is unknown.
3. **Evaluator dependence.** The rubric was fixed and scoring was blinded to condition identity, but independent expert graders were not used for the local A/B scores.
4. **ATTICUS is a prompt/framework intervention**, not a model-weight intervention.
5. **Training-data contamination cannot be ruled out.** The benchmark was public before this August 2026 experiment. Retrieval was disabled during the trials, but prior model training exposure is unknown.
6. **P09 materially affects the mean effect size.** Robust summaries stay positive, but smaller.
7. **False completion remains unsolved.** Both conditions produced three false-complete declarations.
8. **Public replication cannot be exact without authorized ATTICUS access.**

9. **Rubric provenance.** The scoring rubric was written by the
   intervention being evaluated. This is instrument-intervention
   coupling: the criteria defining "completeness" — the dimension
   carrying 64.5% of the net effect — were specified by the system
   that scored higher on it. The direction and size of any resulting
   bias is unmeasured. This is the most serious limitation in this
   study and it was identified after publication of the initial
   results.

10. **Correctness dimension is ceilinged.** Mathematical correctness
    scored 38.6/40 and 38.5/40, i.e. 96.5% and 96.3% of maximum,
    leaving under 1.5 points of headroom. The flat correctness result
    therefore cannot distinguish "no effect on correctness" from
    "effect not measurable by this instrument." A 40-point correctness
    scale that saturates above 96% on research-level problems, while
    only 3–4 of 10 proofs are judged complete, is not discriminating
    on the property its name denotes.

11. **Concurrent execution and platform limits.** Multiple cases were
    run simultaneously and encountered platform rate/capacity limits.
    Whether this affected conditions symmetrically has not been
    determined. If generation occurred in condition-blocked rather
    than interleaved order, throttling effects alias with condition.

12. **Condition-to-label assignment was constant, not randomized.**
    All Sample A was the ATTICUS condition across all ten problems.
    Any single correct inference of the mapping would compromise the
    full set rather than one item. Future runs should randomize
    assignment per problem.

13. **Resource use was not matched between conditions.** Output
    length, reasoning tokens, and wall time were not controlled or
    reported. Completeness scores tracking output length is an
    untested alternative explanation for the observed effect.

## What independent validation should do

A serious replication should use 30–50+ research-level problems, 3–5 independent runs per condition/problem, identical resource limits, blind domain-expert grading, preregistered endpoints, and an intermediate verification-only ablation. Fresh/unpublished problems are strongly preferred to reduce contamination risk.

Primary endpoint: **full-proof acceptance rate**. Secondary endpoints: completeness score, false-complete rate, calibration, self-checking, and tokens/time to an accepted proof.

The rubric must not be authored by, or derived from, the intervention
under test. Adopt a published instrument from the mathematical
evaluation literature, or have one written by a party with no stake
in the outcome, and freeze it before any output is generated. Any
replacement rubric must discriminate on correctness at this problem
difficulty rather than saturating.

## Peer review / contact

Critical review is invited. Please open a GitHub issue with:

- the problem number(s) reviewed,
- the mathematical field/expertise relevant to the review,
- whether you agree with the locked COMPLETE/INCOMPLETE status,
- any theorem/proof obligation you believe was misgraded,
- and a proposed corrected score under the published rubric if applicable.

The goal is falsifiable evaluation, not promotion.
