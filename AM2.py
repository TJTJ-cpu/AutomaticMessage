from keyboard import press
from keyboard import release
import random
import time
import pyperclip
import os
import glob


SongListArr = ['ThaiSongs']
Prefix = 'p!play '
start = time.time()
ThaiSongs = [
    'Bear Knuckle - DONG',
    'SPRITE - ทน',
    'Tilly Birds - เพื่อนเล่น ไม่เล่นเพื่อน (Just Being Friendly)',
    '25 hours - ยินดีที่ไม่รู้จัก (เพลงประกอบภาพยนตร์ กวน มึน โฮ)',
    'Silly Fools - ขี้หึง',
    'Ice Paris - รักติดไซเรน (My Ambulance) -',
    'Big Ass - เล่นของสูง',
    'JOEY PHUWASIT - ROCKET FESTIVAL (สัญญาเดือนหก)',
    'URBOYTJ - เค้าก่อน',
    'Three Man Down - วันเกิดฉันปีนี้ (HBD to me)',
    'F.HERO - เสือสิ้นลาย',
    'Buddha Bless - ชิงหมาเกิด',
    'NONT TANONT - พิง (เพลงประกอบละคร กระเช้าสีดา)',
    'Pop Pongkool - Undo',
    'Violette Wautier - จังหวะจะรัก',
    'URBOYTJ - ถามคำ',
    '321 - แค่ที่รัก',
    'URBOYTJ - วายร้าย',
    'Ink Waruntorn - สายตาหลอกกันไม่ได้ (Eyes Don’t Lie)',
    'Bow Maylada - เเฟนผมน่ารัก',
    'Three Man Down - น้อง (Nong)',
    'Singto Numchok - เธอคือของขวัญ',
    'MEYOU - อิจฉา',
    'MEYOU - วันนี้ปีที่แล้ว',
    'Big Ass - ดีแต่ปาก',
    'Lipta - ทักครับ',
    'Singto Numchok - อยู่ต่อเลยได้ไหม',
    'Slot Machine - จันทร์เจ้า (Goodbye)',
    'JOEY PHUWASIT - นะหน้าทอง',
    'Palmy - ดวงใจ',
    'THE TOYS - หน้าหนาวที่แล้ว',
    'Room 39 - ความจริง',
    '25 hours - ไม่เคย',
    'PAPER - ท้องฟ้า',
    'Slot Machine - ผ่าน',
    'LADIIPRANG - โลกเอียง (LOVE MOMENTUM)',
    'BOWKYLION - วาดไว้',
    'Getsunova - ไกลแค่ไหน คือ ใกล้',
    'Cocktail - คุกเข่า',
    'Jaonaay - คนละชั้น',
    'MEYOU - ภาวนา',
    'Slot Machine - เคลิ้ม',
    'THE TOYS - ลาลาลอย (100%)',
    'atom chanakan - อ้าว',
    'WANYAi - เจ็บจนพอ (Enough)',
    'WANYAi - ลืมไป (Blind) [feat. ปู่จ๋าน ลองไมค์]',
    'Cocktail - เรา',
    'URBOYTJ - เป็นได้ทุกอย่าง',
    'Fymme Bongkot - กะทันหัน',
    'BOWKYLION - ลงใจ',
    'Getsunova - คนไม่จำเป็น',
    'KLEAR - จะรักหรือจะร้าย',
    'Getsunova - ความเงียบดังที่สุด',
    'Palmy - ซ่อนกลิ่น',
    'NONT TANONT - ทุกนาทีที่สวยงาม',
    'Pause - ดาว - Cover version',
    'Indigo - ถ้าฉันเป็นเขา',
    'Bedroom Audio - กอดไม่ได้',
    'Room 39 - เป็นทุกอย่าง',
    'ACTART - นอกจากชื่อฉัน',
    'NONT TANONT - วันครบเลิก',
    'Cocktail - เธอ',
    'Ice Sarunyu - คนใจง่าย',
    'Taylor Swift - Fifteen (Taylor’s Version)',
    'ZENTYARB - ฉบับปรับปรุง',
    'URBOYTJ - เป็นได้ทุกอย่าง',
    'JOEY PHUWASIT - นะหน้าทอง',
    'No One Else - ต่อจากนี้เพลงรักทุกเพลงจะเป็นของเธอเท่านั้น',
    'Three Man Down - ถ้าเธอรักฉันจริง',
    'PAPER - ท้องฟ้า',
    'SLAPKISS - แฟนเก่าคนโปรด',
    'NONT TANONT - วันครบเลิก',
    'Blackbeans - Wish',
    'Lipta - ทักครับ',
    'Tilly Birds - ถ้าเราเจอกันอีก (Until Then)',
    'bonnadol - ฉลามชอบงับคุณ Feat.IIVY B',
    'BOWKYLION - วาดไว้',
    'Singto Numchok - I JUST WANNA PEN FAN YOU DAI BOR ? (อ้ายจัสวอนน่าเป็นแฟนยูได้บ่ ?)',
    'BELL WARISARA - เอาปากกามาวง',
    'Kinkaworn - ตกหลุมรักรอบที่ล้าน',
    'No One Else - แค่มีเธอไปเดินเตะคลื่นทะเลด้วยกัน',
    'PROXIE - คนไม่คุย (Silent Mode)',
    'Room 39 - ความจริง',
    'Bodyslam - สักวันฉันจะดีพอ',
    'BAY6IX - ຕື່ນຈາກຝັນ (ตื่นจากฝัน)',
    'NONT TANONT - โต๊ะริม',
    '3.2.1 - แค่ที่รัก (My boo)',
    'KLEAR - จะรักหรือจะร้าย',
    'KLEAR - One way',
    'ไทรอัมส์คิงดอม - ผ้าเช็ดหน้า (Handkerchief)',
    'URBOYTJ - ถามคำ',
    'Slot Machine - ผ่าน',
    'Ink Waruntorn - สายตาหลอกกันไม่ได้ (Eyes Don’t Lie)',
    'atom chanakan - PLEASE',
    'Getsunova - ความเงียบดังที่สุด',
    'ดูโอเมย์ (Duo May) - เมาทุกขวดเจ็บปวดทุกเพลง - Original',
    'Indigo - ถ้าฉันเป็นเขา',
    'MEYOU - ภาวนา',
    'Three Man Down - ฝนตกไหม',
    'Zeal - เจ็บน้อยที่สุด',
    'Cocktail - เรา',
    'Cocktail - Heartless',
    'Cocktail - ความเข้าใจ',
    'Room 39 - บอกตัวเอง (feat. โป่ง หินเหล็กไฟ)',
    'WANYAi - เจ็บจนพอ (Enough)',
    'Potato - ทิ้งไว้กลางทาง',
    'Getsunova - พระเอกจำลอง',
    'Getsunova - คนไม่จำเป็น',
    'Getsunova - อยู่ตรงนี้ นานกว่านี้',
    'Violette Wautier - I’d Do It Again',
    'เขียนไขและวานิช - แก้มน้องนางนั้นแดงกว่าใคร',
    'Getsunova - ไกลแค่ไหน คือ ใกล้',
    'Cocktail - ฟ้าสูงแค่ไหน',
    'Room 39 - เป็นทุกอย่าง',
    'Bedroom Audio - ไม่บอกเธอ',
    'Getsunova - ความเงียบดังที่สุด',
    'The Mousses - เจ็บที่ต้องรู้',
    'ACTART - นอกจากชื่อฉัน',
    'KLEAR - สิ่งของ',
    'Palmy - ซ่อนกลิ่น',
    'Cocktail - น้ำตาสุดท้าย',
    'Boy Peacemaker - ไม่ไหวบอกไหว',
    'Bodyslam - แสงสุดท้าย',
    'Da Endorphine - รักจะนำทาง',
    'KLEAR - ความทรมานที่แสนมีความสุข',
    'Singto Numchok - อยู่ต่อเลยได้ไหม',
    'Labanoon - แพ้ทาง',
    'Slot Machine - ผ่าน',
    'PURE - ทางผ่าน',
    'Fymme Bongkot - กะทันหัน',
    'THE TOYS - ก่อนฤดูฝน',
    'WANYAi - ไปได้ดี (So Long)',
    'Ploychompoo - ปลิ้ว',
    'WANYAi - หัวหิน (Huahin Loop)',
    'Slot Machine - เคลิ้ม',
    'Slot Machine - รอ',
    'Slot Machine - จันทร์เจ้า (Goodbye)']


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
    if Playlist == 'ThaiSongs':
        for song in ThaiSongs:
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
