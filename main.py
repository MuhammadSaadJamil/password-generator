from utilities.passwordUtils import generate_password


def initiate():
    print("=" * 30)
    print("\tPassword generator")
    print("=" * 30)
    print('Create your password, Enter "y" for YES and any other key for NO')
    alpha = input("Include alphabets : ") == "y"
    num = input("Include numerics : ") == "y"
    special = input("Include special characters : ") == "y"
    length = int(input("Length : "))
    print(f"Password : {generate_password(length, alpha, num, special)}")


if __name__ == "__main__":
    initiate()
