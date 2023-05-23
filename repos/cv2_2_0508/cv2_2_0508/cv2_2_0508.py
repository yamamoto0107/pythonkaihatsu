#PNG orjpeg�摜���ꖇ�p�ӁB
import cv2

def Pic(path):
    #path = "./cv2img.jpg"#���΃p�X
    img = cv2.imread(path)
    cv2.imshow('img',img)
    #()�̒��ɂ́A2�̕ϐ�:��ʂ̃^�C�g���Aimread�����摜���K�v
    cv2.waitKey(0)#�ҋ@���Ԃ��w��(�~���b�P��)�A0�̓{�^�����������܂�
    cv2.destroyAllWindows()

def Cv2resize(path):
    img = cv2.imread(path)
    re1 = cv2.resize(img,dsize=(480,640))#�c���̉摜��30����f�Ƀ��T�C�Y
    re2 = cv2.resize(img,dsize=None,fx=0.5,fy=0.5)#�䗦�Ń��T�C�Y
    cv2.imshow('img',re1)
    cv2.waitKey(0)#�ҋ@���Ԃ��w��(�~���b�P��)�A0�̓{�^�����������܂�
    cv2.imwrite('save.png',re1)#�摜�̕ۑ�(���O,cv2�摜)���O���������Ə㏑��
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

def Cv2rectangle(path):#rectangle�͋�`(�����`)�ň͂�
    img = cv2.imread(path)
    cv2.rectangle(img,
                  pt1 = (200,100),#����̍��W
                  pt2 = (300,200),#�E���̍��W
                  color = (255,0,0),#�F
                  thickness = 3,#���̑���,�}�C�i�X�̐������Ɠh��Ԃ�
                  lineType = cv2.LINE_4,#���̎��(4�A��)
                  shift = 0) #�����_�ȉ��̌���(�����Ȃ��Ă�OK) 
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Cv2gray(path,path2):#�F�̕ϊ����\����1�F����(�O���[�X�P�[����)
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Cv2cas(img,gray,path2)#�Q�Fimg��ǉ�����ƁA�J���[�Ɋ�F���̘g��������
    cv2.imshow('image',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def Cv2cas(img,gray,path2):#�J�X�P�[�h���ށA��F���B�Q�Fimg��ǉ�����ƁA�J���[�Ɋ�F���̘g��������
    cas = cv2.CascadeClassifier(path2)#���f���̓ǂݍ���
    faces = cas.detectMultiScale(gray)#�J�X�P�[�h���ފ�ɂ�镪��
    print(faces)
    for x,y,w,h in faces:
        cv2.rectangle(img,#�Q�Fgray����img�ɕς���ƃJ���[�ɘg��������B
                      pt1 = (x,y),#����̍��W
                      pt2 = (x+w,y+h),#�E���̍��W
                      color = (255,0,0),#�F
                      thickness = 3,#���̑���,�}�C�i�X�̐������Ɠh��Ԃ�
                      lineType = cv2.LINE_4,#���̎��(4�A��)
                      shift = 0) #�����_�ȉ��̌���(�����Ȃ��Ă�OK) 
    cv2.imshow('image',img)#�Q�Fgray����img�ɕς���ƃJ���[���\�������
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cam(path):
    cas = cv2.CascadeClassifier(path)#���f���̓ǂݍ���
    cap = cv2.VideoCapture(1)
    while True:
        _,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = cas.detectMultiScale(gray)#�J�X�P�[�h���ފ�ɂ�镪��
        for x,y,w,h in faces:
            cv2.rectangle(frame,#�Q�Fgray����img�ɕς���ƃJ���[�ɘg��������B
                      pt1 = (x,y),#����̍��W
                      pt2 = (x+w,y+h),#�E���̍��W
                      color = (255,0,0),#�F
                      thickness = 3,#���̑���,�}�C�i�X�̐������Ɠh��Ԃ�
                      lineType = cv2.LINE_4,#���̎��(4�A��)
                      shift = 0) #�����_�ȉ��̌���(�����Ȃ��Ă�OK) 
        cv2.imshow('image',frame)#�Q�Fgray����img�ɕς���ƃJ���[���\�������
        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    pic1 = "./cv2img.jpg"#���΃p�X
    pic2 = "./save.png"#���΃p�X
    #Pic(pic1)    #Cv2resize(pic1)    #Cv2text(pic2)    #Cv2rectangle(pic2)    #Cv2gray(pic2)
    path = "./haarcascade_frontalface_default.xml"
    #Cv2gray(pic2,path)
    cam(path)
