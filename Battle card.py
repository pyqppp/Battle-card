# 导入库
import random

# 创建变量
ak47 = {'attack': 50, 'name': 'ak47', 'kind': 'attack', 'step': 1.5, 'repeat': True}
m416 = {'attack': 35, 'name': 'm416', 'kind': 'attack', 'step': 1.0, 'repeat': True}
p18c = {'attack': 20, 'name': 'p18c', 'kind': 'attack', 'step': 0.5, 'repeat': True}
Riot_shield = {'defense': 30, 'name': '防爆盾', 'kind': 'defense', 'step': 0.5, 'repeat': False}
bandage = {'treat': 30, 'name': '绷带', 'kind': 'treat', 'step': 0.5, 'repeat': False}


# 人物库
def game_player():
    player = {'blood': 100, 'Shield': 0}
    return player


def draw_card():
    i = 1
    card = []
    __ak47 = 0
    __m416 = 0
    __p18c = 0
    __attack = 0
    while i < 6:
        msg = random.randint(1, 6)
        if msg == 1:
            if __ak47 < 1 and __attack < 1:
                card.append(ak47)
                __ak47 += 1
                __attack += 1
            else:
                continue
        elif msg == 2:
            if __m416 < 1 and __attack < 1:
                card.append(m416)
                __m416 += 1
                __attack += 1
            else:
                continue
        elif msg == 3:
            if __p18c < 1 and (__ak47 == 1 or __m416 == 1):
                card.append(p18c)
                __p18c += 1
            else:
                continue
        elif msg == 4:
            card.append(Riot_shield)
        elif msg == 5:
            card.append(bandage)
        i += 1
    return card