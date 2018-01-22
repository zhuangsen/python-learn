#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("train.csv")
label = df['TARGET']
df = df.drop(['ID', 'TARGET'], axis=1)
# print(df)


## 1.Basic Analysis ##
# (1)Missing value #
missSet = [np.nan, 9999999999, -999999]

# (2)Count dostomce #
len(df.iloc[:, 0].unique())

count_un = df.iloc[:, 0: 3].apply(lambda x: len(x.unique()))

# (3)Zero Values #
np.sum(df.iloc[:, 0] == 0)

count_zero = df.iloc[:, 3].apply(lambda x: np.sum(x == 0))

# (4)Mean Vales #
np.mean(df.iloc[:, 0])  # 没有去除缺失值之间的均值很低

df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)]  # 去除缺失值
np.mean(df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)])  # 去除缺失值后进行均值计算

df_mean = df.iloc[:, 0: 3].apply(lambda x: np.mean(x[~np.isin(x, missSet)]))

# (5) Median Values #
np.median(df.iloc[:, 0])  # 没有去除缺失值之前

df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)]  # 去除缺失值
np.median(df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)])  # 去除缺失值之后进行计算

df_median = df.iloc[:, 0: 3].apply(lambda x: np.median(x[~np.isin(x, missSet)]))


# #######统计描述-众数#########
# （6）Mode Values #
df_mode = df.iloc[:, 0: 3].apply(lambda x: stats.mode(x[~np.isin(x, missSet)])[0][0])

# (7) Mode Percentage #
df_mode_count = df.iloc[:, 0: 3].apply(lambda x: stats.mode(x[~np.isin(x, missSet)])[1][0])

df_mode_perct = df_mode_count/df.shape[0]


# ########统计指标示例-最小值/最大值############
# （8）Min Values #
np.min(df.iloc[: 0])

df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)]  # 去除缺失值
np.min(df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)])  # 去除缺失值后进行最小值计算

df_min = df.iloc[:, 0: 3].apply(lambda x: np.min(x[~np.isin(x, missSet)]))

# (9) Max Values #
np.max(df.iloc[:, 0])

df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)]  # 去除缺失值
np.max(df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)])  # 去除缺失值后进行最大值计算

df_max = df.iloc[:, 0: 3].apply(lambda x: np.max(x[~np.isin(x, missSet)]))


# ########   统计指标示例-分位点  ############
# （10）quantile value #
np.percentile(df.iloc[:, 0], (1, 5, 25, 50, 75, 95, 99))

df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)]  # 去除缺失值
np.percentile(df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)], (1, 5, 25, 50, 75, 95, 99))    # 去除缺失值后进行分位点计算


json_quantile = {}

for i, name in enumerate(df.iloc[:, 0: 3].columns):
    print('the {} columns: {}'.format(i, name))
    json_quantile[name] = np.percentile(df[name][~np.isin(df[name], missSet)], (1, 5, 25, 50, 75, 95, 99))

df_quantile = pd.DataFrame(json_quantile)[df.iloc[:, 0: 3].columns].T

# ########   统计指标示例-频数  ############
# (11) Frequent Values #
df.iloc[:, 0].value_counts().iloc[0: 5, ]

df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)]  # 去除缺失值
df.iloc[:, 0][~np.isin(df.iloc[:, 0], missSet)].value_counts()[0: 5]  # 去除缺失值后进行频数的计算


json_fre_name = {}
json_fre_count = {}


def fill_free_top_5(x):
    if(len(x)) <= 5:
        new_array = np.full(5, np.nan)
        new_array[0: len(x)] = x
        return new_array

df['ind_var1_0'].value_counts()
df['imp_sal_var16_ult1'].value_counts()

for i, name in enumerate(df[['ind_var1_0', 'imp_sal_var16_ult1']].columns):
    # #1. Index Name
    index_name = df[name][~np.isin(df[name], missSet)].value_counts().iloc[0: 5, ].index.values
    # #1.1 If th length of array is less than 5
    index_name = fill_free_top_5(index_name)
    json_fre_name[name] = index_name
    # #2. Value Count
    values_count = df[name][~np.isin(df[name], missSet)].value_counts().iloc[0: 5, ].index.values
    # #2.1 If th length of array is less than 5
    values_count = fill_free_top_5(values_count)
    json_fre_count[name] = values_count

df_fre_name = pd.DataFrame(json_fre_name)[df[['ind_var1_0', 'imp_sal_var16_ult1']].columns].T
df_fre_count = pd.DataFrame(json_fre_count)[df[['ind_var1_0', 'imp_sal_var16_ult1']].columns].T

df_fre = pd.concat([df_fre_name, df_fre_count], axis=1)


# ########   统计指标示例-缺失值  ############
# (12) Miss Values #
np.sum(np.isin(df.iloc[:, 0], missSet))   # 统计缺失值
df_miss = df.iloc[:, 0: 3].apply(lambda x: np.sum(np.isin(x, missSet)))   # 遍历每一个遍历的缺失值情况