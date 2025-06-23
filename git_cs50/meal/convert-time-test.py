time=input("?")

def convert(time):
    hour, minute = time.split(":")
    converted_h=int(hour)
    converted_m=int(minute)
    return converted_h + float(converted_m/60)

print(convert(time))
