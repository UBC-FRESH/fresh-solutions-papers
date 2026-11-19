# Paper 1 replay

Prerequisites:

```bash
git clone --branch ws4-v0.2.0-p14rc1 --depth 1 https://github.com/UBC-FRESH/ws4 "$WS4_ROOT"
git clone https://github.com/UBC-FRESH/fhops "$FHOPS_ROOT"
git -C "$FHOPS_ROOT" checkout 135321b1f5a7a557823ea6241650a6431b4f121b
mkdir -p "$TSA24_ROOT"
curl -L -o /tmp/ws4-tsa24-evenflow-v1.tar.gz \
  https://github.com/UBC-FRESH/femic-tsa24-instance/releases/download/ws4-tsa24-evenflow-v1/ws4-tsa24-evenflow-v1.tar.gz
tar -xzf /tmp/ws4-tsa24-evenflow-v1.tar.gz -C "$TSA24_ROOT" --strip-components=1
```

From the papers repository:

```bash
WS4_ROOT=/path/to/ws4 \
TSA24_ROOT=/path/to/extracted-tsa24 \
FHOPS_ROOT=/path/to/fhops \
bash paper/replay_all.sh
```

The TSA24 release tarball is required; the instance repository root does not contain `compiled/` and
`evenflow_tsa24.yaml` on its default branch. The replay scripts accept either the public artifact
layout (`compiled/`, `evenflow_tsa24.yaml`) or the historical build layout.
