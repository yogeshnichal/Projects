def string(words):
    sen = "Something" + ' ' + words
    return sen

def main():
    print("Enter the words: ")
    sen1 = (input())

    write = string(sen1)
    print("Give_me_"+write)

if __name__ == "__main__":
    main()