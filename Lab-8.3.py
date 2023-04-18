import time
import cv2

def video_processing():
    # поставил ссылку на видео
    cap = cv2.VideoCapture('sample.mp4')
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                print(a, b)
                
                # Вывод координат метки в правом верхнем углу
                cv2.putText(frame, f"X:{a} Y:{b}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()

video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()