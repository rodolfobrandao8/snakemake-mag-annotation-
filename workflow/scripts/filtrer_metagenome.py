import pandas as pd
import sys

def main():
    if len(sys.argv) != 4:
        print("Uso: python filter_metagenome.py <annotation_samples.tsv> <quality_report.tsv> <output.tsv>")
        sys.exit(1)

    samples_path = sys.argv[1]
    checkm2_path = sys.argv[2]
    output_path = sys.argv[3]

    print("A ler os ficheiros...")
    df_samples = pd.read_csv(samples_path, sep="\t")
    df_checkm2 = pd.read_csv(checkm2_path, sep="\t")
    id_col = df_samples.columns[0]

    prok_df = df_samples[df_samples['domain'] == 'prok'].copy()
    euk_df = df_samples[df_samples['domain'] == 'euk'].copy()

    prok_merged = prok_df.merge(df_checkm2, left_on=id_col, right_on='Name', how='left')
    prok_merged['Completeness'] = prok_merged['Completeness'].fillna(0)
    prok_merged['Contamination'] = prok_merged['Contamination'].fillna(100)

    prok_filtrado = prok_merged[(prok_merged['Completeness'] > 90) & (prok_merged['Contamination'] < 5)]
    best_proks = prok_filtrado[df_samples.columns]

    df_final = pd.concat([best_proks, euk_df])
    df_final.to_csv(output_path, sep="\t", index=False)

    print(f"\n✅ SUCESSO ABSOLUTO!")
    print(f"-> Proks de alta qualidade (>90 comp, <5 cont): {len(best_proks)}")
    print(f"-> Euks mantidos (todos): {len(euk_df)}")

if __name__ == "__main__":
    main()