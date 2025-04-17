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
| paradigm          | 范式         |  
| implementation          | 实施，工具         |  
| exposing          | 暴露         |  
| interfaces          | 接口         |  
| module          | 模块         |  
| default value          | 缺省值         |  
| efficient          | 有效率的         |  
| initialization       | 初始化       |  
| storage          | 存储         |  
| traverse          | 遍历         |  
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
  
## new&init
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
  
在 Python 里，抽象修饰器和抽象类、抽象方法关联紧密，主要借助 `abc`（Abstract Base Classes） 模块中的 `@abstractmethod` 与 `@abstractclassmethod`、`@abstractstaticmethod`、`@abstractproperty` 等修饰器来定义抽象类和抽象方法。下面为你详细介绍：

### 核心概念
- **抽象类**：不能被实例化的类，主要用于为子类提供统一的接口和规范。
- **抽象方法**：仅包含方法声明，没有具体实现的方法，子类必须实现这些抽象方法。

### 常用抽象修饰器及示例

#### 1. `@abstractmethod`
- **作用**：把类的方法标记为抽象方法，含有抽象方法的类就是抽象类，不能被实例化。
- **示例代码**：
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 尝试实例化抽象类会报错
# s = Shape()  

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(5, 3)
print(rect.area())
print(rect.perimeter())
```
在上述代码中，`Shape` 类是抽象类，`area` 和 `perimeter` 是抽象方法。`Rectangle` 类继承自 `Shape` 类，并且实现了抽象方法，所以可以实例化。

#### 2. `@abstractclassmethod 等`
- **作用**：将类方法标记为抽象类方法，子类必须实现该抽象类方法。
- **示例代码**：
```python
from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def speak(cls):
        pass

class Dog(Animal):
    @classmethod
    def speak(cls):
        print("Woof!")


Dog.speak()
```
这里 `Animal` 类的 `speak` 是抽象类方法，`Dog` 类继承 `Animal` 类并实现了该方法。

### 抽象修饰器的用途
- **规范接口**：抽象类和抽象方法为子类提供了统一的接口，确保子类实现必要的方法，增强了代码的规范性和可维护性。
- **提高代码复用性**：通过抽象类可以定义通用的行为和属性，子类可以继承并扩展这些功能，减少代码重复。   
  
### @staticmethod和@classmethod的区别  

#### 语法及参数
- **`@staticmethod`**：将一个方法转换为静态方法，静态方法不需要传入特殊的参数，它不依赖于类或实例的状态。静态方法的定义与普通函数类似，只是它位于类的命名空间中。
- **`@classmethod`**：将一个方法转换为类方法，类方法的第一个参数通常命名为 `cls`，它代表类本身。通过 `cls` 参数，类方法可以访问和修改类的属性。

以下是一个简单的示例代码，展示了两者在语法和参数上的区别：
```python
class MyClass:
    class_variable = 10

    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method. Class variable: {cls.class_variable}")

```
  
  
## 一些奇怪的关键字  

### 1. `await`
- **功能**：`await` 是 Python 异步编程里的关键字，用于暂停异步函数的执行，等待一个可等待对象（像 `asyncio.Future`、`asyncio.Task` 或者另一个异步生成器）执行完毕，之后再继续执行。
- **示例代码**：
```python
import asyncio

async def async_function():
    print("开始执行异步函数")
    await asyncio.sleep(1)
    print("异步函数执行完毕")

async def main():
    await async_function()

asyncio.run(main())
```
- **解释**：在 `async_function` 中，`await asyncio.sleep(1)` 会暂停函数执行 1 秒，等这 1 秒过去后再接着执行后续代码。

### 2. `async`
- **功能**：`async` 用来定义异步函数或者异步生成器。以 `async` 定义的函数是异步函数，调用时不会马上执行，而是返回一个协程对象。
- **示例代码**：
```python
import asyncio

async def async_task():
    print("执行异步任务")
    await asyncio.sleep(2)
    print("异步任务完成")

async def main():
    task = async_task()
    await task

