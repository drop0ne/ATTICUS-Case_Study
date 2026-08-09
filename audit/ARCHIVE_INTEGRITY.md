# Audited upstream archive integrity

Audited file: `batch-2-main.zip`

- SHA-256: `bd4268a439c69ab2121d6a94867ea7211f4e264809201582f4ffe83667900ac9`
- archive bytes: 435,679,876
- ZIP entries: 7,767
- uncompressed payload: 767,856,206 bytes
- CRC test: pass
- path traversal entries: 0
- absolute paths: 0
- ZIP symlinks: 0
- unique content hashes: 4,486
- duplicate-hash groups: 952

A full per-entry SHA-256/CRC manifest was generated during the audit (`batch2_archive_manifest_sha256.csv`, 1,745,848 bytes). The GitHub connector used for this publication pass does not provide a direct local-file/binary upload route for that large generated manifest, so it is not yet versioned here. This file is an **upstream-archive forensic artifact**, not an input to the ATTICUS-vs-Sol score calculation.

The exact archive SHA-256 above allows an independent reviewer with the same public upstream snapshot to regenerate the entry-level manifest. The analysis should not be treated as dependent on an unpublished ATTICUS artifact; the ATTICUS framework remains separately restricted.
