import pickle

from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from pipeline.preprocess import get_processed_data, MODELS_DIR, get_house_data, train_filepath

X = get_processed_data(get_house_data(train_filepath))
print(f'The features in X are: {X}')
y = get_house_data(train_filepath).loc[:, ['price']].values
# print(f'The prediction label is: {y.shape}')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# print(X_train)
# print(X_train.shape, X_test.shape)
# print(y_train.shape, y_test.shape)


def fit_model_linear(x, y):
    state = 1
    model1 = LinearRegression()
    model1.fit(X_train, y_train)
    filename1 = MODELS_DIR / 'linearReg.pkl'
    pickle.dump(model1, open(filename1, 'wb'))


def fit_model_xgboost(x, y):
    model2 = linear_model.Ridge(alpha=.5)
    model2.fit(X_train, y_train)
    filename2 = MODELS_DIR / 'RidgeReg.pkl'
    pickle.dump(model2, open(filename2, 'wb'))


if __name__ == '__main__':
    fit_model_linear(X_train, y_train)
    fit_model_xgboost(X_train, y_train)
