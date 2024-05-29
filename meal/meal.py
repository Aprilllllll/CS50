#def main():
#    ...
inputtime="7:50"

def convert(time):
    hour, minute = time.split(":")
    convert_hour = float(hour)
    convert_minute = float(float(minute)/60)
    sum_up = convert_hour + convert_minute
    return round(sum_up, 2)
#    return hour

result=convert(inputtime)
print(result)
#if __name__ == "__main__":
#    main()
