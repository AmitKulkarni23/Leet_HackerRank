# https://leetcode.com/playground/bzSMcEUD
# Time -> O(USG)
# Space -> Is this true? O(n * m + m * s), where n is the number of users,
# and m is the amount of genres, and s is the number of songs

def initialize():
    userSongs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"]
    }
    songGenres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }
    # return userSongs, {}
    return userSongs, songGenres


def favGenres(userSongs, songGenres):
    output = {}
    for user in userSongs:
        song_list = userSongs[user]
        count = {}

        for song in song_list:
            for genre in songGenres:
                if (genre not in count):
                    count[genre] = 0
                if (song in songGenres[genre]):
                    count[genre] += 1

        print(count)
        output[user] = [key for key, val in count.items() if val == max(count.values())]

    return output


if __name__ == '__main__':
    userSongs, songGenres = initialize()
    print(favGenres(userSongs, songGenres))