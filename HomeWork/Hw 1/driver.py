from song import *
from cd import *
from musicLibrary import *

def main():


    files = ["CelticWoman.txt", "Hysteria.txt", "PianoGuys.txt", "SandlerYoung.txt", "X.txt"]
    
    #Create the music library
    my_library = MusicLibrary()

    for each_file in files:
        a_cd = get_cd(each_file)
        print("Test 2:  Worth 5 points each run if it matches the sample execution")
        print(a_cd)
        my_library.add_item(a_cd)
        print()

    #Create playlist
    print("Test 3:  Worth 20 points, runs only once")
    my_playlist = my_library.generate_playlist(5)
    print("My Playlist:")
    for each_song in my_playlist:
        print(each_song)
    print()

    #Create genre list
    print("Test 4:  Worth 15 points, runs only once")
    christmas_list = my_library.generate_genre_list("Classical")
    for each_cd in christmas_list:
        print(each_cd)
    print()

    #Create artist list
    print("Test 5: Worth 15 points, runs only once")
    def_leppard_list = my_library.generate_artist_list("Def Leppard")
    for each_cd in def_leppard_list:
        print(each_cd)
    print()


def get_cd(file_name):
    print("Test 1:  5 points each run if it matches the sample execution")
    file = open(file_name)
    count = 0
    song_titles = []
    for each_line in file:
        if count == 0:
            artist = each_line.strip()
            count += 1
        elif count == 1:
            album = each_line.strip()
            count += 1
        elif count == 2:
            category = each_line.strip()
            count += 1
        else:
            song_titles.append(each_line.strip())


    file.close()

    favorite = CD(album, artist)
    print(str(favorite) + ':')
    for each_song in song_titles:
        a_song = Song(each_song, album, artist, category)
        print(a_song)
        favorite.add_song(a_song)
    print()
    return favorite




main()





