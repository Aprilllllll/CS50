calendar_dic = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
    }

def main():
    while True:
        user_input_date=input("Date: ").strip()
        try:
            if "/" in user_input_date:
                month, day, year = user_input_date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 0 < day < 31 and 0 < month < 13:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
                else:
                    pass
            else:
                if not "," in user_input_date:
                    pass
                else:
                    word_format_string = user_input_date.replace(","," ").split()
                    month_str = word_format_string[0].lower().capitalize()
                    day = int(word_format_string[1])
                    year = int(word_format_string[2])
                    if month_str in calendar_dic:
                        month = calendar_dic[month_str]
                        if 0 < day < 31 and 0 < month < 13:
                            print(f"{year:04d}-{month:02d}-{day:02d}")
                            break
                        else:
                            pass
        except (ValueError, IndexError):
            pass

main()
