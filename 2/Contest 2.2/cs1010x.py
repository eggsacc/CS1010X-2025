def time_difference(time1, time2):
    # Fill in your code here
    time1_s = time_to_seconds(time1)
    time2_s = time_to_seconds(time2)
    difference = (time1_s - time2_s) if time1_s > time2_s else (time2_s - time1_s)
    print(difference)
    
    hours = int((difference - difference % (60 * 60)) / (60 * 60))
    
    difference %= (60 * 60)
    minutes = int((difference - difference % 60) / 60)
    
    difference %= 60
    seconds = int(difference)
    
    
    return make_time_string(hours, minutes, seconds)
    
# Predefined helper functions. Do not edit them.
def time_to_seconds(time):
    x = list(map(int, time.split(":")))
    return x[0] * 3600 + x[1]*60 + x[2]

def make_time_string(hours, mins, seconds):
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, seconds)

print(time_difference('01:02:03', '13:12:11'))