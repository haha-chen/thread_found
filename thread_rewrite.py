import threading
import time
"""

重写方式
"""

#多线程运行
class Thread_class(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        #接收线程执行结果
        self.result=''
        self.func = func


    #重写RUN创建线程
    def run(self):
        """
        fnuc() 需要执行的模块
        """
        #执行方法
        gpcResult=self.func()
        #记录返值
        self.result+=gpcResult

    #多线程结果返回
    def thread_result(self):
        #返回结果
        return self.result




if __name__ == '__main__':
    import datetime
    def th_test_func():
        """测试1"""
        print("1")
        time.sleep(0.5)
        print(datetime.datetime.now())
        return str(datetime.datetime.now())

    def th_test_funcb():
        """测试2"""
        print("2")
        time.sleep(1)
        print(datetime.datetime.now())
        return str(datetime.datetime.now())

    test_list = [] #生成多线程
    test_result = [] #接收返回值
    test_list.append(Thread_class(th_test_func))
    test_list.append(Thread_class(th_test_funcb))
    #计算线程数并执行
    for i in range(len(test_list)):
        test_list[i].start()

    for i in range(len(test_list)):
        #join堵塞等待字线程结束
        test_list[i].join()
        #返回结果
        test_result.append(test_list[i].thread_result())
    print("多线程结果",test_result)