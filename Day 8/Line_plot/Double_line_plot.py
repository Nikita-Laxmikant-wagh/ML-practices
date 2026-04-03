import matplotlib.pyplot as plt

movies_data =[
    "Dhurandar",
    "Phir hera pheri",
    "Golmal",
    "Andaz apna apna",
    "jab we met",
    "3 idiots",
    "Munna Bhai MBBS",
    "PK",
    "kabhi khushi kabhie gham",
    "Dilwale Dulhaniya Le Jayenge"
]

# year and ratings of comedy movies
comedy_movies_year = [2007, 2006, 2006, 1994]
comedy_movies_ratings= [7.8, 8.2, 7.9, 8.2]

# year and ratings of family_drama movies
family_drama_movies_year = [2003, 2006, 2001, 1995, 2001]
family_drama_movies_ratings = [8.1, 8.2, 8.0, 8.3, 8.0]

# make a plot with year on x-axis and ratings on y-axis

# Create a line plot for comedy movies with markers, solid lines, and red color
plt.plot(comedy_movies_year, comedy_movies_ratings, marker='o', linestyle='-', color='r', label='Comedy')

# Create another line plot for family_drama movies with markers, dashed lines, and blue color
plt.plot(family_drama_movies_year, family_drama_movies_ratings, marker='s', linestyle='--', color='b', label='Family_Drama')

plt.title('Movie Ratings Over the Years')

plt.xlabel('Year')
plt.ylabel('Ratings')

plt.legend()
plt.grid()
plt.show()