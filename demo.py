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

# prompt: usando el dataframe df, crear un filtro con la columna Region, y dentro de ese filtro crear otro filtro con la columna State

# Assuming 'Region' and 'State' are column names in your DataFrame.
# Replace with your actual column names if different.
if 'Region' in df.columns and 'State' in df.columns:
    region_filter = st.selectbox("Select Region", df['Region'].unique())
    filtered_df_region = df[df['Region'] == region_filter]

    state_filter = st.selectbox("Select State", filtered_df_region['State'].unique())
    filtered_df_state = filtered_df_region[filtered_df_region['State'] == state_filter]

    st.write(filtered_df_state)
else:
    st.error("Error: 'Region' or 'State' column not found in the DataFrame.")

# prompt: con el filtro creado anteriormente, crear una grafica de pastel interactiva

import pandas as pd
# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx")

    # Assuming 'Region' and 'Sales' are column names in your DataFrame.
    # Replace with your actual column names if different.
    if 'Region' not in df.columns or 'Sales' not in df.columns:
        st.error("Error: 'Region' or 'Sales' column not found in the DataFrame.")
    else:
        region_filter = st.selectbox("Select Region", df['Region'].unique())
        filtered_df = df[df['Region'] == region_filter]

        # Create the interactive pie chart
        fig = px.pie(filtered_df, names='State', values='Sales', title=f'Sales by State in {region_filter}')
        st.plotly_chart(fig)

except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")
