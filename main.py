import random
import xml.etree.ElementTree as ET

def load_settings():
    tree = ET.parse('settings.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def generate_target_number(x1, x2):
    return random.randint(x1, x2)

def play_game():
    x1, x2, n = load_settings()
    target_number = generate_target_number(x1, x2)
    
    for _ in range(n):
        guess = int(input("請猜一個數字："))
        if guess == target_number:
            print("恭喜！你猜對了！")
            break
        elif guess < target_number:
            print("太低了！")
        else:
            print("太高了！")
    else:
        print(f"遊戲結束，你沒有在 {n} 次內猜中。目標數字是 {target_number}。")

if __name__ == "__main__":
    play_game()
