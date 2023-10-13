def interestCal():
    amount = int(input("Nhap so tien vay: "))
    duration = int(input("Nhap so nam vay: "))

    if amount <= 5000:
        rate = 0
    elif amount <= 100000:
        rate = 10.5
    elif amount <= 250000:
        rate = 10
    elif amount <= 500000:
        rate = 9.6
    else:
        rate = 9

    interest = (amount * duration * rate) / 100

    total = amount + interest

    print("So tien lai la: ", interest)
    print("So tien phai tra la: ", total)

interestCal()