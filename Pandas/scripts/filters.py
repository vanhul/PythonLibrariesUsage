import pandas as pd

#Reading as DataFrame
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", index_col=0, decimal=",") 
print(df)

#Getting students with all subjects over 5
df1 = df.loc[(df['Maths'] >= 5) & (df['Physics'] >= 5) & (df['Spanish'] >= 5) & (df['English'] >= 5) & (df['Sports'] >= 5)]
print(df1)

#Percent of students between 3 and 4 using query
filtered_marks = df.query('3 <= `Final` <= 4')
print(filtered_marks)
print(str(round(len(filtered_marks)/len(df)*100,2))+"%")


#Getting the student with the highest Final score 
studentHigh = df['Final'].idxmax()
print(studentHigh)

#Creating a variable with the mean of all the subjects and compare if Final column has the same result
df['CalculatedScore'] = df.mean(axis=1)
print(df) #we have different results
print(df['CalculatedScore'].idxmax())
#Student 223 is the best according to our calculated score. However, the best student accordint to the 'Final' column is Student 99.

# Dropping NA from our DataFrame
df.dropna()
print(df)

