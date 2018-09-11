import threading
import time


# 耗时操作
def longIo(callback):
    def run(cb):
        print("开始耗时操作")
        time.sleep(5)
        print("结束耗时操作")
        cb("shixintai is cool")
    threading.Thread(target=run, args=(callback,)).start()


# 函数（回调函数）
def finish(data):
    print("开始处理回调函数")
    print("接收到longIo响应的数据为：", data)
    print("结束处理回调函数")



def reqA():
    print("开始处理A")
    longIo(finish)
    print("结束处理A")


def reqB():
    print("开始处理B")
    time.sleep(2)
    print("结束处理B")


def main():
    reqA()
    reqB()


if __name__ == "__main__":
    main()