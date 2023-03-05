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
    while i < 6:
        msg = random.randint(1, 6)
        if msg == 1:
            if not (ak47 in msg):
                card.append(ak47)
            else:
                continue
        elif msg == 2:
            if not (m416 in msg):
                card.append(m416)
            else:
                continue
        elif msg == 3:
            if not (p18c in msg):
                card.append(p18c)
            else:
                continue
        elif msg == 4:
            card.append(Riot_shield)
        elif msg == 5:
            card.append(bandage)
        i += 1
    return card
