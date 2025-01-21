def decoration(func):
    def greeter(nm):
        print(f"Hello , {func(nm)}")
    return greeter





def main():

    @decoration
    def sayname(name):
        return name
    
    sayname("jhon")
    
    




if __name__ == "__main__":
    main()