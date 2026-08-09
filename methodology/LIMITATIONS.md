# Limitations and threats to validity

1. **N=10.** Statistical power is low and uncertainty is high.
2. **One run per condition/problem.** Stochastic run-to-run variance is unmeasured.
3. **Single primary evaluator.** Scoring was blinded to condition identity and reference-grounded, but independent expert inter-rater reliability is unavailable.
4. **Framework intervention.** ATTICUS modifies inference-time instructions/governance, not model weights.
5. **Training contamination unresolved.** The benchmark was public before the experiment. Retrieval was disabled during testing, but prior model exposure cannot be ruled out.
6. **Outlier sensitivity.** P09 contributes +22 of the +31 aggregate point difference. Excluding P09 reduces mean lift to ~+1.0.
7. **False completion remains.** Both conditions produced three false-complete declarations.
8. **Resource accounting gap.** Exact local token/time accounting was not captured in a standardized log.
9. **Restricted treatment implementation.** Exact ATTICUS reproduction requires authorized access to the framework.
10. **Official-system comparisons are contextual only.** The official Batch 2 submissions used very different tool, retrieval, multi-agent, and compute budgets and are not direct controls for this experiment.
