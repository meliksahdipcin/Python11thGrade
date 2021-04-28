import pandas as pd

df = pd.read_csv("iris.csv")
print(df.columns)
print(df.Species.unique())
print(df.info())
print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())

print(versicolor.describe())

# %%
import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis = 1)
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "virginica")
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()

# %% Histogram
plt.hist(setosa.PetalLengthCm, bins = 50)
plt.xlabel("Id")
plt.ylabel("frequance")
plt.title("Histogram")
plt.show()
# %% Scatter
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color = "red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, setosa.PetalWidthCm, color = "green", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color = "blue", label = "virginica")
plt.legend()
plt.title("Scatter")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.show()

# %% Bar
import numpy as np
x = np.array([1,2,3,4,5,6,7])
y = ["Turkey", "Canada", "England", "Germany", "Holland", "USA", "France"]
z = x/2+5

plt.bar(y, z)
plt.title("Sütun")
plt.xlabel("x")
plt.ylabel("z")
plt.show()

# %% Subplot
df.plot(grid = True, alpha = 0.9, subplots = True)
plt.show

setosa = df[df.Species == "Iris_setosa"]
versicolorr = df[df.Species == "Iris_versicolor"]
virginica = df[df.Species == "Iris_virginica"]
plt.subplot(2, 1, 1)
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.ylabel("setosa -PetalLengthCm"")
plt.subplot(2, 2, 1)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.ylabel("versicolor -PetalLengthCm"")
plt.subplot(2, 2, 2)
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "virginica")
plt.ylabel("virginica -PetalLengthCm"")
plt.show
