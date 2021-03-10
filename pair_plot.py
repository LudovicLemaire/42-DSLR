import matplotlib.pyplot as plt
import seaborn as sns
import utils

def main():
	df = utils.dataframe('dataset_train.csv')
	colors = utils.colors_house()

	df = df.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])

	colors = [colors['Ravenclaw'], colors['Slytherin'], colors['Gryffindor'], colors['Hufflepuff']]
	sns.set_palette(sns.color_palette(colors))
	sns.pairplot(df, hue="Hogwarts House")

	plt.show()

if __name__ == '__main__':
	main()
