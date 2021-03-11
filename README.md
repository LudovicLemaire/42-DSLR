# DSLR
DataScience x Logistic Regression - School-42 project

#### Goals:
* Learn how to read a dataset, to visualize it in different ways, to select and clean unnecessary information from your data.
* Implement one-vs-all logistic regression that will solve classification problem

Look at [subject.pdf](assets/fr.subject.pdf) for more information

## Requirements:
* `Python 3`
* `NumPy`
* `Pandas`
* `Matplotlib`
* `SeaBorn`

## Setup:
```
git clone https://github.com/LudovicLemaire/DSLR.git
cd DSLR
pip3 install pandas numpy matplotlib seaborn
```

### Data description
This are some visualizations for dataset:

|[describe.py](describe.py)      |[describe_object.py](describe_object.py)      |
|--------------------------------|----------------------------------------------|
|![describe](assets/describe.PNG)|![describe_object](assets/describe_object.PNG)|

|[scatter_plot.py‎‎‎‎](scatter_plot.py)   ‎‎‎‎‎                  |[scatter_plot_house.py](scatter_plot_house.py)      |[scatter_plot_house_upgraded.py](scatter_plot_house_upgraded.py)      |
|-------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------|
|![scatter_plot](assets/scatter_plot.PNG)               |![scatter_plot_house](assets/scatter_plot_house.PNG)|![scatter_plot_house_upgraded](assets/scatter_plot_house_upgraded.PNG)|
|Show values for two courses using Cartesian coordinates|Same but with color for houses                      |Show features I will use                                              |

|[pair_plot.py](pair_plot.py)      |[pair_plot_useless.py](pair_plot_useless.py)                                                 |
|----------------------------------|---------------------------------------------------------------------------------------------|
|![pair_plot](assets/pair_plot.PNG)|![pair_plot_useless](assets/pair_plot_useless.PNG)                                           |
|Pair plot from SeaBorn            |Tried to find if I could use birthday, names, best hand in some way, but they are all useless|

### Training phase
This are some visualizations during training:
|[log_train.py](log_train.py)                    |[log_train.py](log_train.py)                |
|------------------------------------------------|--------------------------------------------|
|![log_train_result](assets/log_train_result.PNG)|![log_train_cost](assets/log_train_cost.PNG)|
|Result once training is made between 2 features |Cost function                               |