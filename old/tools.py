# should probably credit this to robot apocalypse committee
import math
import cv2

def get_centroid_and_max_contour(boolean_image, *args):

    contours, hierarchy = cv2.findContours(boolean_image.copy(), *args)
    if contours:
        # If there are countours (i.e. a line) then find the largest one (the most likely to be your line)
        # Also draws lines on the image so it can be seen by humans (not NEEDED, but good for debugging purposes)

        max_contour = max(contours, key=cv2.contourArea)
        moment = cv2.moments(max_contour)
        if moment['m00'] == 0:
            return (False, False, False, False)
        center_x = int(moment['m10']/moment['m00'])
        center_y = int(moment['m01']/moment['m00'])

        return center_x, center_y, max_contour, contours
    
    else:
        return (False, False, False, False)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    '''
        Maps a value in range x1, y1 to a value in range x2, y2
        '''
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

# this actually isn't stolen :D

def rotateCoords(origin, point, angle):
    angle = math.radians(angle)
    ox,oy = origin
    px,py = point
    qx = ox + math.cos(angle) * (px-ox) - math.sin(angle) * (py-oy)
    qy = oy + math.sin(angle) * (px-ox) + math.cos(angle) * (py-oy)
    return qx,qy