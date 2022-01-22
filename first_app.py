"""
# GUI diagram https://drive.google.com/drive/folders/1yd5JlFOCSO6GEN4d0U7sOlITkTQyLkVd
"""

import streamlit as st
import pandas as pd
import numpy as np
import cv2


in_operator = st.sidebar.selectbox(
     'Operator',
     ('Scott', 'Kala', 'Seth','Zarek','Zeta','April','Amare'))

in_lotnumber = st.sidebar.selectbox(
     'Lot Number',
     (10001,10002))

in_partnumber = st.sidebar.selectbox(
     'Lot Number',
     ('ST101','ST202'))

in_sequence = st.sidebar.selectbox(
     'Sequence',
     ('Red,Blue,Grey','Red,Blue,Blue,Gray'))

in_num_iter =  st.sidebar.number_input('Number of Iterations',min_value=1,max_value=5,step=1)

if st.sidebar.button('Start'):
     st.write('Starting Process')
else:
     st.write('Goodbye')
#--------------------------------
#Page Layout
#--------------------------------
col1, col2 = st.columns([1, 3])

#---------------------------------
#Chart
#---------------------------------
st_red = [1]
st_blue = [1]
st_gray = [1]
index = ['stack']
df = pd.DataFrame({'red': st_red,
                   'grey': st_gray,
                   'blue': st_blue}, index=index)

chart_data = pd.DataFrame(df )

col1.bar_chart(chart_data,height=100,width=5)

#------------------------------------
#Video Controls
#------------------------------------

button_start = col2.button('Start Recording')
button_stop = col2.button('Stop Recording')

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)


