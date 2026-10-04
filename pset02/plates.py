def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

def valid_num(s):
    num = False
    for c in s:
        if c.isalpha() and num == True:
            return False
        if c.isnumeric():
            if c == '0' and num == False:
                return False
            num = True
    return True



# “All vanity plates must start with at least two letters.”
def is_2letter(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    return False


# “No periods, spaces, or punctuation marks are allowed.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def valid_len_alnum(s):
    if 2<=len(s)<=6 and s.isalnum():
        return True
    return False


def is_valid(s):
    if valid_len_alnum(s) and is_2letter(s) and valid_num(s):
        return True
    return False







main()
