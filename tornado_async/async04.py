import threading
import time


# 耗时操作
def longIo():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    yield "shixintai is cool"


def getCoroutine(func):
    def wrapper(*args, **kwargs):
        # reqA的生成器
        gen1 = func()
        # longIo的生成器
        gen2 = next(gen1)
        def run(g):
            res = next(g)
            try:
                gen1.send(res)
            except StopIteration as e:
                pass
        threading.Thread(target=run, args=(gen2,)).start()
    return wrapper


@getCoroutine
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
    # global gen
    # gen = reqA() # 生成一个生成器
    # next(gen) # 执行reqA
    reqA()

    reqB()


if __name__ == "__main__":
    main()