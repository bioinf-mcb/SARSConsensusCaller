# SARS-CoV-2 Consensus caller
SARSConsensusCaller pipeline is a snakemake pipeline that produces consensus sequences from IonTorrent VCF.GZ files with fasta reference and later on assigns clades to them with use of pangolin. ALWAYS USE THE REFERENCE WHICH WAS USED DURING SEQUENCING!!!

## HOWTO

#### Preparation of work-dir

1. Download the SARSConsensusCaller
2. Place the VCF.GZ files in subfolders of the ./data/ e.g ./data/experiment1/
3. Add the subfolders to the config.yaml as elements of the "dirnames" list

```yaml
dirnames:
   - experiment1
   - experiment2
   - experimentn
```
4. Save the yaml file and run snakemake

#### Installation

```bash
1. git clone https://github.com/bioinf-mcb/SARSConsensusCaller.git
2. cd SARSConsensusCaller
3. git checkout pipeline
```
#### Running

```bash
1. snakemake --use-conda
```

#### Output
Output will be saved in data/\<experiment\>/results