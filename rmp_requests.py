import requests
from rmp_configuration import URL, HEADERS, create_payload


def get_professor(professor: str) -> dict:
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
