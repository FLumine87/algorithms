## 复习-中英  
| 英             | 中           |
|-----------------|---------------|
| reference       | 引用         |  
| indentation       | 缩进         |  
| template          | 模板         |  
| assign          | 分配；赋值         |  
| instance          | 实例         |  
| parameters          | 参数         |  
| terminate          | 终止         |  
| residual value          | 残差值         |  
| properties          | 特征         |  
| Attribute          | 属性         |  
|  Inheritance          | 继承         |  
| Polymorphism          | 多态         |  
| Encapsulation          | 封装         |  
| invoke          | 调用         |  
| association          | 关联         |  
| composition          | 组成         |  
| aaaa          | 1111         |  
| aaaa          | 1111         |  
  

## 说一句  
py中的浅拷贝有意思啊  
  
## OOP概念及特征  
面向对象编程（Object-Oriented Programming，OOP）是一种编程范式，它围绕“对象”来组织代码，有许多重要的概念和特征，以下为你详细介绍：

### 基本概念
- **对象（Object）**：对象是类的实例，它将数据（属性）和操作数据的方法捆绑在一起。例如，在一个模拟学校的程序里，“学生”可以是一个对象，该对象有姓名、年龄、成绩等属性，还有学习、考试等方法。
- **类（Class）**：类是对象的抽象模板，定义了对象的属性和方法。以汽车为例，“汽车”类可以定义汽车的颜色、品牌、型号等属性，以及启动、加速、刹车等方法。通过类可以创建多个具体的汽车对象。
- **封装（Encapsulation）**：封装是把数据和操作数据的方法绑定在一起，并隐藏对象的内部实现细节，只对外提供必要的接口。这样可以保护数据不被外部随意访问和修改，提高代码的安全性和可维护性。比如，一个银行账户类，将账户余额作为私有属性，通过存款和取款方法来操作余额，外部无法直接修改余额。
- **继承（Inheritance）**：继承允许一个类（子类）继承另一个类（父类）的属性和方法，从而实现代码的复用和扩展。子类可以在父类的基础上添加新的属性和方法，或者重写父类的方法。例如，“轿车”类可以继承“汽车”类的属性和方法，并且添加自己特有的属性（如座位数）和方法（如天窗开启）。
- **多态（Polymorphism）**：多态指不同的对象对同一消息做出不同的响应。多态通过继承和方法重写来实现，提高了代码的灵活性和可扩展性。例如，“动物”类有“叫”的方法，“猫”类和“狗”类继承自“动物”类，并分别重写了“叫”的方法，当调用“叫”的方法时，猫和狗会发出不同的叫声。

### 其他特征
- **抽象（Abstraction）**：抽象是忽略对象的非本质特征，只关注对象的本质特征和行为。通过抽象可以创建抽象类和接口，为子类提供统一的规范。例如，在一个图形绘制程序中，“图形”类可以是一个抽象类，定义了绘制图形的抽象方法，具体的图形（如圆形、矩形）类继承自“图形”类，并实现绘制方法。
- **组合（Composition）**：组合是将不同的对象组合在一起，形成一个新的对象。组合强调的是“有一个”（has - a）的关系，而不是“是一个”（is - a）的关系（继承）。例如，“汽车”对象可以由“发动机”对象、“轮胎”对象等组合而成。
- **消息传递（Message Passing）**：对象之间通过发送和接收消息来进行通信。当一个对象需要另一个对象执行某个操作时，它会向该对象发送一个消息。例如，在一个游戏中，玩家对象向敌人对象发送“攻击”消息，敌人对象接收到消息后执行相应的防御或反击操作。  
  
## OOP设计模式  
  
### 单例模式
#### 介绍
单例模式确保一个类只有一个实例，并提供一个全局访问点。在一些需要共享资源的场景中非常有用，比如数据库连接池，整个应用程序只需一个连接池实例，避免资源浪费。
#### 代码示例
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


# 使用示例
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # 输出: True

```

### 工厂模式（简单工厂）
#### 介绍
工厂模式将对象的创建逻辑封装在工厂类中，客户端通过工厂类创建对象，而无需了解具体的创建细节。简单工厂根据不同的条件创建不同类型的对象。
#### 代码示例
```python
# 简单工厂模式
class Car:
    def drive(self):
        pass


class Sedan(Car):
    def drive(self):
        print("Driving a sedan.")


class SUV(Car):
    def drive(self):
        print("Driving an SUV.")


class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        return None


# 使用示例
sedan = CarFactory.create_car("sedan")
suv = CarFactory.create_car("suv")
sedan.drive()
suv.drive()