asyncio.run(main())
```
- **解释**：`async def async_task()` 定义了一个异步函数，`main` 函数里调用 `async_task()` 得到一个协程对象，然后用 `await` 来执行这个协程。


### 3. `yield`
`yield` 关键字用于定义生成器函数。生成器函数在调用时不会立即执行，而是返回一个生成器对象。每次调用生成器的 `__next__()` 方法，函数会执行到 `yield` 语句处并暂停，同时返回 `yield` 后面的值。示例如下：
```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
```


  

## 问答题  
  
### What is OOP  
  
OOP stands for Object - Oriented Programming. It is a programming paradigm that organizes software design around objects. Here are its main characteristics:
- **Encapsulation**: It hides the internal implementation details of an object and only exposing necessary interfaces to the outside.
 - **Inheritance**: Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). This promotes code reuse. 
 - **Polymorphism**: Polymorphism enables different objects to respond differently to the same message. 
 - **Abstraction**: Abstraction is about simplifying complex systems by hiding unnecessary details and showing only the essential features.   
 - **interactiveness**：Program execution involves the delivery of messages between objects.

Over all, OOP provides a modular, organized, and extensible way of programming.   
  
### What is OOA  
In Python, OOA stands for Object-Oriented Analysis, which is a crucial part of the software development process. Its main objective is to analyze and understand the problem domain using object-oriented concepts and methods, and then construct an object-oriented model of the problem domain. The following is a detailed introduction to OOA:

**Analysis Steps**
1. **Identify Objects and Classes**: Identify the key objects and classes from the problem domain.  
2. **Determine the Attributes and Methods of Objects**: Define the corresponding attributes and methods for each class.   
3. **Analyze the Relationships between Classes**: Determine the relationships between classes, such as inheritance, association, aggregation, etc.   
4. **Build an Object Model**: Use tools such as UML (Unified Modeling Language) to build an object model, intuitively representing classes, objects, and the relationships between them.


### 类与对象的区别  
A class and an object are fundamental concepts in object - oriented programming (OOP), and they have the following differences:
- **Definition and Nature**: A class is a template for creating objects. It defines a set of attributes (data) and methods (functions).After class instance, it becomes an object
 - **Memory Allocation**: When a class is defined, no memory is allocated for the data members of the class.In Python, objects always occupy memory space  
  
  
## 须知  
  
下面是Python OOP的一些考试范围和复习建议：
一、知识点类（选择、判断类小题为主，自行斟酌复习程度）
1、OOP技术的主要优势（与结构化编程相比）  
2、OOP中继承、封装、多态的概念  
3、子类继承父类后，父类中被override的方法和未被override的方法，从子类对象调用时有哪些情况？  
4、<u>Python中哪个方法用于访问父类？使用场景是这样的？</u>  
5、类方法（class method）的概念，类与对象间的关系（object is an instance of a class）。    
>在面向对象编程里，类方法是绑定到类而非类实例的方法。  
  

6、Python中定义一个类的正确方法/语法。  
7、Python中的构造函数(constructors)，即__init__的概念、使用场景。  
8、Python中全局命名空间（global namespace）的作用/目的是什么？  
> 在 Python 里，命名空间是一种管理变量和函数名称的机制，它规定了名称的可见范围和作用域。全局命名空间（global namespace）是 Python 中一个重要的命名空间，下面为你详细介绍它的作用和目的。  
**存储全局变量和函数**  
全局命名空间用于存储在模块级别定义的变量和函数，这些变量和函数在整个模块中都可以被访问。全局变量和函数在程序运行期间始终存在，除非被显式删除或程序结束。  
**模块间的数据共享**  
在 Python 中，每个模块都有自己的全局命名空间。不同模块之间可以通过导入模块的方式访问其他模块的全局命名空间中的变量和函数，从而实现模块间的数据共享。  
**示例代码**  
```python
# module1.py
global_variable = 20

def global_function():
    print("这是 module1 中的全局函数")

# module2.py
import module1

# 访问 module1 中的全局变量和函数
print(module1.global_variable)
module1.global_function()

