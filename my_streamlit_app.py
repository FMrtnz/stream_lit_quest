# Import pacakage for the exercice
import streamlit as st
import pandas as pd
import seaborn as sns

# Set a title to the page
st.title('WCS Challenge : Cars analyse')

#Set links to navigate in the page
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
    df_filtered = df_cars[df_cars['continent'].isin(regions_selected)]
else:
    df_filtered = df_cars

df_filtered

# Set correlation then see the chart with
viz_correlation = sns.heatmap(df_filtered.corr(),
							center=0,
							cmap = sns.color_palette("vlag", as_cmap=True)
							)

# st.write is like a print function of python tyo display results
if(df_filtered.isnull().sum().sum() > 0):
    st.subheader("NaN elements")
    st.warning('There are NaN in the table')
    st.write(df_filtered.isnull().sum())
    st.write('Total rows', len(df_filtered.index) )
    st.write('Total columns', len(df_filtered.columns) )

st.subheader("Statistics' observations")
# st.write is like a print function of python tyo display results
st.write(df_filtered.describe())

st.subheader("Correlation")
# We replace plt.show() by st.pyplot()
st.pyplot(viz_correlation.figure)


# Should be delete columns or rows with less than 10% of available datas.
