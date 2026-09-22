# Contributing

Thank you for helping develop the AI Effort Estimation Framework and REEF.

## Before contributing

- Read the [Code of Conduct](CODE_OF_CONDUCT.md) and [governance model](GOVERNANCE.md).
- Search existing issues and proposals before opening a duplicate.
- Never contribute proprietary, confidential, client-specific, export-controlled, or personally identifiable information.
- Do not contribute organization-specific processes, internal integrations, private identity configuration, or privately calibrated models.
- Use synthetic or explicitly redistributable data. Record its provenance and license.

## Change types

Framework changes should update the relevant canonical document under `docs/framework/`, explain assumptions and testable consequences, and identify affected schemas or examples. REEF changes should remain conformant with the documented contracts and [`docs/product/reef-poc.md`](docs/product/reef-poc.md), or explicitly propose a contract change.

For a substantial methodology change, open an issue describing:

1. the problem and intended users;
2. definitions and assumptions;
3. the proposed change;
4. evidence or planned evaluation;
5. compatibility and ethical risks.

## Pull requests

- Keep changes focused and explain the motivation.
- Add or update tests, schemas, examples, and documentation as applicable.
- Mark empirical claims as hypotheses unless supported by reproducible evidence.
- Use PH for canonical effort values; adapters may display other units.
- Add an entry under `Unreleased` in `CHANGELOG.md` for user-visible changes.
- Confirm that all included material is safe to publish under Apache-2.0.

By submitting a contribution, you agree that it is licensed under this repository's Apache-2.0 license.
