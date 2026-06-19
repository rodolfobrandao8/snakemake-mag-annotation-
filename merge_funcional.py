import pandas as pd
import sys

def main():
    upimapi_file = sys.argv[1]
    recognizer_file = sys.argv[2]
    output_file = sys.argv[3]

    print("A interligar UPIMAPI e reCOGnizer...")
    
    df_upimapi = pd.read_csv(upimapi_file, sep='\t')
    df_upimapi = df_upimapi.groupby('qseqid', as_index=False).agg(lambda x: '; '.join(x.dropna().astype(str).unique()))

    df_recognizer = pd.read_csv(recognizer_file, sep='\t')
    df_recognizer = df_recognizer.groupby('qseqid', as_index=False).agg(lambda x: '; '.join(x.dropna().astype(str).unique()))

    df_master = pd.merge(df_upimapi, df_recognizer, on='qseqid', how='outer', suffixes=('_upimapi', '_recognizer'))
    df_master = df_master.fillna("-")

    df_master.to_csv(output_file, sep='\t', index=False)
    print("Sucesso! Tabela Funcional Master criada.")

if __name__ == "__main__":
    main()
