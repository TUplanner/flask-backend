from typing import List, Tuple

# Define types for days and times
Days = List[str]
StartTime = int
EndTime = int

# Define the type for a meeting time
MeetingTime = Tuple[Days, StartTime, EndTime]

# Define the type for a course (list of meeting times)
Course = List[MeetingTime]

# Define the type for a course group (list of courses)
CourseGroup = List[Course]

# Define the type for all courses (list of course groups)
AllCourses = List[CourseGroup]

# Define the type for a schedule (list of courses)
Schedule = List[Course]

# Define the type for all schedules (list of schedules)
AllSchedules = List[Schedule]


def reformat_courses(all_courses: List[List[dict]]) -> AllCourses:
    return [
        [
            [
                (mt["days"], int(mt["beginTime"]), int(mt["endTime"]))
                for mt in course["meetingTime"]
            ]
            for course in course_group
        ]
        for course_group in all_courses
    ]


def is_overlapping(mt1: MeetingTime, mt2: MeetingTime) -> bool:
    # Check for common days
    if not set(mt1[0]) & set(mt2[0]):
        return False

    # Check for time overlap on common days
    return mt1[1] < mt2[2] and mt2[1] < mt1[2]


def valid_meeting_time(schedule: Schedule, new_mt: MeetingTime) -> bool:
    # if any of the meeting times in the schedule overlap with the new meeting time, return False
    return not any(is_overlapping(mt, new_mt) for course in schedule for mt in course)


def valid_course(schedule: Schedule, course: Course) -> bool:
    # if all meeting times in the course are valid, return True
    return all(valid_meeting_time(schedule, mt) for mt in course)


def get_all_schedules(all_courses: AllCourses) -> AllSchedules:
    all_schedules = []

    for fixed_course in all_courses[0]:  # iterate over the 1st course group
        schedule = [fixed_course]

        for course_group in all_courses[1:]:  # skip the first course group
            valid_course_found = next(
                (course for course in course_group if valid_course(schedule, course)),
                None,
            )
            if valid_course_found:
                schedule.append(valid_course_found)
            else:
                break  # Stop iterating over the course groups and move on to the next schedule
        else:
            all_schedules.append(schedule)

    return all_schedules
