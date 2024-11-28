-- Import necessary libraries

# importing all necessary libraies
import pandas as pd # type: ignore
import numpy as np # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
from wordcloud import WordCloud # type: ignore

print("import successful")

df = pd.read_csv(r"C:\Users\Pratik Banik\Downloads\UM_Projects\Project_2_Netflix\netflix_titles.csv\netflix_titles.csv")
df.head()
df.info()

#checking for null values
df.isnull().sum()

#checking for duplicated rows
df.duplicated()


