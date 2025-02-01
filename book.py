class Book:
    def __init__(self,bookname,id):
        self.bookname = bookname
        self.id = id
    def display(self):
        print(f"{self.bookname} {self.id}")
    
def main():
    book1 = Book("history",1)
    book1.display()

if __name__ == "__main__":
    main()
