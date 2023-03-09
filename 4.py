import numpy as np 
import scipy.stats as stats
x = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

import scipy.stats as stats
print(stats.ttest_rel(x, y))

# TtestResult(statistic=0.559522990335608, pvalue=0.5911212354055175, df=8)
# принимаем гипотезу H0 (статистических различий нет), так как pvalue > a = 0.05