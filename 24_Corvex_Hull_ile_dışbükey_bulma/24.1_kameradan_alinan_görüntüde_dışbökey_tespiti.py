import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Görüntü gri tonlamaya çevir
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Eşikleme işlemi
    ret, thresh = cv2.threshold(gri, 75, 200, cv2.THRESH_BINARY)

    # Konturları bul
    contur, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Konveks kılıfları hesapla
    h = []
    for i in range(len(contur)):
        h.append(cv2.convexHull(contur[i], False))

    # Yeni görüntü oluştur
    z = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

    # Kontur ve konveks kılıfları çiz
    for i in range(len(contur)):
        cv2.drawContours(z, contur, i, (255, 0, 0), 3, 8)
        cv2.drawContours(z, h, i, (0, 255, 0), 1, 8)

    # Sonuç görüntüsünü göster
    cv2.imshow("Canlı Kontur ve Konveks Kılıf", z)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()