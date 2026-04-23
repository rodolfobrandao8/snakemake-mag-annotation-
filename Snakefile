rule all:
    input:
        "results/anotacao/amostra_teste"

rule anotar_bacterias:
    input:
        fasta="data/{amostra}.fasta"
    output:
        outdir=directory("results/anotacao/{amostra}")
    log:
        "logs/prokka_{amostra}.log"
    params:
        extra="--cpus 2",
        prefix="resultado_final"
    wrapper:
        "file://../snakemake-wrappers/bio/prokka"