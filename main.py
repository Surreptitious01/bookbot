def main():
    bookpath = 'books/frankenstein.txt'
    with open(bookpath) as f:
        file_contents = f.read()

    def charCount():
        chars = {}
        for c in file_contents:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
        print(chars)
    
    def wordCount():
        words = file_contents.split()

        count = 0
        for word in words:
            count+=1

        print(count)

    def readBook():
        print(file_contents)

    def bookReport():
        print("---Begin report of", bookpath)
        wordCount()
        print("\n")
        charCount()
    bookReport()

main()