```  
  
9、递归函数中的base case的定义、作用。 
>base case（基例，也被称为基本情况或终止条件）base case 指的是递归函数里能够直接得出结果，无需再进行递归调用的情况.。  
>1. 避免无限递归  
>2.  确保函数的正确性  
>3. 简化问题的求解过程  
  
10、双链表（doubly-linked list）相比单链表（singly-linked list）的优势是什么？  
> 1. 双向遍历  
> 2. 节点删除和插入操作更高效（特定场景）  
> 3. 实现某些算法更方便:双链表的双向指针使得实现这些算法更加方便，例如实现双向队列（deque）、LRU（Least Recently Used）缓存算法等。在这些算法中，需要频繁地在链表的头部和尾部进行插入和删除操作，以及访问节点的前一个节点  
> 4. 数据回溯更容易  
  
11、Python文件处理的相关函数（open()、close()）、常用符号('w','r')、模式（with open() as f:）.  
>- **参数说明**：  
    - `file`：必需参数，代表要打开的文件的路径，可以是相对路径或绝对路径。  
    - `mode`：可选参数，指定文件的打开模式，默认值为 `'r'`（只读模式）。常见的模式有：  
        - `'r'`：只读模式，文件指针位于文件开头。  
        - `'w'`：写入模式，若文件存在则清空内容，若文件不存在则创建新文件。  
        - `'a'`：追加模式，文件指针位于文件末尾，若文件不存在则创建新文件。  
        - `'x'`：创建模式，若文件已存在则抛出 `FileExistsError` 异常，若文件不存在则创建新文件。  
        - `'b'`：二进制模式，可与其他模式组合使用，如 `'rb'` 表示以二进制只读模式打开文件。  
        - `'t'`：文本模式，默认值，可与其他模式组合使用，如 `'wt'` 表示以文本写入模式打开文件。  
    - `encoding`：可选参数，指定文件的编码方式，如 `'utf-8'`、`'gbk'` 等，默认使用系统默认编码。  
**上下文管理器：`with` 语句**
为避免忘记关闭文件，可使用 `with` 语句来打开文件。`with` 语句会在代码块执行完毕后自动关闭文件。
**文件读取方法**
**`read()` 方法**
用于读取文件的全部内容或指定数量的字符。
```python
with open('example.txt', 'r', encoding='utf-8') as file:
    # 读取全部内容
    content = file.read()
    print(content)

    # 读取前 10 个字符
    file.seek(0)  # 将文件指针移到文件开头
    partial_content = file.read(10)
    print(partial_content)

