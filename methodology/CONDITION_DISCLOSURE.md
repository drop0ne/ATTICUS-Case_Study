# Condition disclosure

## Publicly disclosed
The ATTICUS condition used the same underlying GPT-5.6 Sol model as baseline plus the user's ATTICUS reasoning/governance framework. The solver instructions emphasized proof rigor, weak-premise detection, calibration, contradiction detection, verification, uncertainty handling, hallucination resistance, assumption tracking, adversarial self-checking, bounded self-correction, and explicit INCOMPLETE status when proof obligations remained.

The raw/baseline condition explicitly instructed GPT-5.6 Sol not to apply ATTICUS, its named modules, its custom scaffold, or user-created ATTICUS governance procedures for the trial.

Both conditions were subject to the same one-shot/no-retrieval/no-hints benchmark rules.

## Not publicly disclosed
The exact ATTICUS framework implementation, internal module text, proprietary governance procedures, hidden prompt material, and architecture are **restricted/request-only** and are not included in this repository.

This means the public repository supports audit of the **measurement and analysis**, but not exact unauthorized reproduction of the ATTICUS treatment.
