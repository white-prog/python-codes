def text_count(string):
    return len(string.split(" "))

def character_count(string):
    return len(string)

def main():
    print("Word counter")
    print("------------")
    lines = []
    while True:
        line = input("Enter text (type 'STOP' to finish): ")
        if line == "STOP":
            break
        else:
            lines.append(line)
    print("Summary: ")
    print(f"- Lines: {len(lines)}")
    print(f"- Words: {sum([text_count(ele) for ele in lines])}")
    print(f"- Characters (including spaces): {sum([character_count(ele) for ele in lines])}")

if __name__ == "__main__":
    main()