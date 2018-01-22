#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("train.csv")
label = df['TARGET']
df = df.drop(['ID', 'TARGET'], axis=1)