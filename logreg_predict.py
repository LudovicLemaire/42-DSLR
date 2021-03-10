import numpy as np
import pandas as pd
import utils
import sys

def predict_house(student, weights):
	results = [[], [], [], []]
	house_rev = utils.get_house()
	for row in weights:
		if not np.isnan(student[row[1]]) and not np.isnan(student[row[2]]):
			x = np.array([student[row[1]], student[row[2]]])
			theta = np.array([row[3], row[4], row[5]])
			mean = np.array([row[6], row[7]])
			std = np.array([row[8], row[9]])
			x = (x - mean) / std
			x = np.insert(x, 0, 1, axis=0)
			results[utils.get_house_id(row[0])].append(utils.sigmoid(np.dot(x, theta)))
	for i in range(4):
		if (len(results[i]) != 0):
			# results[i] = max(results[i])
			results[i] = sum(results[i]) / len(results[i])
		else:
			results[i] = 0
	return house_rev[results.index(max(results))]

def get_accuracy(house_pred, house_real):
	is_ok = 0
	for i in range(len(house_real)):
		if (house_real[i] == house_pred[i]):
			is_ok += 1
	return is_ok / len(house_real)

def contain_value_from_train(df):
	df = df[["Hogwarts House"]]
	if df.isnull().values.any() == True:
		return 0
	return 1

if __name__ == "__main__":
	student_results = []
	if not (len(sys.argv) == 2+1):
		print('\033[91m' + '✘ Error: ' + '\033[0m' + 'CSV files are missing, please add .csv to predict as argument, then weight')
		print('\033[94m' + 'Example: ' + '\033[0m' + 'python3.9 logreg_predict.py dataset_test.csv weights.csv')
		sys.exit()
	df = pd.read_csv(sys.argv[1])
	weights = pd.read_csv(sys.argv[2])
	show_chart = True
	
	row_list = [["Index", "Hogwarts House"]]
	
	for i in range(len(df)):
		tmp = predict_house(df.loc[i], weights.to_numpy())
		student_results.append(tmp)
		row_list.append([i, tmp])
	if (contain_value_from_train(df)):
		accuracy = get_accuracy(df["Hogwarts House"].tolist(), student_results)
		print("Accuracy: ", end='')
		if accuracy >= 0.98:
			print('\033[92m', end='')
		else:
			print('\033[91m', end='')
		print(accuracy, '\033[0m')
		
		if (show_chart == True):
			utils.show_repartition(student_results, df["Hogwarts House"].tolist())
	else:
		print('\033[93m' + '⚠ Houses are missing, pls provide a csv with them if you want to see Accuracy.' + '\033[0m')
	utils.create_csv(row_list, "houses.csv")
	