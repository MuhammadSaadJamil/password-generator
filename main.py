from utilities.passwordUtils import generate_password


def initiate():
    print("=" * 30)
    print("\tPassword generator")
    print("=" * 30)
    print('Create your password, Enter "y" for YES and any other key for NO')
    alpha = input("Include alphabets : ") == "y"
    num = input("Include numerics : ") == "y"
    special = input("Include special characters : ") == "y"
    length = 0
    while True:
        try:
            length = int(input("Length : "))
        except:
            pass
        if length and 1 <= length <= 100:
            break
        print("Invalid input. Try again!\nChoose a number between 1 and 100.")

    print(f"Password : {generate_password(length, alpha, num, special)}")


if __name__ == "__main__":
    initiate()
