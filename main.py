from keyboard import press
from keyboard import release
import random
import time
import pyperclip
import os
import glob
import thaisong


SongListArr = ['ThaiPOP', 'ThaiRock']
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
        print(f"{count}. {song}")
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
    else:
        Lists = open(Playlist + '.txt')
        for song in Lists:
            songArr.append(song)
        PrintingSong(songArr)

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
        # if count % 60 == 0:
        #     time.sleep(7)
        if count % 6 == 0:
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
