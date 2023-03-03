from collections import defaultdict


def solution(genres, plays):
    genre_dict = defaultdict(list)
    play_dict = defaultdict(int)
    for genre, (song_num, play) in zip(genres, enumerate(plays)):
        genre_dict[genre].append((song_num, play))
        play_dict[genre] += play

    for genre in genre_dict.keys():
        genre_dict[genre].sort(key=lambda x: (-x[1], x[0]))

    genre_and_play_list = sorted(play_dict.items(), key=lambda x: -x[1])
    answer = []
    for genre, _ in genre_and_play_list:
        musics = genre_dict[genre]
        if len(musics) == 1:
            answer.append(musics[0][0])
        elif len(musics) >= 2:
            answer.append(musics[0][0])
            answer.append(musics[1][0])

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
