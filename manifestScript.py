import pathlib
import csv
import pandas as pd

names = open("names.txt","r")
absolute_filepath=[]
sampleID =[]

for line in names.readlines():
    if('R2' not in line):
        absolute_filepath.append("$PWD/"+line[:-1] )
        sampleID.append(line[:-10])

names.close()

d = {'sample-id':sampleID,'absolute-filepath':absolute_filepath}

manifest=pd.DataFrame(list(zip(sampleID,absolute_filepath)),columns=["sample-id",'absolute-filepath'])
manifest.to_csv("manifest.tsv", index=False, sep="\t")
