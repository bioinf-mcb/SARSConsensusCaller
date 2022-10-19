import os
import argparse
from tqdm import trange
from Bio import SeqIO

parser = argparse.ArgumentParser(description = "Creates consensus from vcf and reference for SARS-CoV-2")
parser.add_argument('-f', '--folder', help = "Specify folder with vcf.gz files")
parser.add_argument('-r', '--reference', help = "Specify path to reference genome")
parser.add_argument('-o', '--output', help = "Specify path to output folder (will be created if not exists)")


def CallConsensus(folder, ref_path, result_dir):
    os.chdir(folder)
    filelist = [x for x in os.listdir() if "vcf.gz" in x and ".vcf.gz." not in x]
    print(filelist)
    os.makedirs(result_dir, exist_ok = True)
    bulk = []
    for f in trange(len(filelist)):
        fname = filelist[f]
        os.system(f"bcftools consensus -f {ref_path} -o {result_dir}/{fname}.fasta {fname}")
        seqs = list(SeqIO.parse(f"{result_dir}/{fname}.fasta", "fasta"))
        seq = seqs[0]
        seq.id = fname[:-6]
        bulk.append(seq)
    SeqIO.write(bulk, f"{result_dir}/final_output.fasta", "fasta")

if __name__ == "__main__":

    args = parser.parse_args()
    folder = args.folder
    ref_path = args.reference
    result_dir = args.output
    CallConsensus(folder, ref_path, result_dir)
    print("Done")
