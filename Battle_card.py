#!/usr/bin/env python
# coding=utf-8
# 导入库
import random
import os
# 创建变量
ak47 = {'attack': 50, 'name': 'ak47', 'kind': 'attack', 'step': 1.5, 'repeat': True}
m416 = {'attack': 35, 'name': 'm416', 'kind': 'attack', 'step': 1.0, 'repeat': True}
p18c = {'attack': 20, 'name': 'p18c', 'kind': 'attack', 'step': 0.5, 'repeat': True}
grenade = {'attack': 60, 'name': 'grenade', 'kind': 'attack', 'step': 1.5, 'repeat': False}
riot_shield = {'defense': 50, 'name': '护盾', 'kind': 'defense', 'step': 1.0, 'repeat': False}
bandage = {'health': 30, 'name': '绷带', 'kind': 'treat', 'step': 0.5, 'repeat': False}
medicine_bag = {'health':80, 'name': '药包', 'kind': 'health', 'step': 1.5, 'repeat': False}
p1 = {'health': 100, 'shield': 0, 'step': 0.0}
p2 = {'health': 100, 'shield': 0, 'step': 0.0}


def draw_card():
    i = 0
    card = []
    __ak47 = 0
    __m416 = 0
    __p18c = 0
    __rifle = 0
    while i < 5:
        msg = random.randint(1, 6)
        if msg == 1:
            if __ak47 < 1 and __rifle < 1:
                card.append('ak47,1.5步')
                __ak47 += 1
                __rifle += 1
            else:
                continue
        elif msg == 2:
            if __m416 < 1 and __rifle < 1:
                card.append('m416,1步')
                __m416 += 1
                __rifle += 1
            else:
                continue
        elif msg == 3:
            if __p18c < 1 and (__ak47 == 1 or __m416 == 1):
                card.append('p18c,0.5步')
                __p18c += 1
            else:
                continue
        elif msg == 4:
            msg = random.randint(1, 3)
            if msg != 1:
                card.append('护盾,0.5步')
            else:
                continue
        elif msg == 5:
            card.append('绷带,0.5步')
        elif msg == 6:
            card.append('手榴弹,1.5步')
        elif msg == 7:
            card.append('药包,1.5步')
        i += 1
    if __rifle == 0:
        del card[1]
        msg = random.randint(1, 3)
        if msg == 1:
            card.append('ak47,1.5步')
        if msg == 2:
            card.append('m416,1步')
    return card


# 各种武器库
# ak47
def ak47_attack(who):  # who是发起攻击的人
    if who == 'p1' and p1['step'] >= ak47['step']:
        if p2['shield'] >= ak47['attack']:
            p2['shield'] -= ak47['attack']
            p1['step'] -= ak47['step']
        elif p2['shield'] < ak47['attack']:
            p2['health'] -= ak47['attack'] - p2['shield']
            p1['step'] -= ak47['step']
    if who == 'p2' and p2['step'] >= ak47['step']:
        if p1['shield'] >= ak47['attack']:
            p1['shield'] -= ak47['attack']
            p2['step'] -= ak47['step']
        elif p1['shield'] < ak47['attack']:
            p1['health'] -= ak47['attack'] - p1['shield']
            p2['step'] -= ak47['step']


# m416
def m416_attack(who):  # who是发起攻击的人
    if who == 'p1' and p1['step'] >= m416['step']:
        if p2['shield'] >= m416['attack']:
            p2['shield'] -= m416['attack']
            p1['step'] -= m416['step']
        elif p2['shield'] < m416['attack']:
            p2['health'] -= m416['attack'] - p2['shield']
            p1['step'] -= m416['step']
    if who == 'p2' and p2['step'] >= m416['step']:
        if p1['shield'] >= m416['attack']:
            p1['shield'] -= m416['attack']
            p2['step'] -= m416['step']
        elif p1['shield'] < m416['attack']:
            p1['health'] -= m416['attack'] - p1['shield']
            p2['step'] -= m416['step']


# p18c
def p18c_attack(who):  # who是发起攻击的人
    if who == 'p1' and p1['step'] >= p18c['step']:
        if p2['shield'] >= p18c['attack']:
            p2['shield'] -= p18c['attack']
            p1['step'] -= p18c['step']
        elif p2['shield'] < p18c['attack']:
            p2['health'] -= p18c['attack'] - p2['shield']
            p1['step'] -= p18c['step']
    if who == 'p2' and p2['step'] >= p18c['step']:
        if p1['shield'] >= p18c['attack']:
            p1['shield'] -= p18c['attack']
            p2['step'] -= p18c['step']
        elif p1['shield'] < p18c['attack']:
            p1['health'] -= p18c['attack'] - p1['shield']
            p2['step'] -= p18c['step']


# grenade
def grenade_attack(who):  # who是发起攻击的人
    if who == 'p1' and p1['step'] >= grenade['step']:
        if p2['shield'] >= grenade['attack']:
            p2['shield'] -= grenade['attack']
            p1['step'] -= grenade['step']
        elif p2['shield'] < grenade['attack']:
            p2['health'] -= grenade['attack']
            if p2['health'] <= 5:
                p2['health'] = 0
            p1['step'] -= grenade['step']
    if who == 'p2' and p2['step'] >= grenade['step']:
        if p1['shield'] >= grenade['attack']:
            p1['shield'] -= grenade['attack']
            p2['step'] -= grenade['step']
        elif p1['shield'] < grenade['attack']:
            p1['health'] -= grenade['attack']
            if p1['health'] <= 5:
                p1['health'] = 0
            p2['step'] -= grenade['step']


