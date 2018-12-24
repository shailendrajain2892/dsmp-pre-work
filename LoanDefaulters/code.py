# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico']>700])/len(df)
p_b = len(df[df['purpose'] == "debt_consolidation"])/len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
p_b_a = len(df1[df1['fico']>700])/len(df1)
p_a_b = (p_b * p_b_a)/p_a
result = (p_a_b == p_a)
print(result)
# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)
prob_cs = len(df[df['credit.policy']=='Yes'])/len(df)
new_df = df[df['paid.back.loan']=='Yes']
prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)


# code ends here


# --------------
# code starts here
df.purpose.value_counts(normalize=True).plot(kind='bar')
df1 = df[df['paid.back.loan']=="No"]
df1.purpose.value_counts(normalize=True).plot(kind='bar')
# code ends here


# --------------
# code starts here
inst_median = df.installment.median()
inst_mean = df.installment.mean()
df['installment'].hist(normed=True, bins=50)
df['log.annual.inc'].hist()

# code ends here


