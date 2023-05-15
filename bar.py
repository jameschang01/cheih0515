import cv2
circleRadius=1#半徑 

def update(x):
    print(x)
    global circleRadius#明確的告訴此func這是外面的變數 非隨意設定的
    circleRadius = x
px=1
py=2#設定x和y的參數
def update1(x):
    print(x)
    global px
    px = x 
def update3(x):
    print(x)
    global py
    py = x
img = cv2.imread("lena.jpg")
cv2.namedWindow("win")
cv2.createTrackbar("bar","win",0,100,update)#附著在win裡面,把function當作變數放在func裡面
cv2.createTrackbar("x","win",0,100,update1)
cv2.createTrackbar("y","win",0,100,update3)
color = (255,0,0)
thickness = 2
while True:
    circleImg = img.copy()
    center=(px,py)#位置
    cv2.circle(circleImg,center,circleRadius,color,thickness)
    cv2.imshow("win",circleImg)
    x = cv2.waitKey(100)
    if x == 27:
        break