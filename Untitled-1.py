class MovieRating: 
    def __init__(self,movieName,story,acting,music):
        self.movieName = movieName
        self.story = story
        self.acting = acting
        self.music = music
        self.average = int((self.story + self.acting + self.music)/3)

        self.myRating = {
            "Movie Name" : self.movieName,
            "Story Rating" : self.story,
            "Acting Rating" : self.acting,
            "Music Rating" : self.music,
            "Overall Rating" : self.average
        }

    def showRating(self):
        if self.average == 1:
            print("Thanks for the response, You rated Movie with   *")
        elif self.average == 2:
            print("Thanks for the response, You rated Movie with   **")
        elif self.average == 3:
            print("Thanks for the response, You rated Movie with   ***")
        elif self.average == 4:
            print("Thanks for the response, You rated Movie with   ****")
        elif self.average == 5:
            print("Thanks for the response, You rated Movie with   *****")
        

m1 = MovieRating("Avengers", 5,5,5)
m1.showRating()



