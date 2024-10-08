import requests

def get_url(url: str):
    """
    Function that will call a provided GET API endpoint URL and return its status code and either its content or error message as a string.

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        return response.status_code, str(e)
