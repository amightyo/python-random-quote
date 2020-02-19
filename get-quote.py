import random


def begin():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes)-1
    nQuotes = random.randint(0, last)
    rnd = []
    for i in range(nQuotes):
        rnd.append(random.randint(0, last))

    for i in set(rnd):
        print(quotes[i], end="")


def addNewQuote():
    f = open("quotes.txt", "a")
    f.write("We always find the time to do what we love")
    f.close()


if __name__ == "__main__":
    begin()
    # addNewQuote()
