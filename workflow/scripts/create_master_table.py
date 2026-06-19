import pandas as pd
import sys

def main():
    if len(sys.argv) != 5:
        print("Uso: python create_master_table.py <bakta.tsv> <upimapi.tsv> <recognizer.tsv> <output_final.tsv>")
        sys.exit(1)

    bakta_file = sys.argv[1]
    upimapi_file = sys.argv[2]
    recognizer_file = sys.argv[3]
    output_file = sys.argv[4]

    print("A carregar as tabelas e a preservar toda a informação...")
    
    cols_bakta = ['Sequence Id', 'Type', 'Start', 'Stop', 'Strand', 'Locus Tag', 'Gene', 'Product', 'DbXrefs']
    df_bakta = pd.read_csv(bakta_file, sep='\t', comment='#', names=cols_bakta)
    df_bakta = df_bakta[df_bakta['Type'] == 'cds'].copy()

    df_upimapi = pd.read_csv(upimapi_file, sep='\t')
    df_upimapi = df_upimapi.groupby('qseqid', as_index=False).agg(lambda x: '; '.join(x.dropna().astype(str).unique()))

  
    df_recognizer = pd.read_csv(recognizer_file, sep='\t')
    df_recognizer = df_recognizer.groupby('qseqid', as_index=False).agg(lambda x: '; '.join(x.dropna().astype(str).unique()))

    print("A interligar os resultados numa única linha por proteína...")

    df_master = pd.merge(df_bakta, df_upimapi, left_on='Locus Tag', right_on='qseqid', how='left')
    if 'qseqid' in df_master.columns:
        df_master = df_master.drop(columns=['qseqid'])

    df_master = pd.merge(df_master, df_recognizer, left_on='Locus Tag', right_on='qseqid', how='left', suffixes=('_upimapi', '_recognizer'))
    if 'qseqid' in df_master.columns:
        df_master = df_master.drop(columns=['qseqid'])

    df_master = df_master.fillna("-")

    print(f"A guardar a Master Table Completa em: {output_file}")
    df_master.to_csv(output_file, sep='\t', index=False)
    print("Concluído")

if __name__ == "__main__":
    main()