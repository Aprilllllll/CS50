input_time=input("What time is it? ")

def main():
    converted_time=convert(input_time).strip()
    if 7.00 <= converted_time <= 8.00:
        print("breakfast time")
    elif 12.00 <= converted_time <= 13.00:
        print("lunch time")
    elif 18.00 <= converted_time <= 19.00:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    int_h=int(hour)
    int_m=int(minute)
    return int_h+int_m/60

if __name__ == "__main__":
   main()







