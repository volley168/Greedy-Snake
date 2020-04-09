import turtle
import time
import random
def go_up():
    print("W pressed")
    head.setheading(90)
def go_down():
    print("S pressed")
    head.setheading(270)
def go_left():
    print("D pressed")
    head.setheading(360)
def go_right():
    print("A pressed")
    head.setheading(540)    
s=turtle.Screen()  #画布
tails=[]           #设置一个数组存放尾巴


s.tracer(0)            #手动刷新屏幕

head=turtle.Turtle()   #蛇头
apple=turtle.Turtle()  #苹果

s.update()
head.shape("square")
head.color("Black")
head.penup()           #提起笔移动，不绘制图形
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)

s.onkeypress(go_up,"W")
s.onkeypress(go_down,"S")
s.onkeypress(go_left,"D")
s.onkeypress(go_right,"A")
s.listen()
while True:
    if len(tails)>0:
        h_x=head.xcor()
        h_y=head.ycor()        #返回上一个坐标值（cor）
        tails[0].goto(h_x,h_y)
    for i in range(len(tails)-1,0,-1):   #获取每次尾巴长度，每次减一
        last_tail=tails[i-1]
        this_tail=tails[i]
        this_tail.goto(last_tail.xcor(),last_tail.ycor())
    head.forward(15)
    if head.distance(apple)<=20:
        new_x=random.randint(-300,300)
        new_y=random.randint(-300,300)
        apple.goto(new_x,new_y)
        tail=turtle.Turtle()
        tail.shape("circle")
        tail.color("gray")
        tail.penup()
        tails.append(tail)     #tail存入tails数组
    time.sleep(0.1)
    s.update()
s.mainloop()
