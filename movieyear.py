movies = {
    "The Shawshank Redemption": 1994,
    "The Godfather": 1972,
    "The Dark Knight": 2008,
    "Pulp Fiction": 1994,
    "Forrest Gump": 1994,
    "Inception": 2010,
    "Fight Club": 1999,
    "The Matrix": 1999,
    "The Lord of the Rings: The Fellowship of the Ring": 2001,
    "Star Wars: Episode IV - A New Hope": 1977
}

def check_lis(lis):
    min_val = min([i[1] for i in lis.items()])
    min_movie = ""
    max_val = max([i[1] for i in lis.items()])
    max_movie = ""
    for i in lis.items():
        if i[1] == min_val:
            min_movie = i[0]
        elif i[1] == max_val:
            max_movie = i[0]
    return "Oldest movie: "+ str(min_movie) + " Youngest movie: " + str(max_movie)

print(check_lis(movies))
