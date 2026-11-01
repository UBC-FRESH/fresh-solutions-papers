# Benchmark corpus and literature leads

Status: first pass; bibliographic and data availability verification pending
Date: 2026-11-01

Google Scholar was not queried directly. This list comes from open web and publisher/metadata pages.
Do not treat a lead as usable until the paper, objective, constraints, instance, and license are
verified.

## Spatially explicit harvest scheduling

| Lead | Method / why it matters | Data status |
|---|---|---|
| Lockwood, C. & Moore, T. (1993). Harvest scheduling with spatial constraints: a simulated annealing approach. *Canadian Journal of Forest Research* 23: 468–478. DOI: 10.1139/x93-065 | Historical SA anchor for spatial harvest scheduling | Instance availability unknown; likely reconstruction |
| Boston, K. & Bettinger, P. (2002). Combining tabu search and genetic algorithm heuristic techniques to solve spatial harvest scheduling problems. *Forest Science* 48: 35–46. | Hybrid tabu/GA benchmark family | Verify case data |
| Bettinger, P., Graetz, D., Sessions, J., et al. (2002). Eight heuristic planning techniques applied to three increasingly difficult wildlife planning problems. *Silva Fennica* 36. <https://www.silvafennica.fi/article/545> | Multiple heuristics on a common problem ladder | Verify schedules/parameters |
| Bachmatiuk, J., Garcia-Gonzalo, J. & Borges, J.G. (2015). Analysis of the performance of different implementations of a heuristic method to optimize forest harvest scheduling. *Silva Fennica* 49. <https://silvafennica.fi/article/1326> | SA implementation comparison; time-to-quality | Verify case data |
| McDill, M.E., et al. (2002). Harvest scheduling with area-based adjacency constraints. | Area/adjacency formulation | Verify instance |
| Goycoolea, M., Murray, A.T., et al. (2005). Harvest scheduling subject to maximum area restrictions: exploring exact approaches. | Exact/upper-bound lane | Verify instance and time limits |
| Dong, L., Bettinger, P., et al. (2015). Spatial forest harvest scheduling for areas involving carbon and timber. *Forests* 6(4): 1362. DOI: 10.3390/f6041362 | Multi-account spatial harvest scheduling | Case data may be proprietary |

## Reproducible stack lead

- **FHOPS: a reproducible optimisation and benchmarking stack for forest harvest operations**
  (Gregory Eric Paradis; publication status to verify). Find the paper, public repository, license,
  reference ladder, and instance versions. This is the highest-value benchmark lead.

## Conservation and prioritisation

- Martin Conservation Decisions Lab: <https://www.taramartin.org/research/> and
  <https://www.taramartin.org/publications/>.
- Carwardine, J., et al. (2015). Spatial priorities for restoring biodiverse carbon forests.
  *BioScience*.
- Gopalakrishna, T., et al. (2024). Optimizing forest restoration: a holistic spatial approach...
  IIASA: <https://pure.iiasa.ac.at/id/eprint/20283/>.
- Marxan and Zonation are spatial prioritisation tools, not like-for-like harvest schedulers. Use them
  as transfer tests unless the temporal scheduling structure is genuinely equivalent.

## General combinatorial benchmark libraries

- OR-Library: <https://people.brunel.ac.uk/~mastjjb/jeb/info.html>
- MIPLIB 2017: <https://miplib.zib.de/>
- QAPLIB: <https://coral.ise.lehigh.edu/data-sets/qaplib/>
- TSPLIB: <http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/>
- CVRPLIB: <http://vrp.galgos.inf.puc-rio.br/index.php/en/>
- SATLIB: <https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html>

## Status vocabulary

- **public**: data/code and license permit direct use.
- **reconstructable**: enough detail to rebuild, but not the original instance.
- **abstract-only**: no usable instance or objective details.
- **unusable**: no defensible comparison.

Populate this table before writing any benchmark claim.
