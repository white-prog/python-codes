def word_cnt(st,wrdd):
    wrd = 0
    li = st.split(" ")
    for i in li:
        if i.lower().replace(".", "") == wrdd:
            wrd += 1
    return "wrdd" + " " + "repeats" + " " + str(wrd) + " " + "times"

def main():
    passage = "God is love. Love is patient and kind. Love does not envy or boast."
    print(word_cnt(passage,"love"))

if __name__ == "__main__":
    main()