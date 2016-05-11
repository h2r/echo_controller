#!/usr/bin/env python

# imports
import rospy
from std_msgs.msg import String

#global variables
global rightPub
global leftPub
global echoPub

# functions

def echo_callback(data):
    speech = data.data
    print speech
    msg = ''
    if 'scan' in speech or 'map' in speech:
        msg = 'clearBlueBoxMemories clearMapForPatrol mappingPatrol'
        if 'right' in speech:
            rightPub.publish(msg)
        if 'left' in speech:
            leftPub.publish(msg)
        else:
            msg = 'which arm?'
            echoPub.publish(msg)
    
    print msg

def echo_listener():
    rospy.Subscriber('/speech_recognition', String, echo_callback)
    rospy.spin()

def main():
    global rightPub
    global leftPub
    global echoPub
    rospy.init_node('echo_controller')

    rightPub = rospy.Publisher('/ein/right/forth_commands', String, queue_size = 0)
    leftPub = rospy.Publisher('/ein/left/forth_commands', String, queue_size = 0)
    echoPub = rospy.Publisher('/echo_speech', String, queue_size = 0)
    rospy.sleep(1)
    
    print 'Listening'
    echo_listener()

if __name__ == "__main__":
    main()
