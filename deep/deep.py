answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")

case_insensitive_answer=answer.lower()
no_space_string=case_insensitive_answer.strip
match no_space_string:
    case "42" | "forty two" | "forty-two":
        print("Yes")

    case _:
        print("No")

