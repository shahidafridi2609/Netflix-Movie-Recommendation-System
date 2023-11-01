import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_excel("netflix_data.xlsx")

# Modify 'Title' to ensure it's of string type
data['Title'] = data['Title'].astype(str)

# Demographic Filtering
C = data["IMDb Score"].mean()
m = data["IMDb Votes"].quantile(0.9)
popular_movies = data.copy().loc[data["IMDb Votes"] >= m]

def weighted_rating(x, C=C, m=m):
    v = x["IMDb Votes"]
    R = x["IMDb Score"]
    return (v / (v + m) * R) + (m / (v + m) * C)

popular_movies["Score"] = popular_movies.apply(weighted_rating, axis=1)
popular_movies = popular_movies.sort_values('Score', ascending=False)

def plot():
    top_rated_and_popular = popular_movies.head(10)
    plt.figure(figsize=(12, 6))
    plt.barh(top_rated_and_popular["Title"], top_rated_and_popular["Score"], align="center", color="skyblue")
    plt.gca().invert_yaxis()
    plt.title("Top 10 Popular Movies")
    plt.xlabel("Score")
    plt.show()

# Call the plot function to display the chart
plot()

# Content-Based Filtering
tfidf = TfidfVectorizer(stop_words="english")
data["Summary"] = data["Summary"].fillna("")  # Handle missing values in the "Summary" column
tfidf_matrix = tfidf.fit_transform(data["Summary"].values.astype('U'))

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(data.index, index=data["Title"]).drop_duplicates()

def get_recommendations(title):
    # Convert the user input to lowercase
    title = title.lower()

    # Check if the user input is not in any movie titles
    if all(title not in movie_title.lower() for movie_title in data["Title"]):
        return "Movie not found"

    # Find the movie that matches the user input
    matching_titles = [movie_title for movie_title in data["Title"] if title in movie_title.lower()]

    # Get the first matching title (you can modify this part as needed)
    matched_title = matching_titles[0]

    # Get the index of the matched title
    idx = indices[matched_title]

    # Calculate the cosine similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 10 most similar movies
    sim_scores = sim_scores[1:11]
    movies_indices = [ind[0] for ind in sim_scores]
    recommended_movies = data["Title"].iloc[movies_indices]
    return recommended_movies

def main():
    print("Welcome to the Movie Recommendation System")
    while True:
        print("\nChoose an option:")
        print("1. Demographic Filtering (Top Rated and Popular Movies)")
        print("2. Content-Based Filtering (Movie Recommendations)")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("Top Rated and Popular Movies:")
            print(data[["Title", "IMDb Votes", "View Rating", "IMDb Score"]].head(10))
            plot()  # Calling the plot function to display the chart
        elif choice == '2':
            movie_title = input("Enter a movie title for recommendations: ")
            recommendations = get_recommendations(movie_title)
            print(f"Recommended Movies for '{movie_title}':")
            if isinstance(recommendations, str):
                print(recommendations)
            else:
                for idx, movie in enumerate(recommendations, start=1):
                    print(f"{idx}. {movie}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
