def encode(value,emoji_map):
    new_val = ""
    for i in value:
        if i in emoji_map:
            new_val += emoji_map[i]
        else:
            new_val += i
    value = "blur"
    return new_val
#function for decode

def main():
    emoji_map = {
    'a': '\U0001F34E',  # 🍎
    'b': '\U0001F34F',  # 🍏
    'c': '\U0001F350',  # 🍐
    'd': '\U0001F34A',  # 🍊
    'e': '\U0001F34C',  # 🍌
    'f': '\U0001F352',  # 🍒
    'g': '\U0001F353',  # 🍓
    'h': '\U0001F34D',  # 🍍
    'i': '\U0001F96D',  # 🥭
    'j': '\U0001F34B',  # 🍋
    'k': '\U0001F349',  # 🍉
    'l': '\U0001F348',  # 🍈
    'm': '\U0001F336',  # 🌶️
    'n': '\U0001F33F',  # 🌿
    'o': '\U0001F344',  # 🍄
    'p': '\U0001F341',  # 🍁
    'q': '\U0001F340',  # 🍀
    'r': '\U0001F33E',  # 🌾
    's': '\U0001F33D',  # 🌽
    't': '\U0001F33A',  # 🌺
    'u': '\U0001F33B',  # 🌻
    'v': '\U0001F32E',  # 🌮
    'w': '\U0001F32F',  # 🌯
    'x': '\U0001F331',  # 🌱
    'y': '\U0001F332',  # 🌲
    'z': '\U0001F334',  # 🌴
}
    val = "Hello world"
    encoded = encode(val,emoji_map)
    print(encoded)

if __name__ == "__main__":
    main()

        
                
    