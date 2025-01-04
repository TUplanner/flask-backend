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


def is_overlapping(meeting_time1: MeetingTime, meeting_time2: MeetingTime) -> bool:
    # Extract days and times
    days1, start_time1, end_time1 = meeting_time1
    days2, start_time2, end_time2 = meeting_time2

    # Check for common days
    common_days = set(days1) & set(days2)
    if not common_days:
        return False  # No common days, no overlap

    # Check for time overlap on the common days
    # Two times overlap if one start time is before the other end time and the other start time is before the first end time
    return start_time1 < end_time2 and start_time2 < end_time1


def valid_meeting_time(schedule: Schedule, new_meeting_time: MeetingTime) -> bool:
    for course in schedule:
        for meeting_time in course:
            if is_overlapping(meeting_time, new_meeting_time):
                return False

    return True


def valid_course(schedule: Schedule, course: Course) -> bool:
    for meeting_time in course:
        if not valid_meeting_time(schedule, meeting_time):
            return False

    return True


def get_all_schedules(all_courses: AllCourses) -> AllSchedules:
    all_schedules = []

    for fixed_course in all_courses[0]:  # iterate over the 1st course group
        schedule = [fixed_course]

        for course_group in all_courses[1:]:  # skip the first course group
            for course in course_group:  # iteration starts from 2nd course group
                if valid_course(schedule, course):
                    schedule.append(course)
                    break  # Move on to the next course group
            else:  # If no course is added from this group, move on to the next possible schedule
                break
        else:  # if a course is added from each group, add the schedule to the list of all schedules
            all_schedules.append(schedule)

    return all_schedules
