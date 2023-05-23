#PNG orjpeg画像を一枚用意。
import cv2

def Pic(path):
    #path = "./cv2img.jpg"#相対パス
    img = cv2.imread(path)
    cv2.imshow('img',img)
    #()の中には、2つの変数:画面のタイトル、imreadした画像が必要
    cv2.waitKey(0)#待機時間を指定(ミリ秒単位)、0はボタンが押されるまで
    cv2.destroyAllWindows()

def Cv2resize(path):
    img = cv2.imread(path)
    re1 = cv2.resize(img,dsize=(480,640))#縦長の画像を30万画素にリサイズ
    re2 = cv2.resize(img,dsize=None,fx=0.5,fy=0.5)#比率でリサイズ
    cv2.imshow('img',re1)
    cv2.waitKey(0)#待機時間を指定(ミリ秒単位)、0はボタンが押されるまで
    cv2.imwrite('save.png',re1)#画像の保存(名前,cv2画像)名前が同じだと上書き
    cv2.imshow('img',re2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Cv2text(path):
    img = cv2.imread(path)
    cv2.putText(img,
                "Hello Python",
                org = (50,100),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.5,
                color = (0,255,0),
                thickness = 2,
                lineType = cv2.LINE_AA)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Cv2rectangle(path):#rectangleは矩形(長方形)で囲む
    img = cv2.imread(path)
    cv2.rectangle(img,
                  pt1 = (200,100),#左上の座標
                  pt2 = (300,200),#右下の座標
                  color = (255,0,0),#色
                  thickness = 3,#線の太さ,マイナスの数字だと塗りつぶし
                  lineType = cv2.LINE_4,#線の種類(4連結)
                  shift = 0) #小数点以下の桁数(書かなくてもOK) 
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Cv2gray(path,path2):#色の変換が可能その1：白黒(グレースケール化)
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Cv2cas(img,gray,path2)#２：imgを追加すると、カラーに顔認識の枠が書ける
    cv2.imshow('image',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def Cv2cas(img,gray,path2):#カスケード分類、顔認識。２：imgを追加すると、カラーに顔認識の枠が書ける
    cas = cv2.CascadeClassifier(path2)#モデルの読み込み
    faces = cas.detectMultiScale(gray)#カスケード分類器による分類
    print(faces)
    for x,y,w,h in faces:
        cv2.rectangle(img,#２：grayからimgに変えるとカラーに枠が書ける。
                      pt1 = (x,y),#左上の座標
                      pt2 = (x+w,y+h),#右下の座標
                      color = (255,0,0),#色
                      thickness = 3,#線の太さ,マイナスの数字だと塗りつぶし
                      lineType = cv2.LINE_4,#線の種類(4連結)
                      shift = 0) #小数点以下の桁数(書かなくてもOK) 
    cv2.imshow('image',img)#２：grayからimgに変えるとカラーが表示される
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cam(path):
    cas = cv2.CascadeClassifier(path)#モデルの読み込み
    cap = cv2.VideoCapture(1)
    while True:
        _,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = cas.detectMultiScale(gray)#カスケード分類器による分類
        for x,y,w,h in faces:
            cv2.rectangle(frame,#２：grayからimgに変えるとカラーに枠が書ける。
                      pt1 = (x,y),#左上の座標
                      pt2 = (x+w,y+h),#右下の座標
                      color = (255,0,0),#色
                      thickness = 3,#線の太さ,マイナスの数字だと塗りつぶし
                      lineType = cv2.LINE_4,#線の種類(4連結)
                      shift = 0) #小数点以下の桁数(書かなくてもOK) 
        cv2.imshow('image',frame)#２：grayからimgに変えるとカラーが表示される
        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    pic1 = "./cv2img.jpg"#相対パス
    pic2 = "./save.png"#相対パス
    #Pic(pic1)    #Cv2resize(pic1)    #Cv2text(pic2)    #Cv2rectangle(pic2)    #Cv2gray(pic2)
    path = "./haarcascade_frontalface_default.xml"
    #Cv2gray(pic2,path)
    cam(path)
