# Benchmark corpus and availability matrix

Status: P1.1–P1.3 first pass
Date: 2026-11-01

This is a **lead matrix**, not a claim that every paper is usable. The status vocabulary is defined in
`notes/design/benchmark-record-schema.md`. A paper moves to `public` only after the instance, objective,
constraints, and license are verified.

## Spatially explicit harvest scheduling

| Lead | Method | Verified bibliographic detail | Availability | Notes |
|---|---|---|---|---|
| Lockwood & Moore (1993) | Simulated annealing, spatial harvest constraints | **DOI 10.1139/x93-065**; *Canadian Journal of Forest Research* 23: 468–478 | **Reconstructable candidate** | Original instance not located. The paper describes a simulated forest; obtain the PDF and reconstruct only if the objective and constraints are fully stated. |
| Boston & Bettinger (2002) | Tabu search + genetic algorithm | **DOI 10.1093/forestscience/48.1.35**; *Forest Science* 48(1): 35–46 | **Verify** | Hybrid benchmark family; check case data and schedules. |
| Bettinger, Graetz, Sessions et al. (2002) | Eight heuristics on three problem levels | **DOI 10.14214/sf.545**; *Silva Fennica* 36 | **Verify** | High-value comparison ladder; check whether objective values and constraints are published. |
| Bachmatiuk, Garcia-Gonzalo & Borges (2015) | SA implementation comparison | *Silva Fennica* 49, article 1326: <https://silvafennica.fi/article/1326> | **Verify** | Useful for tuning and time-to-quality; DOI and case data still to check. |
| McDill et al. (2002) | Area-based adjacency constraints | *Forest Science*; PDF: <https://faculty.washington.edu/toths/Presentations/Lecture%2010/McDill_etal_2002.pdf> | **Verify** | Check instance and exact formulation before use. |
| Goycoolea et al. (2005) | Exact approaches to maximum area restrictions | Search lead: <https://www.semanticscholar.org/paper/d914ed5983bf89442726466bb32a319ce22c3d02> | **Verify** | Exact/upper-bound lane; not a wall-clock peer without equal limits. |
| Dong, Bettinger et al. (2015) | Spatial harvest scheduling with carbon and timber | **DOI 10.3390/f6041362**; *Forests* 6(4): 1362 | **Verify** | Multi-account case study; data may be proprietary. |

## Reproducible stack lane

| Lead | Why it matters | Status |
|---|---|---|
| FHOPS — *Forest Harvesting Operations Planning System*; <https://github.com/UBC-FRESH/fhops> | Public MIT-licensed Python package, benchmark scripts, scenario fixtures, MIP + SA lanes. | **Public**; inspect the FHOPS paper (*SoftwareX* 36, 2026 lead), repository version, benchmark ladder, and data license. This is the primary reproducibility anchor. |

## Conservation and prioritisation transfer lane

These are not automatically like-for-like harvest schedulers. Use them as transfer tests unless the
temporal harvest-sequencing structure is genuinely equivalent.

| Lead | Why it matters | Status |
|---|---|---|
| Carwardine et al. (2015), *Spatial priorities for restoring biodiverse carbon forests*, *BioScience* 65(4): 372–382 | Martin-lab spatial prioritisation and carbon/biodiversity trade-offs. | **DOI 10.1093/biosci/biv008**; data availability to verify. |
| Gopalakrishna et al. (2024), *Optimizing forest restoration: a holistic spatial approach...* | Landscape restoration optimization with published repository lead. | **Repository listed** at IIASA: <https://pure.iiasa.ac.at/id/eprint/20283/>; verify input data/license. |
| Martin Conservation Decisions Lab publications | Conservation decision science, priority threat management, spatial prioritization. | **Bibliography source**: <https://www.taramartin.org/publications/>; build the list from the lab page. |
| Marxan / Zonation | Widely used spatial prioritization systems with public software and case data. | **Public tools**; transfer tests, not harvest-scheduling peers. |

## General combinatorial benchmark libraries

| Library | Problems | Status |
|---|---|---|
| OR-Library: <https://people.brunel.ac.uk/~mastjjb/jeb/info.html> | Assignment, covering, scheduling, routing, etc. | Public |
| MIPLIB 2017: <https://miplib.zib.de/> | Mixed-integer programming | Public |
| QAPLIB: <https://coral.ise.lehigh.edu/data-sets/qaplib/> | Quadratic assignment | Public |
| TSPLIB: <http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/> | Travelling salesman and variants | Public |
| CVRPLIB: <http://vrp.galgos.inf.puc-rio.br/index.php/en/> | Vehicle routing | Public |
| SATLIB: <https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html> | SAT and MaxSAT | Public |

## P1 conclusions

1. The Lockwood and Moore citation is verified. The original instance is **not yet available**; the
   honest status is reconstructable candidate, not public.
2. FHOPS is the strongest public reproducibility lead and should be the first stack-level comparison.
3. Most historical forestry papers require reconstruction or author contact; they cannot be called
   public benchmarks.
4. Conservation prioritisation must be separated from temporal harvest scheduling in the comparison
   design.
5. The general libraries are the Paper 2 transfer suite, not Paper 1 forestry evidence.
