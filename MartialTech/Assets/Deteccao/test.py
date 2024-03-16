import math

import Soco, Cotovelada, Cruzado, InicialPosition
from cvzone.PoseModule import PoseDetector
import cv2
from connection import UnityServer

unity_server = UnityServer("127.0.0.1", 25002)
unity_server.start()
cap = cv2.VideoCapture(0)

detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)


detector.printPunch = Soco.printPunch

atualestado = "Inicial"
maoatual = 'nenhuma'


# Loop to continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    success, img = cap.read()

    # Find the human pose in the frame
    img = detector.findPose(img)

    # Find the landmarks, bounding box, and center of the body in the frame
    # Set draw=True to draw the landmarks and bounding box on the image
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=True)

    # Check if any body landmarks are detected
    if lmList:
        # Get the center of the bounding box around the body
        center = bboxInfo["center"]

        # Draw a circle at the center of the bounding box
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        imgatual = img.copy()

        imgatual, ehsocoesq, ehsocodir = Soco.ehsoco(img, lmList, detector)

        imgatual, ehcotoveladaesq, ehcotoveladadir = Cotovelada.ehcotovelada(img, lmList, detector)

        imgatual, ehcruzadoesq, ehcruzadodir = Cruzado.ehcruzado(img, lmList, detector)

        imgatual, ehposinicialesq, ehposinicialdir = InicialPosition.ehposinicial(img, lmList, detector)


        if ( ehsocoesq or ehsocodir ) and atualestado == 'estliberado':
            print("SOCO DADO")
            unity_server.send_message("soco")
            atualestado = 'estsoco'
        if ( ehcotoveladaesq or ehcotoveladadir ) and atualestado == 'estliberado':
            print("COTOVELADA DADA")
            unity_server.send_message("cotovelada")
            atualestado = 'estcotovelada'
        if ( ehcruzadoesq or ehcruzadodir ) and atualestado == 'estliberado':
            print("CRUZADO DADO")
            atualestado = 'estcruzado'
            unity_server.send_message("cruzado")
        if ( ehposinicialesq and ehposinicialdir ) and atualestado != 'estliberado':
            print("ESTADO inicial")
            atualestado = 'estliberado'

        if ( ehposinicialdir and ehposinicialesq ) and atualestado != 'estliberado':
            print("ESTADO inicial")
            atualestado = 'estliberado'
        
    # Display the frame in a window
    # cv2.imshow("Image", imgatual)

    # Wait for 1 millisecond between each frame
    cv2.waitKey(1)