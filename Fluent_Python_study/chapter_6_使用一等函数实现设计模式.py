from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')  # 顾客信息姓名，积分


class LineItem:
    """商品
    商品名称 数量 价格"""

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):  # 总价
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.custome = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 抽象基类 策略接口
    @abstractmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):
    """第一种策略"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """第二种策略"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    """第三种策略"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


'------------------------------------------------------------------------------------'


# 使用函数策略
def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


# 使用最佳策略
# def best_promo(order):
#     peomos = [fidelity_promo, bulk_item_promo, large_order_promo]
#     return max(promo(order) for promo in peomos)


# globals()返回字典，全局符号表,返回⼀个字典，表示当前的全局符号表
print([name for name in globals()])


# 优化查找全部策略
def best_promo(order):
    peomos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']
    return max(promo(order) for promo in peomos)


"""
inspect.getmembers 函数⽤于获取对象（这⾥是 promotions 模块）的属性，第⼆个参数是可选的判断条件（⼀个布尔值函数）
inspect.isfunction，只获取模块中的函数
def best_promo(order):
    import inspect
    promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]
    return max(promo(order) for promo in peomos)
"""

############'命令'模式############
