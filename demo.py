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

# prompt: usando el dataframe df, crear un filtro con la columna Region

# Assuming 'Region' is a column in your DataFrame.
# Replace 'Region' with the actual column name if different.
if 'Region' in df.columns:
    region_filter = st.selectbox("Select Region", df['Region'].unique())
    filtered_df = df[df['Region'] == region_filter]
    st.write(filtered_df)
else:
    st.error("Error: 'Region' column not found in the DataFrame.")

# prompt: usando el dataframe df, crear un filtro con la columna State

# Assuming 'State' is a column in your DataFrame.
# Replace 'State' with the actual column name if different.
if 'State' in df.columns:
    state_filter = st.selectbox("Select State", df['State'].unique())
    filtered_df = df[df['State'] == state_filter]
    st.write(filtered_df)
else:
    st.error("Error: 'State' column not found in the DataFrame.")
