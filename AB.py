import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
#We are setting the seed to assure you get the same answers on quizzes as we set up
random.seed(42)

ab=pd.read_csv('ab_data.csv')

pold=ab.query('group=="control"')['converted'].mean()
pnew=ab.query('group=="treatment"')['converted'].mean()
obs=pold-pnew
diffs = []
for _ in range(10000):
    samp=ab.sample(ab.shape[0],replace=True)
    pold_s=samp.query('group=="control"')['converted'].mean()
    pnew_s=samp.query('group=="treatment"')['converted'].mean()
    diffs.append(pold_s-pnew_s)
plt.hist(diffs)
