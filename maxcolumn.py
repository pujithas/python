import csv
import operator
import pandas as pd

def maxmin():
    with open('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv') as csvfile:
        csvfile=csv.reader('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv')
        df = pd.read_csv('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv', skip_blank_lines=True)
        print("maximum timestamp fpr ticket prob datais",df['TKT_PROB_DATE'].max(),"at position",df['TKT_PROB_DATE'].idxmax())
        print("maximum timestamp for ticket close date",df['TKT_CLOSE_DATE'].min(),"at position",df['TKT_CLOSE_DATE'].idxmin())
 

maxmin()
