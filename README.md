# 🎵 Discord Song Automator  
This is a small automation project for sending song commands. 
It copy the song name from .txt file and uses keyboard simulation to paste `p!play <song>` commands.

## 🌟 Features
- Auto-sends song commands using `p!play <song name>`
- For non ASCII add another python file, example: ThaiSong.py
- Automatically detects `.txt` playlists from the `Songs/` folder
- Random song order every time 

---

## ⚙️ Requirements

Make sure you have Python installed, then install dependencies:

   ```bash
   pip install keyboard pyperclip
   ```

---

## 🛠 Setup

1. **Clone the project**  
   ```bash
   git clone https://github.com/TJTJ-cpu/AutomaticMessage
   ```

2. **Prepare the Songs folder**  
  - Create a new `.txt` file in `Songs/`.
  - Add songs line by line (Recommend to add artist as well):
    ```
    Not Like Us - Kendrick Lamar
    Song Two - Artist Name
    Song Three - Artist Name
    ```

3. **Run the script**  
   ```bash
   python main.py
   ```
   Main Menu :
   Your playlist will pop up.
   ```
   1. ThaiPOP
   2. ThaiRock
   3. FastRandom
   4. ChillVibes
   5. Party
   ```
   Choose the number then press enter.
   
   ---

## 🤖 How It Works

1. You’re shown a menu of all playlists (playlists_name`.txt` files from the `Songs/` folder).
2. You pick one.
3. It copies each `p!play <song>` command to your clipboard and simulates pressing Ctrl+V and Enter to send it.
4. Done—just sit back and enjoy the tunes.
5. You might need to find tune the speed to avoid spamming the server.

---

## 🧪 Customization

- **Prefix change:**  
  Prefix such as `p!play` can be edited in `main.py`:
  ```python
  Prefix = 'p!play '
  ```
- **Speed tuning:**  
  If the commands are sending too fast or too slow, you can adjust the delay times in `main.py`.  
  Look for `time.sleep()` lines and tweak the values:
  ```python
  time.sleep(0.5)  # Delay between songs
  ```
  
---

## 📸 Example

```txt
Songs/
├── ChillVibes.txt
├── Party.txt
├── ThaiPOP.txt  <- built-in
└── ThaiRock.txt <- built-in
```

Menu on run:
```
1. ThaiPOP
2. ThaiRock
3. FastRandom
4. ChillVibes
5. Party
```

Thank You ❤️ 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/tungjai-mady/)
