import pandas as pd

with open("./ressources/sonar_sweep.txt", "r") as f:
    file = f.readlines()
    file = [int(x.replace("\n", "")) for x in file]

df = pd.Series(file)
df1 = df.diff()
solution1 = df1.loc[df1 > 0].size

print("Solution Sonar Sweep 1: ", solution1)

df2 = pd.Series(
    [(df.loc[i] + df.loc[i + 1] + df.loc[i + 2]) for i in range(df.size - 2)]
).diff()

solution2 = df2.loc[df2 > 0].size

print("Solutio Sonar Sweep 2: ", solution2)
