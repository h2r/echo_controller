#!/usr/bin/env python

# imports
import rospy
from std_msgs.msg import String

#global variables
global rightPub
global leftPub
global echoPub
cur_arm = ''
# functions

def echo_callback(data):
    global cur_arm

    speech = data.data
    print speech
    msg = ''

    # determine robot arm
    if 'right' in speech:
        cur_arm = 'right'
    if 'left' in speech:
        cur_arm = 'left'

    # scanning command
    if 'scan' in speech or 'map' in speech:
        msg = 'clearMapForPatrol clearBlueBoxMemories goHome waitUntilAtCurrentPosition tableMapBestClass'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
        else:
            msg = 'which arm?'
            echoPub.publish(msg)

    # picking command
    if 'pick' in speech:
        msg = 'setPlaceModeToHand deliverTargetObject'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
        else:
            msg = 'which arm?'
            echoPub.publish(msg)
    if 'dribble' in speech:
        msg = 'tableInfiniteDribbleBest'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
            print ""
    if 'open' in speech:
        msg = 'openGripper'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
        else:
            msg = 'which arm?'
            echoPub.publish(msg)

    if 'close' in speech:
        msg = 'closeGripper'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
        else:
            msg = 'which arm?'
            echoPub.publish(msg)

    if 'crane' in speech or 'enter' in speech or 'idle' in speech:
        msg = 'idler'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
        else:
            msg = 'which arm?'
            echoPub.publish(msg)
    if 'sad' in speech:
        rightPub.publish('sadFace');
    if 'happy' in speech:
        rightPub.publish('happyFace');
    if 'neutral' in speech:
        rightPub.publish('neutralFace');
    if 'home' in speech:
        msg = 'goHome'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
    if 'clear' in speech or 'stacks' in speech:
        msg = 'clearStacks'
        if cur_arm == 'right':
            rightPub.publish(msg)
        elif cur_arm == 'left':
            leftPub.publish(msg)
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
