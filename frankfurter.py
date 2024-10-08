from api import get_url

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter to get the list of available currencies.
    
    Returns
    -------
    dict or None
        Dictionary with currency codes as keys or None in case of error.
    """
    url = "https://api.frankfurter.app/currencies"
    status_code, response = get_url(url)
    if status_code == 200:
        return response
    return None

def get_latest_rates(from_currency, to_currency, amount):
    """
    Function to get the latest conversion rates between two currencies from Frankfurter API.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}&amount={amount}"
    status_code, response = get_url(url)
    if status_code == 200:
        return response['date'], response['rates'][to_currency]
    return None, None

def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Function to get the historical conversion rate for given currencies and a specific date.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Conversion rate on the given date or None in case of error
    """
    url = f"https://api.frankfurter.app/{from_date}?from={from_currency}&to={to_currency}&amount={amount}"
    status_code, response = get_url(url)
    if status_code == 200:
        return response['rates'][to_currency]
    return None


