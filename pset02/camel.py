def main():
    camel = input("camelCase : ")
    snake = snake_case(camel)
    print(f"snake_case : {snake}")


def snake_case(camel):
    s = ""
    for c in camel:
        if c.islower() :
            s+=c
        else:
            s+="_"
            s+=c.lower()

    return s


main()

