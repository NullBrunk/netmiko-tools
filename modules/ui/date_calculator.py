def date_calculator(starting, ending):
    s_hour, s_minute, s_second = starting.split(":")
    e_hour, e_minute, e_second = ending.split(":")

    # On converti en seconde
    start_seconds = s_hour * 3600 + s_minute * 60 + s_second
    end_seconds = e_hour * 3600 + e_minute * 60 + e_second

    # On calcul la duree en secondes
    duration_seconds = end_seconds - start_seconds

    # On reconverti en heures, minutes, secondes
    hours = duration_seconds // 3600
    minutes = (duration_seconds % 3600) // 60
    seconds = duration_seconds % 60

    to_ret = ""
    if(hours != 0):
        to_ret += f"{hours:02} hours "
    if(minutes != 0):
        to_ret += f"{minutes:02} minutes "
    if(seconds != 0):
        to_ret += f"{seconds:02} seconds "

    return to_ret
