import os

configfile: "config.yaml"

for subdir in config["dirnames"]:
    os.makedirs(f"data/{subdir}/results")

rule all:
    input:
        expand("data/{dirname}/results/pangolin_report.csv", dirname = config["dirnames"])

rule call_consensus:
    input:
        folder=expand("data/{dirname}/", dirname = config["dirnames"]),
        refpath="data/reference/reference.fasta",
        outfolder=expand("data/{dirname}/results", dirname = config["dirnames"])
    conda:
        "environment.yaml"
    output:
        "data/{dirname}/results/bulk_output.fasta"
    script:
        "utils/call_consensus.py"
        
rule assign_clades:
    input:
        "data/{dirname}/results/bulk_output.fasta"
    conda:
        "environment.yaml"
    output:
        "data/{dirname}/results/pangolin_report.csv"
    shell:
        "pangolin {input} --threads 1 --outfile {output}"
        