```
>**`readline()` 方法**
用于逐行读取文件内容，每次调用返回文件的一行。
```python
with open('example.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    while line:
        print(line.strip())  # 去除行尾的换行符
        line = file.readline()

```
>**`readlines()` 方法**
用于读取文件的所有行，并将每行内容作为一个元素存储在列表中。
```python
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

```
>**文件写入方法**
**`write()` 方法**
用于向文件中写入字符串。
```python
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!\n')
    file.write('This is a test.')

```
>**`writelines()` 方法**
用于向文件中写入一个字符串列表，不会自动添加换行符。
```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3']
with open('example.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)

```
>**文件指针操作方法**
>**`seek()` 方法**
用于移动文件指针到指定位置。
```python
with open('example.txt', 'r', encoding='utf-8') as file:
    # 移动文件指针到第 5 个字符的位置
    file.seek(5)
    content = file.read()
    print(content)

```
>**`tell()` 方法**
用于返回文件指针的当前位置。
```python
with open('example.txt', 'r', encoding='utf-8') as file:
    position = file.tell()
    print(f'文件指针当前位置: {position}')

```
   
12、队列和栈的访问特性（哪个是先进先出，那个是后进先出）。  
13、二叉搜索树中搜索一个元素的最好时间复杂度如何推导？  
14、<u>树的遍历策略：前序、中序、后序、分层。</u>  
15、哪个数据结构适合用于实现一个文本编辑器中的undo操作？（考虑现行结构，比如队列、栈、链表等）。  
16、Python的异常处理（exception handling）方法。  
| **异常类型**          | **描述**                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `ValueError`          | 传递给函数的参数类型或值无效。                                           |
| `TypeError`           | 操作或函数应用于不支持的类型。                                           |
| `ZeroDivisionError`   | 除数为零时引发的异常。                                                   |
| `FileNotFoundError`   | 尝试打开不存在的文件时引发的异常。                                       |
| `IndexError`          | 尝试访问超出序列范围的索引时引发的异常。                                 |
| `KeyError`            | 尝试访问字典中不存在的键时引发的异常。                                   |
| `AttributeError`      | 尝试访问对象中不存在的属性时引发的异常。                                 |
| `IOError`             | 输入/输出操作失败时引发的异常。                                          |
| `ImportError`         | 导入模块失败时引发的异常。                                               |
| `RuntimeError`        | 程序运行时引发的通用异常。                                               |  

17、如果使用Pickle库将一个Python对象串行化。  
 **Pickle 的常用方法**  
| **方法**                | **描述**                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| `pickle.dump(obj, file)` | 将对象 `obj` 序列化并保存到文件 `file` 中。                              |
| `pickle.load(file)`      | 从文件 `file` 中加载序列化的对象。                                      |
| `pickle.dumps(obj)`      | 将对象 `obj` 序列化为字节流。                                           |
| `pickle.loads(bytes)`    | 将字节流 `bytes` 反序列化为对象。                                       |  
  
**Pickle 与 JSON 的对比**  
| **特性**          | **Pickle**                          | **JSON**                           |
|-------------------|-------------------------------------|------------------------------------|
| **用途**          | Python 专用序列化工具               | 跨语言的数据交换格式               |
| **可读性**        | 二进制格式，不可读                  | 文本格式，可读性强                 |
| **性能**          | 对复杂对象性能较高                  | 对简单数据性能较高                 |
| **安全性**        | 存在安全风险（不可信数据可能执行代码） | 安全性较高                         |
| **支持的对象**    | 支持几乎所有 Python 对象             | 仅支持基本数据类型（如字符串、数字）|  

18、OOP中UML的作用/目标。  
- **作用**：
  - **可视化设计软件系统**：用图形展示软件系统的结构和行为，便于理解架构及各部分交互。
  - **促进团队协作**：为不同角色提供共同交流平台，确保对系统理解一致，减少沟通问题。
  - **文档记录**：作为重要文档记录系统设计和实现细节，利于项目维护、升级及新成员了解。
  - **支持软件分析与设计**：适用于开发生命周期各阶段，提前发现问题，优化设计，提高软件质量。
- **目标**：
  - **提高软件质量**：通过设计和分析，理解需求，优化架构，减少缺陷和错误。
  - **降低开发成本**：早期发现并解决问题，避免后期大规模修改，减少沟通成本。
  - **实现软件复用**：清晰展示结构，便于识别和提取可复用组件，提高效率和质量。
  - **促进软件标准化**：作为国际标准语言，提高软件互操作性和可移植性。 
 
19、常见设计模式的使用场景（Adapter, Factory, Singleton, Strategy）。(我个人认为OOP课程直接讲设计模式，是过度抽象的。因此，这个问题，重点理解单例模式)  
20、Python迭代器（iterator）的基本操作，尤其是next()方法。  
21、Python装饰器（decorator）的基本操作，尤其是@staticmethod的作用。  
22、Python代码的风格，Pythonic代码的内涵、特征。（我没有OOP的PPT,以前有学生发过我没保存，我猜这个问题PPT肯定有）  
23、区分几个缩写，MVC（Model-View-Control）、LIFO（Last-In First-Out）、FIFO(First-In First-Out)、DFS（Depth-First Search）。如果问Web设计用哪个设计模式，你怎么答？（这个问题，其实是考智商的吧，四个名词，只有一个是设计模式，答错的话，能怎么解释？）  
24、在版本控制中，Git的作用是什么？  
在版本控制中，Git的作用如下：
1. **版本管理**
    - 记录历史版本
    - 版本回溯
2. **团队协作**
    - 多人并行开发
    - 解决冲突
3. **代码审查**
    - 分支管理与审查
    - 代码历史审查
4. **项目备份与恢复**
    - 分布式存储
    - 远程仓库同步
5. **实验与创新**
    - 分支实验
    - 版本对比  

25、多态如何实现不同子类同一个函数的多重不同实现？  
26、继承机制能否允许子类直接修改父类的私有成员？  
27、一个类是否可以有多个带不同参数的构造函数？  
28、在OOP里this关键字的含义、使用场景。

二、关键概念（可能会做概念名称与表述的匹配）
Class, Object, Attribute, Interface, Method, Encapsulation, Inheritance, Polymorphism, Abstraction

三、概念对比：method overloading和method overriding的区别。试举例。

四、算法：
二叉搜索树（构建、元素插入操作、元素删除操作、前序遍历、中序遍历、后序遍历、广度优先搜索、深度优先搜索）。