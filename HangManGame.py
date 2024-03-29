# "Trò chơi Hang Man"
import random

#tạo danh sách từu bí ẩn
someWords = '''apple mango banana pineapple grape orange avocado starfruit cherry durian dates jujube'''
someWords = someWords.split(' ')

#chon một từ ngẫu nhiên trong số từ đã cho
word = random.choice(someWords)

hint = 0
hintt = [0, 0]

#tạo trợ giúp
def support():
    print("Bạn có" , hint,  "sự trợ giúp!")
    for i in range(2):
        if hintt[0] == 0:
            print("1. Kiểm tra 1 chữ cái có trong từ cần tìm hay không")
        if hintt[1] == 0:
            print("2. Mở chữ cái ở vị trí muốn biết")
    x = int().input()
    if x == 1:
        hintt[0] = 1
        hint1()
    else:
        hint[1] = 1
        hint2()
#trợ giúp một
def hint1():
    print("Bạn muốn kiểm tra chữ cái nào?")
    x = input()
    if x in word:
        print("Chữ" , x , "có trong chữ cần tìm")
    else:
        print("Không có chữ", x, "nào!")
#trợ giúp 2
def hint2():
    print("Bạn muốn mở vị trí nào?") 
    x = int(input())
    string[x-1] = word[x-1]

def inlen():
    print("Từ này là: ", string)

if __name__ == '__main__': 
    string = ''
    choice = 0
    count = 0
    print("Hãy bắt đầu chơi trò chơi nào")
    print("Hôm nay chúng ta sẽ đoán về tên các loại trái cây bằng tiếng anh")
    print("Từ này có", len(word), "chữ cái")
    print("Bạn có", len(word) + 2, "lượt đoán và 2 trợ giúp")
    print("Lưu ý bạn chỉ có duy nhất một lần đoán toàn bộ từ, hãy bấm GUESS khi bạn đã có đáp án của riêng mình")
    print("Hãy nhấn SOS để được trợ giúp\n Chúc bạn may mắn")
    for i in range(len(word)):
        string += '-'
    inlen()
    while True:
        print("Mời bạn nhập lựa chọn của mình:" , end = " ")
        choice = input()
        if choice.lower() == "sos":
            support()
        elif choice.lower() == "guess":
            print("Đáp án của bạn là:", end = " ")
            guess = input()
            if guess == word:
                print("Chúc mừng bạn đã đoán đúng")
                print("Mời bạn lên nhận một phần quà từ chương trình")
            else:
                print("Rất tiếc!!! Bạn đã quá vội vàng rồi")
            print("Từ cần tìm đó là: " , word.upper())
            break
        elif len(choice) >= 2:
            print("Bạn chỉ được đoán từng chữ cái")
        elif choice == '':
            print("Nhập đi đừng lười")
            count -= 1
        else:
            if choice in word:
                ok = ''
                for i in range(len(string)):
                    if word[i] == choice:
                        ok += choice
                    else:
                        ok += string[i]
                string = ok
                inlen()
            else:
                print("Không có chữ", choice,"nào cả:((")
        count += 1
        if string == word:
            print("Tuyệt vời!! Bạn đã đoán trúng từ bí ẩn của chúng tôi")
            break
        elif count == len(word) + 2:
            print("Bạn đã hết lượt đoán từ và bạn đã THUA")
            break
        print('_*'*50)
