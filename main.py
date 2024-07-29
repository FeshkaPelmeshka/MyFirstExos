"""
author:Natalia"""
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv', encoding="ISO-8859-1")

df[['Termd', 'EngagementSurvey']].boxplot()
plt.show()







