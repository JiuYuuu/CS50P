user_input = input("File name: ").strip().lower()

if "." in user_input:
    extensions = user_input.split(".")[-1]

    if user_input.endswith((".gif", ".png")):
        print(f"image/{extensions}")
    elif user_input.endswith(".txt"):
        print(f"text/{user_input.split('.')[0]}")
    elif user_input.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    elif user_input.endswith((".pdf", ".zip")):
        print(f"application/{extensions}")
    else:
        print("application/octet-stream")

else:
    print("application/octet-stream")
