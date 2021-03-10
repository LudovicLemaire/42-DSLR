import pandas as pd
import numpy as np
import utils
import json
import sys
import math	

def describe(dico_objects):
	ordered_describe = ['count', 'unique', 'top', 'freq']
	dico_size_chars = {}
	for label in dico_objects:
		dico_size_chars[label] = len(label) + 2
		for label2 in ordered_describe:
			if len(str(dico_objects[label][label2])) + 2 > dico_size_chars[label]:
				dico_size_chars[label] = len(str(dico_objects[label][label2])) + 2

	sys.stdout.write('\033[95m')
	sys.stdout.write('{0: <6}'.format(''))
	for label in sorted(dico_size_chars):
		sys.stdout.write('{message: >{width}}'.format(message=label, width=dico_size_chars[label]))
	sys.stdout.write('\n')
	sys.stdout.write('\033[0m')
	sys.stdout.flush()
	for label_type in ordered_describe:
		sys.stdout.write('\033[96m{0: <6}\033[0m'.format(label_type))
		for label in sorted(dico_size_chars):
			sys.stdout.write('{message: >{width}}'.format(message=dico_objects[label][label_type], width=dico_size_chars[label]))
		sys.stdout.write('\n')
		sys.stdout.flush()

def main():
	df2 = pd.DataFrame()
	if not (len(sys.argv) == 1+1):
		print('\033[91m' + '✘ Error: ' + '\033[0m' + 'CSV file is missing, please add his path as argument')
		sys.exit()
	df = utils.dataframe(sys.argv[1])
	columnsNamesArr = df.columns.values
	listOfColumnNames = list(columnsNamesArr)

	dico_objects = {} 
	for label in listOfColumnNames:
		if df[label].dtypes == str or df[label].dtypes == object:
			dico_objects[label] = {
				'count': 0,
				'unique': 0,
				'top': 0,
				'freq': 0,
				'all': {}
			}
		
	for label in listOfColumnNames:
		if df[label].dtypes == str or df[label].dtypes == object:
			for index, row in df.iterrows():
				if (isinstance(row[label], float) and np.isnan(row[label])):
					continue
				dico_objects[label]['count']+=1
				if row[label] in dico_objects[label]['all']:
					dico_objects[label]['all'][row[label]]+=1
				else:
					dico_objects[label]['all'][row[label]] = 1

	for label in dico_objects:
		i = 0
		for k in dico_objects[label]['all']:
			i+=1
			if dico_objects[label]['all'][k] > dico_objects[label]['freq']:
				dico_objects[label]['freq'] = dico_objects[label]['all'][k]
				dico_objects[label]['top'] = k
		dico_objects[label]['unique'] = i

	describe(dico_objects)


if __name__ == '__main__':
	main()