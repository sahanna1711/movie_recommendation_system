"""
Movie Dataset Module
Contains movie data and functions to load/access it
"""

import pandas as pd

def create_movie_dataset():
    """Create a sample movie dataset with 85 movies"""
    
    movies_data = [
        # Action Movies (10 movies)
        {"movie_title": "The Dark Knight", "genre": "Action", "rating": 9.0},
        {"movie_title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1},
        {"movie_title": "The Avengers", "genre": "Action", "rating": 8.0},
        {"movie_title": "Die Hard", "genre": "Action", "rating": 8.2},
        {"movie_title": "The Terminator", "genre": "Action", "rating": 8.0},
        {"movie_title": "John Wick", "genre": "Action", "rating": 7.4},
        {"movie_title": "Mission: Impossible - Fallout", "genre": "Action", "rating": 7.7},
        {"movie_title": "Fast & Furious 6", "genre": "Action", "rating": 7.0},
        {"movie_title": "The Rock", "genre": "Action", "rating": 7.4},
        {"movie_title": "Speed", "genre": "Action", "rating": 7.2},
        
        # Comedy Movies (11 movies)
        {"movie_title": "The Grand Budapest Hotel", "genre": "Comedy", "rating": 8.1},
        {"movie_title": "Super Bad", "genre": "Comedy", "rating": 7.6},
        {"movie_title": "The Hangover", "genre": "Comedy", "rating": 7.7},
        {"movie_title": "Step Brothers", "genre": "Comedy", "rating": 6.9},
        {"movie_title": "Anchorman", "genre": "Comedy", "rating": 7.2},
        {"movie_title": "Bridesmaids", "genre": "Comedy", "rating": 6.8},
        {"movie_title": "The Big Lebowski", "genre": "Comedy", "rating": 8.0},
        {"movie_title": "Airplane!", "genre": "Comedy", "rating": 7.7},
        {"movie_title": "Ghostbusters", "genre": "Comedy", "rating": 7.8},
        {"movie_title": "Dumb and Dumber", "genre": "Comedy", "rating": 7.3},
        {"movie_title": "Ace Ventura: Pet Detective", "genre": "Comedy", "rating": 6.9},
        
        # Drama Movies (11 movies)
        {"movie_title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
        {"movie_title": "Forrest Gump", "genre": "Drama", "rating": 8.8},
        {"movie_title": "The Social Network", "genre": "Drama", "rating": 7.7},
        {"movie_title": "The Pursuit of Happyness", "genre": "Drama", "rating": 8.0},
        {"movie_title": "Good Will Hunting", "genre": "Drama", "rating": 8.3},
        {"movie_title": "The Green Mile", "genre": "Drama", "rating": 8.6},
        {"movie_title": "12 Years a Slave", "genre": "Drama", "rating": 8.1},
        {"movie_title": "Spotlight", "genre": "Drama", "rating": 8.0},
        {"movie_title": "Moonlight", "genre": "Drama", "rating": 7.4},
        {"movie_title": "The King's Speech", "genre": "Drama", "rating": 8.0},
        {"movie_title": "A Beautiful Mind", "genre": "Drama", "rating": 8.2},
        
        # Romance Movies (10 movies)
        {"movie_title": "The Notebook", "genre": "Romance", "rating": 7.8},
        {"movie_title": "La La Land", "genre": "Romance", "rating": 8.0},
        {"movie_title": "Titanic", "genre": "Romance", "rating": 7.9},
        {"movie_title": "Before Sunrise", "genre": "Romance", "rating": 8.1},
        {"movie_title": "Eternal Sunshine of the Spotless Mind", "genre": "Romance", "rating": 8.3},
        {"movie_title": "Her", "genre": "Romance", "rating": 8.0},
        {"movie_title": "500 Days of Summer", "genre": "Romance", "rating": 7.7},
        {"movie_title": "The Fault in Our Stars", "genre": "Romance", "rating": 7.7},
        {"movie_title": "Crazy, Stupid, Love", "genre": "Romance", "rating": 7.6},
        {"movie_title": "Love Actually", "genre": "Romance", "rating": 7.6},
        
        # Thriller Movies (11 movies)
        {"movie_title": "The Silence of the Lambs", "genre": "Thriller", "rating": 8.6},
        {"movie_title": "Se7en", "genre": "Thriller", "rating": 8.6},
        {"movie_title": "The Sixth Sense", "genre": "Thriller", "rating": 8.1},
        {"movie_title": "Shutter Island", "genre": "Thriller", "rating": 8.2},
        {"movie_title": "Gone Girl", "genre": "Thriller", "rating": 8.1},
        {"movie_title": "Prisoners", "genre": "Thriller", "rating": 8.1},
        {"movie_title": "The Fugitive", "genre": "Thriller", "rating": 7.8},
        {"movie_title": "No Country for Old Men", "genre": "Thriller", "rating": 8.1},
        {"movie_title": "Zodiac", "genre": "Thriller", "rating": 7.7},
        {"movie_title": "Memento", "genre": "Thriller", "rating": 8.4},
        {"movie_title": "The Usual Suspects", "genre": "Thriller", "rating": 8.5},
        
        # Sci-Fi Movies (11 movies)
        {"movie_title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
        {"movie_title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
        {"movie_title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
        {"movie_title": "Back to the Future", "genre": "Sci-Fi", "rating": 8.5},
        {"movie_title": "Alien", "genre": "Sci-Fi", "rating": 8.4},
        {"movie_title": "Blade Runner", "genre": "Sci-Fi", "rating": 8.1},
        {"movie_title": "Arrival", "genre": "Sci-Fi", "rating": 7.9},
        {"movie_title": "Ex Machina", "genre": "Sci-Fi", "rating": 7.7},
        {"movie_title": "District 9", "genre": "Sci-Fi", "rating": 8.0},
        {"movie_title": "Edge of Tomorrow", "genre": "Sci-Fi", "rating": 7.9},
        {"movie_title": "The Martian", "genre": "Sci-Fi", "rating": 8.0},
        
        # Horror Movies (10 movies)
        {"movie_title": "The Shining", "genre": "Horror", "rating": 8.4},
        {"movie_title": "Get Out", "genre": "Horror", "rating": 7.7},
        {"movie_title": "A Quiet Place", "genre": "Horror", "rating": 7.5},
        {"movie_title": "The Conjuring", "genre": "Horror", "rating": 7.5},
        {"movie_title": "Hereditary", "genre": "Horror", "rating": 7.3},
        {"movie_title": "It Follows", "genre": "Horror", "rating": 6.8},
        {"movie_title": "The Babadook", "genre": "Horror", "rating": 6.8},
        {"movie_title": "Sinister", "genre": "Horror", "rating": 6.8},
        {"movie_title": "The Descent", "genre": "Horror", "rating": 7.2},
        {"movie_title": "Insidious", "genre": "Horror", "rating": 6.9},
        
        # Adventure Movies (11 movies)
        {"movie_title": "Jurassic Park", "genre": "Adventure", "rating": 8.1},
        {"movie_title": "Indiana Jones", "genre": "Adventure", "rating": 8.4},
        {"movie_title": "The Lord of the Rings: The Fellowship of the Ring", "genre": "Adventure", "rating": 8.8},
        {"movie_title": "Pirates of the Caribbean: The Curse of the Black Pearl", "genre": "Adventure", "rating": 8.0},
        {"movie_title": "Jumanji: Welcome to the Jungle", "genre": "Adventure", "rating": 6.9},
        {"movie_title": "The Revenant", "genre": "Adventure", "rating": 8.0},
        {"movie_title": "Cast Away", "genre": "Adventure", "rating": 7.8},
        {"movie_title": "Into the Wild", "genre": "Adventure", "rating": 8.1},
        {"movie_title": "Life of Pi", "genre": "Adventure", "rating": 7.9},
        {"movie_title": "The Martian", "genre": "Adventure", "rating": 8.0},
        {"movie_title": "Raiders of the Lost Ark", "genre": "Adventure", "rating": 8.4}
    ]
    
    return pd.DataFrame(movies_data)

def load_movies():
    """Load the movie dataset"""
    return create_movie_dataset()
