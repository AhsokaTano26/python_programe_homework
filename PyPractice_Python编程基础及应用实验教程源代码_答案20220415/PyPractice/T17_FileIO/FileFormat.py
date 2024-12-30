years = [2020,2019,2018,2017,2016]
incomes = { '北京市':[5483.89,5817.10,5785.92,5430.79,5081.26],
            '天津市':[1923.05,2410.41,2106.24,2310.36,2723.50],
            '上海市':[7046.30,7165.10,7108.15,6642.26,6406.13],
            '重庆市':[4257.98,4070.83,3911.01,3577.99,3388.85] }

import json 
with open("IncomesData.json","w") as f:
    json.dump([years,incomes],f)

with open("IncomesData.json") as f:
    years1, incomes1 = json.load(f)
print("years1:",years1)
print("incomes1:",incomes1)

import os
print("json file size:",os.path.getsize("IncomesData.json"))

import pickle
with open("IncomesData.dat","wb") as f:
    pickle.dump([years,incomes],f)

with open("IncomesData.dat","rb") as f:
    years2, incomes2 = pickle.load(f)
print("years2:",years2)
print("incomes2:",incomes2)

import os
print("dat file size:",os.path.getsize("IncomesData.dat"))





