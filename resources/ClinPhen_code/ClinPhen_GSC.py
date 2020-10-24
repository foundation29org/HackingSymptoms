import pandas as pd 
import os

#### Code to concatenate the individual output files to a CSV

src_dir = "C:/Users/srlava/OneDrive - Microsoft/Hackathon/2020 HAckathon/IHP-master/Annotations/Output"
files = os.listdir(src_dir)

Input = pd.read_csv('GSC+.csv')

hpo_id = []
phenotype_name = []
occurences = []
earliness = []
example = []
file_name = []
text = []
for f in files:
    df = pd.read_csv(f"{src_dir}/{f}",sep = '\t')
    name = f.split('.')[0]
    file_name.append(name)
    hpo_id.append(list(df['HPO ID']))
    phenotype_name.append(list(df['Phenotype name']))
    occurences.append(list(df['No. occurrences']))
    earliness.append(list(df['Earliness (lower = earlier)']))
    example.append(list(df['Example sentence']))
    text.append(list(Input.loc[Input.file == int(name),'text']))

final = pd.DataFrame({"FileName" : file_name,'Actual Text' : text,"HPO ID" : hpo_id, "Phenotype name" : phenotype_name,'No. occurrences' : occurences, 'Earliness (lower = earlier)' : earliness,'Example sentence' : example })
final.to_csv('ClinPhen_Output.csv',index = False)

