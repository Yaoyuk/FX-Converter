def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    return round(rate, 4)

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate != 0:
        return round(1 / rate, 4)
    return 0

def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function to format the conversion output text.

    Parameters
    ----------
    date : str
        Date of the conversion rate
    from_currency : str
        Origin currency code
    to_currency : str
        Destination currency code
    rate : float
        Conversion rate
    amount : float
        Amount in origin currency

    Returns
    -------
    str
        Formatted output string
    """
    converted_amount = round_rate(rate * amount)
    inverse_rate = reverse_rate(rate)
    return (f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate}. "
            f"So {amount} in {from_currency} correspond to {converted_amount} in {to_currency}. "
            f"The inverse rate was {inverse_rate}.")
