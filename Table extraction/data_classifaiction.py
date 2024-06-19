import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.tokenize import word_tokenize
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import contractions


# data loading


data = pd.read_csv('./table_dataset.csv', delimiter=';')

df = data[['text', 'interest_table']]
print(df['interest_table'].value_counts())

print('none')