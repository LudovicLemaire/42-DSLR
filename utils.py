import pandas as pd
import numpy as np
import sys
import math

def colors():
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
	return colors

def colors_house():
	colors_house = {
		"Ravenclaw": "#409EFF",
		"Slytherin": "#F56C6C",
		"Gryffindor": "#67C23A",
		"Hufflepuff": "#E6A23C"
	}
	return colors_house

def dataframe():
	df = pd.read_csv(r'dataset_train.csv')
	return df

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