# riot_shield
def riot_shield_defense(who):  # who是被加护盾的人
    if who == 'p1' and p1['step'] >= riot_shield['step']:
        p1['shield'] += riot_shield['defense']
        p1['step'] -= riot_shield['step']
    elif who == 'p2' and p2['step'] >= riot_shield['step']:
        p2['shield'] += riot_shield['defense']
        p2['step'] -= riot_shield['step']


# bandage
def bandage_treat(who):  # who 是被治疗的人
    if who == 'p1' and p1['health'] <= 70 and p1['step'] >= bandage['step']:
        p1['health'] += bandage['treat']
        p1['step'] -= bandage['step']
    elif who == 'p1' and p1['health'] > 70 and p1['step'] >= bandage['step']:
        p1['health'] = 100
        p1['step'] -= bandage['step']
    if who == 'p2' and p2['health'] <= 70 and p2['step'] >= bandage['step']:
        p2['health'] += bandage['health']
        p2['step'] -= bandage['step']
    elif who == 'p2' and p2['health'] > 70 and p2['step'] >= bandage['step']:
        p2['health'] = 100
        p2['step'] -= bandage['step']


# midisions_bag
def midisions_bag(who): # who 是被治疗的人
    if who == 'p1' and p1['health'] <= 20 and p1['step'] >= midisions_bag['step']:
        p1['health'] += midisions_bag['treat']
        p1['step'] -= midisions_bag['step']
    elif who == 'p1' and p1['health'] > 20 and p1['step'] >= midisions_bag['step']:
        p1['health'] = 100
        p1['step'] -= midisions_bag['step']
    if who == 'p2' and p2['health'] <= 20 and p2['step'] >= midisions_bag['step']:
        p2['health'] += midisions_bag['health']
        p2['step'] -= midisions_bag['step']
    elif who == 'p2' and p2['health'] > 20 and p2['step'] >= midisions_bag['step']:
        p2['health'] = 100
        p2['step'] -= midisions_bag['step']

# 游戏主体
p1_cards = draw_card()
p2_cards = draw_card()
while True:
    print('现在是玩家1的回合，您现在有:', p1_cards,
          '\n玩家2现在有: ', p2_cards,
          '\n玩家1，你现在的状态为', '血量:', p1['health'], '护盾:', p1['shield'], '步数:', p1['step'],
          '\n玩家2，你现在的状态为', '血量:', p2['health'], '护盾:', p2['shield'], '步数:', p2['step'],
          '\n请问您现在要使用物品(输入名字)或积攒步数(输入s):', end='')
    msg1 = input()
    if msg1 == 'ak47':
        if 'ak47,1.5步' in p1_cards:
            ak47_attack('p1')
        else:
            print('您没有ak47')
    elif msg1 == 'm416':
        if 'm416,1步' in p1_cards:
            m416_attack('p1')
        else:
            print('您没有m416')
    elif msg1 == 'p18c':
        if 'p18c,0.5步' in p1_cards:
            p18c_attack('p1')
        else:
            print('您没有p18c')
    elif msg1 == '护盾':
        if '护盾,0.5步' in p1_cards:
            riot_shield_defense('p1')
            p1_cards.remove('护盾,0.5步')
        else:
            print('您没有护盾')
    elif msg1 == '绷带':
        if '绷带,0.5步' in p1_cards:
            bandage_treat('p1')
            p1_cards.remove('绷带,0.5步')
        else:
            print('您没有绷带')
    elif msg1 == '手榴弹':
        if '手榴弹,1.0步' in p1_cards:
            grenade_attack('p1')
            p1_cards.remove('手榴弹,1.0步')
        else:
            print('您没有手榴弹')
    elif msg1 =='midisions_bag':
        if 'midisions_bag,1步' in p1_cards:
            midisions_bag('p1')
            p1_cards.remove('midisions_bag,1步')
        else:
            print('您没有midisions_bag')
    elif msg1 == 's':
        p1['step'] += 1
    if p2['health'] <= 0:
        print('p2失败了')
        break
    os.system('cls')
    print('现在是玩家2的回合，您现在有:', p2_cards,
          '\n玩家1现在有: ', p1_cards,
          '\n玩家2，你现在的状态为', '血量:', p2['health'], '护盾:', p2['shield'], '步数:', p2['step'],
          '\n玩家1，你现在的状态为', '血量:', p1['health'], '护盾:', p1['shield'], '步数:', p1['step'],
          '\n请问您现在要使用物品(输入名字)或积攒步数(输入s):', end='')
    msg1 = input()
    if msg1 == 'ak47':
        if 'ak47,1.5步' in p2_cards:
            ak47_attack('p2')
        else:
            print('您没有ak47')
    elif msg1 == 'm416':
        if 'm416,1步' in p2_cards:
            m416_attack('p2')
        else:
            print('您没有m416')
    elif msg1 == 'p18c':
        if 'p18c,0.5步' in p2_cards:
            p18c_attack('p2')
        else:
            print('您没有p18c')
    elif msg1 == '护盾':
        if '护盾,0.5步' in p2_cards:
            riot_shield_defense('p2')
            p2_cards.remove('护盾,0.5步')
        else:
            print('您没有护盾')
    elif msg1 == '绷带':
        if '绷带,0.5步' in p2_cards:
            bandage_treat('p2')
            p2_cards.remove('绷带,0.5步')
    elif msg1 == '手榴弹':
        if '手榴弹,1.0步' in p2_cards:
            grenade_attack('p2')
            p2_cards.remove('手榴弹,1.0步')
        else:
            print('您没有手榴弹')
    elif msg1 =='midisions_bag':
        if'midisions_bag,1步' in p2_cards:
            midisions_bag('p2')
            p2_cards.remove('midisions_bag,1步')
        else:
            print('您没有midisions_bag')
    elif msg1 == 's':
        p2['step'] += 1
    if p1['health'] <= 0:
        print('p1失败了')
        break
    os.system('cls')
