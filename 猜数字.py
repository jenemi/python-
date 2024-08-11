import random
ran_result = random.randint(1,10)
try_times = 3
while try_times >= 1:
    user_input = int(input("请输入1到10以内的整数:"))
    if ran_result == user_input:
        print("你赢了，你真聪明")
        break
    elif ran_result < user_input:
        print("太大了")
    else:
        print("太小了")
    try_times = try_times - 1
else:
    print("你输了")