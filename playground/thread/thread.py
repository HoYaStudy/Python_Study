import threading
import logging
import time


# Thread Example 1 -----------------------------------------------------------#
# def threadRun():
# 	print('Thread id running')

# def threadRunMessage(msg):
#     print('Thread is running', msg)

# for i in range (1000):
#     t1 = threading.Thread(target=threadRun)
#     t2 = threading.Thread(target=threadRunMessage, args=('Service',))

#     t1.start()
#     t2.start()
#-----------------------------------------------------------------------------#

# Thread Example 2 -----------------------------------------------------------#
# class ThreadRun(threading.Thread):
#     def run(self):
#         print('Thread is running')

# for i in range(1000):
#     t = ThreadRun()
#     t.start()
#-----------------------------------------------------------------------------#

# Thread Example 3 -----------------------------------------------------------#
# logging.basicConfig( level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-8s) %(message)s',)

# def worker1():
#     logging.debug('Start')
#     time.sleep(0.5)
#     logging.debug('Finish')

# def worker2():
#     logging.debug('Start')
#     time.sleep(0.5)
#     logging.debug('Finish')

# t1 = threading.Thread(name='Service1', target=worker1)
# t2 = threading.Thread(name='Service2', target=worker2, daemon=True)
# t3 = threading.Thread(target=worker1, daemon=True)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# print('Is t3 alive?', t3.isAlive())
# t3.join()
# print('Is t1 alive?', t1.isAlive())
#-----------------------------------------------------------------------------#

# Thread Example 4 -----------------------------------------------------------#
# def threadRun():
#     print('===', time.ctime(), '===')
#     for i in range(1, 10001):
#         print('Thread is running -', i)
#     threading.Timer(2.5, threadRun).start()

# threadRun()
#-----------------------------------------------------------------------------#
