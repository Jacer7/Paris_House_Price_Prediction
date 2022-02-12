# House Price Prediction in Paris
### Using Linear Regression Model
### Created a web app for a user to input the parameter such as
- Size of the House
- Number of Rooms in the house
- Garden present or not
- Orientation of house (House in which part of Geography)

### Streamlit Web App and Heroku for model deployment
#### This would be the model as a service web app for a Data Science Project.

## Used technologies
1. FastAPI
2. Python
3. Streamlit


# Steps for Installation and Setup to run this project after clone !!
1. [Install Dependencies](#install-dependencies)
2. [Run API](#run-api)
3. [Run Airflow](#run-airflow)
4. [Run Frontend](#run-frontend)

### Install Dependencies
1. Create a virtual environment with python3
   ```shell
   python3 -m venv House Price Prediction
   ```
2. Activate the virtual environment:
   ```shell
   cd House Price Prediction
   source /bin/activate
   ```
3. Install dependencies
   ```shell
   pip install -r requirements.txt
   ```
### Run Frontend
Please read the following guidelines for the Streamlit Setup:
https://docs.streamlit.io/library/get-started/installation

1. Navigate to the ```/webApp``` directory of application
2. Run streamlit application as:

```bash
   streamlit run frontend.py
```
### Run Fast API Server
FastAPI
Please read the following guidelines for the FastAPI Setup:
https://fastapi.tiangolo.com/tutorial/

1. Run Unicorn Server
```bash
uvicorn api.app:app --reload
```

## Streamlit Cloud Deployment
The web app has been deployed on Streamlit Cloud. You can go ahead and check it out on the following link:
https://share.streamlit.io/jacer7/paris_house_price_prediction/webapp/webApp/frontend.py

## Heroku Deployment
The Model has been exposed to API and deployed as Model As Service (MAS) for the user who wants to check at:   
https://predict-price-house-paris.herokuapp.com/docs

**Happy to receive feedback !!**