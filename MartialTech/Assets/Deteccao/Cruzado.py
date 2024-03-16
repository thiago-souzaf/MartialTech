import math

from cvzone.PoseModule import PoseDetector
import cv2

def printCruzado(p1, p2, p3, img=None, color=(255, 0, 255), scale=5):
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
        cv2.putText(img, 'CRUZADO', (x2 - 50, y2 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, color, max(1, scale // 5))
    return img

def angleMinorCheck(myAngle, targetAngle, offset=5):
    return myAngle < targetAngle + offset

def angleMajorCheck(myAngle, targetAngle, offset=5):
    return targetAngle - offset < myAngle

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

def distanceXaxis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dist = abs(x2 - x1)

    a = ((x2 - x1)**2) + ((y2 - y1)**2)
    b = math.sqrt(a)
    b2 = b/2
    
    if dist < b2:
        return True
    else:
        return False
    
def distanceXMajor(p1, p2, p3, offset):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    dist = abs(x2 - x1)

    dist2 = abs(x3-x1)
    
    
    if dist2-offset > dist:
        return True
    else:
        return False
    
def positionYMaior(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if y1 > y2:
        return True
    else: return False
    
def absoluteDistanceXY(p1, p2, mindist=100):
    x1, y1 = p1
    x2, y2 = p2
    distx = abs(x2 - x1)
    disty = abs(y2 - y1)
    if distx + disty < mindist:
        return True
    else: return False

def distanciatotal(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a = ((x2 - x1)**2) + ((y2 - y1)**2)
    b = math.sqrt(a)
    return b

def ehcruzado(img, lmList, detector):
    ehsimdir = False
    ehsimesq = False
    verifyCotoveloDir = False
    verifyCotoveloEsq = False

    isAngleArmHipDir = False
    isAngleArmHipEsq = False

    p11 = lmList[11][0:2]
    p13 = lmList[13][0:2]

    p12 = lmList[12][0:2]
    p14 = lmList[14][0:2]

    p15 = lmList[15][0:2]
    p16 = lmList[16][0:2]

    offsetEsq = 100
    offsetDir = 100

    # Calculate the angle between landmarks 11, 13, and 15 and draw it on the image
    #DIR
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
    

    
    #ESQ
    angle1, img = detector.findAngle(lmList[12][0:2],
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
    
    #print(angle)

    # checa o lado dos braços
    if angle > 180:
        angle = 360-angle
    if angle1 > 180:
        angle1 = 360-angle1
    
    angletarget=90
    verifyCotoveloDir = detector.angleCheck(myAngle=angle,
                                            targetAngle=angletarget,
                                            offset=50)
    if angleArmHipDir> 180:
        angleArmHipDir = 360-angleArmHipDir
    isAngleArmHipDir = detector.angleCheck(myAngle=angleArmHipDir,
                                    targetAngle=90,
                                    offset=20)
    
        # PARA ELE PODER CONSIDERAR A POSIÇÃO DE BASE



    verifyCotoveloEsq = detector.angleCheck(myAngle=angle1,
                                        targetAngle=90,
                                        offset=50)
    if angleArmHipEsq> 180:
        angleArmHipEsq = 360-angleArmHipEsq
    isAngleArmHipEsq = detector.angleCheck(myAngle=angleArmHipEsq,
                                    targetAngle=90,
                                    offset=20)
        
    

    
    '''if isAngleArmHipDir == False and MesmaAltura(p11, p13):
        isAngleArmHipDir = True
    if isAngleArmHipEsq == False and MesmaAltura(p14, p12):
        isAngleArmHipEsq = True
    
    if distanciatotal(p11, p15) > distanciatotal(p13, p15):
        verifyCotoveloDir = False

    if distanciatotal(p16, p12) > distanciatotal(p16, p14):
        verifyCotoveloEsq = False'''

    '''isAngleArmHip = detector.angleCheck(myAngle=angleArmHip,
                                        targetAngle=90,
                                        offset=15)'''
    # Print the result of the angle check
    if verifyCotoveloDir and isAngleArmHipDir:
        if  absoluteDistanceXY(p13, p15):
            ehsimdir = True
            img = printCruzado(lmList[11][0:2],
                                        lmList[13][0:2],
                                        lmList[15][0:2],
                                        img=img,
                                        color=(0, 0, 255),
                                        scale=10)
            
    if verifyCotoveloEsq and isAngleArmHipEsq:
        if  absoluteDistanceXY(p14, p16):
            ehsimesq = True
            img = printCruzado(lmList[12][0:2],
                                        lmList[14][0:2],
                                        lmList[16][0:2],
                                        img=img,
                                        color=(0, 0, 255),
                                        scale=10)
            
    return img, ehsimesq, ehsimdir
