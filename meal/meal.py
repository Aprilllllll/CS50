#def main():
#    ...
inputtime="7:50"

def convert(time):
    hour, minute = time.split(":")
    convert_minute = float(int(minute)/60)
    return hour+str(convert_minute)
#    return hour

result=convert(inputtime)
print(result)
#if __name__ == "__main__":
#    main()
