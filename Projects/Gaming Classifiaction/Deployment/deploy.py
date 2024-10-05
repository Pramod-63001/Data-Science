import pickle
import pandas as pd
import streamlit as st 


file_path = "C:\\Users\\DELL\\OneDrive\\Documents\\Data Science\\DataSets\\ML Projects\\Gaming Classifiaction\\gaming_classification.pkl"


# Load the pickled model
with open(file_path, 'rb') as file:
    random_forest_gaming = pickle.load(file)
st.title('Model Deployment Using Random Forest classifier')


st.sidebar.header('User Input Parameters')

def user_input_features():

    age = st.sidebar.number_input('Enter the Age',min_value=15 , max_value=49 , value=34 , step=1)
    gender = st.sidebar.radio('Gender of the Player',["Male" , "Female"])
    location = st.sidebar.selectbox('Location of the Player',["USA","Europe","Asia","Other"])
    gamegenre = st.sidebar.selectbox('Game Genre',['Sports', 'Action', 'Strategy', 'Simulation', 'RPG'])
    play_time_hours = st.sidebar.number_input('Play Time in Hours',min_value= 0.00001 , max_value=24.01 , value=12.89 , step=1.0)
    in_game_purchases = st.sidebar.radio('In Game Purchases',["0" , "1"])
    game_difficulty = st.sidebar.select_slider("Game Difficulty" ,['Easy', 'Medium', 'Hard'])
    sessions_per_week = st.sidebar.number_input('Sessions Per Week',min_value=0 , max_value=19 , value=9 , step=1)
    avg_session_duration_minutes = st.sidebar.number_input('Avg Session Duration in Minutes',min_value=10 , max_value=179 , value=54 , step=1)
    player_level = st.sidebar.number_input('Level Of The Player',min_value=1 , max_value=99 , value=78 , step=1)
    achievements_unlocked = st.sidebar.slider('AchievementsUnlocked',min_value=1 , max_value=99 , value=78 , step=1)

    data = {'Age' : age, 
            'Gender' : gender,
            'Location' : location,
            'GameGenre' : gamegenre, 
            'PlayTimeHours' : play_time_hours ,
            'InGamePurchases' : in_game_purchases,
            'GameDifficulty' : game_difficulty , 
            'SessionsPerWeek' : sessions_per_week,
            'AvgSessionDurationMinutes' : avg_session_duration_minutes , 
            'PlayerLevel' : player_level, 
            'AchievementsUnlocked' : achievements_unlocked
            }
        
    features = pd.DataFrame(data,index = [0])
    return features
    
df= user_input_features()
st.subheader('User Input parameters')
st.write(df)

prediction = random_forest_gaming.predict(df)
st.subheader('Predicted Result')
st.write(f"The Chance Of Player to Keep Playing are : {prediction[0]}")