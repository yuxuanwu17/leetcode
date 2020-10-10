### Python 

#### 面向对象
万物都是对象，属性&行为 封装成对象 

python等面向对象的提出是为了更好的处理和管理同属一个类别的事情，这样就可以省去多余重复的基础代码，让程序变得更加简洁和强大

python就是彻底OOP，所有的值都是对象类型

关注是解决掉问题的对象，对象具有几个属性（技能），在调度而不是具体的实现，可以分配给谁来做

只负责调度，不分配具体步骤

#### 对象 vs 过程
面向对象本身是对面向过程的封装

分解任务的能力，找对象，划分对象的条件

#### 如何转变这种思维方式
1。 列出一个任务的具体实现步骤
2。 试图分离这些实现步骤重的功能代码块
3。 将这些功能代码块，划分到某一个对象中
4。 根据这个对象以及对应的行为，抽出对应的类，进而设计类

#### 类：一个有具体对象特征的抽象 vs 实例，就是具体的补充
作用： 根据抽象的类，生产出具体的对象 

组成： 名称，属性，方法

注意： 首先是产生对象之后，对象才拥有具体的属性值，和对应的方法实现

逻辑链： 对象->抽象->类->实例化->对象

#### Python 实际操作
class + 名字（首字母大写）--大驼峰的规范：

pass 代表一个空的语句，是为了保证结构的完整

定义一个类
```
class Money:
    pass
```

根据这个类，创建并且实例化一个对象

```
one = Money()
## 可以比较print(Money) 和 print(one) 

print(Money.__name__)
```

*注意，这个Money既是类名，也是变量，可以更改赋值*

#### 区别属性和变量
1。 变量是可以改变的量值
2。 属性是属于某个对象的特性，属性必须通过一个对象来进行访问，必须有一个宿主

```
# class Money:
#     pass

# one = Money()
# one.age = 10
# one.age = 18


# Money.count = 1
# Money.age = 18
# Money.num = 666

# print(Money.count)
# print(Money.__dict__)
.__dict__ 代表当前对象的所有属性
```

<br />

先去找对象的属性，若没有，再去找class的属性

del 只能删除直系的属性

#### 类属性的内存存储问题
类的__dict__ 是不可修改的，但对象的是可以改的 （unwritteable）
一般情况下，属性存储在__dict__的字典种，有些内置对象没有__dict__属性


#### 限制对象的属性 \_\_slots\__ 
```
class Person:
    __slots__ = ["age"]
    pass
p1 = Person 
p1.age = 18 ## 不能添加其他的属性，否则会报错
```
面向对象的方法：第一个参数必须要接收到的实例数据类型
1。 实例方法 （第一个参数接受的类型）
```
class Person:
    def eat2(self):
        print("这是一个实例方法"，self)
```

2。 类方法
```
class Person:
    @classmethod
    def leifangfa(cls):
        print("这是一个类方法）
```
3。 静态方法
```
class Person:
    @staticmethod
    def jingtaifangfa():
        print("这是一个静态方法"）

```

装饰器的作用：在保证原本函数不变的前提下，直接给这个函数增加一些功能
例如  @classmethod

延伸类（derived class）
```
class A (Person):
    pass
A.leifangfa(0)
```
A 继承了Person的类

元类： 创建类对象的类 （最终都指向了一个叫type的类，type可以自己调用自己）

继承一个类 __meta__class
```
class Person
    __metaclass__ = Student
    pass 
```
另一种写法
```
class Animal: 
    pass

class Person(Animal):
    pass
```

流程
1。检查类中是否有明确__metacclass__属性<br />
2。检查父类种是否存在__metaclass_属性<br />
3。检查模块里是否存在__metaclass_属性<br />
4。检查内置的type这类元素来创建这个对象<br />

#### 类的描述，标准注释方式

```
class Person:
    """
    关于这个类的描述，类的作用，类的构造函数；类属性的描述
        attribute: count 解释解释
    """
    count = 1 
    
    def run(self, distance, step):
        """
        这个方法的作用效果 
        :param distance: 参数的含义，参数的类型int，是否有默认值
        :param step: 
        :return: 返回的结果的含义（时间），返回数据的类型int 
        """
        print("I am running")
```
可以通过help(Person)来进行文档内容的查看
```angular2
help(Person)
```

生成项目文档具体步骤：
1. 查看文档的描述,先去当前路径下 python3 -m pydoc 模块名称(注意千万不要加.py,不是文件) (使用内置模块pydoc)
2. 启动本地服务，浏览文档 python3 -m pydoc -p 666
3. 生成制定模块html文档 python3 -m pydoc -w 模块名称

_x 受保护的属性
__x 私有属性

#### Python from 和 import 用法区别
客户端可以执行import或from语句。如果模块还没有加载，这两个语句会去搜索、编译以及执行模块文件程序。主要差别在于，import会读取整个模块，所以必须进行定义后才能读取它的变量名；from将获取（或者是复制）模块特定的变量名。

　　import使一个变量名引用整个模块对象，因此必须通过模块名称来得到该模块的属性（例如，module1.printer）。而from会把变量名复制到另一个作用域，所以它就可以直接在脚本中使用复制后的变量名，而不用通过模块（例如，printer）。

　　from语句有破坏命名空间的潜质。如果使用from导入变量，而那些变量碰巧和作用域中现有变量重名，变量就会被悄悄的覆盖掉。使用import语句时就不存在这种问题，因为必须通过模块名才能获取其内容。不过，使用from时，只要你了解并预料到可能发生这种事，在实际情况下这就不是一个大问题了，尤其是当你明确列出导入变量名时（例如，from module import x, y, z）。

　　另一方面，和reload调用同时使用时，from语句有比较严重的问题，因为导入的变量名可能引用之前版本的对象。再者，from module import *形式的确可能破坏命名空间，让变量名难以理解，尤其是在导入一个以上的文件时。

　　比较务实的建议是：简单的模块一般倾向于使用import，而不是from。多数的from语句是用于明确列举想要的变量，而且限制在每个文件中只用一次from *形式。这样一来，任何无定义的变量名都可以认为是存在于from *所引用的模块内。当你必须使用两个不同模块内定义的相同变量名变量时，才真的必须使用import，这种情况下不能使用from。