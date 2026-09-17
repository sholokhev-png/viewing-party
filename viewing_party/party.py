# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): 
    """ Creates a movie dictionary with the given title, genre, and rating. 
    If any of the parameters are None or empty, returns None."""

    movie_dict = {}
    if not title or not genre or rating is None:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }
def add_to_watched(user_data, movie):
    """ Adds a movie to the user's watched list """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """ Adds a movie to the user's watchlist """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """ Moves a movie from the user's watchlist to their watched list """

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

# -----------------------------------------

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    """ Returns the average rating of the movies in the user's watched list """

    if not user_data["watched"]:
        return 0.0
    total_rating = 0
    for movie in user_data["watched"]:

        total_rating += movie["rating"]
    return total_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
    """ Returns the most watched genre of the movies in the user's watched list """

    if not user_data["watched"]:
        return None
    genre_count = {}
    for movie in user_data["watched"]:

        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    most_watched_genre = None
    highest_count = 0
    for genre, count in genre_count.items():

        if count > highest_count:
            highest_count = count
            most_watched_genre = genre
    return most_watched_genre 

# -----------------------------------------
# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    """ Returns a list of movies that the user has watched, but their friends have not """
    user_movies_list = set()
    friend_movies_list = set() 
    only_user_watched = [] 
    for movie in user_data["watched"]:
        user_movies_list.add(movie["title"])  
    for friend in user_data["friends"]:

        for friend_movie in friend["watched"]:
            friend_movies_list.add(friend_movie["title"])
    only_user_watched_set = list(user_movies_list - friend_movies_list)
    for movie in user_data["watched"]:
        if movie["title"] in only_user_watched_set:
            only_user_watched.append(movie)
    return only_user_watched

def get_friends_unique_watched(user_data):
    """ Returns a list of movies that the user's friends have watched, but the user has not """

    user_movies_list = set()
    friend_movies_list = set()
    only_friends_watched = [] 
    for movie in user_data["watched"]:

        user_movies_list.add(movie["title"])
    for friend in user_data["friends"]:

        for friend_movie in friend["watched"]:

            friend_movies_list.add(friend_movie["title"])
    only_friends_watched_set = list(friend_movies_list - user_movies_list)
    for friend in user_data["friends"]:

        for friend_movie in friend["watched"]:

            if friend_movie["title"] in only_friends_watched_set and friend_movie not in only_friends_watched:
                only_friends_watched.append(friend_movie)            
    return only_friends_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
def get_available_recs(user_data):

    """ Returns a list of movie recommendations for the user based 
    on their friends' watched movies and the user's subscriptions """

    available_recs = []
    friend_recs = get_friends_unique_watched(user_data)
    for movie in friend_recs:

        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)    
    return available_recs



# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    """ Returns a list of movie recommendations for the user based on their most 
    watched genre and their friends' watched movies """

    recommendations = []
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movie in friends_unique_movies:

        if movie["genre"] == most_watched_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    """ Returns a list of movie recommendations for the user based on their favorite movies """

    recommendations = []
    unique_movies = get_unique_watched(user_data)
    for movie in unique_movies:

        if movie in user_data["favorites"]:
            recommendations.append(movie)
    return recommendations

