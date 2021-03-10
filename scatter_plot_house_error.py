import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import numpy as np
import sys
import math
import time
import datetime
import utils
import itertools

def main():
	#matplotlib.use('webagg')

	'''
		'Arithmancy',
		'Astronomy',
		'Herbology',
		'Defense Against the Dark Arts',
		'Divination',
		'Muggle Studies',
		'Ancient Runes',
		'History of Magic',
		'Transfiguration',
		'Potions',
		'Care of Magical Creatures':,
		'Charms',
		'Flying',
	'''
	iterable = [
		'Astronomy',
		'Herbology',
		'Ancient Runes',
		'Divination',
	]
	plt.style.use('dark_background')

	colors_house = utils.colors_house()


	df = utils.dataframe('dataset_train.csv')
	colors = utils.colors()

	df_house = df['Hogwarts House']

	allIterables = list(itertools.combinations(iterable, 2))
	nb_columns = 0
	for column in allIterables:
		nb_columns += 1

	i = 1
	for el in allIterables:
		plt.subplot(math.ceil(nb_columns / 3 + 1), 3, i)
		i += 1
		plt.scatter(df[el[0]], df[el[1]], c=df['Hogwarts House'].map(colors_house), alpha=0.25, label=[el[0][:10], el[1][:10]], marker='o', s=2)
		df_errors = df.loc[[184, 200, 255, 339, 443, 445, 456, 504, 515, 618, 681, 704, 815, 820, 824, 915, 941, 1078, 1098, 1113, 1191, 1282, 1419, 1435, 1444, 1446, 1448, 1515, 1525, 1596]]
		plt.scatter(df_errors[el[0]], df_errors[el[1]], c=df_errors['Hogwarts House'].map(colors_house), marker='x')
		plt.xticks([])
		plt.yticks([])
		plt.legend(loc='upper right', fontsize=5)
	plt.show()

	print() 


if __name__ == '__main__':
	main()
