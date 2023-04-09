import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
from scipy import stats


chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: 


alpha = 0.03
p = stats.mannwhitneyu(x, y).pvalue
return p < alpha
