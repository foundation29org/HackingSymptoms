# Performance Comparison

This study is incomplete. Please, also consider looking at the [notebook](https://github.com/foundation29org/HackingSymptoms/blob/master/code/PerformanceComparison/PerformanceComparison.ipynb).

## Golden Standard Corpora
Data: GSC
- Algorithms:
  - NCR (bias, data used in training?)
  - Text Analytics for Health
  - ClinPhen
  - BioLink
  - IHP (could be buggy)
  - TODO: ensemble algorithms
 - Metrics:
   - simgic (a form of semantic similarity)
   - jaccard (simple but poor metric)
   - in weighed version we calculate average weighed with the number of symptoms in the ground truth, so the entries with more symptoms contribute more to the result
 - Links:
   - all raw results - gsc_scores.json
   - notebook - PerformanceComparison.ipynb
   - table above in CSV - GSC_results_average.csv 
   - modified package with similarity metrics - patient_similarity

### Results (average over the metrics), the higher the better, blue marks the maximum
<img src="../resources/GSC_results.png" alt="Initial results" width="600"/>

## Other results
Resource for below similarities: [Notebook 2](https://github.com/foundation29org/HackingSymptoms/blob/master/code/PerformanceComparison/BenchmarkPerformance.ipynb)

### Gold Standard Corpora Dataset:

| Algorithm (All algorithms used whole dataset)	| Jacard Similarity |
|-------|-------|
| Biolink | 0.3714 |
| NCR	| 0.36920 |
| Text Analytics (Considering Only Symptoms that are detected to be true-Only Non-Negated ones) | 0.2949 |
| Text Analytics (Including Negated and non negated HPO) | 0.3036 | 
| ClinPhen	| 0.4042 |

### MedMention Dataset
4392 observations ( Discarding all observations if there is [] HPO in true label ie NULL HPO ie No Symptoms )

Total = 2151 after removing null HPO valued observations ie removing observation if there were no symptoms 

Due to time limitations, only a subset of data is tried for MedMention Biolink, NCR and TA.

| Algorithm (All algorithms used whole dataset)	| Jacard Similarity |
|-------|-------|
| Biolink (281 observations used) | 0.4088 |
| NCR (243 observations used)	| 0.3748 |
| Text Analytics (Considering Only Symptoms that are detected to be true-Only Non-Negated ones) (331 Observations) | 0.5126 |
| ClinPhen (2151 Observations) | 0.3702 |

### OMIM-WIKI-Dataset
665 observations

Only 347 observations were having non-empty HPO values/symptoms. Discarded rest.

| Algorithm (All algorithms used whole dataset)	| Jacard Similarity |
|-------|-------|
| Biolink (347 observations used) | 0.0968 |
| NCR (347 observations used)	| 0.1062 |
| Text Analytics (Considering Only Symptoms that are detected to be true-Only Non-Negated ones) (347 Observations) | 0.09755 |
| ClinPhen (347 Observations) | 0.09415 |




