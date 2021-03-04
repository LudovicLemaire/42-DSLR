import pandas as pd
import numpy as np
import sys
import math
import utils

def predict(features, weights):
  z = np.dot(features, weights)
  return sigmoid(z)

def sigmoid(z):
	return 1.0 / (1 + np.exp(-z))

def cost_function(features, labels, weights):
	# Using Mean Absolute Error
	# Returns 1D matrix of predictions
	# Cost = (labels*log(predictions) + (1-labels)*log(1-predictions) ) / len(labels)
	observations = len(labels)
	predictions = predict(features, weights)
	class1_cost = -labels*np.log(predictions)
	class2_cost = (1-labels)*np.log(1-predictions)
	cost = class1_cost - class2_cost
	cost = cost.sum() / observations
	return cost

def update_weights(features, labels, weights, lr):
	# Vectorized Gradient Descent
	N = len(features)
	predictions = predict(features, weights)
	gradient = np.dot(features.T,  predictions - labels)
	gradient /= N
	gradient *= lr
	weights -= gradient
	return weights

def accuracy(predicted_labels, actual_labels):
	diff = predicted_labels - actual_labels
	return 1.0 - (float(np.count_nonzero(diff)) / len(diff))

def train(features, labels, weights, lr, iters):
	cost_history = []
	for i in range(iters):
		weights = update_weights(features, labels, weights, lr)
		# Calculate error
		cost = cost_function(features, labels, weights)
		cost_history.append(cost)
		# Log Progress
		if i % 1000 == 0:
			print("iter: " + str(i) + " cost: " + str(cost))
	return weights, cost_history

def classify(predictions):
	decision_boundary = np.vectorize(decision_boundary)
	return decision_boundary(predictions).flatten()

def decision_boundary(prob):
	return 1 if prob >= .5 else 0

def get_valuable_dataframe():
	df_complete = utils.dataframe()
	df = pd.DataFrame()

	df['Hogwarts House'] = df_complete['Hogwarts House']
	df['Ancient Runes'] = df_complete['Ancient Runes']
	df['Astronomy'] = df_complete['Astronomy']
	df['Charms'] = df_complete['Charms']
	df['Divination'] = df_complete['Divination']
	df['Flying'] = df_complete['Flying']
	df['Herbology'] = df_complete['Herbology']
	df['Transfiguration'] = df_complete['Transfiguration']
	return df

def main():
	df = get_valuable_dataframe()
	print(df.describe())

if __name__ == '__main__':
	main()