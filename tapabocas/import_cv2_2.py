import cv2
from ultralytics import YOLO

# Cargar el modelo YOLOv8x preentrenado
model = YOLO('yolo11m.pt')  # Asegúrate de que este archivo esté en tu carpeta

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
