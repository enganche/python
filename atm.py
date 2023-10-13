#Bai toan ATM

def transaction():
    print("-------------------")
    print("Nhap chu cai (a, b, c, d, e) de chon tinh nang")
    print("-------------------")
    print("a. Gui tien")
    print("b. Rut tien")
    print("c. Xem so du")
    print("d. Xem lich su giao dich")
    print("e. Quay ve")

    user = input()

    if user == 'a':
        print("Gui tien nao hihi")
    elif user == 'b':
        print("Rut tien nao hihi")
    elif user == 'c':
        print("Rut tien nao hihi")
    elif user == 'd':
        print("Rut tien nao hihi")
    elif user == 'e':
        print("Quay ve")
    else:
        print("Moi ban nhap lai!!!")

def atm():
    isRunning = True
    while (isRunning):
        print('''
.___________. __    __       ___      .__   __. .______        ___      .__   __.  __  ___ 
|           ||  |  |  |     /   \     |  \ |  | |   _  \      /   \     |  \ |  | |  |/  / 
`---|  |----`|  |  |  |    /  ^  \    |   \|  | |  |_)  |    /  ^  \    |   \|  | |  '  /  
    |  |     |  |  |  |   /  /_\  \   |  . `  | |   _  <    /  /_\  \   |  . `  | |    <   
    |  |     |  `--'  |  /  _____  \  |  |\   | |  |_)  |  /  _____  \  |  |\   | |  .  \  
    |__|      \______/  /__/     \__\ |__| \__| |______/  /__/     \__\ |__| \__| |__|\__\ 
                                                                                           
        ''')
        print("Nhap so (1, 2, 3) de chon tinh nang")
        print("-------------------")
        print("1. Tao tai khoan")
        print("2. Giao dich")
        print("3. Ket thuc")

        user = int(input())

        if user == 1:
            print("Tao tai khoan nao hihi ><")
        elif user == 2:
            transaction()
        elif user == 3:
            isRunning = False
        else:
            print("Moi ban nhap lai!!!")
    print("Chao tam biet!")

def main():
    atm()

if __name__ == '__main__':
    main()
