from catboost import CatBoostClassifier
from Config import model_filename_ves, model_filename_mes


def ml_based_mes(iot):
    from_file = CatBoostClassifier()
    model = from_file.load_model(model_filename_mes, format="cbm")
    # print(model.feature_names_)
    y_preds = model.predict_proba(iot)
    return y_preds

def ml_based_ves(iot):
    from_file = CatBoostClassifier()
    model = from_file.load_model(model_filename_ves, format="cbm")
    # print(model.feature_names_)
    y_preds = model.predict_proba(iot)
    return y_preds


def preprocess_data(iot):
    """ preprocess iot data if needed"""

    return iot


def classify_mes(iot):
    # iot.label = UNKNOWN
    # STEP 1 (pre-process data)
    iot = preprocess_data(iot)
    # STEP 2 (ML method)
    label = ml_based_mes(iot)
    # print(label)
    return label

def classify_ves(iot):
    # iot.label = UNKNOWN
    # STEP 1 (pre-process data)
    iot = preprocess_data(iot)
    # STEP 2 (ML method)
    label = ml_based_ves(iot)
    # print(label)
    return


import itertools
import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean


def s_entropy(freq_list):
    ''' This function computes the shannon entropy of a given frequency distribution.
    USAGE: shannon_entropy(freq_list)
    ARGS: freq_list = Numeric vector represnting the frequency distribution
    OUTPUT: A numeric value representing shannon's entropy'''
    freq_list = [element for element in freq_list if element != 0]
    sh_entropy = 0.0
    for freq in freq_list:
        sh_entropy += freq * np.log(freq)
    sh_entropy = -sh_entropy
    return (sh_entropy)


def ordinal_patterns(ts, embdim, embdelay):
    ''' This function computes the ordinal patterns of a time series for a given embedding dimension and embedding delay.
    USAGE: ordinal_patterns(ts, embdim, embdelay)
    ARGS: ts = Numeric vector represnting the time series, embdim = embedding dimension (3<=embdim<=7 prefered range), embdelay =  embdding delay
    OUPTUT: A numeric vector representing frequencies of ordinal patterns'''
    time_series = ts
    possible_permutations = list(itertools.permutations(range(embdim)))
    lst = list()
    for i in range(len(time_series) - embdelay * (embdim - 1)):
        sorted_index_array = list(np.argsort(time_series[i:(embdim + i)]))
        lst.append(sorted_index_array)
    lst = np.array(lst)
    element, freq = np.unique(lst, return_counts=True, axis=0)
    freq = list(freq)
    if len(freq) != len(possible_permutations):
        for i in range(len(possible_permutations) - len(freq)):
            freq.append(0)
        return (freq)
    else:
        return (freq)


def weighted_ordinal_patterns(ts, embdim, embdelay):
    time_series = ts
    possible_permutations = list(itertools.permutations(range(embdim)))
    temp_list = list()
    wop = list()
    for i in range(len(time_series) - embdelay * (embdim - 1)):
        Xi = time_series[i:(embdim + i)]
        Xn = time_series[(i + embdim - 1): (i + embdim + embdim - 1)]
        Xi_mean = np.mean(Xi)
        Xi_var = (Xi - Xi_mean) ** 2
        weight = np.mean(Xi_var)
        sorted_index_array = list(np.argsort(Xi))
        temp_list.append([''.join(map(str, sorted_index_array)), weight])
    result = pd.DataFrame(temp_list, columns=['pattern', 'weights'])
    freqlst = dict(result['pattern'].value_counts())
    for pat in (result['pattern'].unique()):
        wop.append(np.sum(result.loc[result['pattern'] == pat, 'weights'].values))
    return (wop)

def p_entropy(ts, embdim=3, embdelay=1):
    ordinal_pat = weighted_ordinal_patterns(ts, embdim, embdelay)
    max_entropy = np.log(len(ordinal_pat))
    p = np.divide(np.array(ordinal_pat), float(sum(ordinal_pat)))
    return(s_entropy(p)/max_entropy)



