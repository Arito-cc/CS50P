def convert(str):
    if ":)"in str:
        str = str.replace(":)","🙂")
    if ":(" in str:
        str = str.replace(":(","🙁")
    return str

str = input()
str = convert(str)
print(str)
