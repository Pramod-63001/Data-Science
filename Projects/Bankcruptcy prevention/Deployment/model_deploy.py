import pickle
import pandas as pd
import streamlit as st 


file_path = "C:\\Users\\DELL\\Downloads\\Project_1\\backruptcy_naive.pkl"


# Load the pickled model
with open(file_path, 'rb') as file:
    backruptcy_naive = pickle.load(file)

st.title('Model Deployment Using Naive Bayes classifier')


st.sidebar.header('User Input Parameters')

def user_input_features():
    industrial_risk = st.sidebar.selectbox('industrial_risk',('1','0','0.5'))
    management_risk = st.sidebar.selectbox('management_risk',('1','0','0.5'))
    financial_flexibility = st.sidebar.selectbox('financial_flexibility',('1','0','0.5'))
    credibility = st.sidebar.selectbox('credibilty',('1','0','0.5'))
    competitiveness= st.sidebar.selectbox('competitiveness',('1','0','0.5'))
    operating_risk= st.sidebar.selectbox('operating_risk',('1','0','0.5'))
    data = {'industrial_risk':industrial_risk,
            'management_risk':management_risk,
            'financial_flexibility':financial_flexibility,
            'credibility': credibility,
            'competitiveness':competitiveness,
           'operating_risk':operating_risk }
        
    features = pd.DataFrame(data,index = [0])
    return features
    
df= user_input_features()
st.subheader('User Input parameters')
st.write(df)

# prediction = backruptcy_naive.predict(df)
prediction_proba = backruptcy_naive.predict_proba(df)

st.subheader('Predicted Result')
st.write('Non Bankruptcy' if prediction_proba[0][1] > 0.5 else 'Bankruptcy')

# st.subheader('prediction probability ')
# st.write(prediction_proba)

# \Users\DELL\Downloads streamlit run C:\Project_1\model_deploy.py