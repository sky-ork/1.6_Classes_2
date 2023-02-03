# Задача №2 "Аудиоколлекция"
class Track:
    def __init__(self, title, duration: int):
        self.title = title
        self.duration = duration

    def show(self):
        return str(f'<{self.title} - {str(self.duration)} мин.>')


class Album:
    def __init__(self, title, group, list_tracks: list):
        self.title = title
        self.group = group
        self.list_tracks = list_tracks

    def get_tracks(self):
        list_track_info = []
        for track in self.list_tracks:
            list_track_info.append(track.show())
        return list_track_info

    def add_track(self, track: Track):
        if not isinstance(track, Track):
            return
        self.list_tracks.append(track)

    def get_duration(self):
        duration_all_tracks = 0
        for track in self.list_tracks:
            duration_all_tracks = duration_all_tracks + track.duration
        return duration_all_tracks


def main():
    kino_1 = Track('Группа крови', 5)
    kino_2 = Track('Спокойная ночь', 6)
    kino_3 = Track('В наших глазах', 4)
    kino_4 = Track('Легенда', 4)
    kino_list = [kino_1, kino_2, kino_3]

    ariya_1 = Track('Раскачаем этот мир', 6)
    ariya_2 = Track('Раб страха', 5)
    ariya_3 = Track('Бой продолжается', 6)
    ariya_4 = Track('Искушение', 4)
    ariya_list = [ariya_1, ariya_2, ariya_3]

    album_kino = Album('Группа крови', 'Кино', kino_list)
    album_ariya = Album('Игра с огнём', 'Ария', ariya_list)

    album_kino.add_track(kino_4)
    album_ariya.add_track(ariya_4)

    for track_info in album_kino.get_tracks():
        print(track_info)
    print(f'Длительность альбома "{album_kino.title}" '
          f'группы "{album_kino.group}" '
          f'составляет {album_kino.get_duration()} мин.\n')

    for track_info in album_ariya.get_tracks():
        print(track_info)
    print(f'Длительность альбома "{album_ariya.title}" '
          f'группы "{album_ariya.group}" '
          f'составляет {album_ariya.get_duration()} мин.\n')


if __name__ == '__main__':
    main()
