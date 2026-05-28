finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
is_hare_asleep = False #Hare starts Awake
hwins = 0
twins = 0
run = 0
import random

while run < 100000:
    x = random.randint(1,100)
    if x<=82:
        is_hare_asleep = True
    else:
        is_hare_asleep = False
    if is_hare_asleep == False:
        hare_pos = hare_pos + random.randint(1,10)
        tortoise_pos = tortoise_pos + random.randint(1,3)

    if is_hare_asleep == True:
        tortoise_pos = tortoise_pos + random.randint(1,3)


    if hare_pos >= 50:
        hwins = hwins + 1
        hare_pos = 0
        tortoise_pos = 0
        run = run + 1
        print("🐇")
    if tortoise_pos >= 50:
        twins = twins + 1
        hare_pos = 0
        tortoise_pos = 0
        run = run + 1
        print("🐢")
print(twins)
print(hwins)
