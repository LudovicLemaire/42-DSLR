import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import sys
import math
import time
import datetime
import utils
import itertools

def main():
	df = utils.dataframe()
	colors = utils.colors()

	df = df.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])

	sns.set_theme()
	sns.pairplot(df, hue="Hogwarts House")


	plt.show()

if __name__ == '__main__':
	main()
