import streamlit as st
import pickle
from docx import Document

with open('C:\\Users\\DELL\\Downloads\\Project No 2\\resume_classification_pipeline.pkl', 'rb') as f:
    loaded_pipeline = pickle.load(f)

important_keywords = {
    # React Developer
    'react': 'React Developer', 'javascript': 'React Developer', 'redux': 'React Developer', 
    'css': 'React Developer', 'html': 'React Developer', 'jsx': 'React Developer', 
    'webpack': 'React Developer', 'babel': 'React Developer', 'node': 'React Developer',
    # Workday
    'workday': 'Workday', 'hcm': 'Workday', 'studio': 'Workday', 'data': 'Workday',
    'integration': 'Workday', 'reports': 'Workday', 'security': 'Workday',
    # Peoplesoft
    'peoplesoft': 'Peoplesoft', 'peoplecode': 'Peoplesoft', 'sql': 'Peoplesoft', 
    'sqr': 'Peoplesoft', 'application': 'Peoplesoft', 'engine': 'Peoplesoft', 
    # SQL Developer
    'sql': 'SQL Developer', 't-sql': 'SQL Developer', 'database': 'SQL Developer',
    'stored': 'SQL Developer', 'procedures': 'SQL Developer', 'etl': 'SQL Developer',
}


def analyze_skills(text, category):         # The text is actual content of resume and category is resume category section
    words = text.lower().split()
    category_keywords = {word for word, cat in important_keywords.items() if cat == category} 
    
    # Above code iterates through keywords in the resume and if the keyword matches any of keywords in above dictionary then
    # we add it in present skills variable below.
    
    present_skills = set(word for word in words if word in category_keywords)
    
    # Missing skills are ones which are in above keyword dictionary but not in present skills.
    missing_skills = category_keywords - present_skills
    return present_skills, missing_skills


st.title('Resume Classification App')


st.sidebar.header("Upload Files")
uploaded_resume = st.sidebar.file_uploader("Upload a Resume (DOCX)", type=["docx"])


if uploaded_resume is not None:

    doc = Document(uploaded_resume)
    resume_content = '\n'.join([para.text for para in doc.paragraphs])


    try:
        predicted_category = loaded_pipeline.predict([resume_content])[0]
    except Exception as e:
        st.error(f"Error predicting the category: {e}")   # If uploaded resume is not from our mentioned category or error in predicting
        st.stop()

    st.write(f"### Predicted Category: **{predicted_category}**")

    present_skills, missing_skills = analyze_skills(resume_content, predicted_category)
    
    st.write(f"### Important Skills Found in the Resume:")
    if present_skills:
        st.write(f"- {', '.join(sorted(present_skills))}")
    else:
        st.write("No important skills found in the resume.")

    if missing_skills:
        st.write(f"### Skills Missing for {predicted_category}:")
        st.write(f"- {', '.join(sorted(missing_skills))}")
    else:
        st.write(f"All important skills for {predicted_category} are present.")
