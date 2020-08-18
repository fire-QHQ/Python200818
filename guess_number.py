import random
nub=random.randint(1,20)
i=0

while i<5:
    ans=int(input("請輸入數字"))
    if ans==nub:
        print("恭喜答對")
        print(i)
        break
    else:
        print("恭喜猜錯")
        if ans>nub:
            print("太大了")
        else:
            print("太小了")
        i=i+1
