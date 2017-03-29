import csv
import pandas as pd
import time
import datetime


def convert_date_to_timestamp(date_string):
    return time.mktime(datetime.datetime.strptime(date_string, "%m/%d/%Y %H:%M").timetuple())


#max and min timestamps 
def input_netcool(f):
	df = pd.read_csv(f, skip_blank_lines=True)
	#cellular_ids = list(df["SITE_ID"])
	prob_date = list(df["TKT_PROB_DATE"])
	close_date = list(df["TKT_CLOSE_DATE"])
	close_timestamp = map(convert_date_to_timestamp, close_date)
	prob_timestamp = map(convert_date_to_timestamp, prob_date)
	tkt_close_date = list(df["TKT_CLOSE_DATE"])
	close_ticket_timestamp=map(convert_date_to_timestamp, tkt_close_date)
	unique_timestamps = set(prob_timestamp)
	unique_timestampclose = set(close_timestamp)
	unique_closeticket_timestamps = set(close_ticket_timestamp)
	print("maximum timestamp fpr ticket prob datais",min(unique_timestamps))
	print("maximum timestamp fpr ticket prob datais",max(unique_timestampclose))

#unique values 
def uniqueattr(f):
	df = pd.read_csv(f, skip_blank_lines=True)
	print(df.SITE_ID.unique(),df.TKT_SEVERITY.unique(),df.TKT_PROB_DATE.unique(),df.TKT_CLOSE_DATE.unique())
	
#loading CSV file
def main():
    with open('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv') as csvfile:
        data=csv.reader(csvfile,delimiter=' ', quotechar='|')
        print(data)
        for row in data:
            print(row)
       
        input_netcool('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv')
        uniqueattr('Netcool_27_03_2017.csv - Netcool_27_03_2017.csv.csv')

main()







