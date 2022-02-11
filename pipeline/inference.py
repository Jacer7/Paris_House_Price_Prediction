import pickle

from sklearn.metrics import r2_score

from pipeline.preprocess import MODELS_DIR, get_house_data, train_filepath
# from pipeline.training import X_test, y_test
from pipeline.training import X_test, y_test

df_for_test = get_house_data(train_filepath)
Test_data = df_for_test.loc[:, ['garden', 'orientation']]
# print(f' Test dataset: {Test_data}')


# Linear Regression Inference Check
LinearReg = pickle.load(open(MODELS_DIR / 'linearReg.pkl', 'rb'))
y_pred1 = LinearReg.predict(X_test)
# print(f'The y_pred of the model with linear Regression {y_pred1}')
accuracy1 = r2_score(y_test, y_pred1)
print(f'The accuracy of the model is: {accuracy1}')

# Ridge Regression Inference Check
LinearReg = pickle.load(open(MODELS_DIR / 'RidgeReg.pkl', 'rb'))
y_pred2 = LinearReg.predict(X_test)
# print(f'The y_pred of the model with linear Regression {y_pred2}')
accuracy2 = r2_score(y_test, y_pred2)
print(f'The accuracy of the model is: {accuracy2}')

# Encoder test whether it works or not
encoder = pickle.load(open(MODELS_DIR / 'ohe_encoder.pkl', 'rb'))
encoded_df = encoder.transform(Test_data).toarray()
# print(encoded_df)

Pred = LinearReg.predict([[250., 4., 0.,   1.,   1.,   0.,   0.,   0.]])
print(f'The Prediction if 250sq.m area, 4 room, garden = Yes and location as East is given: {Pred[0]}')
