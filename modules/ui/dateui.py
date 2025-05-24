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


from datetime import datetime, timedelta

def format_relative_time(timestamp_str):
    # Extrait la date depuis un truc du genre "PE1_2025-05-23_02-03-09"
    dt_str = timestamp_str.split('_', 1)[1]
    dt = datetime.strptime(dt_str, "%Y-%m-%d_%H-%M-%S")
    
    now = datetime.now()
    delta = now - dt

    seconds = int(delta.total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    days = delta.days
    years = days // 365

    if seconds < 60:
        return "just now"
    elif minutes < 60:
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif hours < 24:
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif days < 365:
        return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        return f"{years} year{'s' if years > 1 else ''} ago"

