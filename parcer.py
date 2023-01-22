import pandas as pd

def api_parcer(n, str):
    with open("api.txt", 'r') as fin:
        data = pd.read_csv(fin, sep=';')
    key = data[(data["service"] == str) & (data["numb"] == n)]
    return key["key"].values[0]
