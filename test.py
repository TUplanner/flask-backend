import requests

# Define the URL
BASE_URL = "https://prd-xereg.temple.edu/StudentRegistrationSsb"


def auth_session(txt_term):
    session = requests.Session()
    session.post(f"{BASE_URL}/ssb/term/search?mode=search", data={"term": txt_term})
    return session


# Define the query parameters
def get_all_classes(subjectcoursecombo, term):

    session = auth_session(term)
    params = {
        "txt_subjectcoursecombo": subjectcoursecombo,
        "txt_term": term,
        "pageOffset": 0,
        "pageMaxSize": 10,
        "sortColumn": "subjectDescription",
        "sortDirection": "asc",
    }

    # Make the GET request
    response = session.get(f"{BASE_URL}/ssb/searchResults/searchResults", params=params)
    data = response.json()["data"]

    parsedData = [
        {
            "course": course["subjectCourse"],
            "professor": [
                {
                    "name": professor["displayName"],
                    "primaryIndicator": professor["primaryIndicator"],
                }
                for professor in course["faculty"]
            ],
            "meetingTime": [
                {
                    "beginTime": meeting["meetingTime"]["beginTime"],
                    "endTime": meeting["meetingTime"]["endTime"],
                    "hoursWeek": meeting["meetingTime"]["hoursWeek"],
                    "days": [
                        day
                        for day in [
                            "monday",
                            "tuesday",
                            "wednesday",
                            "thursday",
                            "friday",
                            "saturday",
                            "sunday",
                        ]
                        if meeting["meetingTime"][day]
                    ],
                }
                for meeting in course["meetingsFaculty"]
            ],
        }
        for course in data
    ]

    return parsedData
