import tkinter as tk
import cv2
import pymysql
from PIL import Image, ImageTk, ImageOps
import tensorflow as tf
import numpy as np
import math

def getCardnumber():
    try:
        db = pymysql.connect(host = "localhost", port = 3306, user = "root", passwd = "",charset="utf8", db = "card") # 建立Connection物件
        with db.cursor() as cursor:# 建立Cursor物件
            sql = "SELECT CID, name From card_book"
            cursor.execute(sql)
            result = cursor.fetchall()
            db.commit()#儲存變更
            return len(result)
    except Exception as ex:
        print(ex)
    finally:
        db.close()

def getOwncard():
    try:
        db = pymysql.connect(host = "localhost", port = 3306, user = "root", passwd = "",charset="utf8", db = "card") # 建立Connection物件
        with db.cursor() as cursor:# 建立Cursor物件
            sql = "SELECT * From card_book where own = %s"
            cursor.execute(sql, "1")
            result = cursor.fetchall()
            db.commit()#儲存變更
            return result
    except Exception as ex:
        print(ex)
    finally:
        db.close()

def writeBook(CID):
    try:
        db = pymysql.connect(host = "localhost", port = 3306, user = "root", passwd = "",charset="utf8", db = "card") # 建立Connection物件
        with db.cursor() as cursor:# 建立Cursor物件
            sql = "UPDATE card_book SET own = %s  where CID = %s"
            cursor.execute(sql,( "1", CID,))
            db.commit()#儲存變更
    except Exception as ex:
        print(ex)
    finally:
        db.close()

def loadImage(cards):
    imgs = list()
    for card in cards:
        text = "image/"+card[0]+".jpg"
        img = Image.open(text)
        photo = ImageTk.PhotoImage(img)
        imgs.append(photo)
    return imgs

def AI():
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
# Load the model
    model = tf.keras.models.load_model("keras_Model.h5", compile=False)
# Load the labels
    class_names = open("labels.txt", "r").readlines()
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
    image = Image.open("a.jpg").convert("RGB")
# resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
# turn the image into a numpy array
    image_array = np.asarray(image)
# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
# Load the image into the array
    data[0] = normalized_image_array
# Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
# Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)
    class_name = class_name[2:].replace('\n', "")
    return class_name

def w2(page, cardNumber, imgs, cards):
    frame1.destroy()
    frame2 = tk.Frame(window, bg = "#FFDCB9")
    frame3 = tk.Frame(window, bg = "#FFDCB9")
    frame4 = tk.Frame(window, bg = "#FFDCB9")
    frame2.place(relx = 0,relheight=1, relwidth=0.1)
    frame3.place(relx = 0.1,relheight=1, relwidth=0.8)
    frame4.place(relx = 0.9,relheight=1, relwidth=0.1)
    index = (page-1)*9

    c1 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c1.grid(row=0, column=0, padx=5, pady=5)
    if(index < len(imgs)):
        c1.create_image(0,0,anchor = 'nw', image = imgs[index])
        c1.bind("<Button-1>", lambda event:w3(event, cards[index], index, imgs))
    else :
        c1.create_image(0,0,anchor = 'nw', image = photo)
    #--------------------------------------------------------------
    c2 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c2.grid(row=0, column=1, padx=5, pady=5)
    if(index+1 < len(imgs)):
        c2.create_image(0,0,anchor = 'nw', image = imgs[index+1])
        c2.bind("<Button-1>", lambda event:w3(event, cards[index+1], index+1, imgs))
    else :
        c2.create_image(0,0,anchor = 'nw', image = photo)
    #--------------------------------------------------------------
    c3 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c3.grid(row=0, column=2, padx=5, pady=5)
    if(index+2 < len(imgs)):
        c3.create_image(0,0,anchor = 'nw', image = imgs[index+2])
        c3.bind("<Button-1>", lambda event:w3(event, cards[index+2], index+2, imgs))
    else :
        c3.create_image(0,0,anchor = 'nw', image = photo)
    #-------------------------------------------------------------
    c4 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c4.grid(row=1, column=0, padx=5, pady=5)
    if(index+3 < len(imgs)):
        c4.create_image(0,0,anchor = 'nw', image = imgs[index+3])
        c4.bind("<Button-1>", lambda event:w3(event, cards[index+3], index+3, imgs))
    else :
        c4.create_image(0,0,anchor = 'nw', image = photo)
    #-------------------------------------------------------------
    c5 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c5.grid(row=1, column=1, padx=5, pady=5)
    if(index+4 < len(imgs)):
        c5.create_image(0,0,anchor = 'nw', image = imgs[index+4])
        c5.bind("<Button-1>", lambda event:w3(event, cards[index+4], index+4, imgs))
    else :
        c5.create_image(0,0,anchor = 'nw', image = photo)
    #-------------------------------------------------------------
    c6 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c6.grid(row=1, column=2, padx=5, pady=5)
    if(index+5 < len(imgs)):
        c6.create_image(0,0,anchor = 'nw', image = imgs[index+5])
        c6.bind("<Button-1>", lambda event:w3(event, cards[index+5], index+5, imgs))
    else :
        c6.create_image(0,0,anchor = 'nw', image = photo)
    #-------------------------------------------------------------
    c7 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c7.grid(row=2, column=0, padx=5, pady=5)
    if(index+6 < len(imgs)):
        c7.create_image(0,0,anchor = 'nw', image = imgs[index+6])
        c7.bind("<Button-1>", lambda event:w3(event, cards[index+6], index+6, imgs))
    else :
        c7.create_image(0,0,anchor = 'nw', image = photo)
    #-------------------------------------------------------------
    c8 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c8.grid(row=2, column=1, padx=5, pady=5)
    if(index+7 < len(imgs)):
        c8.create_image(0,0,anchor = 'nw', image = imgs[index+7])
        c8.bind("<Button-1>", lambda event:w3(event, cards[index+7], index+7, imgs))
    else :
        c8.create_image(0,0,anchor = 'nw', image = photo)
    #-------------------------------------------------------------
    c9 = tk.Canvas(frame3, width = 168, height=245, bg= "#BEBEBE")
    c9.grid(row=2, column=2, padx=5, pady=5)
    if(index+8 < len(imgs)):
        c9.create_image(0,0,anchor = 'nw', image = imgs[index+8])
        c9.bind("<Button-1>", lambda event:w3(event, cards[index+8], index+8, imgs))
    else :
        c9.create_image(0,0,anchor = 'nw', image = photo)

    if page != 1:
        bUtton1 = tk.Button(frame2,text="上一頁",command= lambda:w2(page-1, cardNumber, imgs, cards))
        bUtton1.pack(side= tk.BOTTOM)
    if page != math.ceil(cardNumber/9):
        bUtton1 = tk.Button(frame4,text="下一頁", command= lambda:w2(page+1, cardNumber, imgs, cards))
        bUtton1.pack(side= tk.BOTTOM)

    bUtton1 = tk.Button(frame4,text="相機", command =useAI)
    bUtton1.pack()
    pageNumber = tk.Label(frame3, text = page, font=('Arial',10), background= "#FFDCB9")
    pageNumber.place(relx= 0.5, rely=0.97)

