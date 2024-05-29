input_time=input("What time is it? ").strip()

def main():
    converted_time=convert(input_time)
    if 7.00 <= converted_time <= 8.00:
        print("breakfast time")
    elif 12.00 <= converted_time <= 13.00:
        print("lunch time")
    elif 18.00 <= converted_time <= 19.00:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    converted_h=float(hour)
    converted_m=float(minute)
    converted_time=float(converted_h + (converted_m/60))
    return converted_time

#def convert(time):
#    hours, minutes = time.split(":")
# hours = float(time[0])
# minutes = float((time[1])/60)
#   c_minutes = float(minutes)
#    c_hours = float(hours)
#    meal = float(hours + (minutes/60))
#    return meal


if __name__ == "__main__":
   main()







