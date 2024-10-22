# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:46:27 2019

@author: PRATYUSH, Rahul, Somya, Abhay
"""

from flask import Flask, render_template
from flask_cors import CORS
import numpy as np
import pandas as pd
from datetime import datetime
import crops
import random
from sklearn.tree import DecisionTreeRegressor

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

# Set up CORS
cors = CORS(app, resources={r"/ticker": {"origins": "http://localhost:port"}})

commodity_dict = {
    "arhar": "static/Arhar.csv",
    "bajra": "static/Bajra.csv",
    "barley": "static/Barley.csv",
    "copra": "static/Copra.csv",
    "cotton": "static/Cotton.csv",
    "sesamum": "static/Sesamum.csv",
    "gram": "static/Gram.csv",
    "groundnut": "static/Groundnut.csv",
    "jowar": "static/Jowar.csv",
    "maize": "static/Maize.csv",
    "masoor": "static/Masoor.csv",
    "moong": "static/Moong.csv",
    "niger": "static/Niger.csv",
    "paddy": "static/Paddy.csv",
    "ragi": "static/Ragi.csv",
    "rape": "static/Rape.csv",
    "jute": "static/Jute.csv",
    "safflower": "static/Safflower.csv",
    "soyabean": "static/Soyabean.csv",
    "sugarcane": "static/Sugarcane.csv",
    "sunflower": "static/Sunflower.csv",
    "urad": "static/Urad.csv",
    "wheat": "static/Wheat.csv"
}

annual_rainfall = [29, 21, 37.5, 30.7, 52.6, 150, 299, 251.7, 179.2, 70.5, 39.8, 10.9]
base = {
    "Paddy": 1245.5,
    "Arhar": 3200,
    "Bajra": 1175,
    "Barley": 980,
    "Copra": 5100,
    "Cotton": 3600,
    "Sesamum": 4200,
    "Gram": 2800,
    "Groundnut": 3700,
    "Jowar": 1520,
    "Maize": 1175,
    "Masoor": 2800,
    "Moong": 3500,
    "Niger": 3500,
    "Ragi": 1500,
    "Rape": 2500,
    "Jute": 1675,
    "Safflower": 2500,
    "Soyabean": 2200,
    "Sugarcane": 2250,
    "Sunflower": 3700,
    "Urad": 4300,
    "Wheat": 1350
}
commodity_list = []

class Commodity:
    def __init__(self, csv_name):
        self.name = csv_name
        dataset = pd.read_csv(csv_name)
        self.X = dataset.iloc[:, :-1].values
        self.Y = dataset.iloc[:, 3].values
        depth = random.randrange(7, 18)
        self.regressor = DecisionTreeRegressor(max_depth=depth)
        self.regressor.fit(self.X, self.Y)

    def getPredictedValue(self, value):
        if value[1] >= 2019:
            fsa = np.array(value).reshape(1, 3)
            return self.regressor.predict(fsa)[0]
        else:
            c = self.X[:, 0:2]
            fsa = [value[0], value[1]]
            ind = next((i for i, x in enumerate(c) if x.tolist() == fsa), None)
            return self.Y[ind] if ind is not None else None

    def getCropName(self):
        return self.name.split('.')[0]

@app.route('/')
def index():
    context = {
        "top5": TopFiveWinners(),
        "bottom5": TopFiveLosers(),
        "sixmonths": SixMonthsForecast()
    }
    return render_template('index.html', context=context)

@app.route('/commodity/<name>')
def crop_profile(name):
    max_crop, min_crop, forecast_crop_values = TwelveMonthsForecast(name)
    prev_crop_values = TwelveMonthPrevious(name)
    forecast_x = [i[0] for i in forecast_crop_values]
    forecast_y = [i[1] for i in forecast_crop_values]
    previous_x = [i[0] for i in prev_crop_values]
    previous_y = [i[1] for i in prev_crop_values]
    current_price = CurrentMonth(name)
    crop_data = crops.crop(name)
    context = {
        "name": name,
        "max_crop": max_crop,
        "min_crop": min_crop,
        "forecast_values": forecast_crop_values,
        "forecast_x": str(forecast_x),
        "forecast_y": forecast_y,
        "previous_values": prev_crop_values,
        "previous_x": previous_x,
        "previous_y": previous_y,
        "current_price": current_price,
        "image_url": crop_data[0],
        "prime_loc": crop_data[1],
        "type_c": crop_data[2],
        "export": crop_data[3]
    }
    return render_template('commodity.html', context=context)

@app.route('/ticker/<item>/<number>')
def ticker(item, number):
    n = int(number)
    i = int(item)
    data = SixMonthsForecast()
    context = str(data[n][i])

    if i == 2 or i == 5:
        context = '₹' + context
    elif i == 3 or i == 6:
        context = context + '%'
    
    return context

def TopFiveWinners():
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = annual_rainfall[prev_month - 1]
    change = []

    for i in commodity_list:
        current_predict = i.getPredictedValue([float(current_month), current_year, current_rainfall])
        prev_predict = i.getPredictedValue([float(prev_month), current_year, prev_rainfall])
        if prev_predict is not None and prev_predict != 0:
            change.append((((current_predict - prev_predict) * 100 / prev_predict), commodity_list.index(i)))
    
    sorted_change = sorted(change, reverse=True)
    to_send = []
    for j in range(min(5, len(sorted_change))):
        perc, idx = sorted_change[j]
        name = commodity_list[idx].getCropName().split('/')[1]
        to_send.append([name, round((current_predict * base[name]) / 100, 2), round(perc, 2)])
    
    return to_send

def TopFiveLosers():
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = annual_rainfall[prev_month - 1]
    change = []

    for i in commodity_list:
        current_predict = i.getPredictedValue([float(current_month), current_year, current_rainfall])
        prev_predict = i.getPredictedValue([float(prev_month), current_year, prev_rainfall])
        if prev_predict is not None and prev_predict != 0:
            change.append((((current_predict - prev_predict) * 100 / prev_predict), commodity_list.index(i)))
    
    sorted_change = sorted(change)
    to_send = []
    for j in range(min(5, len(sorted_change))):
        perc, idx = sorted_change[j]
        name = commodity_list[idx].getCropName().split('/')[1]
        to_send.append([name, round((current_predict * base[name]) / 100, 2), round(perc, 2)])
    
    return to_send

def SixMonthsForecast():
    months_forecast = [[] for _ in range(6)]
    for i in commodity_list:
        crop = SixMonthsForecastHelper(i.getCropName())
        for k in range(len(crop)):
            time, price, change = crop[k]
            months_forecast[k].append((price, change, i.getCropName().split("/")[1], time))

    for month in months_forecast:
        month.sort()

    crop_month_wise = []
    for month in months_forecast:
        if month:
            crop_month_wise.append(month)
        else:
            crop_month_wise.append(["-", "-", "-", "-"])

    return crop_month_wise

def TwelveMonthsForecast(name):
    # Implementation of TwelveMonthsForecast logic
    pass

def TwelveMonthPrevious(name):
    # Implementation of TwelveMonthPrevious logic
    pass

def CurrentMonth(name):
    # Implementation of CurrentMonth logic
    pass

if __name__ == "__main__":
    # Load commodities
    commodity_list = [Commodity(commodity_dict[key]) for key in commodity_dict]
    app.run(debug=True)
