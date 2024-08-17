import pandas as pd

def get_properties():
    URL_DATASET = "https://drive.google.com/uc?id=1mJWG173twJseJf_RkCIJF1cPwsfMfdHk"

    origin = pd.read_csv(URL_DATASET)

    return origin