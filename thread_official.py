import threading
import datetime
import time

"""
一般方式
"""

def th_test_func():
    """测试1"""
    print("1")
    time.sleep(2)
    print(datetime.datetime.now())
    return str(datetime.datetime.now())


def th_test_funcb():
    """测试2"""
    print("2")
    time.sleep(1)
    print(datetime.datetime.now())
    return str(datetime.datetime.now())


if __name__ == '__main__':
    th_list = []
    th_list.append(threading.Thread(target=th_test_func))
    th_list.append(threading.Thread(target=th_test_funcb))

    #非阻塞时（不等待子线程执行完毕继续执行） 不需要 join()
    for i in th_list:
        i.start()
        # i.join() #阻塞 (等待子线程执行完毕后继续)
    print("执行完毕")
