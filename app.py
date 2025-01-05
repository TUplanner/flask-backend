from flask import Flask, jsonify, make_response, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://tuplanner-v12.vercel.app"])


@app.route("/proxy/session", methods=["POST"])
def auth_session():
    response = requests.post(
        "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/search?mode=search",
        data={"term": 202436},
    )

    flask_response = make_response(response.text, response.status_code)

    for cookie_name, cookie_value in response.cookies.items():
        flask_response.set_cookie(
            cookie_name,
            cookie_value,
            samesite="None",
            secure=True,
        )

    for header, value in response.headers.items():

        if header.lower() not in ["content-length", "transfer-encoding"]:
            flask_response.headers[header] = value

    return flask_response


@app.route("/testing")
def testing():
    cookies = request.cookies

    external_response = requests.get(
        "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202503&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc",
        cookies=cookies,
    )

    flask_response = Response(
        external_response.content, status=external_response.status_code
    )

    return flask_response


# if __name__ == "__main__":
#     app.run(debug=True)
