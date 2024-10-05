import pickle
import pandas as pd
import streamlit as st 
import xgboost as xgb



file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\ExcelR Hydrabaad\\Practics Projects Form online\\Solar generation\\solar_power.pkl"


# Load the pickled model
with open(file_path, 'rb') as file:
    xg_boost_power = pickle.load(file)
st.title('Model Deployment Using XG Boost Regressor')

st.sidebar.header('User Input Parameters')

def user_input_features():
    distance_to_solar_noon = st.sidebar.number_input("distance-to-solar-noon" ,min_value= 0.05 , max_value= 1.14 , value= 0.59 , step=0.01)
    temperature = st.sidebar.number_input("temperature" ,min_value= 42.0 , max_value= 78.0 , value= 60.0 , step=1.0)
    wind_direction = st.sidebar.number_input("wind-direction" ,min_value= 1.0 , max_value= 36.0 , value= 18.5 , step=1.0)
    wind_speed = st.sidebar.number_input("wind-speed" ,min_value= 1.1 , max_value= 26.6 , value= 13.85 , step=1.0)
    sky_cover = st.sidebar.number_input("sky-cover" ,min_value= 0.0 , max_value= 4.0 , value= 2.0 , step=1.0)
    humidity = st.sidebar.number_input("humidity" ,min_value= 14.0 , max_value= 100.0 , value= 57.0 , step=1.0)
    average_wind_speed_period = st.sidebar.number_input("average-wind-speed-(period)" ,min_value= 0.0 , max_value= 40.0 , value= 20.0 , step=1.0)
    average_pressure_period = st.sidebar.number_input("average-pressure-(period)" ,min_value= 29.48 , max_value= 30.53 , value= 30.01 , step=1.0)

    data = {'distance-to-solar-noon': distance_to_solar_noon, 
            'temperature': temperature , 
            'wind-direction': wind_direction , 
            'wind-speed': wind_speed, 
            'sky-cover': sky_cover , 
            'humidity': humidity , 
            'average-wind-speed-(period)': average_wind_speed_period, 
            'average-pressure-(period)': average_pressure_period 
            }

        
    features = pd.DataFrame(data,index = [0])
    return features
    
df= user_input_features()
st.subheader('User Input parameters')
st.write(df)





prediction = xg_boost_power.predict(df)[0]
st.subheader('Predicted Result')

if prediction < 0 :
    prediction = 0
st.write(f"Power Generated will be approximately : {int(prediction)} Jules")