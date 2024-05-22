user_input_answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")

clean_string=user_input_answer.strip().lower()


match clean_string:
    case "42" | "forty two" | "forty-two":
        print("Yes")

    case _:
        print("No")

