XEM_DANH_BA = 1
THEM_SO_LIEN_LAC = 2
TIM_THEO_TEN = 3
TIM_THEO_SO = 4

danhba =  []

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("||                DANH BẠ                  ||")
print("||-----------------------------------------||")
print("|| Mã lệnh ||          Tùy chọn            ||") 
print("||    1    ||       Xem toàn bộ danh bạ    ||")
print("||    2    ||        Thêm số liên lạc      ||")
print("||    3    ||    Tìm số liên lạc theo tên  ||")
print("||    4    ||     Tìm số liên lạc theo số  ||")
print("||    0    ||            Thoát             ||")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
while True:
    lenh = int(input("Vui lòng nhập mã lệnh: "))
    if lenh == XEM_DANH_BA:
        if len(danhba) == 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("||              Danh bạ trống              ||")  
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for i in danhba:
                print("||" + i[0].center(13) + i[1].center(28) + "||" )
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif lenh == THEM_SO_LIEN_LAC:
        ten = input("Vui lòng nhập tên liên lạc: ")
        so = input("Vui long nhập số liên lạc: ")
        a = [ten, so]
        danhba.append(a)
        print("~~~~~~~~~~~~~~~~~~~~~~Đã lưu~~~~~~~~~~~~~~~~~")
    elif lenh == TIM_THEO_TEN:
        ten = input("Vui lòng nhập tên cần tìm: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ok = 0
        for i in danhba:
            if ten in i[0]:
                ok = 1
                print("||" + i[0].center(13) + i[1].center(28) + "||")
        if ok == 0:
            print("||              Danh bạ trống              ||")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif lenh == TIM_THEO_SO:
        so = input("Vui lòng nhập số cần tìm: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ok = 0
        for i in danhba:
            if so in i[1]:
                ok = 1
                print("||" + i[0].center(13) + i[1].center(28) + "||")
        if ok == 0:
            print("||              Danh bạ trống              ||") 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif lenh == 0:
        print("~~~~~~~~~~~~~~~~~~~~Đang thoát~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~Tạm biệt~~~~~~~~~~~~~~~~")
        break
    else:
        print("Mã lệnh không hợp lệ, vui lòng nhập lại")