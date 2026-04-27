# Movie Recommendation System

A simple Python-based movie recommendation system that helps users discover movies based on their preferences using data analysis and basic similarity matching.

## Features

- **Dataset Analysis**: View statistics about the movie collection
- **Genre-based Recommendations**: Get movies based on preferred genre
- **Similarity-based Recommendations**: Find movies similar to ones you like
- **Rating-based Filtering**: Get movies above a minimum rating

## Project Structure

```
movie_recommendation_system/
├── main.py              # Main application with user interface
├── data.py              # Movie dataset and data loading functions
├── analysis.py          # Data analysis and recommendation logic
├── requirements.txt     # Python dependencies
├── run_project.bat      # Windows batch file to run the project
└── README.md           # This file
```

## How It Works

### Recommendation Logic

1. **Genre-based Recommendation**: 
   - Filters movies by the user's preferred genre
   - Sorts by rating (highest first)
   - Returns top 5 recommendations

2. **Similarity-based Recommendation**:
   - Takes a movie the user likes
   - Finds other movies with the same genre
   - Recommends the highest-rated similar movies

3. **Rating-based Recommendation**:
   - Filters movies above a minimum rating
   - Returns the highest-rated movies

### Dataset

The system includes 40 movies across 10 genres:
- Action, Adventure, Animation, Comedy, Crime, Drama, Horror, Romance, Sci-Fi, Thriller

Each movie has:
- Title
- Genre
- Rating (1-10)

## Installation and Running

### Method 1: Using the Batch File (Recommended for Windows)

1. Double-click `run_project.bat`
2. The script will:
   - Create a virtual environment
   - Install required packages
   - Run the application

### Method 2: Manual Setup

1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Sample Output

### Main Menu
```
==================================================
MOVIE RECOMMENDATION SYSTEM
==================================================
1. View Movie Dataset Analysis
2. Get Recommendations by Genre
3. Get Similar Movies (Based on a movie you like)
4. Get Movies Above Minimum Rating
5. Exit
==================================================
```

### Dataset Analysis
```
==================================================
MOVIE DATASET ANALYSIS
==================================================

Total number of movies: 40

Available genres (10):
- Action
- Adventure
- Animation
- Comedy
- Crime
- Drama
- Horror
- Romance
- Sci-Fi
- Thriller

Average rating per genre:
- Crime: 8.93
- Sci-Fi: 8.45
- Drama: 8.43
- Animation: 8.10
- Action: 8.06
- Horror: 7.78
- Thriller: 8.60
- Adventure: 8.25
- Romance: 7.92
- Comedy: 7.80

Top 5 highest-rated movies:

Recommended Movies (Top 5 Movies):
--------------------------------------------------
- The Shawshank Redemption (Drama) - Rating: 9.3
- The Godfather (Crime) - Rating: 9.2
- The Dark Knight (Action) - Rating: 9.0
- Pulp Fiction (Crime) - Rating: 8.9
- Forrest Gump (Drama) - Rating: 8.8
```

### Genre-based Recommendations
```
Recommended Movies (Action):
--------------------------------------------------
- The Dark Knight (Action) - Rating: 9.0
- Mad Max: Fury Road (Action) - Rating: 8.1
- The Avengers (Action) - Rating: 8.0
- Die Hard (Action) - Rating: 8.2
- The Terminator (Action) - Rating: 8.0
```

### Similarity-based Recommendations
```
Similar Movies to 'Inception':
--------------------------------------------------
- Interstellar (Sci-Fi) - Rating: 8.6
- The Matrix (Sci-Fi) - Rating: 8.7
- Back to the Future (Sci-Fi) - Rating: 8.5
- Alien (Sci-Fi) - Rating: 8.4
- Blade Runner (Sci-Fi) - Rating: 8.1
```

## Requirements

- Python 3.7 or higher
- pandas (>=1.3.0)

## Code Style

- Clean and readable code
- Beginner-friendly with simple comments
- Object-oriented design using classes
- Error handling for user input

## Future Enhancements

- Add more movies and genres
- Implement advanced recommendation algorithms (collaborative filtering)
- Add user rating history
- Include movie metadata (year, director, cast)
- Web interface using Flask or Django
