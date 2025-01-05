from flask import Flask, jsonify, make_response, request
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

    cookies = response.cookies

    flask_response = make_response(jsonify({"message": "Session authenticated"}), 200)

    # Set the cookies in the Flask response
    for cookie_name, cookie_value in cookies.items():
        flask_response.set_cookie(
            cookie_name,
            cookie_value,
            samesite="None",
            secure=True,
        )

    return flask_response


@app.route("/testing")
def testing():
    cookies = request.cookies

    external_response = requests.get(
        "https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202503&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc",
        cookies=cookies,
    )

    return jsonify(external_response.json()), 200


# if __name__ == "__main__":
#     app.run(debug=True)
