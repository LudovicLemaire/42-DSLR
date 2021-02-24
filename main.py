import pandas as pd
import numpy as np
import sys
import math

def variance(array, ddof=1):
    n = len(array)
    mean = sum(array) / n
    return sum((x - mean) ** 2 for x in array) / (n - ddof)

def stdev(array):
    if (len(array) == 1):
        return 0
    var = variance(array)
    std_dev = math.sqrt(var)
    return std_dev

def calc_quantile(array, q):
    array = array.sort_values(ascending=True).to_numpy()
    n = len(array)
    index = (n - 1) * q
    if int(index) == index:
        return array[int(index)]
    fraction = index - int(index)
    left = int(index)
    right = left + 1
    i, j = array[left], array[right]
    return i + (j - i) * fraction

def describe(dico_numerals):
    ordered_describe = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'total']
    dico_size_chars = {}
    for label in dico_numerals:
        dico_size_chars[label] = len(label) + 2
        for label2 in dico_numerals[label]:
            if len(str("{:.4f}".format(round(dico_numerals[label][label2], 4)))) + 2 > dico_size_chars[label]:
                dico_size_chars[label] = len(str("{:.4f}".format(round(dico_numerals[label][label2], 4)))) + 2

    sys.stdout.write('\033[95m')
    sys.stdout.write('{0: <5}'.format(''))
    for label in sorted(dico_size_chars):
        sys.stdout.write('{message: >{width}}'.format(message=label, width=dico_size_chars[label]))
    sys.stdout.write('\n')
    sys.stdout.write('\033[0m')
    sys.stdout.flush()
    for label_type in ordered_describe:
        sys.stdout.write('\033[96m{0: <5}\033[0m'.format(label_type))
        for label in sorted(dico_size_chars):
            sys.stdout.write('{message: >{width}}'.format(message="{:.4f}".format(round(dico_numerals[label][label_type], 4)), width=dico_size_chars[label]))
        sys.stdout.write('\n')
        sys.stdout.flush()

def main():
    print('\033[92m' + "----------------------------------------------------------------------------------------------------------START---------------------------------------------------------------------------------------------------------------------------" + '\033[0m')
    df2 = pd.DataFrame()
    df = pd.read_csv(r'dataset_train.csv')
    columnsNamesArr = df.columns.values
    listOfColumnNames = list(columnsNamesArr)

    print(df.describe())
    print('\033[94m' + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" + '\033[0m')

    dico_numerals = {} 
    for label in listOfColumnNames:
        if df[label].dtypes == 'string' or df[label].dtypes == 'object':
            continue
        dico_numerals[label] = {
            'count': 0,
            'mean': 0,
            'std': 0,
            'min': float('inf'),
            '25%': 0,
            '50%': 0,
            '75%': 0,
            'max': float('-inf'),
            'total': 0
        }
    
    for label in listOfColumnNames:
        if df[label].dtypes == 'string' or df[label].dtypes == 'object':
            continue
        for index, row in df.iterrows():
            if row[label] > dico_numerals[label]['max']:
                dico_numerals[label]['max'] = row[label]
            if row[label] < dico_numerals[label]['min']:
                dico_numerals[label]['min'] = row[label]
            if np.isnan(row[label]) != True:
                dico_numerals[label]['count']+=1
                dico_numerals[label]['total'] += row[label]
        dico_numerals[label]['mean'] = dico_numerals[label]['total'] / dico_numerals[label]['count']
        
        dico_numerals[label]['25%'] = calc_quantile(df[label].dropna(), 0.25)
        dico_numerals[label]['50%'] = calc_quantile(df[label].dropna(), 0.5)
        dico_numerals[label]['75%'] = calc_quantile(df[label].dropna(), 0.75)
        dico_numerals[label]['std'] = stdev(df[label].dropna())
        

    describe(dico_numerals)















    print('\033[91m' + "-----------------------------------------------------------------------------------------------------------END----------------------------------------------------------------------------------------------------------------------------" + '\033[0m')
if __name__ == '__main__':
    main()