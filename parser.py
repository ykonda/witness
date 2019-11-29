from bs4 import BeautifulSoup
from dateutil.parser import parse as date_parser
import numpy as np
import pandas as pd
from os.path import abspath, join, dirname
from os import listdir
import seaborn as sns
sns.set(style='white', rc={'axes.facecolor':(0, 0, 0, 0)})
import matplotlib.pyplot as plt
import datetime

def get_date(dot_node):
    return date_parser(dot_node.parent.find('div', {'class':'date'}).attrs['title'])

html = open(join(dirname(abspath(__file__)), 'data/messages.html'), 'r').read()
# html = open('data/messages.html', 'r').read()
soup = BeautifulSoup(html)
date_list = []
for val in soup.find_all('div', {'class':'text'}):
    if val.text.strip() == '.':
        date_list.append(get_date(val))

df = pd.DataFrame()
df['date'] = date_list
df['weekday'] = df.date.apply(lambda x: x.weekday_name)
df['hour'] = df.date.apply(lambda x: (x.hour+9)%24)

pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row='weekday', palette=pal)
g.map(sns.distplot, 'hour', kde=False, bins=24)
plt.show()