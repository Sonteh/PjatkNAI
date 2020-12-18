# Problem: Based on users database find 6 recommended and 6 non recommended to watch movies
# Authors: Gracjan Redwanc s17393, Dawid Szabłowski s16667
# Environment: Make sure you have python3, python3-venv and updated version of pip
# pip install numpy

import json
import numpy as np


class RecommendedMovie:
    @staticmethod
    def pearson_score(dataset, user1, user2):
        """
        Checks if there are any common movies between 2 users and then counts theirs pearson score.

        Return:
        Pearson Score
        """
        if user1 not in dataset:
            raise TypeError('Cannot find ' + user1 + ' in the dataset')

        if user2 not in dataset:
            raise TypeError('Cannot find ' + user2 + ' in the dataset')

        # Movies rated by both user1 and user2
        common_movies = {}

        for item in dataset[user1]:
            if item in dataset[user2]:
                common_movies[item] = 1

        num_ratings = len(common_movies)

        # If there are no common movies between user1 and user2, then the score is 0
        if num_ratings == 0:
            return 0

        # Calculate the sum of ratings of all the common movies
        user1_sum = np.sum([dataset[user1][item] for item in common_movies])
        user2_sum = np.sum([dataset[user2][item] for item in common_movies])

        # Calculate the sum of squares of ratings of all the common movies
        user1_squared_sum = np.sum([np.square(dataset[user1][item]) for item in common_movies])
        user2_squared_sum = np.sum([np.square(dataset[user2][item]) for item in common_movies])

        # Calculate the sum of products of the ratings of the common movies
        sum_of_products = np.sum([dataset[user1][item] * dataset[user2][item] for item in common_movies])

        # Calculate the Pearson correlation score
        Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
        Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
        Syy = user2_squared_sum - np.square(user2_sum) / num_ratings

        if Sxx * Syy == 0:
            return 0

        return Sxy / np.sqrt(Sxx * Syy)

    # Compute the Pearson correlation score between user1 and user2
    def pearson_correlation(self, check_for, json_data):
        """
        Counts Pearson score for user and searches for his max score.

        Return:
        Highest Pearson score
        """
        counter = 0
        correlation_scores = []
        dicts = {}
        values = []

        for item in json_data:
            user1 = check_for
            user2 = item
            score_type = "Pearson"
            if user1 != user2:
                score = self.pearson_score(json_data, user1, user2)
                values.append(item)
                dicts[score] = item
                counter = counter + 1
                print("\nPearson score with user", user2, ":")
                print(self.pearson_score(json_data, user1, user2))
                correlation_scores.append(self.pearson_score(json_data, user1, user2))

        highest_pearson = dicts.get(max(correlation_scores))
        print("\nHighest Pearson score with: ", highest_pearson, "his movies:")
        print(json_data.get(highest_pearson).keys())

        return highest_pearson

    @staticmethod
    def find_same_movies(check_for, json_data, highest_pearson, sorted_movies):
        """
        Finds same movies and deletes them from dictionary.

        Return:
        Dictionary of not watched movies by user
        """
        watched_movies = []

        for i in json_data.get(check_for).keys():
            watched_movies.append(i)

        for key in list(sorted_movies):
            if key in watched_movies and json_data.get(highest_pearson).get(key):
                del sorted_movies[key]

        return watched_movies

    @staticmethod
    def picked_movies(sorted_movies, watched_movies, json_data, highest_pearson):
        """
        Prints the best 6 and worst 6 movies user should watch and skip based of Pearson score.

        Return:
        none
        """
        print("\n6 MOVIES YOU SHOULD SKIP:-----------------------------------------------")
        for key in list(sorted_movies)[:6]:
            print(key, "    /user score-", sorted_movies[key])
        print("6 RECOMMENDED MOVIES TO WATCH-----------------------------------------------")
        for key in list(sorted_movies)[-6:]:
            if key not in watched_movies and json_data.get(highest_pearson).get(key) > 6:
                print(key, "    /user score-", sorted_movies[key])


def main():
    pearson_score = RecommendedMovie()

    ratings_file = 'ratings.json'
    check_for = str(input("Podaj usera: "))
    with open(ratings_file, 'r') as f:
        json_data = json.loads(f.read())

    highest_pearson = pearson_score.pearson_correlation(check_for, json_data)
    sorted_movies = dict(sorted(json_data.get(highest_pearson).items(), key=lambda item: item[1]))
    watched_moves = pearson_score.find_same_movies(check_for, json_data, highest_pearson, sorted_movies)
    pearson_score.picked_movies(sorted_movies, watched_moves, json_data, highest_pearson)


if __name__ == '__main__':
    main()
