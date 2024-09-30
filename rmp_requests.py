import requests
from rmp_configuration import URL, HEADERS, create_payload


def get_professor(professor: str) -> dict:
    """
    Retrieves information about a professor from the RateMyProfessors API.

    Args:
        professor (str): The name of the professor to search for.

    Returns:
        dict: A dictionary containing professor details or an error message.
    """
    try:
        payload = create_payload(professor)
        response = requests.post(URL, json=payload, headers=HEADERS)
        data = response.json()
        # Limited to 1 teacher as specified in rmp_configuration
        teachers = data["data"]["newSearch"]["teachers"]["edges"]
        teacher = teachers[0]["node"]

        return teacher

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
