# -*- coding: utf-8 -*-
"""p138

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-tHBdI26UtSS_nyAgwksmKi9PyPkF7L_
"""

!pip install kaggle

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d gspmoreira/articles-sharing-reading-from-cit-deskdrop

!ls

!unzip articles-sharing-reading-from-cit-deskdrop.zip

!ls

import pandas as pd 
import numpy as np 

df1=pd.read_csv('shared_articles.csv')
df2=pd.read_csv('users_interactions.csv')

df1.head()

df2.head()