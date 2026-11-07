filename = input("Enter filename: ")

try:
    file = open(filename, "r")
    content = file.readlines()

    print("First 3 lines of the file:")
    for line in content[:3]:
        print(line, end="")

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("\nFile operation attempted.")