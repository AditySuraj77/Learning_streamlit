import streamlit as st

st.title('AI Interface')  # title
st.header('ML Interface')  # Header
st.subheader('DL Interface')  # Subheader
st.text('Deep learning is a machine learning technique that')  # text
st.write('Deep learning is a subset of machine learning')  # write

# Images
from PIL import Image

img = Image.open(('dl.jfif'))
st.image(img, caption='DL')

# Colorful text

st.success('Sucess')
st.warning('Again Warning')
st.info('Please Note it')
st.error('0 to 0 Page not Found')
st.exception('ERROR')
st.help('help')

# video
vid = open('vid.mp4', 'rb').read()
st.video(vid)

# SideBar
st.sidebar.header('About')
st.sidebar.text('Deep learning is part of a broader\n family of'
                'machine learning methods based on\n artificial neural networks '
                'with representation learning.\n Learning can be supervised, '
                'semi-supervised or unsupervised.')
# CheckBox
if st.checkbox('Show/Hide'):
    st.write('HAy')

# Radio bUtton
status = st.radio('What is your Status', ('Active', 'InActive'))
if status is 'Active':
    st.success('Active')
else:
    st.warning('InActive')

# Select Box
occupat = st.selectbox('Waht are do for living', ['', 'Engineer', 'Programmer', 'Data Analyst', 'Automation'])
st.write('You are', occupat)

# MultiSelect
lives = st.multiselect('What is your country', ['UK', 'INDIA', 'USA', 'South Korea', 'Japan', 'UAE'])
st.write('You are selected', len(lives), 'location')

# Slider
st.slider('What is your weight', 45, 100)

# button
if st.button('Click'):
    st.success('Welcome to StreamLit without effort User interface')

# input
gmail = st.text_input('Enter Your Email:')
if '@gmail.com' in gmail:
    st.write('Successfully Enterend', {gmail})

# text_area
st.text_area('Suggestions')

# Date & Time

# date

import datetime

st.date_input('Today is ', datetime.datetime.now())

# time

import time

st.time_input('Time is', datetime.time())

# Displaying Code
st.text('How to install Streamlit')
st.code('pip install streamlit')

# echo

with st.echo():
    # How to import streamlit in your python script
    import streamlit

# displaying JSON
st.json({'Name': 'Rohan', 'GEnder': 'Male'})

# spinner
with st.spinner('Please wait'):
    time.sleep(5)
    st.success('Success')
# displaying
st.balloons()
