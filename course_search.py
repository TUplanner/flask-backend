import requests

BASE_URL = "https://prd-xereg.temple.edu/StudentRegistrationSsb"


def auth_session(txt_term):
    session = requests.Session()
    session.post(f"{BASE_URL}/ssb/term/search?mode=search", data={"term": txt_term})
    return session


def course_search(
    txt_term,
    txt_subject=None,
    txt_courseNumber=None,
    txt_course_number_range=None,
    txt_course_number_range_to=None,
    txt_keywordall=None,
    txt_campus=None,
    txt_college=None,
    txt_instructionalMethod=None,
    txt_attribute=None,
    txt_instructor=None,
    txt_partOfTerm=None,
    txt_courseTitle=None,
    txt_session=None,
    txt_credithourlow=None,
    txt_credithourhigh=None,
    chk_include_0=None,
    chk_include_1=None,
    chk_include_2=None,
    chk_include_3=None,
    chk_include_4=None,
    chk_include_5=None,
    chk_include_6=None,
    select_start_hour=None,
    select_start_min=None,
    select_start_ampm=None,
    select_end_hour=None,
    select_end_min=None,
    select_end_ampm=None,
    chk_open_only=None,
    startDatepicker=None,
    endDatepicker=None,
    uniqueSessionId=None,
    pageOffset="0",
    pageMaxSize="10",
    sortColumn="subjectDescription",
    sortDirection="asc",
):
    params = {
        "txt_subject": txt_subject,
        "txt_courseNumber": txt_courseNumber,
        "txt_course_number_range": txt_course_number_range,
        "txt_course_number_range_to": txt_course_number_range_to,
        "txt_keywordall": txt_keywordall,
        "txt_campus": txt_campus,
        "txt_college": txt_college,
        "txt_instructionalMethod": txt_instructionalMethod,
        "txt_attribute": txt_attribute,
        "txt_instructor": txt_instructor,
        "txt_partOfTerm": txt_partOfTerm,
        "txt_courseTitle": txt_courseTitle,
        "txt_session": txt_session,
        "txt_credithourlow": txt_credithourlow,
        "txt_credithourhigh": txt_credithourhigh,
        "chk_include_0": chk_include_0,
        "chk_include_1": chk_include_1,
        "chk_include_2": chk_include_2,
        "chk_include_3": chk_include_3,
        "chk_include_4": chk_include_4,
        "chk_include_5": chk_include_5,
        "chk_include_6": chk_include_6,
        "select_start_hour": select_start_hour,
        "select_start_min": select_start_min,
        "select_start_ampm": select_start_ampm,
        "select_end_hour": select_end_hour,
        "select_end_min": select_end_min,
        "select_end_ampm": select_end_ampm,
        "chk_open_only": chk_open_only,
        "txt_term": txt_term,
        "startDatepicker": startDatepicker,
        "endDatepicker": endDatepicker,
        "uniqueSessionId": uniqueSessionId,
        "pageOffset": pageOffset,
        "pageMaxSize": pageMaxSize,
        "sortColumn": sortColumn,
        "sortDirection": sortDirection,
    }

    params = {k: v for k, v in params.items() if v is not None}

    try:
        session = auth_session(txt_term)
        response = session.get(
            f"{BASE_URL}/ssb/searchResults/searchResults", params=params
        )
        return response.json()

    except requests.RequestException as e:
        print(f"Error during course search: {e}")
        return {"success": "false"}


# Test case
result = course_search(txt_term="202436", txt_keywordall="Data Structures")
print("Test case", result)
