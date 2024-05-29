input_time=input("What time is it? ")

def main():
    converted_time=convert(input_time)
    if 7.00 <= converted_time <= 8.00:
        print("breakfast time")
    if 12.00 <= converted_time <= 13.00:
        print("lunch time")
    if 18.00 <= converted_time <= 19.00:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    convert_minute = float(minute)/60
    return float(hour) + convert_minute

if __name__ == "__main__":
   main()







