species_dna_similarity = {
    "Chimpanzee": 98.8,
    "Bonobo": 98.7,
    "Gorilla": 98.4,
    "Orangutan": 96.9,
    "Mouse": 85.0,
    "Dog": 84.0,
    "Chicken": 60.0,
    "Banana": 60.0,
    "Fruit Fly": 44.0,
    "Yeast": 26.0
}
def to_capital(string):
    try:
        return string[0].upper() + string[1:].lower()
    except:
        return "Error in text"

def get_similarty(spe):
    if spe in species_dna_similarity.keys():
        print(f"{spe} similarity with humans is {species_dna_similarity[spe]} ")
    else:
        print(f"{spe} not found in our storage but adds nearly")
    
def main():
    while True:
        inp = input("Enter name of organism to check similarity with human(TYPE E TO EXIT):::  ")
        get_similarty(to_capital(inp))
        if inp == 'E':
            print("Thank You!")
            break

if __name__ == "__main__":
    main()
