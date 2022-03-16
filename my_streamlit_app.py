# Import pacakage for the exercice
import streamlit as st
import pandas as pd
import seaborn as sns

# Set a title to the page
st.title('Hello Wilders, welcome to my application!')
# Set a text
st.write("I enjoy to discover stremalit possibilities")

# Get the CSV link
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
# READ the CSV link with pandas then display
df_weather = pd.read_csv(link)
df_weather

# set a chart
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# Set correlation then see the chart with
viz_correlation = sns.heatmap(df_weather.corr(),
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

# We replace plt.show() by st.pyplot()
st.pyplot(viz_correlation.figure)

# Set an input
name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")
