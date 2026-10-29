# SWYNEX Data Cleaning and Basic Analysis

## 1. Objective
To clean and summarize a publicly available biological sequence dataset using Python.

## 2. Dataset Information
- Gene: OCA2
- Organism: Homo sapiens
- NCBI Gene ID: 4948
- Sequence type: mRNA
- RefSeq accession: NM_000275.3
- Sequence length: 3,143 nucleotides
- Source: NCBI

## 3. Methodology
1. Retrieved the OCA2 mRNA reference sequence from NCBI in FASTA format.
2. Loaded the FASTA file using Python.
3. Removed the FASTA header and whitespace and converted the sequence to uppercase.
4. Counted A, T, G, and C nucleotides.
5. Calculated GC content.
6. Checked for characters outside the A, T, G, and C alphabet.
7. Exported the summary to a CSV file.

## 4. Results

| Metric | Result |
|---|---:|
| Sequence length | 3,143 nt |
| A count | 710 |
| T count | 798 |
| G count | 825 |
| C count | 810 |
| GC content | 52.02% |
| Invalid characters | 0 |

## 5. Interpretation
The sequence contains 3,143 nucleotides. G and C together account for 52.02% of the sequence. No characters outside A, T, G, and C were detected in this dataset.

## 6. Files Included
- `OCA2-mRNA.fasta`: original sequence dataset
- `analyze_oca2.py`: Python analysis script
- `oca2_analysis.csv`: summary of the analysis results

## 7. References
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/4948
- NCBI RefSeq: https://www.ncbi.nlm.nih.gov/nuccore/NM_000275.3

Prepared for SWYNEX Task 2: Data Cleaning and Basic Analysis.
