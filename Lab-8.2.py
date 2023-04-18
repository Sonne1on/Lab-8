import cv2

# загрузка изображения метки
marker = cv2.imread('marker.png')

# создание детектора меток
detector = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# создание камеры для захвата видео
cap = cv2.VideoCapture(0)

while True:
    # захват изображения с камеры
    ret, frame = cap.read()
    if not ret:
        break

    # конвертирование в чёрно-белое изображение
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # поиск меток на изображении
    corners, ids, rejected = cv2.aruco.detectMarkers(gray, detector, parameters=parameters)

    if ids is not None:
        # если метки обнаружены, нарисуем их на изображении
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # ищем нужную метку
        for i in range(len(ids)):
            if ids[i] == 23:  # номер метки, которую мы ищем
                # вычисляем координаты метки
                c = corners[i][0]
                x = int((c[0][0] + c[1][0] + c[2][0] + c[3][0]) / 4)
                y = int((c[0][1] + c[1][1] + c[2][1] + c[3][1]) / 4) - 30

                # выводим координаты метки на изображение
                cv2.putText(frame, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # показываем обработанное изображение
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
