# TAIKI Platform

Enterprise Quality Engineering Framework

## Components

11 AI Skills
Controller Agent
MetricsDB
Quality Gates
Executive Governance
Evidence Management

## Quality Gate Decisions

GO
CONDITIONAL_GO
NO_GO
NOT_ASSESSABLE

## Supported Reports

Test Assessment
Architecture Review
Security Review
Performance Review
Release Readiness
Executive Summary

## Repository Maturity Proposal

### Kurzfazit

Das Repository enthält bereits zentrale Grundartefakte:

- `.github/workflows`
- `README.md`
- `README_Repo.md`
- `CONTRIBUTING.md`
- `repository-manifest.yaml`

TAIKI ist als controller-gesteuertes Framework mit Evidence Pack und Engineering Skills angelegt. Für den nächsten Reifegrad sollten insbesondere Skills, Controller, Schemas, MetricsDB, Dashboards und Quality Gates operationalisiert werden. Die DQA-Prozessdokumentation legt dabei besonderes Gewicht auf KPIs, Inputs und Outputs, Governance, Monitoring und Quality Gates.

### Priorität 1: Repository professionalisieren

Vorgeschlagene Struktur:

```text
TAIKI/
├── controller/
├── schemas/
├── metricsdb/
├── skills/
├── dashboards/
├── docs/
├── scripts/
├── examples/
├── tests/
└── .github/workflows/
```

### Controller ergänzen

```text
controller/
├── prompts/
│   ├── analyst.prompt.md
│   ├── controller.prompt.md
│   ├── governance.prompt.md
│   └── executive.prompt.md
├── schemas/
│   ├── controller-run.schema.json
│   ├── risk.schema.json
│   ├── action.schema.json
│   └── evidence.schema.json
└── policies/
 ├── quality-gate-policy.md
 ├── confidence-model.md
 └── decision-rules.md
```

### Skill-Library

Die elf vorgesehenen Skills sollten jeweils `SKILL.md`, `prompts/`, `references/`, `schemas/` und `examples/` enthalten:

- `software-landscape-assessment`
- `architecture-discovery`
- `visual-testing-playwright`
- `agentic-test-automation`
- `release-readiness-dqa`
- `technology-radar`
- `skill-gap-analysis`
- `security-by-design`
- `performance-capacity-analytics`
- `ticket-intelligence`
- `executive-engineering-copilot`

### MetricsDB

```text
metricsdb/
├── ddl/
│   ├── controller_runs.sql
│   ├── processing_stages.sql
│   ├── run_metrics.sql
│   ├── evidence.sql
│   ├── risks.sql
│   └── actions.sql
├── views/
├── reports/
└── dashboards/
```

### Grafana-Dashboards

Unter `dashboards/grafana/` sind folgende Dashboards vorgesehen:

- `quality-overview.json`
- `release-readiness.json`
- `skill-usage.json`
- `controller-runs.json`
- `cost-and-token-tracking.json`
- `performance-trends.json`

### GitHub Actions

Zusätzlich zu den bestehenden Workflows sollten folgende Prüfungen und Release-Schritte ergänzt werden:

- `lint.yml`
- `validate-skills.yml`
- `validate-json-schema.yml`
- `mermaid-validation.yml`
- `sql-validation.yml`
- `release.yml`

### Mermaid-Dokumentation

Unter `docs/diagrams/`:

- `taiki-architecture.mmd`
- `controller-sequence.mmd`
- `quality-gate-flow.mmd`
- `metricsdb-erd.mmd`
- `release-readiness-flow.mmd`

### Tests

Vorgeschlagene Testbereiche:

- `tests/schema-tests/`
- `tests/controller-tests/`
- `tests/skill-tests/`
- `tests/integration-tests/`

Beispiele für zentrale Prüffälle sind die Schema-Konformität der Controller-Ausgabe und die korrekte Quality-Gate-Entscheidung.

### Security und Governance

Ergänzungen unter `.github/`:

- `CODEOWNERS`
- `SECURITY.md`
- `SUPPORT.md`
- `ISSUE_TEMPLATE/`
- `PULL_REQUEST_TEMPLATE.md`

### Roadmap

| Version | Geplanter Umfang |
| --- | --- |
| v1.0 | Controller Agent, MetricsDB, 11 Skills |
| v1.1 | Grafana-Integration, PowerBI-Integration |
| v1.2 | Multi-Agent-Controller |
| v2.0 | TAIKI Marketplace, Plugin-Modell, Skill Registry |

### Empfohlene Reihenfolge

1. Controller-JSON-Schema finalisieren.
2. MetricsDB-SQL-Modell einbauen.
3. Erste elf Skill-Verzeichnisse anlegen.
4. GitHub Actions vervollständigen.
5. Grafana- und PowerBI-Dashboards erstellen.

**Konfidenz: hoch.** Die Ergänzungen bauen auf der vorhandenen Repository-Struktur und den beschriebenen DQA- und Governance-Prinzipien auf.

### CSS-Regeln für HTML-Reports

GitHub-README-Dateien übernehmen kein benutzerdefiniertes CSS. Für HTML-Reports können die gewünschten Regeln beispielsweise so verwendet werden:

```css
a {
 text-decoration: none;
 color: #464feb;
}
tr th, tr td {
 border: 1px solid #e6e6e6;
}
tr th {
 background-color: #f5f5f5;
}
```
