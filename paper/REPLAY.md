# Paper 1 replay

Prerequisites:

```bash
git clone https://github.com/UBC-FRESH/ws4 "$WS4_ROOT"
git clone https://github.com/UBC-FRESH/femic-tsa24-instance "$TSA24_ROOT"
git clone https://github.com/UBC-FRESH/fhops "$FHOPS_ROOT"
```

From the papers repository:

```bash
WS4_ROOT=/path/to/ws4 \
TSA24_ROOT=/path/to/femic-tsa24-instance \
FHOPS_ROOT=/path/to/fhops \
bash paper/replay_all.sh
```

The TSA24 replay scripts accept either the public artifact layout (`compiled/`,
`evenflow_tsa24.yaml`) or the historical build layout (`build/compiled`,
`config/ws4/targets/evenflow_tsa24.yaml`). The release tag contains the evidence and scripts; the
software repositories are public.
