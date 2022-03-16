# Import pacakage for the exercice
import streamlit as st
import pandas as pd
import seaborn as sns

# Set a container
with st.container():
    # Set a title to the page
    st.title('WCS Challenge : Cars analyse')

    # Get the CSV link
    link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
    # READ the CSV link with pandas then display
    df_cars = pd.read_csv(link)

    # Set the available country
    regions_list = df_cars.groupby(["continent"]).count().index.values

    # Set an input to choose region
    regions_selected = st.multiselect(
     'Filter by region(s) available in Dataframe',
     regions_list,
     regions_list
    )

    df_filtered = df_cars[df_cars['continent'].isin(regions_selected)]
    df_filtered

# set a chart
#st.line_chart(df_weather['MAX_TEMPERATURE_C'])

with st.container():
    # Set correlation then see the chart with
    viz_correlation = sns.heatmap(df_cars.corr(),
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)
    # We replace plt.show() by st.pyplot()
    st.pyplot(viz_correlation.figure)

# Set an input
# name = st.text_input("Please give me your name:")
# name_length = len(name)
# st.write("Your name has ",name_length, "characters")
