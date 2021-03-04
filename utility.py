import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv, argparse

house = { "Ravenclaw": 1, "Slytherin": 2, "Gryffindor": 3, "Hufflepuff": 4 }
house_rev = { value: key for key, value in house.items() }
f1 = -1
f2 = -1
h = 0

def display_data(x, y, house, df, f1, f2):
	plt.figure()
	pos , neg = (y==1).reshape(len(x[:,0]),1) , (y==0).reshape(len(x[:,1]),1)
	plt.scatter(x[pos[:,0],0],x[pos[:,0],1],c="r",marker="+")
	plt.scatter(x[neg[:,0],0],x[neg[:,0],1],marker="o",s=10)
	plt.xlabel(df.columns[f1])
	plt.ylabel(df.columns[f2])
	plt.legend([house, "Not " + house],loc=0)
	plt.title("Feature1 vs Feature2 data")
	plt.show()

def display_standardize(x, y, house, df, f1, f2, theta):
	plt.figure()
	pos , neg = (y==1).reshape(len(x[:,0]),1) , (y==0).reshape(len(x[:,2]),1)
	plt.scatter(x[pos[:,0],1],x[pos[:,0],2],c="r",marker="+")
	plt.scatter(x[neg[:,0],1],x[neg[:,0],2],marker="o",s=10)
	x_value = np.array([np.min(x[:,1]),np.max(x[:,1])])
	y_value = -(theta[0] + theta[1]*x_value)/theta[2]
	plt.xlabel(df.columns[f1])
	plt.ylabel(df.columns[f2])
	plt.legend([house, "Not " + house],loc=0)
	plt.title("Feature1 vs Feature2 standardized data")
	plt.plot(x_value, y_value, "g")
	plt.show()

def display_cost(error_history):
	plt.figure()
	plt.plot(range(len(error_history)), error_history)
	plt.ylabel("Cost")
	plt.xlabel("Iteration")
	plt.title("Cost function graph")
	plt.show()

def check_dataset(dataset):
	try :
		pd.read_csv(dataset)
	except :
		raise argparse.ArgumentTypeError("invalid dataset, needs to be a csv file")
	return dataset

def check_input(v):
	global h
	global f2
	global f1
	if h == 0 and v in house:
		h = house[v]
		return house[v]
	try :
		int(v)
	except:
		raise argparse.ArgumentTypeError("Invalid input for features, arg '{}' needs to be a number".format(v))
	if h != 0 and int(v) >= 1 and int(v) <= 7 :
		if f1 == -1:
			f1 = int(v)
			if f1 == 7:
				f1 = 6
				print("Value of Feature1 changed to", f1)
			return f1
		elif f2 == -1:
			f2 = int(v)
			if f2 <= f1:
				f2 = f1 + 1
				print("Value of Feature2 changed to", f2)
			return f2
	if h == 0 and v not in house:
		raise argparse.ArgumentTypeError("'{}' is not a valid house. Choose between Ravenclaw, Slytherin, Gryffindor or Hufflepuff".format(v))
	raise argparse.ArgumentTypeError("Invalid input for features, arg '{}' needs to be beetween 1 and 7 (included)".format(v))

def pie_chart(results, title):
	labels = []
	sizes = []
	for i in results:
		if (not i in labels):
			labels.append(i)
			sizes.append(0)
	for i in results:
		sizes[labels.index(i)] += 1
	plt.figure()
	plt.title(title)
	plt.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)
	plt.show()

def get_data_visual(usage, param):
	parser = argparse.ArgumentParser(description=usage)
	parser.add_argument("dataset", type=check_dataset, help="dataset, needs to be a csv")
	if (param == 2) :
		parser.add_argument("weights", type=check_dataset, help="weights, needs to be a csv")
		parser.add_argument("-a", "--accuracy", action="store_true", help="show accuracy for dataset_train")
		parser.add_argument("-p", "--piechart", action="store_true", help="print a piechart for the results")
		args = parser.parse_args()
		args.piechart = 1 if args.piechart is True else 0
		if args.accuracy is True :
			return pd.read_csv(args.dataset), pd.read_csv(args.weights), 1, args.piechart
		return pd.read_csv(args.dataset), pd.read_csv(args.weights), 0, args.piechart
	if (param == 1) :
		parser.add_argument("-v", "--verbose", action="store_true", help="display in real time actions of training")
		parser.add_argument("-vi", type=check_input, nargs=3, metavar=('House','N_feature1', "N_feature2"), help="display data of one house in a separate windows")
		args = parser.parse_args()
		args.verbose =  1 if args.verbose is True else 0
		if args.vi is not None :
			return pd.read_csv(args.dataset), args.vi[0], args.vi[1], args.vi[2], args.verbose
		return pd.read_csv(args.dataset), 0, 0, 0, args.verbose
	args = parser.parse_args()
	return pd.read_csv(args.dataset)

def filter_data(data, house, f1, f2):
	x = []
	y = []
	data = data.to_numpy()
	for row in data:
		if not np.isnan(row[f1]) and not np.isnan(row[f2]):
			x.append([row[f1], row[f2]])
			y.append(1 if row[0] == house else 0)
	return np.array(x), np.array(y)

def sigmoid(z):
	return(1 / (1 + np.exp(-z)))

def create_csv(row_list, name):
	with open(name, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(row_list)