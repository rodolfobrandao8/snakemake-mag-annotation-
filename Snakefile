# A Regra Mestre (O Hambúrguer Final)
rule all:
    input:
        "resultados/anotacao/amostra_teste"

# A Regra do Prokka (A Cozinha)
rule anotar_bacterias:
    input:
        fasta="dados/{amostra}.fasta"
    output:
        outdir=directory("resultados/anotacao/{amostra}")
    log:
        "logs/prokka_{amostra}.log"
    params:
        extra="--cpus 2",
        prefix="resultado_final"
    wrapper:
        "file:///C:/Users/rodol/OneDrive/Documentos/GitHub/snakemake-wrappers/bio/prokka"