import streamlit as st
import pandas as pd

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
  df = pd.read_excel("SalidaFinal.xlsx")
  st.write(df) # Display the DataFrame using Streamlit
except FileNotFoundError:
  st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
  st.error(f"An error occurred: {e}"
