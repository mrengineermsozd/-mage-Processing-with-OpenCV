import cv2

cap = cv2.VideoCapture("video.mp4")
trackers = ["BOOSTING", "MIL", "CSRT", "KCF", "TLD", "MEDIANFLOW", "MOSSE"]

# Kullanıcıya hangi takip algoritmasını seçmek istediğini sor
print("Takip algoritmalari:")
for i, tracker_name in enumerate(trackers):
    print(f"{i}: {tracker_name}")

while True:
    try:
        i = int(input("Lütfen bir takip algoritması seçin (0-6): "))
        if 0 <= i < len(trackers):
            break
        else:
            print("Lütfen geçerli bir sayı girin.")
    except ValueError:
        print("Geçersiz giriş, lütfen bir sayı girin.")

algoritma = trackers[i]
print(f"Seçilen algoritma: {algoritma}")


if algoritma == "BOOSTING":
    tracker = cv2.legacy.TrackerBOOSTING_create()
elif algoritma == "MIL":
    tracker = cv2.legacy.TrackerMIL_create()
elif algoritma == "CSRT":
    tracker = cv2.legacy.TrackerCSRT_create()
elif algoritma == "KCF":
    tracker = cv2.legacy.TrackerKCF_create()
elif algoritma == "TLD":
    tracker = cv2.legacy.TrackerTLD_create()
elif algoritma == "MEDIANFLOW":
    tracker = cv2.legacy.TrackerMedianFlow_create()
elif algoritma == "MOSSE":
    tracker = cv2.legacy.TrackerMOSSE_create()


ret, frame = cap.read()

if not ret:
    print("Video açılamadı")
    exit()

bbox = cv2.selectROI("Nesne Seç", frame, fromCenter=False, showCrosshair=True)
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Takip Basarisiz!", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.imshow("Takip", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
