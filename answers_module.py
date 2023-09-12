import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def g(x):
    if x > 0:
        return x ** 2
    else:
        return 0


def myrec_advanced(x):
    if x < 0:
        raise ValueError("x must be greater than or equal to 0")
    elif x == 0:
        return 0
    else:
        return 2 * x - myrec_advanced(x - 1) + g(x)



def pandas_info(csv_file_path):
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Get the number of rows and columns
        num_rows, num_columns = df.shape

        # Get the column names
        column_names = df.columns.tolist()

        # Create a dictionary to store the information
        info_dict = {
            'Number of Rows': num_rows,
            'Number of Columns': num_columns,
            'Column Names': column_names
        }

        return info_dict
    except Exception as e:
        return {'Error': str(e)}



def normalize_rows(matrix):
    try:
        # Calculate the Euclidean norm (L2 norm) of each row
        row_norms = np.linalg.norm(matrix, axis=1, ord=2)

        # Ensure that row_norms is not zero to avoid division by zero
        row_norms[row_norms == 0] = 1

        # Normalize each row by dividing it by its norm
        normalized_matrix = matrix / row_norms[:, np.newaxis]

        return normalized_matrix
    except Exception as e:
        return None

