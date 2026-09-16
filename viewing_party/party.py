# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): # if there is no title, genre, or rating, return None
    movie_dict = {}
    if not title or not genre or rating is None:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }
def add_to_watched(user_data, movie):
    watched_list = []
    # adds a movie to the user's watched list by the key "watched"
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # adds a movie to the user's watchlist by the key "watchlist"
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # checks if the movie is in the user's watchlist, and if it is, removes it from the watchlist and adds it to the watched list
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

# -----------------------------------------

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):

# check if the watched list is empty
    if not user_data["watched"]:
        return 0.0
    
# calculate the average rating of the watched movies    
    total_rating = 0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    return total_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):

# check if the watched list is empty
    if not user_data["watched"]:
        return None
    
# create empty dictionary to count the number of movies in each genre
    genre_count = {}

# loop through the watched list and count the number of movies in each genre
    for movie in user_data["watched"]:
        genre = movie["genre"]
# check if the genre is already in the dictionary, if it is, increment the count, if not, add it to the dictionary with a count of 1
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

    most_watched_genre = None
    highest_count = 0

# loop through the genre_count dictionary and find the genre with the highest count
    for genre, count in genre_count.items():
# check if the count is higher than the highest_count, if it is, set the most_watched_genre to the current genre and set the highest_count to the current count
        if count > highest_count:
            highest_count = count
            most_watched_genre = genre
    return most_watched_genre 

# -----------------------------------------
# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    user_movies_list = set() # creates a set of movies with the unique movies that the user has watched, but their friends have not
    friend_movies_list = set()
    only_user_watched = [] # creates a list of movies with the unique movies that the user has watched, but their friends have not
    
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
    
    user_movies_list = set()
    friend_movies_list = set()
    only_friends_watched = [] 
    # creates a list of movies with the unique movies that the user's friends have watched, but the user has not
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

    # create a empty list to hold available recommendations
    available_recs = []
    friend_recs = get_friends_unique_watched(user_data)

    #  check movie is in user's subscriptions and add to avaliable if yes
    for movie in friend_recs:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)    
    return available_recs


# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    recommendations = []
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movie in friends_unique_movies:
        if movie["genre"] == most_watched_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    unique_movies = get_unique_watched(user_data)
    for movie in unique_movies:
        if movie in user_data["favorites"]:
            recommendations.append(movie)
    return recommendations

