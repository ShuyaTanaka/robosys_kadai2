#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data*1

    if n > 200:
        n = message.data*2
    if n > 500:
        n = message.data*3
    if n > 900:
        n = message.data*4
    if n > 1500:
        n = message.data*5

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
    
