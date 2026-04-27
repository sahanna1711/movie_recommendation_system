"""
Movie Analysis and Recommendation Module
Contains data analysis functions and recommendation logic
"""

import pandas as pd
from data import load_movies

class MovieAnalyzer:
    """Class to handle movie data analysis and recommendations"""
    
    def __init__(self):
        self.movies_df = load_movies()
    
    def get_basic_stats(self):
        """Get basic statistics about the movie dataset"""
        stats = {
            'total_movies': len(self.movies_df),
            'available_genres': sorted(self.movies_df['genre'].unique()),
            'avg_rating_per_genre': self.movies_df.groupby('genre')['rating'].mean().sort_values(ascending=False),
            'top_5_movies': self.movies_df.nlargest(5, 'rating')[['movie_title', 'genre', 'rating']]
        }
        return stats
    
    def recommend_by_genre(self, genre, min_rating=None, top_n=5):
        """
        Recommend movies by genre
        
        Args:
            genre (str): Preferred genre
            min_rating (float): Minimum rating filter (optional)
            top_n (int): Number of recommendations to return
        
        Returns:
            DataFrame: Recommended movies
        """
        # Filter by genre
        genre_movies = self.movies_df[self.movies_df['genre'].str.lower() == genre.lower()].copy()
        
        if genre_movies.empty:
            return pd.DataFrame()
        
        # Apply minimum rating filter if specified
        if min_rating is not None:
            genre_movies = genre_movies[genre_movies['rating'] >= min_rating]
        
        # Sort by rating (highest first) and return top N
        return genre_movies.sort_values('rating', ascending=False).head(top_n)
    
    def recommend_similar_movies(self, movie_title, top_n=5):
        """
        Recommend movies similar to a given movie (based on genre)
        
        Args:
            movie_title (str): Title of the movie user likes
            top_n (int): Number of recommendations to return
        
        Returns:
            DataFrame: Similar movies
        """
        # Find the movie in the dataset
        movie = self.movies_df[self.movies_df['movie_title'].str.lower() == movie_title.lower()]
        
        if movie.empty:
            return pd.DataFrame()
        
        # Get the genre of the selected movie
        movie_genre = movie.iloc[0]['genre']
        
        # Find movies with the same genre (excluding the selected movie)
        similar_movies = self.movies_df[
            (self.movies_df['genre'] == movie_genre) & 
            (self.movies_df['movie_title'].str.lower() != movie_title.lower())
        ]
        
        # Sort by rating and return top N
        return similar_movies.sort_values('rating', ascending=False).head(top_n)
    
    def recommend_by_rating(self, min_rating, top_n=10):
        """
        Recommend movies above a minimum rating
        
        Args:
            min_rating (float): Minimum rating
            top_n (int): Number of recommendations to return
        
        Returns:
            DataFrame: Recommended movies
        """
        high_rated_movies = self.movies_df[self.movies_df['rating'] >= min_rating]
        return high_rated_movies.sort_values('rating', ascending=False).head(top_n)
    
    def get_movie_list(self):
        """Get list of all movie titles"""
        return sorted(self.movies_df['movie_title'].tolist())
    
    def get_genre_list(self):
        """Get list of all genres"""
        return sorted(self.movies_df['genre'].unique().tolist())
    
    def print_recommendations(self, recommendations, title="Recommended Movies"):
        """Print recommendations in a formatted way"""
        if recommendations.empty:
            print(f"No {title.lower()} found.")
            return
        
        print(f"\n{title}:")
        print("-" * 50)
        for _, movie in recommendations.iterrows():
            print(f"- {movie['movie_title']} ({movie['genre']}) - Rating: {movie['rating']}")
        print()
    
    def print_basic_stats(self):
        """Print basic statistics about the dataset"""
        stats = self.get_basic_stats()
        
        print("\n" + "="*50)
        print("MOVIE DATASET ANALYSIS")
        print("="*50)
        
        print(f"\nTotal number of movies: {stats['total_movies']}")
        
        print(f"\nAvailable genres ({len(stats['available_genres'])}):")
        for genre in stats['available_genres']:
            print(f"- {genre}")
        
        print(f"\nAverage rating per genre:")
        for genre, avg_rating in stats['avg_rating_per_genre'].items():
            print(f"- {genre}: {avg_rating:.2f}")
        
        print(f"\nTop 5 highest-rated movies:")
        self.print_recommendations(stats['top_5_movies'], "Top 5 Movies")
