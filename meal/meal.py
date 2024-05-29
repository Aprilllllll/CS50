input_time=input("What time is it? ")

#def main():
#    if 7.00 <= convert(input_time) <= 8.00:
#        print("breakfast time")
#    if 12.00 <= convert(input_time) <= 13.00:
#        print("lunch time")
#    if 18.00 <= convert(input_time) <= 19.00:
#        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    convert_hour = float(hour)
    convert_minute = float(float(minute)/60)
    sum_up = convert_hour + convert_minute
    return round(sum_up, 1)

print(convert(input_time))


#if __name__ == "__main__":
#   main()







