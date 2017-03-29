import csv
import operator
import pandas as pd

def uniquef():
    with open('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv') as csvfile:
	    csvfile=csv.reader('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv')
	    df = pd.read_csv('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv', skip_blank_lines=True)
	    #print(list(set(df.SITE_ID)))
	    #print(list(set(df.TKT_SEVERITY)))
	    print(df.SITE_ID.unique(),df.TKT_SEVERITY.unique(),df.TKT_PROB_DATE.unique(),df.TKT_CLOSE_DATE.unique())
	    

uniquef()
