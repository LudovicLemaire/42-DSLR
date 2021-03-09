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
	iterable = [
		'Astronomy',
		'Herbology',
		'Ancient Runes',
		'Charms',
		'Transfiguration',
		'Divination',

	]
	plt.style.use('dark_background')

	colors_house = utils.colors_house()

	df = utils.dataframe()
	colors = utils.colors()

	df_house = df['Hogwarts House']
	df = df.drop(columns=[
		'Index',
		'First Name',
		'Last Name',
		'Arithmancy',
		'Defense Against the Dark Arts',
		'Muggle Studies',
		'History of Magic',
		'Potions',
		'Care of Magical Creatures',
		'Flying',
		
	])

	allIterables = list(itertools.combinations(iterable, 2))
	nb_columns = 0
	for column in allIterables:
		nb_columns += 1

	i = 1
	for el in allIterables:
		plt.subplot(nb_columns / 4 + 1, 4, i)
		i += 1
		plt.scatter(df[el[0]], df[el[1]], c=df['Hogwarts House'].map(colors_house), alpha=0.25, label=[el[0][:10], el[1][:10]], marker='o', s=2)
		plt.xticks([])
		plt.yticks([])
		plt.legend(loc='upper right', fontsize=5)
	plt.show()

if __name__ == '__main__':
	main()
