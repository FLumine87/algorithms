## ROW4 
生成唯一的uid的库（不知道要不要import abc）  
优点：  
全局唯一性。  
不需要依赖外部系统或数据库。  
缺点：  
生成的 ID 较长（例如：550e8400-e29b-41d4-a716-446655440000）  
>https://docs.python.org/zh-cn/3.13/library/uuid.html#uuid.uuid4  
由于
  
### 基于uuid4的哈希表生成法  
>是否会产生重复的暂且不知道  
  
## ROW13  
增加了缺省值status  
>注意了，没发现有setter函数  
  
## ROW26  
增加了一个get_energy_usage ，不用了hh^_^ 
  
## ROW29    
新增了多个setting method  
  
## ROW37  
__name的初始化和设置是否需要断言  
在__init__中无法直接添加
实现了  
逻辑大概是：  
    首先保证hub已实例  
    初始化后直接添加  
    如果add发现已经有了，就打印后推出

  
### Confusion  
我觉得在总结的时候可以写声明与初始化与主函数分开，保留适当的接口，既可以增加主文件的可读性，又可以通过接口文件快速了解到文件的接口信息。（但根据assignment的要求，我并没有如此）  
  
## ROW43  
这里是否需要采用断言，我还没有想好  
与此同时，确实被复用了，同时将其复用的函数改变为一个私有函数
  
## ROW51  
如果这里不再需要断言，这需要给id一个数组，这样不仅可以记录过往的id，还可以通过哈希函数倒推过往的对象属性（如果实现了，则必须给数组设置长度，否者也会导致内存过度占用的问题）  
## ROW65  
将输出方式改为列表，这样更加直观  
  
## ROW67  
用了继承，没什么好说的，哦，最多就是函数的复用  
  
## ^104  
可以确保smarthomehub是唯一实例，同时保证devicecontroller也是唯一实例  
  
## ROW87  
由于py不是全部编译完才运行，对于逐行编译，在对于未实例化的成员函数时，不知道是否报错.增加了一个try  
  
## ROW82  
要检测是否已经实例化  
  
## HUB  
都存在需要检测的问题，真的不想弄检测了，回来再说  
  
不用管id的事情了，tmd，但是否也要考虑缺省值  
  
## ROW136  
可以在初始化的时候就自动加入devices字典  
  
## ROW91  
可以之后加一个多个device一次加入  
同时最后还可以添加一个功能，若不存在该对象，则创建并添加  
  
### note  
可以把部分很恶心的函数写成重载，^_^  
  
### 引用2  
datetime
>https://docs.python.org/3/library/datetime.html  
>https://schedule.readthedocs.io/en/stable/
iterator  
>https://docs.python.org/3/library/stdtypes.html#iterator-types  
  
## display_status  
无法读取__schedule