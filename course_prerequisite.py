import requests
from bs4 import BeautifulSoup
import re


def get_curriculum() -> list:
    curriculum = list()

    try:
        response = requests.get(
            "https://bulletin.temple.edu/undergraduate/science-technology/computer-science-bs/#requirementstext"
        )
        soup = BeautifulSoup(response.content, "lxml")
        main_body = soup.find("div", id="requirementstextcontainer")

        rows = main_body.find_all("tr", class_=["even", "odd"])

        for row in rows:
            course_code_html = row.find("a", class_="bubblelink code")
            if course_code_html:
                course_code = (
                    course_code_html.get_text(strip=True).replace("\xa0", " ").strip()
                )
                if str(course_code).find("BIOL") != -1:
                    break

                prerequisite = requests.get(
                    f"https://bulletin.temple.edu/ribbit/index.cgi?page=getcourse.rjs&code={course_code}"
                )
                prerequisite_soup = BeautifulSoup(prerequisite.content, "lxml")
                all_p = prerequisite_soup.find_all("p")

                first_p = re.sub(r"\s+", " ", all_p[0].get_text(strip=True)).replace(
                    "\xa0", " "
                )
                last_p = re.sub(r"\s+", " ", all_p[-1].get_text(strip=True)).replace(
                    "\xa0", " "
                )

                idk = f"{first_p} {last_p}".strip()
                curriculum.append(idk)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    return curriculum
