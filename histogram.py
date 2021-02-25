import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import sys
import math
import time
import datetime

def bin(data):
	return np.linspace(min(data), max(data), 100)


def main():
	df = pd.read_csv(r'dataset_train.csv')
	colors = {
		"Birthday":							"#9C27B0",
		"Best Hand":						"#F44336",
		"Arithmancy":						"#03A9F4",
		"Astronomy":						"#FFEE58",
		"Herbology":						"#4CAF50",
		"Defense Against the Dark Arts":	"#FBC02D",
		"Divination":						"#A5D6A7",
		"Muggle Studies":					"#7B1FA2",
		"Ancient Runes":					"#D32F2F",
		"History of Magic":					"#90CAF9",
		"Transfiguration":					"#EF9A9A",
		"Potions":							"#0277BD",
		"Care of Magical Creatures":		"#FFF59D",
		"Charms":							"#558B2F",
		"Flying":							"#CE93D8",
		"Year":								"#81C784",
		"Month":							"#8E24AA",
		"Day":								"#F44336"
	}

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
		plt.hist(df[column], bins=bin(df[column]), color=colors[column], label=column)
		plt.legend(loc='upper right')
	plt.show()

if __name__ == '__main__':
	main()