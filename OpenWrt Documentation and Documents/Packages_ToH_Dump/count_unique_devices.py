import csv
import pandas as pd


with open("ToH_dump_tab_separated.csv", newline = '') as file:
    text = csv.reader(file, delimiter='\t')
    df = pd.DataFrame(text)

print(f"There are {len(set(df[2]))} unique vendors in the CSV dump! \n There are {len(df)} supported devices")

