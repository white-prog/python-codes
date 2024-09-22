class Movie:
    def __init__(self,title,year,director):
        self.title = title
        self.year = year
        self.director = director
    def get_title(self):
        return self.title
    
movie1 = Movie("Interstellar",2014,"christopher nolan")
print(movie1.get_title())