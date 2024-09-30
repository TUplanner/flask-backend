# Configuration


# Constants for GraphQL request
URL = "https://www.ratemyprofessors.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Basic dGVzdDp0ZXN0",
}
FULL_QUERY = """
query RateMyProfessorAPI($query: TeacherSearchQuery!, $count: Int) {
    newSearch {
        teachers(query: $query, first: $count) {
            didFallback
            edges {
                cursor
                node {
                    id
                    legacyId
                    firstName
                    lastName
                    department
                    departmentId
                    school {
                        legacyId
                        name
                        id
                    }
                    avgRating
                    numRatings
                    wouldTakeAgainPercentRounded
                    mandatoryAttendance {
                        yes
                        no
                        neither
                        total
                    }
                    takenForCredit {
                        yes
                        no
                        neither
                        total
                    }
                    ratingsDistribution {
                        total
                        r1
                        r2
                        r3
                        r4
                        r5
                    }
                    legacyId
                    numRatings
                    lockStatus
                }
            }
        }
    }
}
"""


def create_payload(professor: str, count: int = None) -> dict:
    """
    Constructs the payload for the GraphQL request.

    Args:
        professor (str): The name of the professor to search for.
        count (int, optional): The number of results to retrieve.
    """
    variables = {
        "query": {
            "text": professor,
            "schoolID": "U2Nob29sLTk5OQ==",
        }
    }

    if count is not None:
        variables["count"] = count

    return {"query": FULL_QUERY, "variables": variables}
