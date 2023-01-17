# imports
import datetime
import json

from flask import Flask, request
from Iot import Iot
from Ves import Ves
from helper_funtions import classify_ves, classify_mes, p_entropy
import pandas as pd
from scipy.stats import weibull_min
import matplotlib.pyplot as plt


app = Flask(__name__)

# Define the API endpoints
@app.route('/podium_classifier_mes/', methods=['POST'])
def podium_classifier_mes():
    content = json.loads(request.get_json(silent=True))
    print(content)
    iot = Iot(**content)
    iot_dict = json.loads(json.dumps(iot.__dict__))
    df = pd.DataFrame(iot_dict, index=[0])
    labeld_iot = classify_mes(df)
    json_str = json.dumps(labeld_iot.tolist())
    print(json_str)
    return json_str


@app.route('/podium_classifier_ves/', methods=['POST'])
def podium_classifier_ves():
    content = json.loads(request.get_json(silent=True))
    # print(content)
    ves = Ves(**content)
    ves_dict = json.loads(json.dumps(ves.__dict__))
    df = pd.DataFrame(ves_dict, index=[0])
    labeld_iot = classify_ves(df)
    json_str = json.dumps(labeld_iot.tolist())
    print(json_str)
    return json_str


"""The Weibull distribution is commonly used in reliability engineering to model the time to failure of a system. 
The method involves fitting a Weibull distribution to the historical failure data and then using the fitted distribution to predict the RUL for a given system or component. 
The Weibull method is a popular choice for RUL prediction because it can handle both increasing and decreasing failure rates, 
and it can be used for both mechanical and electronic systems"""
@app.route('/podium_weibull/', methods=['POST'])
def podium_weibull():
    content = json.loads(request.get_json(silent=True))
    # print(content)
    failure_dates = content

    # Extract the date strings from the JSON input
    date_strings = [failure_dates[key] for key in failure_dates.keys()]

    # Convert the date strings to datetime objects
    failure_times = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in date_strings]

    failure_times = list(set(failure_times))
    print(failure_times)

    if len(failure_times) < 2:
        raise ValueError('At least 2 failure dates are required to calculate RUL')
        return 'At least 2 failure dates are required to calculate RUL'

    # Calculate the time to failure for each sample
    failure_times = sorted(failure_times)
    time_to_failure = [(failure_times[i + 1] - failure_times[i]).total_seconds() for i in range(len(failure_times) - 1)
                       if (failure_times[i + 1] - failure_times[i]).total_seconds() > 0]

    # Fit a Weibull distribution to the data
    shape, loc, scale = weibull_min.fit(time_to_failure)

    # Predict the RUL at a given confidence level
    confidence_level = 0.95
    RUL = weibull_min.ppf(confidence_level, shape, loc, scale)
    print(RUL)

    json_str = json.dumps(RUL)
    print(json_str)
    return json_str

@app.route('/podium_permutation_entropy/', methods=['POST'])
def podium_permutation_entropy():
    content = json.loads(request.get_json(silent=True))
    # print(content)
    D = 3
    Window = 100
    df = pd.DataFrame(content, index=[0])
    rolling_pe = df.rolling(Window).apply(p_entropy)
    data = rolling_pe
    ax = data.plot(figsize=(20, 8))
    ax.set_ylabel("Permutation Entropy_Window = " + str(Window) + " D = " + str(D))
    ax.set_title("Daily mean of ")
    xposition = [u'2015-10-11  00:00:00', u'2015-10-14  00:00:00', u'2015-11-24  00:00:00',
                         u'2015-12-05  00:00:00', u'2016-01-05  00:00:00',
                         u'2016-01-06  00:00:00', u'2016-02-09  00:00:00']
    for xc in xposition:
        plt.axvline(x=xc, color='r', linestyle='--')
    # plt.show()

    # json_str = json.dumps(RUL)
    # print(json_str)
    return 'OK'

@app.route('/')
def index():
    return 'Welcome to PoDiuM for maritime defect diagnosis'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
