import cv2
import numpy as np

# Kamerayı başlat
cap = cv2.VideoCapture(0)


def shape_detect(contour):

    shape = "Tanımsız"
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

    if len(approx) == 3:
        shape = "UCGEN"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspectRatio = w / float(h)
        if 0.95 <= aspectRatio <= 1.05:
            shape = "KARE"
        else:
            shape = "DIKDORTGEN"
    elif len(approx) == 5:
        shape = "BESGEN"
    else:
        shape = "DAIRE"
    return shape


while True:
    # Kameradan bir kare al
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break

    # Görüntüyü gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gürültüyü azaltmak için bulanıklaştırma işlemi
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Eşikleme işlemi
    ret, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)

    # Konturları bul
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Küçük gürültüleri önlemek için minimum alan filtresi
            shape = shape_detect(contour)
            M = cv2.moments(contour)
            if M["m00"] > 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                cv2.putText(frame, shape, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Sonuç görüntüsünü göster
    cv2.imshow("Canlı Şekil Tespiti", frame)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
