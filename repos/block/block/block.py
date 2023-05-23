from itertools import filterfalse
import cv2
import numpy as np

class Ball:
    def __init__(self,x,y,w,h):
        self.r = 10
        self.c=(255,255,255)
        self.x=int(w/2)
        self.y=int(h/2)
        self.ofset_x=5
        self.ofset_y=5
        self.w=w
        self.h=h
    def pos(self):
        return (self.x,self.y)
    def top(self):
        return self.y - self.r
    def left(self):
        return self.x - self.r
    def bottom(self):
        return self.y + self.r
    def right(self):
        return self.x + self.r

    def update(self):
        self.x+=self.ofset_x
        self.y+=self.ofset_y
        if  self.left() <= 0 or self.w <=self.right():
            self.ofset_x*=-1
        if self.top() <= 0 or self.h <=self.bottom():
            self.ofset_y*=-1
    def draw(self,f):
        cv2.circle(f,self.pos(),10,(255,255,255),-1,cv2.LINE_AA)
    def end(self,f):
        is_end = False
        if self.y >= 470:
            is_end = True
        return is_end
    def collision(self,block):
        is_hit = False
        intersect_x = block.x <=self.right() and self.left() < block.x+block.w
        intersect_y = block.y <=self.bottom() and self.top() < block.y+block.h
        if intersect_y:
            if(self.ofset_x>0 and self.left()<=block.x <=self.right()) or (self.ofset_x < 0 and self.left()<=block.x + block.w <= self.right()):
                self.ofset_x *=-1
                is_hit = True
        if intersect_x:
            if(self.ofset_y>0 and self.top()<=block.y <=self.bottom()) or (self.ofset_y < 0 and self.top()<=block.y + block.h <= self.bottom()):
                self.ofset_y *=-1
                is_hit = True
        return is_hit

class Block:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c=(0,255,0)
    def draw(self,f):
         cv2.rectangle(f,(self.x,self.y),(self.x+self.w,self.y+self.h),self.c,-1)


class Paddle(Block):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        self.c = (255,0,0)
    def update(self,x,w):
        self.x = x-int(self.w/2)



m=[0,0]
def onMouse(event,x,y,flags,params):
    global m
    if event ==cv2.EVENT_MOUSEMOVE:
        m=[x,y]

def main():
    global m
    cv2.namedWindow('f',cv2.WINDOW_GUI_NORMAL)
    cv2.setMouseCallback('f',onMouse)
    f=np.zeros((480,910,3),np.uint8)
    b=f.copy()
    h,w=f.shape[:2]
    print(h,w)
    
    ball_list=[]
    ball_list.append(Ball(int(w/2),int(h/2),w,h))
    block_list =[]
    #block
    block_offset =5
    block_w=40
    block_h=15
    for i in range(20):
        for j in range(6):
            block_x=block_offset+(block_w+block_offset)*i
            block_y=block_offset+(block_h+block_offset)*j
            block_list.append(Block(block_x,block_y,block_w,block_h))
    paddle=Paddle(0,h-30,100,20)

    while True:
        
        f=b.copy()
        for ball in ball_list:
            ball.update()
            for block in reversed(block_list):
                if ball.collision(block):
                    block_list.remove(block)
            if len(ball_list) != 0:
                if ball.end(ball):
                    ball_list.remove(ball)
            ball.collision(paddle)
            ball.draw(f)
        if len(ball_list) == 0:
            cv2.putText(f,text='GAME OVER press Q key',org=(100,300),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(255,255,255),thickness=2,lineType=cv2.LINE_4)

        for block in block_list:
            block.draw(f)
        
               
        #paddle
        paddle.update(m[0],w)
        paddle.draw(f)

        cv2.imshow('f',f)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
    cv2.destroyAllWindows()
main()


