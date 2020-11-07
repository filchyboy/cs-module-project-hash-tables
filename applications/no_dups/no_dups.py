def no_dups(s):
    duplicates = {}
    words = s.split(" ")
    new_string = []
    for word in words:
        if word not in duplicates:
            duplicates[word] = 1
            new_string.append(word)
    new_string = ' '.join(new_string)
    return new_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs and spam and sausage but no spam spam and spam"))