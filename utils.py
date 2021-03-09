import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv, argparse
import sys
import math
from collections import Counter

def get_house():
	return ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff']

def get_house_id(name):
	house = { 'Ravenclaw': 0, 'Slytherin': 1, 'Gryffindor': 2, 'Hufflepuff': 3 }
	return house[name]

def colors():
	colors = {
		'Birthday':							'#9C27B0',
		'Best Hand':						'#F44336',
		'Arithmancy':						'#03A9F4',
		'Astronomy':						'#FFEE58',
		'Herbology':						'#4CAF50',
		'Defense Against the Dark Arts':	'#FBC02D',
		'Divination':						'#A5D6A7',
		'Muggle Studies':					'#7B1FA2',
		'Ancient Runes':					'#D32F2F',
		'History of Magic':					'#90CAF9',
		'Transfiguration':					'#EF9A9A',
		'Potions':							'#0277BD',
		'Care of Magical Creatures':		'#FFF59D',
		'Charms':							'#558B2F',
		'Flying':							'#CE93D8',
		'Year':								'#81C784',
		'Month':							'#8E24AA',
		'Day':								'#F44336'
	}
	return colors

def colors_house():
	colors_house = {
		'Ravenclaw': '#015783',
		'Slytherin': '#25a148',
		'Gryffindor': '#c91018',
		'Hufflepuff': '#ffd63b'
	}
	return colors_house

def dataframe():
	df = pd.read_csv(r'dataset_train.csv')
	return df

def sigmoid(z):
	return(1 / (1 + np.exp(-z)))

def variance(array, ddof=1):
	n = len(array)
	mean = sum(array) / n
	return sum((x - mean) ** 2 for x in array) / (n - ddof)

def stdev(array):
	if (len(array) == 1):
		return 0
	var = variance(array)
	std_dev = math.sqrt(var)
	return std_dev

def calc_quantile(array, q):
	array = array.sort_values(ascending=True).to_numpy()
	n = len(array)
	index = (n - 1) * q
	if int(index) == index:
		return array[int(index)]
	fraction = index - int(index)
	left = int(index)
	right = left + 1
	i, j = array[left], array[right]
	return i + (j - i) * fraction

def rgb2hex(rgb):
	return '#%02x%02x%02x' % rgb

def hex2rgb(hexa):
	return tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))

def combine_hex_values(c1, c2):
	rgb1 = hex2rgb(c1[1:])
	rgb2 = hex2rgb(c2[1:])
	final_rgb = (int((rgb1[0] + rgb2[0]) / 2), int((rgb1[1] + rgb2[1]) / 2), int((rgb1[2] + rgb2[2]) / 2))
	return rgb2hex(final_rgb)

def get_valuable_dataframe():
	df_complete = dataframe()
	df = pd.DataFrame()

	df['Hogwarts House'] = df_complete['Hogwarts House']
	df['Ancient Runes'] = df_complete['Ancient Runes']
	df['Defense Against the Dark Arts'] = df_complete['Defense Against the Dark Arts']
	df['Herbology'] = df_complete['Herbology']
	df['Divination'] = df_complete['Divination']

	return df

def show_standardize(x, y, house, df, feature_1, feature_2, theta):
	plt.style.use('dark_background')
	plt.figure()
	is_house , not_house = (y==1).reshape(len(x[:,0]),1) , (y==0).reshape(len(x[:,2]),1)
	plt.scatter(x[is_house[:,0],1], x[is_house[:,0],2], c='#008FFB', marker='D', s=4, alpha=0.35)
	plt.scatter(x[not_house[:,0],1], x[not_house[:,0],2], c='#FF4560', marker='s', s=4, alpha=0.35)
	x_value = np.array([np.min(x[not_house[:,0],1]),np.max(x[not_house[:,0],1])])
	y_value = -(theta[0] + theta[1]*x_value)/theta[2]
	plt.xlabel(df.columns[feature_1])
	plt.ylabel(df.columns[feature_2])
	plt.legend([house, 'Other'],loc=0)
	plt.title(df.columns[feature_1] + ' vs ' + df.columns[feature_2] + ': standardized data')
	plt.plot(x_value, y_value, '#00E396', alpha=0.5)
	plt.show()

def show_cost(error_history):
	plt.style.use('dark_background')
	plt.figure()
	plt.plot(range(len(error_history)), error_history, c='#FF4560')
	plt.ylabel('Cost')
	plt.xlabel('Iteration')
	plt.title('Cost function graph')
	plt.show()

def show_repartition(house_pred, house_real):
	plt.style.use('dark_background')
	clrs = colors_house()

	wrongs = []
	for i, v in enumerate(house_pred):
		if not (house_pred[i] == house_real[i]):
			wrongs.append(i)
	print('\033[91m', end='')
	print('Failed to predict: \033[0m', end='')
	print(wrongs)

	plt.subplot(1, 2, 1)
	counts = Counter(house_pred)
	common = counts.most_common()
	labels = [item[0] for item in common]
	number = [item[1] for item in common]
	nbars = len(common)
	plt.bar(np.arange(nbars), number, tick_label=labels, color=[clrs['Hufflepuff'], clrs['Ravenclaw'], clrs['Gryffindor'], clrs['Slytherin']])
	for i, v in enumerate(counts):
		plt.text(i-0.12, number[i]+5, str(number[i]))
	plt.title('My prediction')

	plt.subplot(1, 2, 2)
	counts = Counter(house_real)
	common = counts.most_common()
	labels = [item[0] for item in common]
	number = [item[1] for item in common]
	nbars = len(common)
	plt.bar(np.arange(nbars), number, tick_label=labels, color=[clrs['Hufflepuff'], clrs['Ravenclaw'], clrs['Gryffindor'], clrs['Slytherin']])
	for i, v in enumerate(counts):
		plt.text(i-0.12, number[i]+5, str(number[i]))
	plt.title('The subject')

	plt.show()

def filter_data(data, house, feature_1, feature_2):
	x = []
	y = []
	data = data.to_numpy()
	for row in data:
		if not np.isnan(row[feature_1]) and not np.isnan(row[feature_2]):
			x.append([row[feature_1], row[feature_2]])
			y.append(1 if row[0] == house else 0)
	return np.array(x), np.array(y)

def create_csv(row_list, name):
	with open(name, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(row_list)