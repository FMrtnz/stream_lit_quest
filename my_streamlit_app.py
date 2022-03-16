# Import pacakage for the exercice
import streamlit as st
import pandas as pd
import seaborn as sns

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
 regions_list
)

if len(regions_selected) > 0:
    df_filtered = df_cars[df_cars['continent'].isin(regions_selected)]
else:
    df_filtered = df_cars

df_filtered

# Set correlation then see the chart with
viz_correlation = sns.heatmap(df_filtered.corr(),
							center=0,
							cmap = sns.color_palette("vlag", as_cmap=True)
							)
# We replace plt.show() by st.pyplot()
st.pyplot(viz_correlation.figure)

# Set an input
# name = st.text_input("Please give me your name:")
# name_length = len(name)
# st.write("Your name has ",name_length, "characters")
