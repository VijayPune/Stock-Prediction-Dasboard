import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Sidebar and Charts Widgets
# Can insert Charts (matplotlib or plotty) inside the App

# st.markdown("<H1 style='text-align: center;'> User Registration</H1>", unsafe_allow_html=True)
x = np.linspace(0,10,100)
bar_x = np.array([1,2,3,4,5])

opt = st.sidebar.radio("Select any Graph", options=("Line", "Bar", "Hor Bar"))
if opt == "Line":
    st.markdown("<h1 style='text-align: center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')
   
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.write(fig)

elif opt == "Bar":
    st.markdown("<h1 style='text-align: center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')

    plt.bar(bar_x, bar_x*10)
    st.write(fig)

else:
    st.markdown("<h1 style='text-align: center;'>Hor. Bar</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')

    plt.barh(bar_x*10, bar_x)
    st.write(fig)