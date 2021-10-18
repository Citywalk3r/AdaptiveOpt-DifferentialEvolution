import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# plt.style.use(['seaborn-white', 'seaborn-paper'])
matplotlib.rc("font", family="monospace")
# import seaborn as sns

column_names = ['gmax', 'ps', 'CR', 'F', 776, 1, 234, 9238, 123556]

df = pd.read_excel("../de_bin_pop100_gen150_CR09_F04_multipleCR_5_seeds.xlsx")
problem = "Eggholder function"

fig = plt.figure(figsize=(10, 5))

# Effect of ps
grouped = pd.melt(df, id_vars=["ps"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["ps"] == 10]
plt.subplot(2,3,1)
plt.title('ps = 10')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["ps"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["ps"] == 20]
plt.subplot(2,3,2)
plt.title('ps = 20')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["ps"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["ps"] == 30]
plt.subplot(2,3,3)
plt.title('ps = 30')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["ps"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["ps"] == 60]
plt.subplot(2,3,4)
plt.title('ps = 60')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["ps"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["ps"] == 80]
plt.subplot(2,3,5)
plt.title('ps = 80')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["ps"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["ps"] == 100]
plt.subplot(2,3,6)
plt.title('ps = 100')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

plt.suptitle("Impact of population size on DE for the " + problem)
plt.show()


# Effect of gmax
fig = plt.figure(figsize=(10, 5))

grouped = pd.melt(df, id_vars=["gmax"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["gmax"] == 5]
print(grouped)
plt.subplot(2,3,1)
plt.title('gmax = 5')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["gmax"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["gmax"] == 20]
plt.subplot(2,3,2)
plt.title('gmax = 20')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["gmax"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["gmax"] == 50]
plt.subplot(2,3,3)
plt.title('gmax = 50')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["gmax"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["gmax"] == 100]
plt.subplot(2,3,4)
plt.title('gmax = 100')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["gmax"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["gmax"] == 200]
plt.subplot(2,3,5)
plt.title('gmax = 200')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["gmax"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["gmax"] == 500]
plt.subplot(2,3,6)
plt.title('gmax = 500')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")


plt.suptitle("Impact of g_max on DE for the " + problem)
plt.show()

# Effect of F
fig = plt.figure(figsize=(10, 5))

grouped = pd.melt(df, id_vars=["F"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["F"] == 0.1]
print(grouped)
plt.subplot(2,3,1)
plt.title('F = 0.1')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["F"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["F"] == 0.2]
plt.subplot(2,3,2)
plt.title('F = 0.2')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["F"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["F"] == 0.4]
plt.subplot(2,3,3)
plt.title('F = 0.4')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["F"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["F"] == 0.6]
plt.subplot(2,3,4)
plt.title('F = 0.6')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["F"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["F"] == 0.7]
plt.subplot(2,3,5)
plt.title('F = 0.7')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["F"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["F"] == 0.9]
plt.subplot(2,3,6)
plt.title('F = 0.9')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")


plt.suptitle("Impact of F on DE for the " + problem)
plt.show()

# Effect of F
fig = plt.figure(figsize=(10, 5))

grouped = pd.melt(df, id_vars=["CR"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["CR"] == 0.2]
print(grouped)
plt.subplot(2,3,1)
plt.title('CR = 0.2')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["CR"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["CR"] == 0.4]
plt.subplot(2,3,2)
plt.title('CR = 0.4')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["CR"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["CR"] == 0.5]
plt.subplot(2,3,3)
plt.title('CR = 0.5')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["CR"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["CR"] == 0.6]
plt.subplot(2,3,4)
plt.title('CR = 0.6')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["CR"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["CR"] == 0.8]
plt.subplot(2,3,5)
plt.title('CR = 0.8')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")

grouped = pd.melt(df, id_vars=["CR"],value_vars=["776", "1", "234", "9238", "123556"])
grouped = grouped[grouped["CR"] == 0.9]
plt.subplot(2,3,6)
plt.title('CR = 0.9')
# plt.yscale('log')
boxplot = grouped.boxplot(column="value")


plt.suptitle("Impact of CR on DE for the " + problem)
plt.show()