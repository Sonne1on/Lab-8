import time
import cv2

def video_processing():
    # загрузка изображения
    img = cv2.imread('fly64.png', cv2.IMREAD_UNCHANGED)

    # уменьшение размера изображения
    scale_percent = 30  # процент уменьшения
    width = int(img.shape[1])
    height = int(img.shape[0])
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

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
                
                # наложение изображения на кадр
                x_offset = a - (img.shape[1] // 2)
                y_offset = b - (img.shape[0] // 2)
                if x_offset >= 0 and y_offset >= 0:
                    frame[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = cv2.addWeighted(frame[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]], 0.4, img[:, :, 0:3], 0.6, 0)
                
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    cap.release()

video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()