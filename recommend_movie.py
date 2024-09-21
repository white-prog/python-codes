movies_by_genre = {
    "Action": ["Mad Max: Fury Road", "Die Hard", "The Dark Knight", "John Wick"],
    "Comedy": ["The Hangover", "Superbad", "Anchorman", "Step Brothers"],
    "Drama": ["The Godfather", "Shawshank Redemption", "Fight Club", "Forrest Gump"],
    "Science Fiction": ["Inception", "The Matrix", "Blade Runner 2049", "Interstellar"],
    "Horror": ["The Exorcist", "A Nightmare on Elm Street", "Get Out", "The Conjuring"],
    "Romance": ["The Notebook", "Pride and Prejudice", "Titanic", "La La Land"],
    "Animated": ["Toy Story", "Finding Nemo", "Spirited Away", "The Lion King"],
    "Thriller": ["Se7en", "Gone Girl", "Prisoners", "The Silence of the Lambs"],
    "Fantasy": ["The Lord of the Rings", "Harry Potter and the Sorcerer's Stone", "The Hobbit", "Pan's Labyrinth"],
    "Documentary": ["Planet Earth", "The Last Dance", "Won't You Be My Neighbor?", "13th"]
}

# Example of accessing movies under a specific genre
def camelCase(word):
    word = list(word)
    word[0] = word[0].upper()
    word = "".join(word)
    return word



def recommend_movies(genre):
    try:
        for i in movies_by_genre[camelCase(genre)]:
            print(i)
    except:
        print("Genre don't found in our data")
recommend_movies("fantasy")

