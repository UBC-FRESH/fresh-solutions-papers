# Paper 2 replay

```bash
git clone --recurse-submodules https://github.com/UBC-FRESH/fresh-solutions-papers
cd fresh-solutions-papers
python3 -m pip install -r container/requirements-evidence.txt
export QAPLIB_ROOT=/path/to/QAPLIB
export TSPLIB_ROOT=/path/to/tsplib
bash paper2/replay_all.sh
```

The submodule must be present; the scripts do not fall back to an ambient `fresh_solutions` install.
The expected output is 200/200 expanded QAP, 200/200 BLS, 100/100 expanded TSP, 1,060 broad,
40 generic, and 40 framework + 20 deep TSP.
