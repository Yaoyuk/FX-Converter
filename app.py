import streamlit as st
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output
from api import get_url
import streamlit as st
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output
from api import get_url

# Display Streamlit App Title

# Get the list of available currencies from Frankfurter

# If the list of available currencies is None, display an error message in Streamlit App

# Add input fields for capturing amount, from and to currencies

# Add a button to get and display the latest rate for selected currencies and amount

# Add a date selector (calendar)

# Add a button to get and display the historical rate for selected date, currencies and amount


st.title("FX Converter")


currencies = get_currencies_list()

if currencies:
    currency_codes = list(currencies.keys())


    amount = st.number_input("Enter the amount to be converted:", min_value=0.0, value=50.0)
    from_currency = st.selectbox("From Currency:", currency_codes)
    to_currency = st.selectbox("To Currency:", currency_codes)


    if from_currency == to_currency:
        st.error("Please select different currencies for conversion.")
    else:
        if st.button("Get Latest Rate"):
            date, rate = get_latest_rates(from_currency, to_currency, amount)
            if rate:
                result = format_output(date, from_currency, to_currency, rate, amount)
                st.write(result)
            else:
                st.error("Error: Fetching latest rates.")

 
    selected_date = st.date_input("Select a date for historical rates:", value=datetime.date.today(), max_value=datetime.date.today())

    
    if st.button("Get Historical Rate"):
        historical_rate = get_historical_rate(from_currency, to_currency, selected_date, amount)
        if historical_rate:
            st.write(format_output(selected_date, from_currency, to_currency, historical_rate, amount))
        else:
            st.error("Error: Fetching historical rates.")
    
    
    st.subheader("Historical Exchange Rate Trend")
    start_date = st.date_input("Start Date:", value=datetime.date(2023, 1, 1), max_value=datetime.date.today())
    end_date = st.date_input("End Date:", value=datetime.date.today(), max_value=datetime.date.today())

    # Limit the maximum day is 15
    max_days = 15
    date_diff = (end_date - start_date).days

    if date_diff > max_days:
        st.error(f"Please select a date range of no more than {max_days} days.")
    else:
        # Get the exchange rate day by day
        if st.button("Show Historical Trend"):
            if start_date >= end_date:
                st.error("Start date must be before the end date.")
            else:
                dates = pd.date_range(start=start_date, end=end_date).to_pydatetime().tolist()
                rates = []
                for date in dates:
                   
                    url = f"https://api.frankfurter.app/{date.strftime('%Y-%m-%d')}?from={from_currency}&to={to_currency}"
                    
                    status_code, response = get_url(url)
                    
                    if status_code == 200:
                        rate = response['rates'].get(to_currency, None)
                        if rate:
                            rates.append(rate)
                        else:
                            rates.append(None)
                    else:
                        st.error("Error: Fetching historical rates.")
                        break
                

                if rates:
                    dates = pd.to_datetime(dates)
                    fig, ax = plt.subplots()
                    ax.plot(dates, rates, label=f"{from_currency} to {to_currency}")
                    ax.set_xlabel('Date')
                    ax.set_ylabel('Exchange Rate')
                    ax.legend()
                    
                   
                    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
                    plt.xticks(rotation=45)
                    
                    st.pyplot(fig)
else:
    st.error("Error: Fetching currencies list.")
