def study_schedule(permanence_period, target_time):
    count_students = 0
    if not target_time:
        return None
    for entry_hour, exits_hour in permanence_period:
        if type(entry_hour) != int or type(exits_hour) != int:
            return None
        if entry_hour <= target_time <= exits_hour:
            count_students += 1
    return count_students
