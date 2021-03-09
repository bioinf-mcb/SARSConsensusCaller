# SARS-CoV-2 Consensus caller
SARSConsensusCaller is a wrapper python script for fast consensus sequence calls based on generated vcf files

## HOWTO

#### Installation
<code>1. git clone https://github.com/bioinf-mcb/SARSConsensusCaller.git</code>
<code>2. cd SARSConsensusCaller</code>
<code>3. conda env create -f consensus_caller.yaml</code>
<code>4. conda activate consensus_caller</code>

#### Running
<code>1. cd [...]/SARSConsensusCaller</code>
<code>2. python call_consensus.py -f <vcf_folder> -r <reference_fasta_path> -o <output_folder> </code>

#### Output
Output will be placed within specified output folder within VCF directory