import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import math
import time
import datetime
import utils

def count_vowel(word):
	vowel=0
	for char in word:
		if char.lower() in "aeiouy":
			vowel+=1
	return vowel

def main():
	b_df = utils.dataframe()

	b_df['Year'] = b_df['Birthday'].apply(lambda x: int(x[0:4]))
	b_df['Best Hand'] = b_df['Best Hand'].replace(to_replace=['Left', 'Right'], value=[1, 2])
	b_df['Year'] = b_df['Birthday'].apply(lambda x: int(x[0:4]))
	b_df['Month'] = b_df['Birthday'].apply(lambda x: int(x[5:7]))
	b_df['Day'] = b_df['Birthday'].apply(lambda x: int(x[8:10]))
	b_df['Birthday'] = b_df['Birthday'].apply(lambda x: time.mktime(datetime.datetime.strptime(x, "%Y-%m-%d").timetuple()))

	df = pd.DataFrame()
	df['Hogwarts House'] = b_df['Hogwarts House']
	df['Best Hand'] = b_df['Best Hand']
	df['Year'] = b_df['Year']
	df['Month'] = b_df['Month']
	df['Day'] = b_df['Day']
	df['Birthday'] = b_df['Birthday']
	df['First Name'] = b_df['First Name'].apply(lambda x: int(len(x)))
	df['Last Name'] = b_df['Last Name'].apply(lambda x: int(len(x)))
	df['Last Name Vowel'] = b_df['Last Name'].apply(lambda x: int(count_vowel(x)))
	df['First Name Vowel'] = b_df['First Name'].apply(lambda x: int(count_vowel(x)))
	df['Last Name Consonant'] = b_df['Last Name'].apply(lambda x: int(len(x) - count_vowel(x)))
	df['First Name Consonant'] = b_df['First Name'].apply(lambda x: int(len(x) - count_vowel(x)))
	
	sns.pairplot(df, hue="Hogwarts House")
	plt.show()

if __name__ == '__main__':
	main()
