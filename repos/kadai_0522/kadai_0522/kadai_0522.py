import cv2
path = "haarcascade_frontalface_default.xml"
cas = cv2.CascadeClassifier(path)#モデルの読み込み
cap = cv2.VideoCapture(1)#学生は1ではなく0
while True:
    ret,frame = cap.read()
    #print("ret,",ret)
    #print("frame,",frame[0])
    print("frameの型は、",type(frame),"frameの長さは",frame.size)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#青、緑、赤。=>白黒。
    faces = cas.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6,minSize=(30,30))
    #scaleFactor:画像スケールにおける縮小量。大きいほど誤検知が多く、小さいほど未検出が多くなる
    #minNeighbors:信頼性。重複する箇所の信頼性の高さを設定する(閾値)。
    #　　　　　　 値が大きくなるにつれて信頼性が上がるが、顔を見逃しやすくなる。
    #minSize:顔の最小サイズ。
    #print(faces)#[[x,y,w,h],[x,y,w,h],…]
    for x,y,w,h in faces:
        face = frame[y-10:y+h+10,x-10:x+w+10]
        """
        cv2.rectangle(frame,
                     pt1 = (x,y),
                     pt2 = (x+w,y+h),
                     color=(255,0,0),
                     thickness = 3,
                     lineType = cv2.LINE_4,
                     shift = 0)
        """
    try:
        cv2.imshow("face",face)
    except Exception as e:
        cv2.imshow("frame",frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("frame.jpg",frame)
        break
cap.release()
cv2.destroyAllWindows()