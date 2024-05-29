def main(converted_time):
    if 7.00 <= converted_time <= 8.00:
        print("breakfast time")
    if 12.00 <= converted_time <= 13.00:
        print("lunch time")
    if 18.00 <= converted_time <= 19.00:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    convert_hour = float(hour)
    convert_minute = float(float(minute)/60)
    sum_up = convert_hour + convert_minute
    return round(sum_up, 2)


input_time=input("What time is it? ")
main(convert(input_time))

if __name__ == "__main__":
    main()







