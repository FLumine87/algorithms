import keyboard
import time

###这里写一些全局参数

###

class method_gobal:
    pass
    #这里面主要写静态类
    #类相当于namespace
    #@staticmethod

class component_eve:
    pass
#类参数应该包含时间戳

def main():
    def HotKeyEsc():
        running = False
    
    running = True
    keyboard.add_hotkey('esc', HotKeyEsc)

    while running:
        pass
    #没想好调用逻辑是什么


try:
    main()
except KeyboardInterrupt:
    print("exit")

# import keyboard

# def my_action():
#     print("你按下了 F2，执行自定义操作！")
#     # 这里写你想要的行为，比如调用某个类的静态方法
#     # method_gabol.some_static_method()

# # 非阻塞监听 F2 键
# keyboard.add_hotkey('f2', my_action)

# print("程序运行中，按 F2 会触发自定义行为，主循环不会被阻塞。")

# while True:
#     # 主循环其它逻辑
#     pass