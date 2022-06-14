import math

import pandas as pd


def do_calc(x, friends: pd.DataFrame({})):
    total_distance = 0
    for _row in friends.iterrows():
        distance = math.dist(_row[1]['location'], x)
        total_distance += distance
    return total_distance


def do_work(input_friends: pd.DataFrame({})):
    friends_pd = pd.DataFrame(input_friends)

    friends_pd['total_distance'] = friends_pd['location'].apply(lambda x: do_calc(x, friends_pd))

    friend_min_dist = friends_pd[friends_pd['total_distance'] == friends_pd['total_distance'].min()]

    print(f'Friend with minimum distance: {friend_min_dist.loc[:, "name"].values[0]}, distance: {friend_min_dist.loc[:, "total_distance"].values[0]}')


if __name__ == '__main__':
    friends = [{"name": "Bob", "location": (5, 2, 10)}, {"name": "David", "location": (2, 3, 5)}, {"name": "Mary", "location": (19, 3, 4)}, {"name": "Skyler", "location": (3, 5, 1)}]

    do_work(input_friends=friends)
