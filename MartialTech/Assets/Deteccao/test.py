import Soco, Cotovelada, Cruzado, InicialPosition
from cvzone.PoseModule import PoseDetector
import cv2
from connection import UnityServer
import threading

def iniciar_servidor_golpes(host, port):
    global golpes_server
    golpes_server = UnityServer(host, port)
    golpes_server.start()

def iniciar_servidor_imagens(host, port):
    global imagens_server
    imagens_server = UnityServer(host, port)
    imagens_server.start()

host = "127.0.0.1"
# Threads para iniciar os servidores
thread1 = threading.Thread(target=lambda: iniciar_servidor_golpes(host, 25002))
thread2 = threading.Thread(target=lambda: iniciar_servidor_imagens(host, 25003))

# Inicia as threads
thread1.start()
thread2.start()

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

    imgatual = img.copy()
    _, img_encoded = cv2.imencode(".jpg", img)
    try:
        imagens_server.send_image(img_encoded)
    except Exception as e:
        print("Falha ao enviar: ", e)
        imagens_server.disconnect()
        golpes_server.disconnect()

    # Check if any body landmarks are detected
    if lmList:
        # Get the center of the bounding box around the body
        center = bboxInfo["center"]

        # Draw a circle at the center of the bounding box
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        imgatual, ehsocoesq, ehsocodir = Soco.ehsoco(img, lmList, detector)

        imgatual, ehcotoveladaesq, ehcotoveladadir = Cotovelada.ehcotovelada(img, lmList, detector)

        imgatual, ehcruzadoesq, ehcruzadodir = Cruzado.ehcruzado(img, lmList, detector)

        imgatual, ehposinicialesq, ehposinicialdir = InicialPosition.ehposinicial(img, lmList, detector)


        if ( ehsocoesq or ehsocodir ) and atualestado == 'estliberado':
            print("SOCO DADO")
            golpes_server.send_message("soco")
            atualestado = 'estsoco'
        if ( ehcotoveladaesq or ehcotoveladadir ) and atualestado == 'estliberado':
            print("COTOVELADA DADA")
            golpes_server.send_message("cotovelada")
            atualestado = 'estcotovelada'
        if ( ehcruzadoesq or ehcruzadodir ) and atualestado == 'estliberado':
            print("CRUZADO DADO")
            atualestado = 'estcruzado'
            golpes_server.send_message("cruzado")
        if ( ehposinicialesq and ehposinicialdir ) and atualestado != 'estliberado':
            print("ESTADO inicial")
            atualestado = 'estliberado'

        if ( ehposinicialdir and ehposinicialesq ) and atualestado != 'estliberado':
            print("ESTADO inicial")
            atualestado = 'estliberado'
        
    # Display the frame in a window
    cv2.imshow("Image", imgatual)

    # Wait for 20 millisecond between each frame
    cv2.waitKey(20)