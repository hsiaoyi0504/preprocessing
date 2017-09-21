import re
import pandas as pd
from helper import preprocessing

# Read input file
train_text = pd.read_csv("input/training_text", sep="\|\|", engine="python", skiprows=1, names=["ID", "Text"])
test_text = pd.read_csv("input/test_text", sep="\|\|", engine="python", skiprows=1, names=["ID", "Text"])
train = pd.read_csv('input/training_variants')
test = pd.read_csv('input/test_variants')

out_f = open("output/train","w")
out_f.write("ID,Text\n")
for i in range(len(train)):
    text = train_text.Text[i]
    gene = train.Variation[i]
    var = train.Variation[i]
    text = preprocessing(text, gene, var)
    out_f.write(str(i)+"||"+ text+"\n")
out_f.close()

out_f = open("output/test","w")
out_f.write("ID,Text\n")
for i in range(len(test)):
    text = test_text.Text[i]
    gene = test.Variation[i]
    var = test.Variation[i]
    text = preprocessing(text, gene, var)
    out_f.write(str(i)+"||"+ text+"\n")
out_f.close()
