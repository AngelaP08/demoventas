# prompt: muestra el dataframe con streamlit

import pandas as pd
import streamlit as st

# prompt: arma una grafica de las ventas por region del dataframe df con streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx")

    # Assuming 'Region' and 'Sales' are column names in your DataFrame.
    # Replace with your actual column names if different.
    if 'Region' not in df.columns or 'Sales' not in df.columns:
        st.error("Error: 'Region' or 'Sales' column not found in the DataFrame.")
    else:
        fig = px.bar(df, x='Region', y='Sales', title='Sales por Region')
        st.plotly_chart(fig)

except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# prompt: usando el dataframe df, crea un filtro con streamlit de la columna Region, y otro filtro con los resultados del filtro Region, usando la columna State. Tambien crea una grafica de pastel con la columna Category considerando los datos de las columnas de los primeros filtros

import pandas as pd
import streamlit as st
import plotly.express as px

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx")
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
    st.stop()  # Stop execution if the file is not found
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()


# Region filter
if 'Region' in df.columns:
    region_filter = st.selectbox("Select Region", df['Region'].unique())
    filtered_df_region = df[df['Region'] == region_filter]
else:
    st.error("Error: 'Region' column not found in the DataFrame.")
    st.stop()

# State filter based on Region filter
if 'State' in filtered_df_region.columns:
    state_filter = st.selectbox("Select State", filtered_df_region['State'].unique())
    filtered_df_state = filtered_df_region[filtered_df_region['State'] == state_filter]
else:
    st.error("Error: 'State' column not found in the DataFrame.")
    st.stop()


# Pie chart based on Category and the applied filters
if 'Category' in filtered_df_state.columns:
    fig = px.pie(filtered_df_state, names='Category', title='Category Distribution')
    st.plotly_chart(fig)
else:
    st.error("Error: 'Category' column not found in the DataFrame.")
