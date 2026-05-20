import streamlit as st
import pandas as pd

# Set up the page
st.set_page_config(page_title="TIMpeccable Shop", layout="wide")
st.title("✨ TIMpeccable Auto Spa - Shop")

# Load the database
try:
    df = pd.read_csv("products.csv")
    
    # Display products dynamically
    for index, row in df.iterrows():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(row['Image_URL'], width=150)
        with col2:
            st.subheader(row['Name'])
            st.write(f"Category: {row['Category']}")
            st.write(f"Price: R{row['Price']}")
            if st.button(f"Buy {row['Name']}", key=index):
                st.success(f"Added {row['Name']} to cart!")
except Exception as e:
    st.error(f"Error loading products: {e}")

