import pandas as pd
import numpy as np

#Normal read of csv
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";")
print(df)

#Second row is now header
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", header=1)
print(df)

#Renamming header
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";",names = ["Students","M","P","S","E", "Sp","Final"])
print(df)

#Removing duplicates while renamming
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", header=0, names = ["Students","M","P","S","E", "Sp","Final"])
print(df)

#Do not use first column as the index
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", index_col=False)
print(df)

#Use the thirth and forth column names for rename the first and second
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", index_col=[2,3])
print(df)

#Only use the first and second column
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";",usecols=[0,1])
print(df)

#Error code. usecols only accept all strings, all integers, all unicode or all callable
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", usecols=[1,"Maths"])
print(df)

#Math and English columns
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", usecols=["Maths","English"])
print(df)

#Parsed data becomes a Series type. squeeze is deprecated. 
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", usecols=["Maths"], squeeze = True)
print(df)
#Insted we use print(df.squeeze("columns"))

df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", header=None,prefix="Subject: ")
print(df)

#Only 100 rows
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", nrows=100)
print(df)
