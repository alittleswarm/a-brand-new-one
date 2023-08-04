# 设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量
class Item:
    def __init__(self, id: int = 0, name: str = None, price: float = 0, leftones: int = 0, total: int = 0):
        self._id = id
        self._name = name
        self._price = price
        self._leftones = leftones
        self._total = total

    def display(self):  # 显示信息
        print(f"id:{self.id},名字:{self.name},单价:{self.price},剩余:{self.leftones},总计:{self.total}")

    def income(self):
        return self.price * (self.total - self.leftones)

    def setdata(self, price, leftones, *, id=None, name=None, total=None):  # 修改信息
        self.price = price
        self.leftones = leftones
        if id:
            self.id = id
        if total:
            self.total = total
        if name:
            self.name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def leftones(self):
        return self._leftones

    @property
    def total(self):
        return self._total

    @id.setter# 注意下划线
    def id(self, id):
        self._id = id

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @leftones.setter
    def leftones(self, leftones):
        self._leftones = leftones

    @total.setter
    def total(self, total):
        self._total = total


snake = Item(114514, '先辈的雪', 1.14541, 114, 514)
snake.display()
print('卖出金额:', snake.income())
snake.setdata(11.4, 0)
snake.display()
print('卖出金额:', snake.income())