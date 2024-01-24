import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

df = pd.read_csv('data.csv')

x = df['inbreeding.coefficient']
y = df['pups']

# Коэффициенты корреляции
print('Коэффициент корреляции Пирсона (r) =', st.pearsonr(x, y).statistic, '\nДвусторонний p-value =', st.pearsonr(x, y).pvalue)
# print('Spearman\'s rho:', x.corr(y, method='spearman')) # непараметрический аналог коэф.Пирсона

x_ticks = [i for i in range(len(x))]

plt.rcParams["figure.figsize"] = (len(x) / 1.7, max(y) / 1.7)
plot = plt.subplot()