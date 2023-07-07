#!/usr/bin/env python
#!/usr/bin/env python

import rospy
import sys
from lifter_service_assignment.srv import Lifter
from lifter_service_assignment.srv  import LifterRequest

def lifter_client(elevation):
    rospy.wait_for_service('elevator_lifter')
    try:
        elevator_lifter = rospy.ServiceProxy('elevator_lifter', Lifter)
        request = LifterRequest()
        request.elevation = elevation
        server_response = elevator_lifter(elevation)
        return server_response.result
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "Usage: %s [elevation]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        elevation = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting the elevator to lift %s elevation" % elevation)
    server_response = lifter_client(elevation)
    print(server_response)