```

### 代理模式
#### 介绍
代理模式为其他对象提供一种代理以控制对这个对象的访问。可以在访问真实对象前后添加额外的操作，如权限验证、日志记录等。
#### 代码示例
```python
class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")


class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        if self.check_access():
            self.real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")


# 使用示例
real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()

```

### 装饰器模式
#### 介绍
装饰器模式动态地给一个对象添加一些额外的职责，比生成子类更为灵活。可以在不改变原有对象结构的基础上，为对象添加新的功能。
#### 代码示例
```python
class Coffee:
    def cost(self):
        return 5


class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2


class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1


# 使用示例
simple_coffee = Coffee()
coffee_with_milk = MilkDecorator(simple_coffee)
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_and_sugar.cost())

```

### 观察者模式
#### 介绍
观察者模式定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。常用于实现事件驱动系统。
#### 代码示例
```python
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class Observer:
    def update(self):
        pass


class ConcreteObserver(Observer):
    def update(self):
        print("ConcreteObserver: Received an update.")


# 使用示例
subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify()

```

### 策略模式
#### 介绍
策略模式定义一系列算法，把它们一个个封装起来，并且使它们可相互替换。可以在运行时根据不同的需求选择不同的算法。
#### 代码示例
```python
class PromotionStrategy:
    def discount(self, price):
        pass


class PercentageDiscount(PromotionStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def discount(self, price):
        return price * (1 - self.percentage)


class FixedAmountDiscount(PromotionStrategy):
    def __init__(self, amount):
        self.amount = amount

    def discount(self, price):
        return max(0, price - self.amount)


class ShoppingCart:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate_total(self, price):
        return self.strategy.discount(price)


# 使用示例
original_price = 100
percentage_discount = PercentageDiscount(0.2)
fixed_amount_discount = FixedAmountDiscount(20)

cart = ShoppingCart(percentage_discount)
print(cart.calculate_total(original_price))

cart.set_strategy(fixed_amount_discount)
print(cart.calculate_total(original_price))

```  
  
## __new__&__init__
 - `__new__` 方法是类的构造方法，用于创建类的实例并返回它，是在实例创建之前被调用的静态方法。它的第一个参数是类本身（cls） ，主要负责对象的创建。
 - `__init__` 方法是实例的初始化方法，在`__new__`返回实例对象后被调用，第一个参数是实例对象（self），主要用于对新创建的实例进行初始化设置，比如给实例属性赋值 。例如：
```python
class Test:
    def __new__(cls):
        print('__new__ method is called')
        return super().__new__(cls)
    def __init__(self):
        print('__init__ method is called')
        self.attr = 10
t = Test()
``` 
执行上述代码，先输出`__new__ method is called`，再输出`__init__ method is called`，说明`__new__`方法先被调用用于创建对象，然后`__init__`方法被调用用于初始化对象属性。   
  
## super()  
判断题第5题内容是 “The super() function in Python is used to call a method from the parent class.”，答案是True。在Python中，`super()`函数用于调用父类（超类）的方法，能在子类中复用父类的方法，优化代码，避免重复编写。例如：
```python
class Animal:
    def speak(self):
        print("I'm an animal.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("I'm a dog and I bark.")

d = Dog()
d.speak()
```  
  
在Python中，装饰器（修饰器）是一种强大的工具，它可以在不修改原函数代码的情况下，对函数或类进行扩展和增强。以下为你介绍一些常见的修饰器：

## 内置装饰器
#### 1. `@staticmethod`
- **作用**：将类中的方法转换为静态方法。静态方法不需要实例化类就可以调用，它不依赖于类的实例，也没有`self`或`cls`参数。
- **示例代码**：
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 可以直接通过类名调用静态方法
result = MathUtils.add(3, 5)
print(result)
```
#### 2. `@classmethod`
- **作用**：将类中的方法转换为类方法。类方法的第一个参数通常是`cls`，代表类本身，类方法可以通过类名或实例调用。
- **示例代码**：
```python
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

p1 = Person()
p2 = Person()
# 可以通过类名调用类方法
print(Person.get_count())
```
#### 3. `@property`
- **作用**：将类中的方法转换为属性，使得可以像访问属性一样调用方法，同时还可以为属性设置`setter`和`deleter`方法。
- **示例代码**：
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
# 像访问属性一样调用方法
print(c.radius)
c.radius = 10
print(c.radius)
```

### 自定义装饰器
#### 1. 简单的函数装饰器
- **作用**：用于记录函数的执行时间。
- **示例代码**：
```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def my_function():
    time.sleep(2)

my_function()
```
#### 2. 带参数的装饰器
- **作用**：可以根据传入的参数来定制装饰器的行为。
- **示例代码**：
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

