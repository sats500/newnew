import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_player import st_player
import plotly.graph_objects as go

st.sidebar.image('https://tse1.mm.bing.net/th?id=OIP.Tke75-O-c15RFr5ksn06AgHaEK&pid=Api&P=0&w=290&h=162', width=300)
st.sidebar.title('''Analyzing what's best for your sales!!!!''')
st.title('CARs4ever')
st.sidebar.image("https://media.gettyimages.com/photos/car-salesman-giving-keys-to-customer-picture-id137546659",width=300)
st.sidebar.image("https://i.pinimg.com/474x/36/27/a6/3627a62febb2cb4c773391b2c40dc26e.jpg",width=300)
st.markdown("""
    We will do some analysis by looking at the data of Cars.
    * Which one's the women's best choice?
    * Which model had the highest sales?
    * There Latest launch Dates?
    * Which one's having best fuel efficiency?
    """)
options = st.selectbox('Please select', ['WOMENS_CHOICE', 'Car_Body_specifications', 'Manufacturers_And_Models' ,'Best_FuelEfficient_ANd_FuelCapacity','Latest_Launch','Best_Time_To_Launch_Car', 'Most desirable feature', 'Best of All'])
st.sidebar.image("https://i.pinimg.com/564x/f4/ce/87/f4ce873f304f7b257a8d6ed46e6af43d.jpg",width=300)


st_player("https://www.youtube.com/watch?v=tpucO5tobBw",height=200)


if options == 'Car_Body_specifications':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    with col1:
        st.write(df.iloc[:, 0:1])
    with col2:
        st.write(df.iloc[:, 8:9])
    with col3:
        st.write(df.iloc[:, 9:10])
    with col4:
        st.write(df.iloc[:, 10:11])
    with col5:
        st.write(df.iloc[:, 11:12])


elif options == 'WOMENS_CHOICE':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    df[df['WomensChoice'] == df['WomensChoice'].max()]
    st.title("BEST CAR ACCORDING TO WOMEN")
    df[df['FuelEfficiency'] == df['FuelEfficiency'].max()]
    col1, col2 = st.columns([1, 1])

    with col1:
        st.write(df.iloc[:, 0:1])
    with col2:
        st.write(df.iloc[:, 17:18])
    data = pd.read_csv(r'Book 5 (1) (3).csv')

    df = pd.DataFrame(data)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 17])

    # Plot the data using bar() method
    plt.bar(X, Y, color='b')
    plt.title("Womens Choice")
    plt.xlabel("Model")
    plt.ylabel("Womens choice")

    # Show the plot
    st.pyplot(plt)


elif options == 'Manufacturers_And_Models':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    st.write(df.iloc[:, 0:2])
    data = pd.read_csv(r'Book 5 (1) (3).csv')

    df = pd.DataFrame(data)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.scatter(X, Y, color='b')
    plt.title("Manufacturers and models")
    plt.xlabel("Manufacturers")
    plt.ylabel("Models")

    # Show the plot
    st.pyplot(plt)

elif options == 'Best_FuelEfficient_ANd_FuelCapacity':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.write(df.iloc[:, 0:2])
    with col2:
        st.write(df.iloc[:, 12:14])
    st.subheader("Most Fuel efficent car")
    df[df['FuelEfficiency'] == df['FuelEfficiency'].max()]

elif options == 'Latest_Launch':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.write(df.iloc[:, 0:1])
    with col2:
        st.write(df.iloc[:, 14:17])
    with col3:
        st.write(df.iloc[:, 15:16])
    with col4:
        st.write(df.iloc[:, 16:17])


elif options == 'Best_Time_To_Launch_Car':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    st.subheader("Least decreament in price in 4years!")
    df[df['Priceefficiency'] == df['Priceefficiency'].min()]
    st.subheader("Month of Launch")
    st.write(df.iloc[18:19, 14:15])
    st.subheader("Highest Sales")
    df[df['SalesInMillion'] == df['SalesInMillion'].max()]
    st.subheader("Month of Launch")
    st.write(df.iloc[19:20, 14:15])
    data = pd.read_csv(r'Book 5 (1) (3).csv')

    df = pd.DataFrame(data)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 3])

    # Plot the data using bar() method
    plt.bar(X, Y, color='b')
    plt.title("Sales In Millions")
    plt.xlabel("Manufacturers")
    plt.ylabel("Sales")

    # Show the plot
    st.pyplot(plt)


elif options == 'Most desirable feature':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    st.bar_chart(df.iloc[:, 19:20])
    st.bar_chart(df.iloc[:, 0:1])
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.write(df.iloc[:, 0:1])
    with col2:
        st.write(df.iloc[:, 1:2])
    with col3:
        st.write(df.iloc[:, 19:20])
    with col4:
        st.write(df.iloc[:, 20:21])
    st.subheader("After analyzing the sales and price efficiency and other features,most desirable feature that the customers want nowdays is blindspot monitoring and sunproof in cars")
    st.write(df.iloc[31:32, :])
elif options == 'Best of All':
    df = pd.read_csv(r"Book 5 (1) (3).csv")
    st.subheader("Best among there categories")
    st.write(df.iloc[31:32, :])
    df[df['Priceefficiency'] == df['Priceefficiency'].min()]
    df[df['SalesInMillion'] == df['SalesInMillion'].max()]
    df[df['FuelEfficiency'] == df['FuelEfficiency'].max()]
    df[df['WomensChoice'] == df['WomensChoice'].max()]


st.subheader("Thank you for visiting!!!!")


