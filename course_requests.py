import requests


def get_request(endpoint: str) -> list:
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
