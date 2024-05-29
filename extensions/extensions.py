#clear input to all lowercase string
user_input=input("File name: ")

#function that take extension name
clean_string=user_input.strip().lower()

def remove_before_last_dot(t, s):
    splited_set=t.split(s)
    return splited_set[-1]

#match extension
extension=remove_before_dot(clean_string, ".")
output_set={'gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip'}

if extension not in output_set:
    print("application/octet-stream")

else:
    match extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
