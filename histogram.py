import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import sys
import math
import time
import datetime
import utils

def bin(data):
	return np.linspace(min(data), max(data), 100)


def main():
	df = utils.dataframe()
	colors = utils.colors()

	df = df.drop(columns=['Index', 'Hogwarts House', 'First Name', 'Last Name'])
	df['Best Hand'] = df['Best Hand'].replace(to_replace=['Left', 'Right'], value=[1, 2])
	df['Year'] = df['Birthday'].apply(lambda x: int(x[0:4]))
	df['Month'] = df['Birthday'].apply(lambda x: int(x[5:7]))
	df['Day'] = df['Birthday'].apply(lambda x: int(x[8:10]))
	df['Birthday'] = df['Birthday'].apply(lambda x: time.mktime(datetime.datetime.strptime(x, "%Y-%m-%d").timetuple()))
	
	nb_columns = 0
	for column in df:
		nb_columns += 1

	i = 1
	for column in df:
		plt.subplot(4, nb_columns / 4 + 1, i)
		i += 1
		plt.hist(df[column], bins=bin(df[column]), color=colors[column], label=column, alpha=0.75, edgecolor='black', linewidth=0.5)
		plt.legend(loc='upper right')
	plt.show()

if __name__ == '__main__':
	main()