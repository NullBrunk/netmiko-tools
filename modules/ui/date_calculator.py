def date_calculator(starting, ending):
    s_hour, s_minute, s_second = map(int, starting.split(":"))
    e_hour, e_minute, e_second = map(int, ending.split(":"))

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
        to_ret += f"{hours:02} hour{'' if hours == 1 else 's'} "
    if(minutes != 0):
        if(not(hours == 0 and minutes < 10)):
            to_ret += "0"
        to_ret += f"{seconds} minute{'' if minutes == 1 else 's'} "
    if(seconds != 0):
        if(not(hours == 0 and minutes == 0 and seconds < 10)):
            to_ret += "0"
        to_ret += f"{seconds} second{'' if seconds == 1 else 's'}"

    if(to_ret == ""):
        to_ret = "0 second"
    return to_ret
