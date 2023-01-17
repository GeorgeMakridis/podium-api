import json
import pandas as pd
import numpy as np

import requests

# data = pd.read_csv('./input/Bearing Damages.csv')
data = pd.read_csv('./input/all_ves_D_labeled.csv', nrows=100)
# data = pd.read_csv('./input/all_mes_D_labeled.csv', nrows=100)

# data['vessel_code_mes'] = data['vessel_code']
# data['rpm_mes'] = data['RPM']
# data['power_mes'] = data['POWER']
# data['torque'] = data['TORQUE']
# data.drop(['vessel_code', 'scavAirFireDetTempNo11', 'scavAirFireDetTempNo12', 'cylExhGasOutTempNo11', 'cylExhGasOutTempNo12', 'cylPistonCOOutTempNo11',
#            'cylPistonCOOutTempNo12', 'tcExhGasOutTempNo4', 'tcLOOutLETTempNo4', 'coolerCWinTemp', 'exhVVSpringAirInPress', 'coolingWOutLETTempNo4',
#            'hfoViscocityHighLow', 'hpsBearingTemp', 'cylJCFWOutTempNo11', 'cylJCFWOutTempNo12', 'tcLOInLETPressNo4', 'tcExhGasInTempNo4', 'tcRPMNo4', 'orderRPMBridgeLeverer',
#            'RPM', 'POWER', 'scavengeAirPressure','TORQUE'], axis=1, inplace=True)

# data.drop(['label'], axis=1, inplace=True)
# data = data['defect_date'][data['vessel_id']==18]
data = data['power']

# url = 'http://127.0.0.1:9999/podium_weibull'
# url = 'http://127.0.0.1:9999/podium_classifier_ves'
# url = 'http://127.0.0.1:9999/podium_classifier_mes'
url = 'http://127.0.0.1:9999/podium_permutation_entropy'
headers = {'Content-Type': 'application/json'}


# data = data.iloc[50].to_json()
data = data.to_json()

# Serialize the list as a JSON array
json_data = json.dumps(data)

response = requests.post(url, headers=headers, data=json_data)

print(response)

