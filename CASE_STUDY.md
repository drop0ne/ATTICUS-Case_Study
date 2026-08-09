# Case Study CS-01: GPT-5.6 Sol + ATTICUS vs GPT-5.6 Sol Raw on First Proof Batch 2

**Status:** COMPLETE  
**Design:** paired, blinded-before-scoring, N=10 research-mathematics problems  
**Conditions:** GPT-5.6 Sol + ATTICUS vs GPT-5.6 Sol raw  
**Scoring:** fixed 100-point rubric; all problem scores locked before condition identities were revealed

## Executive finding

ATTICUS scored **90.4** versus **87.3** for raw Sol, a mean paired advantage of **+3.1 points/problem** and a total advantage of **+31 points**. ATTICUS won **7 of 10** problems; raw Sol won **3 of 10**.

The effect is not a general increase in raw mathematical correctness. Mean correctness was **38.6/40 vs 38.5/40**. The dominant change was **completeness: 15.8/20 vs 13.8/20**, contributing **20 of the 31 net points (64.5%)**. Calibration contributed another **5 points (16.1%)**.

ATTICUS produced **4 judged-complete proofs** versus **3** for raw Sol. Both conditions produced **3 false-complete declarations**, so the data do not support a claim that ATTICUS eliminated overclaiming.

## Design controls

1. The two conditions received the same ten problem statements in separate chats.
2. Web, external retrieval, connected apps, and reference-solution access were disabled during the one-shot attempts.
3. A fixed rubric was used: correctness 40, completeness 20, unsupported-claim resistance 10, error/self-check 10, calibration 10, exposition/rigor 10.
4. Scores were locked before the user revealed that every Sample A was ATTICUS and every Sample B was raw Sol.
5. Human/reference solutions and repository submissions were used for post-hoc verification, not for generating the tested answers.

## Problem-level results

| Problem | ATTICUS | Sol raw | Delta | ATTICUS actual | Sol actual |
|---|---:|---:|---:|---|---|
| P01 | 97 | 94 | +3 | COMPLETE | COMPLETE |
| P02 | 86 | 98 | -12 | INCOMPLETE | COMPLETE |
| P03 | 89 | 88 | +1 | INCOMPLETE | INCOMPLETE |
| P04 | 87 | 82 | +5 | INCOMPLETE | INCOMPLETE |
| P05 | 91 | 94 | -3 | INCOMPLETE | INCOMPLETE |
| P06 | 99 | 90 | +9 | COMPLETE | INCOMPLETE |
| P07 | 99 | 98 | +1 | COMPLETE | COMPLETE |
| P08 | 79 | 85 | -6 | INCOMPLETE | INCOMPLETE |
| P09 | 98 | 76 | +22 | COMPLETE | INCOMPLETE |
| P10 | 79 | 68 | +11 | INCOMPLETE | INCOMPLETE |

## Rubric decomposition

| Category | ATTICUS mean | Sol raw mean | Net contribution |
|---|---:|---:|---:|
| Correctness | 38.6 | 38.5 | +1 |
| Completeness | 15.8 | 13.8 | +20 |
| Unsupported-claim resistance | 8.8 | 8.8 | 0 |
| Error/self-check | 9.2 | 8.9 | +3 |
| Calibration | 9.2 | 8.7 | +5 |
| Exposition/rigor | 8.8 | 8.6 | +2 |

The category decomposition is the central result. Of the 31-point aggregate ATTICUS advantage, completeness contributes 20 points (64.5%). Thus the observed effect is best described as **proof-development/completion lift**, not a material increase in initial mathematical correctness.

## Completion and calibration

ATTICUS claimed COMPLETE on 7 problems and was judged actually complete on 4: completion-claim precision **57.1%**. Raw Sol claimed COMPLETE on 6 and was actually complete on 3: **50.0%**.

ATTICUS correctly declared INCOMPLETE on P03, P04, and P05. Raw Sol correctly declared INCOMPLETE on P03, P04, P05, and P06. Overall status classification accuracy was 7/10 for each condition, but ATTICUS converted one additional problem into an actually complete proof.

