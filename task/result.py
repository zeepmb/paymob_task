import os
import pandas as pd
from difflib import SequenceMatcher

def get_key_values():
    keys = []
    values = []

    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'task\data\dataset.csv')
    df = pd.read_csv(file_path)
    df_keys = df.Key.dropna()
    df_values = df.Values.dropna()
    keys = df_keys.values
    values = df_values.values
    a = {
        'key': df_keys.values,
        'value': df_values.values
    }
    return a

def get_matching(key):
    """
    Returns text matching percentage between key and values.

    Parameters
    ----------
    key : str
        Key value to be matched with values

    Returns
    -------
    filtered_values : arr[str]
        List of filtered values
    """
    a = get_key_values()
    results = []
    for i in a['value']:
        text_matching = SequenceMatcher(None, key, i).ratio() * 100
        if text_matching >= 50:
            results.append({"value": i, "percent": round(text_matching, 2)})

    # One liner alternative code below, but it becomes difficult to understand
    # filtered_values = [{"value": i, "similarity": round(similar(key, i), 2)} for i in self.values if
    #                    similar(key, i) > 50]
    return results
