from keyboard import press
from keyboard import release
import random
import time
import pyperclip
import os

count = 0
start = time.time()

print('first')
DefaultSongs = []
default_song_list = open('Songs\DefaultSongs.txt', 'r')
for d_song in default_song_list:
    DefaultSongs.append(d_song)

GoodSongs = []
good_song_list = open('Songs\HappySongs.txt', 'r')
for g_song in good_song_list:
    GoodSongs.append(g_song)

print('here')
ThaiSongs = [
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

TotalList = []
TotalList = GoodSongs + ThaiSongs + DefaultSongs

title = 'Pick a Genre' 
menu = True
while(menu):
    print(title.center(20, '='))
    print("1 - Default Songs.\n 2 - Thai Songs. \n 3 - Good Songs. \n 4 - Total")
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        CurrentList = DefaultSongs
        break
    elif user_input == 2:
        CurrentList = ThaiSongs
        break
    elif user_input == 3:
        CurrentList = GoodSongs
        break
    elif user_input == 4:
        CurrentList = TotalList
        break
    else:
        print('\n')
        print("Invalid Unput")


prefix = 'p!play '
postfix = '\n'
random.shuffle(CurrentList)
totalSong = len(CurrentList)
print(f"Total Songs: {totalSong}")
time.sleep(3)
for song in CurrentList:
    result = prefix + song
    count += 1
    print(f"Song Count: {count} / {totalSong}   {song}")
    if count %60 == 0:
        time.sleep(10)
    if count % 6 == 0:
        time.sleep(4.5)
    pyperclip.copy(result)
    press('ctrl')
    press('v')
    time.sleep(0.1)
    press('enter')
    time.sleep(0.7)
    
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

