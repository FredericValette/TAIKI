# Shared Schemas

Controller record contracts are maintained in `controller/schemas/` so the prompts, controller policies, and CI checks use one authoritative location. Add cross-component schemas here only when more than one repository area consumes the contract.

Schemas use JSON Schema Draft 2020-12. Changes to required fields or decision enums require review because they affect stored evidence and downstream dashboards.