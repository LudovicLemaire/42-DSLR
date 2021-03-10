import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import sys
import math
import time
import datetime
import utils
import itertools

def main():
	iterable = [
		"Birthday",
		"Best Hand",
		"Arithmancy",
		"Astronomy",
		"Herbology",
		"Defense Against the Dark Arts",
		"Divination",
		"Muggle Studies",
		"Ancient Runes",
		"History of Magic",
		"Transfiguration",
		"Potions",
		"Care of Magical Creatures",
		"Charms",
		"Flying",
		"Year",
		"Month",
		"Day"
	]

	df = utils.dataframe('dataset_train.csv')
	colors = utils.colors()

	df = df.drop(columns=['Index', 'Hogwarts House', 'First Name', 'Last Name'])
	df['Best Hand'] = df['Best Hand'].replace(to_replace=['Left', 'Right'], value=[1, 2])
	df['Year'] = df['Birthday'].apply(lambda x: int(x[0:4]))
	df['Month'] = df['Birthday'].apply(lambda x: int(x[5:7]))
	df['Day'] = df['Birthday'].apply(lambda x: int(x[8:10]))
	df['Birthday'] = df['Birthday'].apply(lambda x: time.mktime(datetime.datetime.strptime(x, "%Y-%m-%d").timetuple()))


	allIterables = list(itertools.combinations(iterable, 2))

	nb_columns = 0
	for column in allIterables:
		nb_columns += 1

	i = 1
	for el in allIterables:
		plt.subplot(7, math.ceil(nb_columns / 7 + 1), i)
		i += 1
		plt.scatter(df[el[0]], df[el[1]], color=utils.combine_hex_values(colors[el[0]], colors[el[1]]), alpha=0.25, label=[el[0], el[1]], s=3)
		plt.xticks([])
		plt.yticks([])
		plt.legend(loc='upper right', fontsize=5)
	plt.show()

if __name__ == '__main__':
	main()
