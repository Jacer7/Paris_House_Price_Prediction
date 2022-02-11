import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

ROOT_DIR = Path('./')
# print(str(ROOT_DIR.cwd()))

DATA_DIR = ROOT_DIR / 'data'
print(DATA_DIR.resolve())

train_filepath = DATA_DIR / 'house.csv'
print(train_filepath.resolve())
MODELS_DIR = ROOT_DIR / 'models'


def get_house_data(filepath):
    data = pd.read_csv(filepath)
    return data


# print(get_house_data(train_filepath).loc[:,['garden', 'orientation']])


def ohe_encode(df):
    enc = OneHotEncoder(handle_unknown='ignore')
    feature = df.loc[:, ['garden', 'orientation']]
    encoder = enc.fit(feature)
    # my_array = encoded.toarray()
    # enc_df = pd.DataFrame(my_array, columns=enc.get_feature_names_out())
    # save encoder
    filename = MODELS_DIR / 'ohe_encoder.pkl'
    pickle.dump(encoder, open(filename, 'wb'))
    transformed = enc.transform(feature).toarray()
    return transformed


# print(ohe_encode(get_house_data(train_filepath)))


def get_processed_data(df):
    encoder = ohe_encode(df)
    rem = df.loc[:, ['size', 'nb_rooms']].values
    x = np.concatenate((rem, encoder), axis=1)
    return x

# print(get_processed_data(get_house_data(train_filepath)))


if __name__ == '__main__':
    print(ohe_encode(get_house_data(train_filepath)))
