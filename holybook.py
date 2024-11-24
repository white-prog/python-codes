def word_cnt(st,wrdd):
    wrd = 0
    li = st.split(" ")
    for i in li:
        if i == wrdd:
            wrd += 1
    return "wrdd" + " " + "repeats" + " " + str(wrd) + " " + "times"

def main():
    Passage = "God is love. Love is patient and kind. Love does not envy or boast."
    print(word_cnt(Passage,"love"))

if __main__ == "__name__":
    main()
