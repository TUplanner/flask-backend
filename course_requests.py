import requests


def get_request(endpoint: str) -> list:
    """
    Fetches data from a specified endpoint of the Temple University API.

    Args:
        endpoint (str): The API endpoint to call (e.g., "getTerms").

    Returns:
        list: A list of data items returned from the API.
        If the endpoint is "getTerms", filters out items where "Orientation" is in the "description" field.

        EX: [{'code': '202436', 'description': '2024 Fall'}, {'code': '202426', 'description': '2024 Summer II'}, {'code': '202420', 'description': '2024 Summer I'}]

    """
    url = f"https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/classSearch/{endpoint}"
    params = {
        "offset": 1,
        "max": 6,
    }

    try:
        response = requests.get(url, params)
        data = response.json()

        if endpoint == "getTerms":
            data = [term for term in data if "Orientation" not in term["description"]]

    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

    return data
