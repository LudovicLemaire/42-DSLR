from utility import house_rev, display_data, display_standardize, display_cost, get_data_visual, filter_data, sigmoid, create_csv
import numpy as np

def standardize(x):
	mean = np.mean(x, axis=0)
	std = np.std(x, axis=0)
	return (x - mean) / std, mean, std

def cost_function(x, y, theta):
	m = len(x)
	h0 = sigmoid(np.dot(x, theta))
	return (-(1/m) * sum(y * np.log(h0) + (1 - y) * np.log(1 - h0)))[0]

def d_cost_function(x, y, theta):
	m = len(x)
	h0 = sigmoid(np.dot(x, theta))
	grad = 1/m * np.dot(x.transpose(), (h0 - y))
	return grad

def train_theta(x, y, theta, lr, epoch):
	error_history = []
	for i in range(epoch):
		theta -= lr * d_cost_function(x, y, theta)
		error_history.append(cost_function(x, y, theta))
	return theta, error_history

def compute_point(x, theta):
	return (-(theta[0] + theta[1] * x) / theta[2])

def get_accuracy(x, y, theta):
	length = len(x)
	correct = 0
	for i in range(length):
		prediction = 1 if sigmoid(x[i].dot(theta)) >= 0.5 else 0
		correct = correct + 1 if y[i] == prediction else correct
	return (correct / length) * 100

if __name__ == "__main__":
	df, visu, f1v, f2v, verbose = get_data_visual("train our model with a dataset", 1)
	df.drop(["Index", "Arithmancy", "Potions", "Charms", "Care of Magical Creatures", "Flying"], axis=1, inplace=True)
	df = df[["Hogwarts House"] + list(df.select_dtypes(include="number").columns)]
	row_list = [["House", "Feature1", "Feature2", "Theta1", "Theta2", "Theta3", "Mean F1", "Mean F2", "Std F1", "Std F2", "Accuracy"]]
	for i in range(1, 5) :
		if verbose == 1:
			print("\n\t\t\t\033[33m", house_rev[i].upper(), "\033[0m\n")
		for f1 in range(1, len(df.columns) - 1) :
			for f2 in range(f1 + 1, len(df.columns) - 1) :
				x, y = filter_data(df, house_rev[i], f1, f2)
				if verbose == 1:
					print(df.columns[f1], " vs ",df.columns[f2])
				if visu != 0 and i == visu and f1 == f1v and f2 == f2v:
					display_data(x, y, house_rev[i], df, f1, f2)
				x, mean, std = standardize(x)
				col, row = x.shape[0], x.shape[1]
				x = np.insert(x, 0, 1, axis=1)
				y = y.reshape(col, 1)
				theta = np.zeros((row + 1, 1))
				theta, error_history = train_theta(x, y, theta, 1, 400)
				if visu != 0 and i == visu and f1 == f1v and f2 == f2v:
					display_standardize(x, y, house_rev[i], df, f1, f2, theta)
					display_cost(error_history)
				ac = get_accuracy(x, y, theta)
				if verbose == 1:
					print("\t\t\t\t\t\t\t\033[36mAccuracy: {}\033[0m".format(ac))
				if ac >= 97 :
					row_list.append([house_rev[i], df.columns[f1], df.columns[f2], theta[0][0], theta[1][0], theta[2][0], mean[0], mean[1], std[0], std[1], ac])
	create_csv(row_list, "weights.csv")
	print("Weights saved in './weights.csv'")