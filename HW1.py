def lb_Convert(): # 建立一個可以把磅數轉換成其他單位的函式
    lb=float(input("Please enter weight(lb):")) # 輸入想要轉換的磅數並轉成浮點數以利後續公式計算
    print(f'Enter weight(lb): {lb}')
    print("")
    print(f'{"lb" :3}, {"oz" :4}, {"kg"}')
    print(f'{lb :<3}, {lb*16 :<4.1f}, {lb*0.45359237 :<.5f}') # 將輸入的磅數轉換成盎司及公斤，並調整格式

lb_Convert() # 呼叫函式

import random
def Guess_Number(): # 建立猜數字遊戲
    secret_num=random.randint(1,100) # 隨機設定正確答案的範圍在1~100
    print('Welcome to the number guessing game with a range of 1 to 100')
    guess=int(input('Enter your guess:')) # 輸入猜的值並轉成整數
    guess_up=100 # 額外設定兩個值，控制猜的上下限，並以100和1各自作為初始化的值
    guess_down=1
    while guess != secret_num: # 猜錯要繼續猜直到猜對為止
        if guess not in range(guess_down, guess_up+1): # 若不在猜的範圍則直接印出訊息
            print('Out of range!')
        
        elif guess > secret_num: # 當猜的值大於正確答案時，表示範圍應該在之前猜的下限與本次猜的上限中
            if guess < guess_up: # 又若本次猜的上限小於先前猜的上限，則將本次猜的上限值儲存到guess_up中
                guess_up = guess
            print(f'Range form {guess_down} to {guess_up}') # 印出範圍即儲存的上下限
        
        else: # 當猜的值小於正確答案時，表示範圍應該在本次猜的下限與之前猜的上限中
            if guess > guess_down:  # 又若本次猜的下限大於先前猜的下限，則將本次猜的下限值儲存到guess_down中
                guess_down = guess
            print(f'Range form {guess_down} to {guess_up}')
        
        guess = int(input('Enter your guess:'))
    
    if guess == secret_num: # 當猜對時印出訊息
        print('You guessed the correct number!')

Guess_Number() # 呼叫函式

def Sen_to_Cap(sen): # 建立一個會把字串中除了介係詞和連接詞以外的單詞字首都轉成大寫的函式
    word_excluded=['to','for','the', 'and', 'or', 'from', 'on', 'in', 'at', 'with', 'by', 'of'] # 建立排除介係詞和連接詞的表
    sen_splitted=sen.split() # 把字串分開
    sen_cap=[] # 建立一個空字串用來填入被轉換成大寫的字詞
    for word in sen_splitted:
        if word.lower() not in word_excluded: # 若不在排除表中則轉換成大寫並接入空字串 (因為排除表都小寫，所以要先把欲比對的文字轉小寫才進行比對)
            sen_cap.append(word.capitalize())
        else:
            sen_cap.append(word) # 若在排除表則直接接入
    return ' '.join(sen_cap)

sen = 'Deep learning based design of porous graphene for enhanced mechanical resilience.'
# sen = 'The sun rises from the east and sets to the west.'
print(f'Original sentences:\n{sen}')
print(f'Captialized sentences:')
print(Sen_to_Cap(sen))