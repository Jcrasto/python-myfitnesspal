import os
import sys
from datetime import date,timedelta

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from myfitnesspal.client import Client


if __name__ == '__main__':
    client = Client(username=os.environ['MFP_USER'], password=os.environ['MFP_PASS'])
    fileDirectory = os.environ['FILEDIR']
    start = date(2018, 5, 21)
    end = date(2020,2,1)
    delta = end - start
    for i in range(delta.days + 1):
        day = start + timedelta(days=i)
        data = client.get_date(day)
        with open(fileDirectory + 'days.txt', "a") as f:
            f.write(str(day) + str(data.meals) + "\n")
        for entry in data.entries:
            with open(fileDirectory + 'food.txt', "a") as fi:
                fi.write(str(day) + "," +str(entry) + "\n")
