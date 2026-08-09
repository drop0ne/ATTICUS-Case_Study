# Experimental design

## Question
Does adding the ATTICUS reasoning/governance framework to the same GPT-5.6 Sol model change performance on research-level mathematics?

## Paired conditions
- **A (revealed only after scoring):** GPT-5.6 Sol + ATTICUS
- **B (revealed only after scoring):** GPT-5.6 Sol raw/baseline

## Unit of comparison
Ten First Proof Batch 2 problems. Each problem was attempted once in each condition in separate chats.

## Solver controls
During the solver runs:
- web browsing was disabled;
- external search/retrieval was disabled;
- connected applications were disabled;
- no human hints, corrections, or follow-up assistance were provided;
- reference solutions and referee reports were withheld;
- each trial was one-shot.

## Blinding
The grader saw the answers as Sample A/Sample B (P01 used Sample 1/Sample 2 naming) and locked the score/status before the user revealed condition identity. After P10 was locked, the user revealed that all A/1 samples were ATTICUS and all B/2 samples were Sol raw.

## Post-hoc verification
After scoring was locked and all ten trials were complete, the study used human solutions, official submissions, reviews, and the full public Batch 2 repository to audit the judgments and benchmark context.

## What was not controlled
- Sampling randomness was not replicated.
- Token counts/time-to-answer for the local A/B trials were not captured in a standardized machine-readable log.
- Independent human domain-expert grading was not performed.
- The possibility of pretraining exposure to the public benchmark cannot be excluded.
