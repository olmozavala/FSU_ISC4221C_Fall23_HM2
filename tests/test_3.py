import numpy as np
from answers_module import normalize_rows

def test_normalize_rows():
    matrix = np.array([[1, 2], [3, 4]])
    expected_output = np.array([[0.4472136, 0.89442719], [0.6, 0.8]])
    np.testing.assert_array_almost_equal(normalize_rows(matrix), expected_output)
    matrix = np.array([[1, -2], [0, -8]])
    expected_output = np.array([[0.4472136 , -0.89442719],
                               [ 0.        , -1.        ]])
    np.testing.assert_array_almost_equal(normalize_rows(matrix), expected_output)