import random

def randomNumber():
    rdNumber = random.randint(1, 100)
    
    while True:
        try:
            numberInput = int(input("ทายตัวเลขที่มีค่าอยู่ที่ 1-100: "))
            if numberInput == rdNumber:
                print("ยินดีด้วยคุณทายถูก!")
                break
            elif numberInput < rdNumber:
                print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
            else:
                print("คุณทายผิดตัวเลขที่ป้อนมากไป")
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")

randomNumber()