def w3(event, card, index, imgs):
    print(card)
    w3 = tk.Toplevel(window)
    w3.title(card[0])
    w3.minsize(width=700, height=350)#畫面大小
    w3.resizable(width=False, height=False)#畫面可否放大縮小
    img = tk.Canvas(w3, width = 166, height=242, bg = "#BEBEBE")
    img.grid(row =0, column=0, rowspan= 4)
    img.create_image(0,0,anchor = 'nw', image = imgs[index])

    name = tk.Label(w3, text= card[1], relief='groove', bg = "green", width=80)
    name.grid(row=0, column=1,columnspan=4)

    a = tk.Label(w3, text= "攻擊", relief='raised',bg = "red", width=13)
    a.grid(row=1, column=1)
    av = tk.Label(w3, text= card[2], relief='groove', bg = "green", width=25)
    av.grid(row=1, column=2)

    d = tk.Label(w3,text= "防禦", relief='raised', bg = "red", width=13)
    d.grid(row=1, column=3)
    dv = tk.Label(w3,text= card[3], relief='groove',bg = "green", width=25)
    dv.grid(row=1, column=4)

    d = tk.Label(w3,text= "效果", relief='raised', bg = "red", width=80)
    d.grid(row=2, column=1,columnspan=4)
    dv = tk.Label(w3,text= card[4], relief='groove',bg = "green", width=80)
    dv.grid(row=3, column=1,columnspan=4)

    w3.mainloop()

def camera():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Cannot open camera")
        exit()
    while(True):        
        ret, frame = camera.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow("camera", frame)
        if cv2.waitKey(1) == ord("q"):
            break
        if cv2.waitKey(1) == ord("p"):
            cv2.imwrite("a.jpg", frame)
            cv2.imshow("a.jpg",frame)
            if cv2.waitKey(1) == ord("q"):
                break
    camera.release()
    cv2.destroyAllWindows()
    return frame

def  useAI():
    camera()
    CID = AI()

    b = False
    for card in cards:
        if(card[0] == CID):
            b = True
            break
    if(b):
        print("已在卡冊")
    else:
        writeBook(CID)
        temp = getOwncard()
        print(temp)
        tempimgs = loadImage(temp)
        w2(1, cardNumber, tempimgs, temp)

window = tk.Tk()

window.title("card")
window.minsize(width=600, height=700)#畫面大小
window.resizable(width=True, height=True)#畫面可否放大縮小

frame1 = tk.Frame(window, pady= 100)
frame1.place(relheight=1, relwidth=1)
tk.Label(frame1, text="卡冊").pack()

# 全 Cid , name
cardNumber = getCardnumber()
# 有的卡片所有內容
cards = getOwncard()
# 將 有的卡 圖片list 轉成Tkinter可以使用的PhotoImage格式
imgs = loadImage(cards)
# 將 預設圖片轉成PhotoImage格式
img = Image.open("image/0000.png")
photo = ImageTk.PhotoImage(img)


bUtton1 = tk.Button(frame1,text="開始",command = lambda:w2(1, cardNumber, imgs, cards))
bUtton1.pack(side= tk.BOTTOM)

window.mainloop()
