import pandas
import os
import datetime
import calendar

read_dir = os.environ['DATADIR']
#for file in os.listdir(read_dir):
weights1 = pandas.read_csv(read_dir + "/manual/weight1.csv")
weights1['Date'] = pandas.to_datetime(weights1['Date'])

weights2 = pandas.read_csv(read_dir + "/manual/weight2.csv", sep = '\t')
weights2['Date'] = pandas.to_datetime(weights2['Date'])

applehealth = pandas.read_csv(read_dir + "/qsaccess/applehealth.csv")
applehealth['Start'] = pandas.to_datetime(applehealth['Start'])

weights1 = weights1.merge(applehealth, left_on='Date',right_on='Start')

weights2 = weights2.merge(applehealth, left_on='Date',right_on='Start')

renpho = pandas.read_csv(read_dir + "/renpho/RENPHO-Josh.csv")

calendarDict = dict((v,k) for k,v in enumerate(calendar.month_abbr))
cols = renpho.columns
renpho[cols[0]] = renpho[cols[0]].str.replace("at","")
renpho[cols[0]] = renpho[cols[0]].apply(lambda x: x.replace(x[0:3],str(calendarDict[x[0:3]])))
renpho[cols[0]] = renpho[cols[0]].apply(lambda x: x.replace(" ", "|").replace(", ","").replace('，',"").split("|"))
Dates = renpho[cols[0]].apply(lambda x: pandas.Timestamp(year = int(x[2]), month = int(x[0]), day = int(x[1])))
#TODO create Times series and then add to Dates column in DateTime format and then use as 1st column
Times = renpho[cols[0]].apply(lambda x: str(x[4]) + " " + str(x[5]))
 # add the times to this
renpho["Date"] = Dates
renpho["Time"] = Times

renpho = renpho.merge(applehealth, left_on='Date',right_on='Start')

print(renpho.head())