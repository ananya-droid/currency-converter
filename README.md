# USD to INR Currency Converter

A simple Python tool that converts US Dollars to Indian Rupees using live exchange rates from ExchangeRate-API. This project includes both a command-line script and a web app built with Streamlit.

Live App:  https://currency-converter-cholycfgpekxi2tvmtc7rc.streamlit.app/

## Features

- Real-time currency conversion using live API data
- Two ways to use: command-line tool and web interface
- Handles errors gracefully with clear messages
- Secure API key management using environment variables
- Clean and user-friendly interface

## How to Setup

1. Make sure you have Python installed on your computer
2. Install the required packages by running:
   pip install streamlit requests python-dotenv

3. Get your free API key from ExchangeRate-API website
4. Create a file named .ENV in your project folder and add your key:
   EXCHANGE_RATE_API_KEY=your_actual_key_here

## How to Use

Web App (Recommended):
- Run the command: python -m streamlit run app.py
- Your browser will open automatically
- Enter the amount in USD and click Convert!

Command Line:
- Run the command: python currency_converter.py
- Follow the prompts to enter the amount
- See the conversion result instantly

## Project Files

- app.py - The web application using Streamlit
- currency_converter.py - The command-line version
- .ENV - Contains your API key (keep this secret!)
- .gitignore - Prevents secret keys from being uploaded
- README.md - This documentation file

## Technical Details

Built with:
- Python for the programming logic
- Streamlit for the web interface
- Requests library for API calls
- ExchangeRate-API for live currency data

## Security Note

The API key is stored in the .ENV file which is not uploaded to GitHub. Never share your API key or commit it to version control.
