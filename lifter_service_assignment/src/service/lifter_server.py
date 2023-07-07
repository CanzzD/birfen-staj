#!/usr/bin/env python

import rospy
from lifter_service_assignment.srv  import Lifter
from lifter_service_assignment.srv import LifterResponse
from lifter_service_assignment.srv import LifterRequest

def elevator_lifter(request):
    elevation = request.elevation
    if elevation < 5:
        return LifterResponse("Yük Başarıyla Kaldırıldı")
    else:
        return LifterResponse("Yük Kaldırılamadı")

def lifter_server():
    rospy.init_node('lifter_server')
    service = rospy.Service('elevator_lifter', Lifter, elevator_lifter)
    rospy.spin()

if __name__ == "__main__":
    lifter_server()
