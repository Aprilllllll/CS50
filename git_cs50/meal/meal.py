

def main():
    converted_time=convert(input("What time is it? ").strip())
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

if __name__ == "__main__":
   main()







