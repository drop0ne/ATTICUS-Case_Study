# Independent validation protocol

A strong replication should:

1. preregister hypotheses, endpoints, scoring rules, and exclusion criteria;
2. use at least 30–50 research-level problems across several mathematical domains;
3. prefer fresh/unpublished problems to reduce training-contamination risk;
4. run 3–5 independent seeds per condition/problem;
5. enforce identical model version, context, tool permissions, time, and token budgets;
6. compare at least:
   - GPT-5.6 Sol raw,
   - GPT-5.6 Sol + full ATTICUS,
   - GPT-5.6 Sol + verification-only ATTICUS ablation;
7. blind domain-expert graders to treatment identity;
8. use multiple graders and report inter-rater agreement;
9. define **full-proof acceptance rate** as the primary endpoint;
10. report completeness, false-complete rate, calibration, unsupported-claim rate, and resource efficiency as secondary endpoints;
11. preserve and publish all allowed raw outputs, including failures;
12. publish the analysis code and an immutable preregistration;
13. report both paired effect sizes and uncertainty intervals rather than relying only on p-values.

For exact ATTICUS treatment replication, qualified reviewers must obtain controlled framework access from the repository owner.
