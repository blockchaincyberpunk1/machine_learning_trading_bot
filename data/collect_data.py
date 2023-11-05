# Import necessary libraries
import os  # Operating System module for handling environment variables
import pandas as pd  # Pandas library for data manipulation
from alpha_vantage.timeseries import TimeSeries  # Alpha Vantage API for financial data retrieval
from dotenv import load_dotenv  # Load environment variables from a .env file

# Load environment variables from a .env file (assuming you have one)
load_dotenv()

# Retrieve the Alpha Vantage API key from environment variables
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# Define a function to fetch historical data for a given stock symbol and save it to a CSV file
def fetch_historical_data(symbol, output_csv):
    # Create a TimeSeries instance with the Alpha Vantage API key and set the output format to Pandas DataFrame
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format="pandas")
    
    # Use the Alpha Vantage API to fetch daily historical data for the specified symbol, requesting "full" data
    data, meta_data = ts.get_daily(symbol=symbol, outputsize="full")
    
    # Save the retrieved data to a CSV file with the specified output_csv filename
    data.to_csv(output_csv)

# The following code block will only run if this script is executed directly, not when it's imported as a module
if __name__ == "__main__":
    # Call the fetch_historical_data function with the symbol "AAPL" (Apple Inc.) and the output CSV file path "data/historical_data.csv"
    fetch_historical_data("AAPL", "data/historical_data.csv")


""" 
Explanation:

Import necessary libraries: Import the required libraries for this script, including os, pandas, alpha_vantage, and dotenv.

Load environment variables: Use load_dotenv() to load environment variables from a .env file. This allows you to securely store sensitive information like your API keys without hardcoding them in your script.

Retrieve the API key: Fetch the Alpha Vantage API key from the environment variables, which was loaded in the previous step.

Define the fetch_historical_data function: This function takes two arguments, symbol (the stock symbol) and output_csv (the output CSV file path). Inside the function, it uses the Alpha Vantage API to fetch daily historical data for the specified symbol, requesting the "full" data. It then saves the retrieved data to a CSV file with the specified filename.

Conditional execution: The if __name__ == "__main__": block ensures that the code inside it is executed only when the script is run directly, not when it's imported as a module in another script.

Fetch historical data: Inside the conditional block, the fetch_historical_data function is called with the symbol "AAPL" (Apple Inc.) and the output CSV file path "data/historical_data.csv". This line of code initiates the data retrieval and CSV file creation process.
"""