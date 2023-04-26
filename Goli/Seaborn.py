import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
a=sns.load_dataset("flights")
p=sns.barplot(x="passengers", y="month", data=a)
plt.show()