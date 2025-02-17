from keyboard import press
from keyboard import release
import random
import time
import pyperclip
import os
import glob
import thaisong


SongListArr = ['ThaiPOP', 'ThaiRock', "FastRandom"]
Prefix = 'p!play '

start = time.time()

ThaiPop = thaisong.thaiPOP
ThaiRock = thaisong.thaiRock

def GetAllFile():
    global SongListArr
    cwd = os.getcwd()
    subDir = 'Songs'
    songPath = os.path.join(cwd, subDir)
    os.chdir(songPath)
    for file in glob.glob("*.txt"):
        song = RemoveSuffix(file, '.txt')
        SongListArr.append(song)
    DisplayMenu(SongListArr)


def DisplayMenu(SongListArr):
    count = 1
    for song in SongListArr:
        songCounts = 0
        if song == 'ThaiPOP':
            songCounts = len(ThaiPop)
        elif song == 'ThaiRock':
            songCounts = len(ThaiRock)
        elif song == 'FastRandom':
            songCounts = len(GatherAllSongs())
        else:
            with open(song + '.txt', 'r', encoding="utf-8") as f:
                songCounts = sum(1 for _ in f)
        print(f"{count}. {song} - {songCounts} songs")
        count += 1
    index = UserInput(SongListArr)
    Playlist = SongListArr[index]
    LoadSong(Playlist)


def LoadSong(Playlist):
    songArr = []
    if Playlist == 'ThaiPOP':
        for song in ThaiPop:
            songArr.append(song)
        PrintingSong(songArr)
    elif Playlist == 'ThaiRock':
        for song in ThaiRock:
            songArr.append(song)
        PrintingSong(songArr)
    elif Playlist == 'FastRandom':
        songArr = GatherAllSongs()
        PrintingSong3(songArr)
    else:
        Lists = open(Playlist + '.txt')
        for song in Lists:
            songArr.append(song)
        PrintingSong(songArr)

def GatherAllSongs():
    files = []
    all_songs = []
    cwd = os.getcwd()
    subDir = 'Songs'
    songPath = os.path.join(cwd, subDir)
    for file in glob.glob("*.txt"):
        files.append(file)
        lists = open(file)
        for song in lists:
            all_songs.append(song)
    return all_songs
        


    songArr = []
    cwd = os.getcwd()
    subDir = 'Songs'
    songPath = os.path.join(cwd, subDir)
    for file in glob.glob(os.path.join(songPath, "*.txt")):
        with open(file, "r", encoding="utf-8") as song_file:
            songs = song_file.readlines()
            songArr.extend([song.strip() for song in songs])
    random.shuffle(songArr)
    print(f"Total Songs Gathered: {len(songArr)}")
    return songArr

# NOTE FOR ME
# make a func that gather all songs
# random all of them

def PrintingSong(SongArr):
    global Prefix
    count = 1
    totalSong = len(SongArr)
    random.shuffle(SongArr)
    print(f'Number of Songs: {totalSong}')
    time.sleep(3)
    for song in SongArr:
        command = Prefix + song
        if count % 6 == 0 and count > 20:
            time.sleep(4)
        pyperclip.copy(command)
        print(f"Song Count: {count} / {totalSong}  -  {song}")
        press('ctrl')
        press('v')
        release('ctrl')
        release('v')
        time.sleep(0.2)
        press('enter')
        release('enter')
        time.sleep(0.5)
        count += 1


def PrintingSong2(SongArr):
    time.sleep(3)
    global Prefix
    count = 1
    totalSong = len(SongArr)
    random.shuffle(SongArr)
    for song in SongArr:
        command = Prefix + song
        count += 1
        pyperclip.copy(command)
        print(f"Song Count: {count} / {totalSong}  -  {song}")
        press('ctrl')
        press('v')
        time.sleep(0.1)
        press('enter')
        release('ctrl')
        release('v')
        release('enter')
    end = time.time()
    seconds = end - start
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    min = seconds // 60
    seconds %= 60
    print(f"Time Taken: {min}:{seconds}")

def PrintingSong3(SongArr):
    global Prefix
    count = 1
    totalSong = len(SongArr)
    random.shuffle(SongArr)
    print(f'Number of Songs: {totalSong}')
    time.sleep(3)
    for song in SongArr:
        command = Prefix + song
        pyperclip.copy(command)
        print(f"Song Count: {count} / {totalSong}  -  {song}")
        press('ctrl')
        press('v')
        release('ctrl')
        release('v')
        time.sleep(0.2)
        press('enter')
        release('enter')
        time.sleep(0.2)
        count += 1

def UserInput(songArr):
    count = len(songArr)
    while True:
        userInput = int(input("Enter a number: "))
        if 0 < userInput <= count:
            return userInput - 1


def RemoveSuffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    else:
        return text


GetAllFile()
