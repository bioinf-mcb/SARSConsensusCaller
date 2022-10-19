import os
import argparse
from tqdm import trange
from Bio import SeqIO

def CallConsensus(folder, ref_path, result_dir, bulk_output):
    filelist = [x for x in os.listdir(folder) if "vcf.gz" in x and ".vcf.gz." not in x]
    print(filelist)
    os.makedirs(result_dir, exist_ok = True)
    bulk = []
    for f in trange(len(filelist)):
        fname = filelist[f]
        os.system(f"bcftools consensus -f {ref_path} -o {result_dir}/{fname}.fasta {folder}/{fname}")
        seqs = list(SeqIO.parse(f"{result_dir}/{fname}.fasta", "fasta"))
        seq = seqs[0]
        seq.id = fname.strip("vcf.gz")
        bulk.append(seq)
    SeqIO.write(bulk, bulk_output, "fasta")


bulk_output = snakemake.output[0]
folder = snakemake.input[0]
ref_path = snakemake.input[2]
result_dir = snakemake.input[1]
CallConsensus(folder, ref_path, result_dir, bulk_output)
print("Done")
