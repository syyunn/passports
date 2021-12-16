import pandas as pd

tsv_file = open("iso3166-1.tsv")
df = pd.read_csv(tsv_file, sep='\t')

if __name__ == "__main__":
    pass
