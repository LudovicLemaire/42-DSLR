import numpy as np
import utils

def standardize(x):
	mean = np.mean(x, axis=0)
	std = np.std(x, axis=0)
	return (x - mean) / std, mean, std

def get_cost(y, m, h0):
	return (-(1/m) * sum(y * np.log(h0) + (1 - y) * np.log(1 - h0)))[0]

def get_theta(x, y, theta, lr, epoch, verb_cost):
	history_err = []
	for i in range(epoch):
		m = len(x)
		h0 = utils.sigmoid(np.dot(x, theta))
		grad = 1/m * np.dot(x.transpose(), (h0 - y))
		theta -= lr * grad
		if verb_cost == True:
			history_err.append(get_cost(y, m, h0))
	theta = [theta[0][0], theta[1][0], theta[2][0]]
	return theta, history_err

def get_point(x, theta):
	return (-(theta[0] + theta[1] * x) / theta[2])

def get_accuracy(x, y, theta):
	length = len(x)
	correct = 0
	for i in range(length):
		prediction = 1 if sigmoid(x[i].dot(theta)) >= 0.5 else 0
		correct = correct + 1 if y[i] == prediction else correct
	return (correct / length)

def sigmoid(z):
	return(1 / (1 + np.exp(-z)))

if __name__ == '__main__':
	min_accuracy = 0.975
	iteration = 5000
	learning_rate = 1.75
	verb_print = True
	verb_standardize = False
	verb_cost = False
	df = utils.get_valuable_dataframe()
	house = utils.get_house()
	row_list = [['House', 'Feature1', 'Feature2', 'Theta1', 'Theta2', 'Theta3', 'Mean1', 'Mean2', 'Std1', 'Std2', 'Accuracy']]
	for i in range(0, len(house)):
		if verb_print == True:
			print('\n\033[93m' + house[i] + '\033[0m')
		for feature_1 in range(1, len(df.columns)):
			for feature_2 in range(feature_1 + 1, len(df.columns)):
				x, y = utils.filter_data(df, house[i], feature_1, feature_2)
				x, mean, std = standardize(x)
				col, row = x.shape[0], x.shape[1]
				x = np.insert(x, 0, 1, axis=1)
				y = y.reshape(col, 1)
				theta = np.zeros((row + 1, 1))
				theta, history_err = get_theta(x, y, theta, learning_rate, iteration, verb_cost)
				ac = get_accuracy(x, y, theta)
				if verb_print == True:
					print('\033[94m' + df.columns[feature_1] + '\033[0m', end='')
					print(' vs ', end='')
					print('\033[96m' + df.columns[feature_2] + '\033[0m')

					print('Accuracy: ', end='')
					if ac > min_accuracy:
						print('\033[92m', end='')
					else:
						print('\033[91m', end='')
					print(str(ac) + '\033[0m\n')
				if verb_standardize == True:
					utils.show_standardize(x, y, house[i], df, feature_1, feature_2, theta)
				if verb_cost == True:
					utils.show_cost(history_err)
				if ac >= min_accuracy:
					row_list.append([house[i], df.columns[feature_1], df.columns[feature_2], theta[0], theta[1], theta[2], mean[0], mean[1], std[0], std[1], ac])
	utils.create_csv(row_list, 'weights.csv')
	global_acc = 0
	i = 1
	while i <= len(row_list) - 1:
		global_acc += row_list[i][10]
		i+=1
	print('\033[92m' + 'Average Accuracy: ' + '\033[0m' + str(global_acc/(i-1)))