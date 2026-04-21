import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, sep=';')
        print(" Data loaded successfully")
        return df

    except FileNotFoundError:
        print(" File not found")
    except PermissionError:
        print(" Permission denied")
    except Exception as e:
        print(" Error:", e)

    return None