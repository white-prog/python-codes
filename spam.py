def isSpam(no,ds):
    val = []
    for i in ds:
        if ds[i] == no:
            val.append(i)
            val.append(ds[i])
            break
    if len(val) > 1:
        return str(val)
    else:
        return "Spam"

def main():
    data_set = {"jhon":"+U78 78363534","george":"+U78 9028288","viera" : "+E88 4444"} #replace it with data base
    print(isSpam("+E88 4444",data_set))

if __name__ == "__main__":
    main()
        




