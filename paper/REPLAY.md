# Paper 1 replay

Prerequisites:

```bash
git clone https://github.com/UBC-FRESH/ws4 "$WS4_ROOT"
git clone https://github.com/UBC-FRESH/fhops "$FHOPS_ROOT"
mkdir -p "$TSA24_ROOT"
curl -L -o /tmp/ws4-tsa24-evenflow-v1.tar.gz \
  https://github.com/UBC-FRESH/femic-tsa24-instance/releases/download/ws4-tsa24-evenflow-v1/ws4-tsa24-evenflow-v1.tar.gz
tar -xzf /tmp/ws4-tsa24-evenflow-v1.tar.gz -C "$TSA24_ROOT" --strip-components=1
```

The TSA24 artifact is distributed as a release tarball; cloning the instance repository root is not
enough. From the papers repository:

```bash
WS4_ROOT=/path/to/ws4 \
TSA24_ROOT=/path/to/extracted-tsa24 \
FHOPS_ROOT=/path/to/fhops \
bash paper/replay_all.sh
```

The scripts accept either the public artifact layout (`compiled/`, `evenflow_tsa24.yaml`) or the
historical build layout (`build/compiled`, `config/ws4/targets/evenflow_tsa24.yaml`).
