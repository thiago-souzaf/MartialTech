import math

from cvzone.PoseModule import PoseDetector
import cv2

def printCruzado(p1, p2, p3, img=None, color=(255, 0, 255), scale=5, angle2=0):
    """
    Finds angle between three points.

    :param p1: Point1 - (x1,y1)
    :param p2: Point2 - (x2,y2)
    :param p3: Point3 - (x3,y3)
    :param img: Image to draw output on. If no image input output img is None
    :return:
    """

    # Get the landmarks
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Calculate the Angle
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                         math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360

    # Draw
    if img is not None:
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), max(1, scale // 5))
        cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), max(1, scale // 5))
        cv2.circle(img, (x1, y1), scale, color, cv2.FILLED)
        cv2.circle(img, (x1, y1), scale + 5, color, max(1, scale // 5))
        cv2.circle(img, (x2, y2), scale, color, cv2.FILLED)
        cv2.circle(img, (x2, y2), scale + 5, color, max(1, scale // 5))
        cv2.circle(img, (x3, y3), scale, color, cv2.FILLED)
        cv2.circle(img, (x3, y3), scale + 5, color, max(1, scale // 5))
        cv2.putText(img, 'SOCO' + str(angle2), (x2 - 50, y2 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, color, max(1, scale // 5))
    return img



def positionXMenor(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 < x2:
        return True
    else: return False

def positionXMaior(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 > x2:
        return True
    else: return False

def bracoEsquerdoladoEsq(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 < x2:
        return True
    else: return False

def bracoDireitoLadoDir(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 < x2:
        return True
    else: return False

def MesmaAltura(p1, p2, offset=100):
    x1, y1 = p1
    x2, y2 = p2

    if y1 - offset < y2 < y1 + offset:
        return True
    else: return False

def absoluteDistanceXY(p1, p2, mindist=40):
    x1, y1 = p1
    x2, y2 = p2
    distx = abs(x2 - x1)
    disty = abs(y2 - y1)
    if distx + disty > mindist:
        return True
    else: return False

def ehsoco(img, lmList, detector):
    ehsim = False
        
    angle = 0

    verifySocoDir = False
    verifySocoEsq = False
    isAngleArmHipDir = False
    isAngleArmHipEsq = False

    p11 = lmList[11][0:2]
    p13 = lmList[13][0:2]

    p12 = lmList[12][0:2]
    p14 = lmList[14][0:2]

    p15 = lmList[15][0:2]
    p16 = lmList[16][0:2]
    
    # Calculate the angle between landmarks 11, 13, and 15 and draw it on the image
    angle, img = detector.findAngle(lmList[11][0:2],
                                    lmList[13][0:2],
                                    lmList[15][0:2],
                                    img=img,
                                    color=(0, 0, 255),
                                    scale=0)
    angleArmHipDir, img = detector.findAngle(lmList[23][0:2],
                                            lmList[11][0:2],
                                            lmList[13][0:2],
                                            img=img,
                                            color=(0, 0, 255),
                                            scale=0)
    

    angle2, img = detector.findAngle(lmList[12][0:2],
                                        lmList[14][0:2],
                                        lmList[16][0:2],
                                        img=img,
                                        color=(0, 0, 255),
                                        scale=0)
    angleArmHipEsq, img = detector.findAngle(lmList[24][0:2],
                                            lmList[12][0:2],
                                            lmList[14][0:2],
                                            img=img,
                                            color=(0, 0, 255),
                                            scale=0)
    
    #DIR

    if bracoDireitoLadoDir(p11, p13):
    # Check if the angle is close to 50 degrees with an offset of 10
        verifySocoDir = detector.angleCheck(myAngle=angle,
                                                targetAngle=170,
                                                offset=15)
        isAngleArmHipDir = detector.angleCheck(myAngle=angleArmHipDir,
                                        targetAngle=280,
                                        offset=20)
        if positionXMenor(p15, p16):
            isAngleArmHipDir = False
        
    else:
        verifySocoDir = detector.angleCheck(myAngle=angle,
                                            targetAngle=190,
                                            offset=15)
        isAngleArmHipDir = detector.angleCheck(myAngle=angleArmHipDir,
                                        targetAngle=100,
                                        offset=20)
        if positionXMaior(p15, p16):
            isAngleArmHipDir = False

    if bracoEsquerdoladoEsq(p14, p12):
    # Check if the angle is close to 50 degrees with an offset of 10
        verifySocoEsq = detector.angleCheck(myAngle=angle2,
                                                targetAngle=190,
                                                offset=15)
        isAngleArmHipEsq = detector.angleCheck(myAngle=angleArmHipEsq,
                                        targetAngle=100,
                                        offset=20)
        if positionXMenor(p15, p16):
            isAngleArmHipEsq = False
    else:
        verifySocoEsq = detector.angleCheck(myAngle=angle2,
                                            targetAngle=170,
                                            offset=15)
        isAngleArmHipEsq = detector.angleCheck(myAngle=angleArmHipEsq,
                                        targetAngle=280,
                                        offset=20)
        if positionXMaior(p15, p16):
            isAngleArmHipEsq = False
        
    if isAngleArmHipDir == False and MesmaAltura(p11, p13):
        isAngleArmHipDir = True
    if isAngleArmHipEsq == False and MesmaAltura(p14, p12):
        isAngleArmHipEsq = True

    
    # Print the result of the angle check
    if verifySocoDir and isAngleArmHipDir and absoluteDistanceXY(p13, p15):
        ehsim = True
        img = detector.printPunch(lmList[11][0:2],
                                    lmList[13][0:2],
                                    lmList[15][0:2],
                                    img=img,
                                    color=(0, 0, 255),
                                    scale=10, angle2=angle)
    if verifySocoEsq and isAngleArmHipEsq and absoluteDistanceXY(p14, p16):
        ehsim = True
        img = detector.printPunch(lmList[12][0:2],
                                    lmList[14][0:2],
                                    lmList[16][0:2],
                                    img=img,
                                    color=(0, 0, 255),
                                    scale=10, angle2=angle2)
        
    return img, ehsim
