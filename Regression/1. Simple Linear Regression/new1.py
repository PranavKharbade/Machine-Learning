# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:50:47 2018

@author: Pranav
import pandas as pd 
import os 
os.getcwd()
import matplotlib.pyplot as plt
import pandas as pd
#importing dataset
dataset=pd.read_csv('Movie-Ratings.csv')
len(dataset) 
dataset.head() 
dataset.columns 
dataset.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 
       'BudgetMillions', 'Year'] 
movies=dataset
movies.head()
movies.info()
movies.Film=movies.Film.astype('category')
movies.Genre=movies.Genre.astype('category')
movies.Year=movies.Year.astype('category')
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
j=sns.jointplot(data=movies,x='CriticRating',y='AudienceRating',kind='hex')
m=sns.distplot(movies.AudienceRating,bins=15)
m1=sns.distplot(movies.CriticRating,bins=15)
m2=plt.hist(movies.CriticRating,bins=15)
m3=plt.hist(movies.BudgetMillions)
movies[FilterDrama]
movies[FilterDrama].BudgetMillions
m4=plt.hist(movies[movies.Genre=='Drama'].BudgetMillions)
m4=plt.hist(movies[movies.Genre=='Action'].BudgetMillions)
m4=plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions,bins=15)
m4=plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions)
plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions,\
                        movies[movies.Genre=='Action'].BudgetMillions,\
                       bins=10, stacked=True)
plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions,\
                        movies[movies.Genre=='Action'].BudgetMillions,\
                       bins=15, stacked=True)
v1=sns.implot(data=movies,x='CriticRating',y='AudienceRating',fit_reg=False,\
                                      hue='Genre',size=1,aspect=7)
plt.hist([movies[movies.Genre=='Action'].BudgetMillions,\ 
               movies[movies.Genre=='Drama'].BudgetMillions,\ 
                    movies[movies.Genre=='Thriller'].BudgetMillions],\ 
                        bins=15,stacked=True)
plt.hist([movies[movies.Genre=='Action'].BudgetMillions, \ 
   movies[movies.Genre=='Drama'].BudgetMillions], \ 
   bins=15,stacked=True) 
for gen in movies.Genre.cat.categories: 
 print(gen)
 for gen in movies.Genre.cat.categories: 
        list1.append(movies[movies.Genre==gen].BudgetMillions
        print(list1)
