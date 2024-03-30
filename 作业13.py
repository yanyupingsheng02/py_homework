"""
作者:张杰
时间:2024年03月26日
"""
import random


def guess_game():
    guess = input("Game Start!\n请输入要猜的选项（石头，剪刀，布）")
    while guess not in ('剪刀', '石头', '布'):
        print("输入错误")
        guess = input("请重新输入要猜的选项（石头，剪刀，布）")
    ran = random.choice(['石头', '剪刀', '布'])
    if guess == ran:
        return "平局"
    elif (guess == '石头' and ran == '剪刀') or (guess == '剪刀' and ran == '布') or (guess == '布' and ran == '石头'):
        return "你赢了"
    else:
        return "你输了"


while True:
    count=1
    c = int(input("按1开始游戏"))
    while c == 1:
        print(f"第{count}回合")
        count += 1
        print(guess_game())
        c = int(input("按1继续游戏"))
