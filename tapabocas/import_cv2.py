import cv2
from ultralytics import YOLO

# Cargar el modelo YOLOv11 preentrenado
model = YOLO('yolo11n.pt')  # Puedes cambiar a 'yolo11s.pt', 'yolo11m.pt', etc., según tus necesidades

# Iniciar la captura de video desde la cámara web
cap = cv2.VideoCapture(0)  # 0 es el índice de la cámara predeterminada

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar la detección de objetos
    results = model.predict(source=frame, show=True, conf=0.5)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
