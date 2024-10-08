# Building Currency Converter in Python

## Author

Name: Zhikang Chen
Student ID: 25402328

## Description

FX Converter is a web program I designed through python and Streamlit. This program provides each user with real-time and historical exchange rate data for the currencies they want to know about. I also designed a currency trend chart to give the user a clear visualization of how the 2 currencies have changed over a specified period of time.
I couldn't wait to try it out when I first finished the code for the trend chart. But I waited 5 minutes FX still didn't finish charting Jan 2023 to Oct 2024 at RUNNING. I then realized that the current reading of the data was being done one day at a time which made it inefficient. So I tried to change the reading method to time-area reading, but I don't know why it kept failing and returning 404 during debugging. So I can only change the strategy back to the original daily query, just set the maximum charting time to 15 days to reduce the program running time.
I've improved the original code a bit, I've added a restriction to the selected time so that the user can't select the number of days in the future. But in the future I might add some other features, such as comparing exchange rates for multiple currencies, adding a history of currency lookups, etc.

## How to Setup

1. **Project Clone**     Clone the project locally via Git：  

    ```bash   git clone https://github.com/Yaoyuk/FX-Converter.git

Python 3.11.5
matplotlib                   3.7.2

pandas                        2.0.3

requests                      2.31.0

streamlit                     1.38.0

## How to Run the Program

Launch the Streamlit application by running the following command in the project directory:
streamlit run app.py
On the page you can do the following:
1.Enter the amount and select the source and target currencies, click “Get Latest Rate” button to get the latest exchange rate.
2.Select a date and click on the “Get Historical Rate” button to get the historical rate for the specified date.
3.Select a date range (up to 15 days) and click “Show Historical Trend” to see the trend of the exchange rate.

## Project Structure

app.py                 # main Streamlit python script used for managing users’ inputs and displaying results

api.py                 #python script that will contain the code for making API calls

frankfurter.py         # python script that will contain the functions used for calling relevant Frankfurter endpoints and extracting information.

currency.py            #  python script that will contain the function used for formatting the results to be displayed in the Streamlit app.

README.md              # a markdown file containing  details

## Citations

Frankfurter API: https://www.frankfurter.app/

Streamlit doc: https://docs.streamlit.io/
