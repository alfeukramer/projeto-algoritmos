def study_schedule(permanence_period, target_time):
    counter = 0

    for first_item, last_item in permanence_period:
        print(first_item, last_item)
        try:
            if first_item <= target_time <= last_item:
                counter += 1
        except TypeError:
            return None

    return counter
