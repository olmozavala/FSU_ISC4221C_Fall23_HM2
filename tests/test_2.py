import pandas as pd
from answers_module import pandas_info
import pytest

def test_pandas_info():
    df = pd.read_csv('data.csv')
    output = pandas_info('data.csv')
    assert output['num_rows'] == df.shape[0]
    assert output['num_cols'] == df.shape[1]
    assert output['col_names'] == list(df.columns)