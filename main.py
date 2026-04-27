"""
Main Movie Recommendation System
Handles user input and displays recommendations
"""

from analysis import MovieAnalyzer

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("MOVIE RECOMMENDATION SYSTEM")
    print("="*50)
    print("1. View Movie Dataset Analysis")
    print("2. Get Recommendations by Genre")
    print("3. Get Similar Movies (Based on a movie you like)")
    print("4. Get Movies Above Minimum Rating")
    print("5. Exit")
    print("="*50)

def get_genre_choice(analyzer):
    """Get genre choice from user"""
    genres = analyzer.get_genre_list()
    print("\nAvailable genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")
    
    while True:
        try:
            choice = input(f"\nEnter genre number (1-{len(genres)}) or genre name: ").strip()
            
            # Try to parse as number
            try:
                genre_num = int(choice)
                if 1 <= genre_num <= len(genres):
                    return genres[genre_num - 1]
                else:
                    print(f"Please enter a number between 1 and {len(genres)}")
                    continue
            except ValueError:
                # Treat as genre name
                if choice.title() in genres:
                    return choice.title()
                else:
                    print("Invalid genre. Please try again.")
        except KeyboardInterrupt:
            print("\nReturning to main menu...")
            return None

def get_movie_choice(analyzer):
    """Get movie choice from user"""
    movies = analyzer.get_movie_list()
    print("\nAvailable movies:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie}")
    
    while True:
        try:
            choice = input(f"\nEnter movie number (1-{len(movies)}) or movie title: ").strip()
            
            # Try to parse as number
            try:
                movie_num = int(choice)
                if 1 <= movie_num <= len(movies):
                    return movies[movie_num - 1]
                else:
                    print(f"Please enter a number between 1 and {len(movies)}")
                    continue
            except ValueError:
                # Treat as movie title
                if choice in movies:
                    return choice
                else:
                    print("Invalid movie title. Please try again.")
        except KeyboardInterrupt:
            print("\nReturning to main menu...")
            return None

def get_rating_input():
    """Get minimum rating from user"""
    while True:
        try:
            rating = float(input("Enter minimum rating (1.0-10.0): "))
            if 1.0 <= rating <= 10.0:
                return rating
            else:
                print("Rating must be between 1.0 and 10.0")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nReturning to main menu...")
            return None

def main():
    """Main function to run the movie recommendation system"""
    analyzer = MovieAnalyzer()
    
    print("Welcome to the Movie Recommendation System!")
    print("This system helps you discover movies based on your preferences.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                # View dataset analysis
                analyzer.print_basic_stats()
                input("\nPress Enter to continue...")
                
            elif choice == '2':
                # Recommendations by genre
                genre = get_genre_choice(analyzer)
                if genre:
                    # Ask for minimum rating (optional)
                    min_rating = None
                    rating_choice = input("Enter minimum rating (optional, press Enter to skip): ").strip()
                    if rating_choice:
                        try:
                            min_rating = float(rating_choice)
                            if not (1.0 <= min_rating <= 10.0):
                                print("Invalid rating. Using no minimum rating filter.")
                                min_rating = None
                        except ValueError:
                            print("Invalid rating. Using no minimum rating filter.")
                            min_rating = None
                    
                    recommendations = analyzer.recommend_by_genre(genre, min_rating)
                    analyzer.print_recommendations(recommendations, f"Recommended Movies ({genre})")
                    input("\nPress Enter to continue...")
                
            elif choice == '3':
                # Similar movies
                movie = get_movie_choice(analyzer)
                if movie:
                    recommendations = analyzer.recommend_similar_movies(movie)
                    analyzer.print_recommendations(recommendations, f"Similar Movies to '{movie}'")
                    input("\nPress Enter to continue...")
                
            elif choice == '4':
                # Movies above minimum rating
                min_rating = get_rating_input()
                if min_rating is not None:
                    recommendations = analyzer.recommend_by_rating(min_rating)
                    analyzer.print_recommendations(recommendations, f"Movies with Rating {min_rating} and Above")
                    input("\nPress Enter to continue...")
                
            elif choice == '5':
                print("\nThank you for using the Movie Recommendation System!")
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                input("\nPress Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\nThank you for using the Movie Recommendation System!")
            print("Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
