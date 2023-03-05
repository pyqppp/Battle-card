# 导入库
import random

# 创建变量
ak47 = {'attack': 50, 'name': 'ak47', 'kind': 'attack', 'step': 1.5, 'repeat': True}
m416 = {'attack': 35, 'name': 'm416', 'kind': 'attack', 'step': 1.0, 'repeat': True}
p18c = {'attack': 20, 'name': 'p18c', 'kind': 'attack', 'step': 0.5, 'repeat': True}
riot_shield = {'defense': 30, 'name': '防爆盾', 'kind': 'defense', 'step': 0.5, 'repeat': False}
bandage = {'treat': 30, 'name': '绷带', 'kind': 'treat', 'step': 0.5, 'repeat': False}
p1 = {'health': 100, 'shield': 0, 'step': 0.0}
p2 = {'health': 100, 'shield': 0, 'step': 0.0}


def draw_card():
    i = 1
    card = []
    __ak47 = 0
    __m416 = 0
    __p18c = 0
    __rifle = 0
    while i < 6:
        msg = random.randint(1, 6)
        if msg == 1:
            if __ak47 < 1 and __rifle < 1:
                card.append(ak47)
                __ak47 += 1
                __rifle += 1
            else:
                continue
        elif msg == 2:
            if __m416 < 1 and __rifle < 1:
                card.append(m416)
                __m416 += 1
                __rifle += 1
            else:
                continue
        elif msg == 3:
            if __p18c < 1 and (__ak47 == 1 or __m416 == 1):
                card.append(p18c)
                __p18c += 1
            else:
                continue
        elif msg == 4:
            card.append(riot_shield)
        elif msg == 5:
            card.append(bandage)
        i += 1
    return card


# 各种武器库
# ak47
def ak47_attack(who):  # who是发起攻击的人
    if who == 'p1' and p1['step'] >= ak47['step']:
        if p2['Shield'] >= ak47['attack']:
            p2['shield'] -= ak47['attack']
            p1['step'] -= ak47['step']
        elif p2['shield'] < ak47['attack']:
            p2['shield'] = 0
            p2['health'] -= ak47['attack']
            p1['step'] -= ak47['step']
    if who == 'p2' and p2['step'] >= ak47['step']:
        if p1['shield'] >= ak47['attack']:
            p1['shield'] -= ak47['attack']
            p2['step'] -= ak47['step']
        elif p1['shield'] < ak47['attack']:
            p1['shield'] = 0
            p1['health'] -= ak47['attack']
            p2['step'] -= ak47['step']


# m416
def m416_attack(who):  # who是发起攻击的人
    if who == 'p1' and p1['step'] >= m416['step']:
        if p2['shield'] >= m416['attack']:
            p2['shield'] -= m416['attack']
            p1['step'] -= m416['step']
        elif p2['shield'] < m416['attack']:
            p2['shield'] = 0
            p2['health'] -= m416['attack']
            p1['step'] -= m416['step']
    if who == 'p2' and p2['step'] >= m416['step']:
        if p1['shield'] >= m416['attack']:
            p1['shield'] -= m416['attack']
            p2['step'] -= m416['step']
        elif p1['shield'] < m416['attack']:
            p1['shield'] = 0
            p1['health'] -= m416['attack']
            p2['step'] -= m416['step']


# p18c
def p18c_attack(who):  # who是发起攻击的人
    if who == 'p1' and p1['step'] >= p18c['step']:
        if p2['shield'] >= p18c['attack']:
            p2['shield'] -= p18c['attack']
            p1['step'] -= p18c['step']
        elif p2['shield'] < p18c['attack']:
            p2['shield'] = 0
            p2['health'] -= p18c['attack']
            p1['step'] -= p18c['step']
    if who == 'p2' and p2['step'] >= p18c['step']:
        if p1['shield'] >= p18c['attack']:
            p1['shield'] -= p18c['attack']
            p2['step'] -= p18c['step']
        elif p1['shield'] < p18c['attack']:
            p1['shield'] = 0
            p1['health'] -= p18c['attack']
            p2['step'] -= p18c['step']


# riot_shield
def riot_shield_defense(who):  # who是被加护盾的人
    if who == 'p1':
        p1['shield'] += riot_shield['defense']
        p1['step'] -= riot_shield['step']
    elif who == 'p2':
        p2['shield'] += riot_shield['defense']
        p2['step'] -= riot_shield['step']


# bandage
def bandage_treat(who):  # who 是被治疗的人
    if who == 'p1' and p1['health'] <= 70:
        p1['health'] += bandage['treat']
        p1['step'] -= bandage['step']
    else:
        p1['health'] = 100
        p1['step'] -= bandage['step']
    if who == 'p2' and p2['health'] <= 70:
        p2['health'] += bandage['treat']
        p2['step'] -= bandage['step']
    elif p2['health'] > 70:
        p2['health'] = 100
        p2['step'] -= bandage['step']
