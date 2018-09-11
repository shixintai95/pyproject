import threading
import time


gen = None

# 耗时操作
def longIo():
    def run():
        print("开始耗时操作")
        time.sleep(5)
        try:
            global gen
            gen.send("shixintai is cool")
        except StopIteration as e:
            pass
    threading.Thread(target=run).start()


def reqA():
    print("开始处理A")
    res = yield longIo()
    print("接收到longIo响应的数据为：", res)
    print("结束处理A")


def reqB():
    print("开始处理B")
    time.sleep(2)
    print("结束处理B")


def main():
    global gen
    gen = reqA() # 生成一个生成器
    next(gen) # 执行reqA

    reqB()


if __name__ == "__main__":
    main()