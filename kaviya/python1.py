import pandas as pd
import matplotlib.pyplot as mp

df=pd.read_csv("genderdata.csv")

df.rename(columns={'PassengerId':'Id','Survived':'Status'},inplace=True)

print(df.head())
print(df.tail())
print(df.info())
print(df.shape)

top_10_survivors=df[df["Status"]==1].head(10)
top_10_nonsurvivors=df[df["Status"]==0].head(10)
print(f"\nTop 10 Survivors:\n{top_10_survivors}")
print(f"\nTop 10 NonSurvivars:\n{top_10_nonsurvivors}")

numberofsurvivor=len(df[df["Status"]==1])
print(f"numberofsurvivor:{numberofsurvivor}")
numberofnonsurvivor=len(df[df["Status"]==0])
print(f"numberofnonsurvivor:{numberofnonsurvivor}")


count=df['Status'].value_counts()
print(count)


total=len(df)
survivors=(numberofsurvivor/total)*100
print(f"survivors:{survivors:.2f}")
nonsurvivors=(numberofnonsurvivor/total)*100
print(f"nonsurvivors:{nonsurvivors:.2f}")

count.plot(kind='bar',color=["red","black"])
mp.xlabel("survivor&nonsurvivor")
mp.ylabel("count")
mp.show()
