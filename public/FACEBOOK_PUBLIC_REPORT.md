# Public report: ATTICUS vs GPT-5.6 Sol raw on First Proof Batch 2

I ran a controlled experiment using ten research-level mathematics problems from First Proof Batch 2. The purpose was to compare the same underlying model — GPT-5.6 Sol — under two conditions: raw/baseline inference and inference governed by my ATTICUS framework.

This is not peer review, and it is not an official OpenAI, Princeton, UCLA, IMProofBench, or First Proof result. I am publishing the outcomes because I want qualified people to be able to challenge the analysis and independently replicate it.

## Experimental design

For each of ten problems I used two separate chats. One was GPT-5.6 Sol + ATTICUS; the other was GPT-5.6 Sol raw. Each was one-shot. Web browsing, external retrieval, connected apps, reference solutions, human hints, corrections, and follow-up assistance were disabled during generation.

The answers were kept blinded as Sample A/Sample B while they were graded under a fixed 100-point rubric:
- correctness 40;
- completeness 20;
- unsupported-claim resistance 10;
- error/self-check quality 10;
- calibration 10;
- exposition/rigor 10.

All ten paired scores and COMPLETE/INCOMPLETE judgments were locked before the condition identities were revealed. Only afterward was the mapping disclosed: every Sample A was ATTICUS; every Sample B was raw Sol.

## Results

ATTICUS scored 904/1000 (mean 90.4). Raw Sol scored 873/1000 (mean 87.3). ATTICUS won 7 of 10 problems. The mean paired advantage was +3.1 points/problem.

The more informative result is the category breakdown. Mathematical correctness was effectively unchanged: 38.6/40 vs 38.5/40. Completeness was 15.8/20 vs 13.8/20, accounting for 20 of the 31 net points (64.5%) of the ATTICUS advantage. Self-checking, calibration, and exposition improved modestly. Unsupported-claim resistance was unchanged in aggregate.

This suggests a narrow hypothesis: ATTICUS may be improving **proof development/completion** more than the model's ability to initially locate correct mathematics.

## Wins and failures

P02 was ATTICUS's largest loss (-12): raw Sol produced the substantially stronger geometric construction.

P06 was a strong ATTICUS win (+9): both conditions found the right reduction, but raw Sol stopped at the missing rooted-branch inequality while ATTICUS supplied the additional argument needed to close the proof.

P08 was another ATTICUS loss (-6): both found the correct high-level duality construction, but both overclaimed completion and raw Sol developed the central lemma further.

P09 was the largest ATTICUS win (+22): raw Sol found an essentially correct combinatorial formula but omitted the main proof bridge. ATTICUS reconstructed an ordered-set-partition involution matching the human-solution architecture and completed the coefficient extraction.

P10 was ATTICUS +11, but **neither proof was complete**. ATTICUS had the better architecture yet still falsely declared completion around a theorem-sized proper-proximality step.

The false-completion result is important: ATTICUS produced 3 false-complete declarations and raw Sol also produced 3. ATTICUS completed 4/10 proofs versus 3/10 for raw Sol, but it did not eliminate overclaiming.

## Statistical reality check

The paired differences were +3, -12, +1, +5, -3, +9, +1, -6, +22, +11. P09 is a large outlier. Removing it reduces the mean ATTICUS advantage to about +1.0 point/problem.

With only ten pairs, formal tests are not significant (paired t p≈0.33; Wilcoxon p≈0.43; sign test p≈0.34). The 95% confidence interval for the mean difference crosses zero. This is preliminary evidence, not statistical validation.

## Post-hoc repository audit

After all solver runs and scores were complete, retrieval was restored and the full public Batch 2 repository was audited. It contains human solutions, institutional submissions, raw outputs, reviews, model-testing material, and source/configuration data from OpenAI, UCLA, Princeton, and IMProofBench.

Those official systems were generally much more agentic and resource-heavy than this local one-shot experiment, so their pass rates are context — not fair direct controls.

## Contamination limitation

The benchmark was publicly available before this experiment. Retrieval was disabled during the trials, but I cannot prove GPT-5.6 Sol never encountered the material during training. **CONTAMINATION RISK: UNRESOLVED.**

## What would independently validate this?

A credible replication should use 30–50+ research-level problems, 3–5 runs per condition/problem, identical resource limits, multiple blind domain-expert graders, preregistered scoring/endpoints, and preferably fresh unpublished problems. It should compare raw Sol, full ATTICUS, and a verification-only ablation. The primary endpoint should be full-proof acceptance rate; secondary endpoints should include completeness, false-complete rate, calibration, unsupported claims, and resource cost.

## ATTICUS disclosure boundary

The ATTICUS framework itself is **not public**. It remains restricted/request-only. This repository publishes the experiment and derived data, not the proprietary framework internals. Qualified reviewers who need controlled access to reproduce the treatment should contact me.

I am interested in attempts to falsify this result, not just agreement. If the effect is real, it should survive independent hostile review. If it is not, I want to know that too.
