# SARS-CoV-2 Consensus caller
SARSConsensusCaller is a wrapper python script for fast consensus sequence calls based on generated vcf files

## HOWTO

#### Installation

```bash
1. git clone https://github.com/bioinf-mcb/SARSConsensusCaller.git
2. cd SARSConsensusCaller
3. conda env create -f consensus_caller.yaml
4. conda activate consensus_caller
```
#### Running

```bash
1. cd [...]/SARSConsensusCaller
2. python call_consensus.py -f <vcf_folder> -r <reference_fasta_path> -o <output_folder>
```

#### Output
Output will be placed within specified output folder within VCF directory