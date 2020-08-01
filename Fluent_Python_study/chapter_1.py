# 魔术方法，双下方法
# Python风格的代码，

import collections
from math import hypot
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


# 示例1纸牌
class FrechDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        # 所有扑克列表
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    # 扑克排序，大小
    rank_value = FrechDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]


# 示例二坐标
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # 将对象用字符串形式表达，输出控制台和调式程序
        # __str__在于，被str()和ptint()调用，
        return 'Vector(%s, %s)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


if __name__ == '__main__':
    deck = FrechDeck()
    # 纸牌数量
    print(len(deck))
    # 纸牌第一张
    # print(deck[0])
    # print(deck[-1])
    # 获得随机纸牌
    # print(choice(deck))
    # for card in reversed(deck):
    #     print(card)
    for card in sorted(deck, key=spades_high):
        print(card)
