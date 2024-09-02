import cv2
import numpy as np

# Video dosyasını veya kamerayı açma
cap = cv2.VideoCapture('cizgi.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Video bitti veya okunamadı.")
        break

    # Görüntüyü HSV renk uzayına çevirme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Sarı renk için HSV aralığını tanımlama
    alt_sari = np.array([18, 94, 140], dtype=np.uint8)
    ust_sari = np.array([48, 255, 255], dtype=np.uint8)

    # Sarı rengi maskeleme
    mask = cv2.inRange(hsv, alt_sari, ust_sari)

    # Maskelenmiş görüntüyü gri tonlamaya çevirme
    gray = cv2.bitwise_and(frame, frame, mask=mask)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

    # Gürültüyü azaltmak için Gaussian Blur uygulama
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Kenar tespiti için Canny algoritmasını kullanma
    edges = cv2.Canny(blur, 50, 150)

    # Hough Çizgi Dönüşümünü uygulama
    lines = cv2.HoughLinesP(edges,
                            rho=1,
                            theta=np.pi / 180,
                            threshold=100,
                            minLineLength=100,
                            maxLineGap=10)

    # Tespit edilen çizgileri orijinal frame üzerinde çizme
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame,(x1, y1),(x2, y2),(0, 255, 0),5)

    # Sonucu gösterme
    cv2.imshow('Yol Cizgisi Tesbiti', frame)

    # 'q' tuşuna basıldığında döngüyü sonlandırma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
