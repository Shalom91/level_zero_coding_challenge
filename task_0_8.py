def to_hours_and_minutes(number):
    """
    converts any number to hours and minutes
    """
    hours = number // 60
    minutes = number % 60
    hours_string = 'hours'
    minutes_string = 'minutes'

    if hours < 2:
        hours_string = 'hour'
    elif minutes < 2:
        minutes_string = 'minute'
    else:
        pass

    print(f"{hours} {hours_string}, {minutes} {minutes_string}")
