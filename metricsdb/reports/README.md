# MetricsDB Reports

Report queries should build on the views in `metricsdb/views/` and preserve the source run and evidence identifiers. Keep calculated values reproducible and document filters, time windows, and units in each report.

The initial `quality_overview` view provides one row per controller run with decision, confidence, risk, and action counts.