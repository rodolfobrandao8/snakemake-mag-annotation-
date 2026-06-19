# Bioinformatics workflow for taxonomic classification and functional annotation of multi-kingdom MAGs using Snakemake.


Development of an Integrated Functional Annotation Workflow for Metagenome-Assembled Genomes.

**Author:** Rodolfo Ferreira  
**Institution:** University of Minho  
**Supervisors:** Andreia Salvador and Artur Gomes

---

## Repository Structure

This repository contains the deliverables and source code for the project 
**"Development of a Functional Annotation Workflow for Metagenome-Assembled Genomes"**.

| Branch | Contents |
|--------|----------|
| [`main`](https://github.com/RodolfoFerreira/Projeto-Bioinf/tree/main) | Project documents, paper, and deliverables (this branch) |
| [`pipeline`](https://github.com/RodolfoFerreira/Projeto-Bioinf/tree/pipeline) | Snakemake workflow source code, environments, and configuration files |

---

## Documents

### Project Presentation
Slide deck presenting the project objectives, the multi-kingdom pipeline architecture, and the biological validation using an anaerobic biomass dataset.

[Apresentacao_Projeto.pdf](./Apresentacao_Projeto.pdf)

### Final Paper
Scientific paper submitted in LNCS format describing the full implementation, validation, and ecological inferences extracted by the new functional annotation workflow.

[Artigo_Final_LNCS.pdf](./Artigo_Final_LNCS.pdf)

---

## Project Summary

Standard, prokaryote-optimized annotation pipelines frequently misclassify or exclude eukaryotic sequences in whole-community datasets. This project solves this challenge by developing a robust **Snakemake pipeline** for the integrated functional annotation of multi-kingdom Metagenome-Assembled Genomes (MAGs).

Key features of the developed workflow:

- **Prokaryotic Module:** Employs Bakta, Prodigal, UPIMAPI, and reCOGnizer for high-resolution structural and functional mapping.
- **Eukaryotic Module:** Utilizes MetaEuk and reCOGnizer with the KOG database to extract core cellular mechanisms from complex, fragmented assemblies.
- **The Master Table:** Converges all multi-domain outputs into standardized, genome-specific Integrated Annotation Tables.
- **Metabolic Profiling:** Enables rapid filtering of KEGG Orthology (KO) identifiers, COG categories, and UniProt homologies, directly supporting downstream community metabolic modeling.
