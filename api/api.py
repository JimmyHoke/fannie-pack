from typing import Union
import uvicorn
import csv
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/stats")
def get_posts():
    data = {}
    failedCredit = 0
    failedLTV = 0
    failedDTI = 0
    failedFEDTI = 0
    hasCarPay = 0
    hasCreditBalance = 0
    hasStudentLoans = 0
    hasMortgage = 0
    count = 0
    csvfile = open('HackUTD-2023-HomeBuyerInfo.csv', newline='')
    datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in datareader:
        row = list(map(float,row))
        count += 1
        if row[9] < 640:
            failedCredit += 1
        if ((row[7] - row[6]) / row[7]) >= 0.8:
            failedLTV += 1
        if (row[2] + row[3] + row[4] + row[8]) / float(row[1]) > 0.43:
            failedDTI += 1
        if (row[8]) / float(row[1]) > 0.28:
            failedFEDTI += 1
        if (row[3] > 0):
            hasCarPay += 1
        if (row[2] > 0):
            hasCreditBalance += 1
        if (row[4] > 0):
            hasStudentLoans += 1
        if (row[8] > 0):
            hasMortgage += 1
    data = {'failedCredit':failedCredit, 'failedLTV':failedLTV, 'failedDTI':failedDTI,
             'failedFEDTI':failedFEDTI,'hasCarPay':hasCarPay, 'hasCreditBalance':hasCreditBalance,
             'hasStudentLoans':hasStudentLoans, 'hasMortgage':hasMortgage, 'count':count}
    return data

@app.get("/api/data")
def get_posts():
    data = []
    
    csvfile = open('HackUTD-2023-HomeBuyerInfo.csv', newline='')
    datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in datareader:
        row = list(map(float,row))
        failedCredit = 0
        failedLTV = 0
        failedDTI = 0
        failedFEDTI = 0
        hasCarPay = 0
        hasCreditBalance = 0
        hasStudentLoans = 0
        hasMortgage = 0
        if row[9] < 640:
            failedCredit += 1
        if ((row[7] - row[6]) / row[7]) >= 0.8:
            failedLTV += 1
        if (row[2] + row[3] + row[4] + row[8]) / float(row[1]) > 0.43:
            failedDTI += 1
        if (row[8]) / float(row[1]) > 0.28:
            failedFEDTI += 1
        if (row[3] > 0):
            hasCarPay += 1
        if (row[2] > 0):
            hasCreditBalance += 1
        if (row[4] > 0):
            hasStudentLoans += 1
        if (row[8] > 0):
            hasMortgage += 1
        person = {'failedCredit':failedCredit, 'failedLTV':failedLTV, 'failedDTI':failedDTI,
             'failedFEDTI':failedFEDTI,'hasCarPay':hasCarPay, 'hasCreditBalance':hasCreditBalance,
             'hasStudentLoans':hasStudentLoans, 'hasMortgage':hasMortgage}
        data.append(person)
    return data

if __name__ == '__main__':
    uvicorn.run(app, port=8080)