"""
作者:张杰
时间:2024年04月02日
"""
# 作业：写一个能批量恢复宝可梦血量的函数，并且再创建两个宝可梦对象，调用battle函数让它们战斗，
# 之后用你写的函数给它们恢复血量，之后再让它们战斗来测试你写的函数

class Pokemon:
    def __init__(self, name, skill_name, skill_power, hp, hpa, attack, defence, speed):
        self.name = name
        self.skill_name = skill_name
        self.power = skill_power
        self.hp = hp
        self.hpa = hpa
        self.attack = attack
        self.defence = defence
        self.speed = speed


# 计算伤害
def get_damage(attack, power, op_defence):
    return round(attack * power / op_defence)


# 创建对象
cat = Pokemon('喵喵', '疯狂乱抓', 40, 80, 80, 40, 35, 80)
dog = Pokemon('卡蒂狗', '咬咬', 35, 100, 100, 40, 40, 65)


# 战斗函数
def battle(pokemon1: Pokemon, pokemon2: Pokemon):
    damage_to1 = get_damage(pokemon1.attack, pokemon1.power, pokemon2.defence)
    damage_to2 = get_damage(pokemon2.attack, pokemon2.power, pokemon1.defence)
    print('*' * 20)
    print('去吧' + pokemon1.name)
    print('去吧' + pokemon2.name)
    print(pokemon1.name + ':' + str(pokemon1.hp))
    print(pokemon2.name + ':' + str(pokemon2.hp))
    print('=' * 20)
    if pokemon1.speed >= pokemon2.speed:
        while True:
            # 第一只攻击第二只
            pokemon2.hp -= damage_to2
            print(pokemon1.name + '使用' + pokemon1.skill_name + '造成' + str(damage_to2) + '点伤害')
            print(pokemon1.name + ':', pokemon1.hp)
            print(pokemon2.name + ':', pokemon2.hp)
            if pokemon2.hp <= 0:
                print(pokemon2.name + '倒下了')
                return
            # 第二只攻击第一只
            pokemon1.hp -= damage_to1
            print(pokemon2.name + '使用' + pokemon2.skill_name + '造成' + str(damage_to1) + '点伤害')
            print(pokemon2.name + ':', pokemon2.hp)
            print(pokemon1.name + ':', pokemon1.hp)
            if pokemon1.hp <= 0:
                print(pokemon1.name + '倒下了')
                return
    else:
        while True:

            pokemon1.hp -= damage_to1
            print(pokemon2.name + '使用' + pokemon2.skill_name + '造成' + str(damage_to1) + '点伤害')
            print(pokemon2.name + ':', pokemon2.hp)
            print(pokemon1.name + ':', pokemon1.hp)
            if pokemon1.hp <= 0:
                print(pokemon1.name + '倒下了')
                return

            pokemon2.hp -= damage_to2
            print(pokemon1.name + '使用' + pokemon1.skill_name + '造成' + str(damage_to2) + '点伤害')
            print(pokemon1.name + ':', pokemon1.hp)
            print(pokemon2.name + ':', pokemon2.hp)
            if pokemon2.hp <= 0:
                print(pokemon2.name + '倒下了')
                return

            # 调用战斗函数测试


def heal(pokemon):
    pokemon.hp = pokemon.hpa


battle(cat, dog)
heal(dog)
heal(cat)
battle(dog, cat)

# 批量回血


def hospital(*pokemon: Pokemon):
    for i in pokemon:
        heal(i)
    print('治疗成功，欢迎下次光临')


pika = Pokemon('皮卡丘', '电击', 40, 80, 80, 40, 35, 80)
littlefire = Pokemon('小火龙', '喷火', 35, 100, 100, 40, 40, 65)
battle(pika, littlefire)
print(pika.name+'hp:', pika.hp,littlefire.name + 'hp:', littlefire.hp)
hospital(pika, littlefire)
print(pika.name+'hp:', pika.hp,littlefire.name + 'hp:', littlefire.hp)
battle(pika,littlefire)
