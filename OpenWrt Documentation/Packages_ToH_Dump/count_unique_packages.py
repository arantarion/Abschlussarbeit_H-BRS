import csv
import pandas as pd


with open("packages_dump_tab_separated.csv", newline = '') as file:
    text = csv.reader(file, delimiter='\t')
    df = pd.DataFrame(text)
    
df = df.drop_duplicates(subset= [13])
print(f"There are {len(df)-1} unique packages in the CSV dump! \n Unique entries are saved in out.xlsx")

df.to_excel('out.xlsx')

tmp = input()