def count_time(filename):
    try:
        with open(filename,encoding="utf-8") as book:
            content=book.read()
    except FileNotFoundError:
        pass
    else:
        num_words=content.lower().count("the")
        print(num_words)

count_time("www.txt")