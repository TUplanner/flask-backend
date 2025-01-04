import requests

BASE_URL = "https://prd-xereg.temple.edu/StudentRegistrationSsb"
COURSE_SEARCH_URL = f"{BASE_URL}/ssb/courseSearchResults/courseSearchResults"
TERM_SEARCH_URL = f"{BASE_URL}/ssb/term/search?mode=courseSearch"
TERM = 202436


def fetch_all_classes():
    page_size = 500
    classes = []
    offset = 0

    with requests.Session() as session:
        session.post(TERM_SEARCH_URL, data={"term": TERM})

        res = session.get(
            "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/get_subject?searchTerm=&term=202436&offset=1&max=500"
        )
        data = res.json()
        
        # while True:
        #     response = session.get(
        #         COURSE_SEARCH_URL,
        #         params={
        #             "txt_term": TERM,
        #             "pageOffset": offset,
        #             "pageMaxSize": page_size,
        #             "sortColumn": "subjectDescription",
        #             "sortDirection": "asc",
        #         },
        #     )

        #     data = response.json()
        #     if not data.get("data"):
        #         break

        #     classes.extend(
        #         {
        #             "s": item["subjectCode"],
        #             "n": item["courseNumber"],
        #             "t": item.get("courseTitle"),
        #             "l": item.get("creditHourLow"),
        #             **(
        #                 {"h": item["creditHourHigh"]}
        #                 if item.get("creditHourHigh") is not None
        #                 else {}
        #             ),
        #         }
        #         for item in data["data"]
        #     )

        #     offset += page_size

    return [item["code"] for item in data]

