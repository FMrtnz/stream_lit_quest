# Import pacakage for the exercice
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a title to the page
st.title('WCS Challenge : Cars analyse')

# Set links to navigate in the page
links = '<ul><li><a href="#table-cars">Table cars</a></li>'
links += '<li><a href="#nan-elements">NaN elements</a></li>'
links += '<li><a href="#statistics-observations">Statistics observations</a></li>'
links += '<li><a href="#correlation">Correlation</a></li></ul>'
st.markdown(links, unsafe_allow_html=True)

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

st.subheader("Table cars")
if len(regions_selected) > 0:
    # Adaptative variable for plots
    labels_countries = regions_selected
    # Adaptative DataFrame
    df_filtered = df_cars[df_cars['continent'].isin(regions_selected)]
else:
    df_filtered = df_cars
    labels_countries = regions_list

df_filtered

# Set correlation then see the chart with
viz_correlation = sns.heatmap(df_filtered.corr(),
							center=0,
							cmap = sns.color_palette("vlag", as_cmap=True)
							)

# st.write is like a print function of python tyo display results
st.subheader("NaN elements")
if(df_filtered.isnull().sum().sum() > 0):
    st.warning('There are NaN in the table')
    st.write(df_filtered.isnull().sum())
    st.write('Total rows', len(df_filtered.index) )
    st.write('Total columns', len(df_filtered.columns) )
else:
    st.write("No NaN found in the table")
    st.write('Total rows', len(df_filtered.index) )
    st.write('Total columns', len(df_filtered.columns) )

st.subheader("Statistics' observations")
# st.write is like a print function of python tyo display results
st.write(df_filtered.describe())

st.subheader("Correlation")
# We replace plt.show() by st.pyplot()
st.pyplot(viz_correlation.figure)

# Set list of colors for each country
colors = {regions_list[0]: "red" , regions_list[1]:"orange", regions_list[2]:"green"}

#Loop to create plot with mpg as x-axis
#Define list of plot to create
cols = ["cubicinches","hp","weightlbs","time-to-60"]
x_axis="mpg"
for col in cols:
    fig, ax = plt.subplots()
    for region in labels_countries:
        df_filtered[df_filtered['continent'] == region].plot(kind="scatter",ax = ax, x=x_axis, y=col, ylabel=col, figsize= (10, 3), color = colors[region])
    ax.legend(labels_countries)
    st.pyplot(fig)

#Loop to create plot with x-axis cylinders
cols_2 = ["mpg", "cubicinches", "hp","weightlbs","time-to-60"]
x_axis="cylinders"
for col in cols_2:
    fig, ax = plt.subplots()
    for region in labels_countries:
        df_filtered[df_filtered['continent'] == region].plot(kind="scatter",ax = ax, x=x_axis, y=col, ylabel=col, figsize= (10, 3), color = colors[region])
    ax.legend(labels_countries)
    st.pyplot(fig)

#Loop to create plot with x-axis cubicinches
cols_3 = ["hp","weightlbs","time-to-60"]
x_axis = "cubicinches"
for col in cols_3:
    fig, ax = plt.subplots()
    for region in labels_countries:
        df_filtered[df_filtered['continent'] == region].plot(kind="scatter",ax = ax, x=x_axis, y=col, ylabel=col, figsize= (10, 3), color = colors[region])
    ax.legend(labels_countries)
    st.pyplot(fig)

#Loop to create plot with x-axis hp
cols_4 = ["weightlbs","time-to-60"]
x_axis = "hp"
for col in cols_4:
    fig, ax = plt.subplots()
    for region in labels_countries:
        df_filtered[df_filtered['continent'] == region].plot(kind="scatter",ax = ax, x=x_axis, y=col, ylabel=col, figsize= (10, 3), color = colors[region])
    ax.legend(labels_countries)
    st.pyplot(fig)

#Loop to create plot with x-axis year
cols_5 = ["mpg","time-to-60"]
x_axis = "year"
for col in cols_5:
    fig, ax = plt.subplots()
    for region in labels_countries:
        df_filtered[df_filtered['continent'] == region].plot(kind="scatter",ax = ax, x=x_axis, y=col, ylabel=col, figsize= (10, 3), color = colors[region])
    ax.legend(labels_countries)
    st.pyplot(fig)
