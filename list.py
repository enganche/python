#Tinh tong
def total(ls):
    total = 0
    for e in ls:
        total += e
    return total

#Trung binh
def avg(ls):
    return total(ls) / len(ls)

#Max
def max(ls):
    max = ls[0]
    for e in ls:
        if e > max:
            max = e
    return max

#Min
def min(ls):
    min = ls[0]
    for e in ls:
        if e < min:
            min = e
    return min

#Tim kiem phan tu
def find(ls):
    x = int(input("Nhap so ban can tim x = "))

    for e in ls:
        if e == x:
            print("So ban can tim co trong danh sach")
            return
    
    print("So ban can tim khong co trong danh sach")
    return

#Tim va vi tri
def findFirstPosition(ls):
    x = int(input("Nhap so ban can tim x = "))

    for e in ls:
        if e == x:
            print("So ban can tim co trong danh sach")
            print("Vi tri dau tien ", ls.index(e))
            return
    
    print("So ban can tim khong co trong danh sach")
    return

def findLastPosition(ls):
    x = int(input("Nhap so ban can tim x = "))
    reverseList(ls)

    for e in ls:
        if e == x:
            print("So ban can tim co trong danh sach")
            print("Vi tri cuoi cung ", len(ls) - ls.index(e))
            return
    
    print("So ban can tim khong co trong danh sach")
    return

def count(ls):
    x = int(input("Nhap so ban can tim x = "))
    count = 0

    for e in ls:
        if e == x:
            count += 1
    return count

def removeList(ls):
    x = int(input("Nhap so ban can xoa x = "))

    for e in ls:
        if e == x:
            ls.remove(e)
    return ls

def removeAll(ls):
    x = int(input("Nhap so ban can xoa x = "))

    return [e for e in ls if e != x]

def reverseList(ls):
    reversedList = []
    for i in range(len(ls) - 1, -1, -1):
        reversedList.append()
    
    return reversedList

def ascendingSort(ls):
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if(ls[i] > ls[j]):
                ls[i], ls[j] = ls[j], ls[i]
    
    return ls

def descendingSort(ls):
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if(ls[i] < ls[j]):
                ls[i], ls[j] = ls[j], ls[i]
    
    return ls

def findIntersect(lsA, lsB):
    lsC = []
    
    for x in lsA:
        for y in lsB:
            if ((x == y) and (x not in lsC)):
                lsC.append(x)
    
    return lsC

def findUnion(lsA, lsB):
    lsC = []
    
    for x in lsA:
        if x not in lsC:
            lsC.append(x)
    
    for x in lsB:
        if x not in lsC:
            lsC.append(x)
    
    return lsC

def findCount(ls):
    dict = {}
    for x in ls:
        if x not in dict:
            count = 0
            for y in ls:
                if x == y:
                    count += 1
            dict[x] = count

    return dict

print(findCount([1, 1, 2, 4, 4, 4, 5, 6, 8, 8]))