import numpy as np
import streamlit as st
import base64
import pickle



df = pickle.load(open('df.pkl','rb'))
gradient = pickle.load(open('gradient.pkl','rb'))
print('no errors')

#################
st.title('Used Car Price Predictor')
###################

brand = st.selectbox('Car Brand', df['brand'].unique())
name = st.selectbox('Car Name', df.loc[df['brand'] == brand, 'name'].unique())

##################

year = st.selectbox('Model Year',df.loc[df['name']==name,'year'].unique())



###############

df['exterior'] = df['exterior'].replace(np.nan,'Not decided')
df['interior'] = df['exterior'].replace(np.nan,'Not decided')

exterior = st.selectbox('Exterior Color',df['exterior'].unique())
interior = st.selectbox('Interior Color',df['interior'].unique())


###############
miles = st.slider('Miles Driven',min_value=1000,max_value=150000)

#############

accidents = st.number_input('No Of Accidents',min_value=0,max_value=5)
owners = st.number_input('Number Of Owners',min_value=0,max_value=5)



###############PREDICTION

if st.button('Predict'):
    query = np.array([name,year,miles,brand,exterior,interior,accidents,owners])

    query = query.reshape(1,8)
    st.markdown(""" # _Predicted Price For The Given Details:_ """+"US$ "+str(int(np.exp(gradient.predict(query)))) + ".")


###################BACKGROUND

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('bgimage.avif')


st.text('')
st.text('')
st.text('')
st.text('')
st.text('')
st.text('By Abdul Rasheed.')


















