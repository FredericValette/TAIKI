# Grafana Dashboards

The dashboard JSON files use the Grafana SQLite datasource plugin (`frser-sqlite-datasource`). Configure the datasource with UID `taiki-metrics` and point it to a database initialized with `metricsdb/ddl/`.

The cost/token dashboard reports only measurements named `tokens_total` and `cost_total`; the performance dashboard reports names containing `duration` or `latency`. Emit those metrics through `run_metrics` before treating the panels as complete operational reporting.
