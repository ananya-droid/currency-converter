# app.py
import streamlit as st
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Set up the page
st.set_page_config(page_title="Currency Converter", page_icon="💰")
st.title("💰 USD to INR Converter")
st.write("Convert US Dollars to Indian Rupees using live exchange rates.")

# TEMPORARY: Hardcode your API key here for testing
API_KEY = "2b36409e266c0dc9581ccce9"  # ← Replace with your actual key
BASE_URL = "https://v6.exchangerate-api.com/v6/"

# Create input form
with st.form("converter_form"):
    usd_amount = st.number_input("Enter amount in USD:", 
                                min_value=0.0, 
                                value=100.0, 
                                step=1.0)
    convert_button = st.form_submit_button("Convert!")
    
# Handle conversion when button is clicked
if convert_button:
    if not API_KEY:
        st.error("❌ API key not found. Please check your .env file.")
    else:
        url = f"{BASE_URL}{API_KEY}/latest/USD"
        
        with st.spinner("Fetching latest exchange rate..."):
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()
                conversion_rate = data['conversion_rates']['INR']
                
                inr_amount = usd_amount * conversion_rate
                
                st.success("✅ Conversion successful!")
                st.metric(
                    label="Conversion Result",
                    value=f"₹{inr_amount:,.2f} INR",
                    delta=f"1 USD = ₹{conversion_rate:.2f} INR"
                )
                
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Network error: {e}")
            except KeyError:
                st.error("❌ Could not find exchange rate data.")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {e}")

# Footer information
st.divider()
st.caption("💡 This app uses ExchangeRate-API for live currency data. "
           "Rates update automatically every 24 hours.")