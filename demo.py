# prompt: muestra el dataframe con streamlit

import pandas as pd
import streamlit as st

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
  df = pd.read_excel("SalidaFinal.xlsx")
  st.dataframe(df) # Display the DataFrame using st.dataframe for better interactivity
except FileNotFoundError:
  st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
  st.error(f"An error occurred: {e}")
  
