# -*- coding: utf-8 -*-
# print "wowowo"
# print "hello world"
# print "hello Again"
# print "I like typing this."
# print "This is fun"


# import sys
# from time import sleep
#
# for i in range(1,5):
#     print "\rHello, Gay! ",  i,
#     sys.stdout.flush()
#     sleep(1)
#

import sys, time

def interface_show(**kwargs):
    lineTmpla = ' '*5 + kwargs['title'] + kwargs['artist'] + kwargs['rate'] + " %-3s"
    print time_remain(lineTmpla, kwargs['minutes']),

def time_remain(lineTmpla, mins):
    count = 0
    while (count < mins):
        count += 1
        n = mins - count
        time.sleep(1)
        sys.stdout.write("\r" + lineTmpla %(n),)
        sys.stdout.flush()
        if not n:
            return 'completed'

interface_show(title="倒计时demo", artist="哗嚓啊", rate="揍起来", minutes=5)