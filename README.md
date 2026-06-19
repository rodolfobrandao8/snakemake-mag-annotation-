# Bioinformatics workflow for the functional annotation of multi-kingdom MAGs using Snakemake

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
<<<<<<< Updated upstream
| [`main`](https://github.com/RodolfoFerreira/Projeto-Bioinf/tree/main) | Project documents, paper, and deliverables (this branch) |
| [`Snakemake-Workflow`](https://github.com/RodolfoFerreira/Projeto-Bioinf/tree/Snakemake-Workflow) | Snakemake workflow source code, environments, and configuration files |
=======
| [`main`]| Project documents, paper, and deliverables (this branch) |
| [`Snakemake-Workflow`]| Snakemake workflow source code, environments, and configuration files |
>>>>>>> Stashed changes

---

## Documents

<<<<<<< Updated upstream
### Interim Paper (State of the Art)
Preliminary paper containing the project introduction, contextualization of the multi-kingdom annotation challenge, and a comprehensive state-of-the-art review of current bioinformatics tools for metagenomics.


### Project Presentation
=======
### 1. Interim Paper (State of the Art)
Preliminary paper containing the project introduction, contextualization of the multi-kingdom annotation challenge, and a comprehensive state-of-the-art review of current bioinformatics tools for metagenomics.


### 2. Project Presentation
>>>>>>> Stashed changes
Slide deck presenting the project objectives, the multi-kingdom pipeline architecture, and the biological validation using an anaerobic biomass dataset.


### 3. Final Paper
Scientific paper submitted in LNCS format describing the full implementation, validation, and ecological inferences extracted by the new functional annotation workflow.

---

## Project Summary

Standard, prokaryote-optimized annotation pipelines frequently misclassify or exclude eukaryotic sequences in whole-community datasets. This project solves this challenge by developing a robust **Snakemake pipeline** for the integrated functional annotation of multi-kingdom Metagenome-Assembled Genomes (MAGs).

Key features of the developed workflow:

- **Prokaryotic Module:** Employs Bakta, Prodigal, UPIMAPI, and reCOGnizer for high-resolution structural and functional mapping.
- **Eukaryotic Module:** Utilizes MetaEuk and reCOGnizer with the KOG database to extract core cellular mechanisms from complex, fragmented assemblies.
- **The Master Table:** Converges all multi-domain outputs into standardized, genome-specific Integrated Annotation Tables.
- **Metabolic Profiling:** Enables rapid filtering of KEGG Orthology (KO) identifiers, COG categories, and UniProt homologies, directly supporting downstream community metabolic modeling.
<<<<<<< Updated upstream

For installation prerequisites and execution instructions, see the 
[`Snakemake-Workflow` branch](https://github.com/RodolfoFerreira/Projeto-Bioinf/tree/Snakemake-Workflow).
=======
>>>>>>> Stashed changes