## Concentration and robustness

The paired differences were:

`P01:+3, P02:-12, P03:+1, P04:+5, P05:-3, P06:+9, P07:+1, P08:-6, P09:+22, P10:+11`

P09 is the largest positive outlier at +22. Removing P09 reduces the mean advantage from +3.1 to **+1.0**. The 10% trimmed mean is **+2.625** and the median paired difference is **+2.0**.

The 95% paired-t confidence interval is **[-3.71, 9.91]**; the nonparametric bootstrap interval is approximately **[-2.3, 8.8]**. The exact two-sided sign-test p-value for 7 wins in 10 is **0.344**, the exact Wilcoxon signed-rank p-value is **0.432**, and the paired t-test p-value is **0.330**. With N=10 these data do **not** establish statistical significance.

Cohen's paired-sample effect size is **dz≈0.326**, a small-to-moderate descriptive effect with substantial uncertainty.

## Mechanistic case analysis

### P06 — completion of the missing inequality (+9)
Both conditions found the correct reduction. Raw Sol stopped at the exact point where a stronger rooted-branch energy inequality was needed. ATTICUS supplied an effective-capacity recursion, the shifted integer-energy bound, and the integrality/distance argument that closed the proof.

### P09 — alternative representation vs proved bridge (+22)
Raw Sol identified a correct marked-descent formula, but the generating-function identity connecting the algebra to that formula was effectively asserted. ATTICUS reconstructed the ordered-set-partition involution that matches the human solution and proved the coefficient extraction. This single problem contributes 22/31 of the net aggregate advantage.

### P10 — better architecture but still false completion (+11)
Both answers remained incomplete. ATTICUS reduced the theorem to one overstrong proper-proximality permanence assertion; raw Sol depended on a still larger unsupported graph-product boundary criterion. ATTICUS scored higher while still demonstrating that its scaffold does not guarantee proof closure or calibrated final status.

### P02/P08 — counterexamples to uniform dominance
Raw Sol decisively won P02 and also won P08. On P02 it supplied a materially stronger constructive argument. On P08 both conditions found the correct duality architecture, but raw Sol developed the central lemma more fully. ATTICUS is therefore not a monotone improvement.

## External benchmark context

The repository audit found that official Batch 2 workflows were substantially more agentic and retrieval-heavy than this local one-shot experiment. Consequently, official submission pass counts are useful as problem-difficulty context but are **not a fair head-to-head performance comparison** with these local runs.

## Threats to validity

1. **N=10.** Statistical uncertainty is large.
2. **Single run per condition/problem.** No estimate of within-condition stochastic variance.
3. **Scoring dependence.** One evaluator and one fixed rubric; although reference-grounded and locked before unblinding, grader variance is not measured.
4. **Prompt/scaffold confounding.** ATTICUS changes reasoning instructions, not model weights.
5. **Public-data contamination unresolved.** Retrieval was disabled during testing, but the First Proof materials were public before the run, so training exposure cannot be excluded.
6. **Outlier sensitivity.** P09 accounts for most of the net margin.
7. **Completion definition.** Rubric scores and journal-style full-pass decisions measure related but distinct things.

## Conclusion

> In this ten-problem blinded paired experiment, ATTICUS produced a **+3.1 point mean rubric lift and 7–3 win record over raw GPT-5.6 Sol**, driven primarily by better proof completion rather than higher underlying mathematical correctness. It completed one additional problem, but did not reduce the absolute number of false-complete declarations. The result is suggestive, not statistically established, and requires replication across more problems and repeated seeds.

## Recommended next experiment

The highest-value follow-up is a preregistered repeated-seed ablation:

- 30–50 problems spanning several research-math domains;
- 3–5 independent runs per condition/problem;
- identical context/token/time limits;
- blind external grading;
- ATTICUS vs raw Sol plus one intermediate verification-only ablation;
- primary endpoint: full-proof acceptance rate;
- secondary endpoints: rubric completeness, false-complete rate, time/tokens to accepted proof.

This would distinguish a real scaffold effect from run variance and identify which ATTICUS components generate the completion lift.
