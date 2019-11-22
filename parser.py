from bs4 import BeautifulSoup
from dateutil.parser import parse as date_parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def get_date(dot_node):
    return date_parser(dot_node.parent.find('div', {'class':'date'}).attrs['title'])

html = open('data/messages.html', 'r').read()
soup = BeautifulSoup(html)
date_list = []
for val in soup.find_all('div', {'class':'text'}):
    if val.text.strip() == '.':
        date_list.append(get_date(val))

hours_counts = np.zeros(24)
for date in date_list:
    hours_counts[date.hour] += 1

hours_counts = np.roll(hours_counts, 9)
x_axis = np.linspace(0, 23, 24)
plt.bar(x_axis, hours_counts)
plt.show()
