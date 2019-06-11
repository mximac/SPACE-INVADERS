class statek():
    def __init__(self):
        self.x=450
        self.y=850
        self.left=0
        self.right=0
    def display(self):
        rect(self.x,self.y,100,100)
        fill(255,0,0)
    def update(self):
        self.x = self.x + (self.right - self.left)
        global pozycjastatku
        pozycjastatku=self.x
        if not (self.x>=0):
            self.x=0
        if (self.x>=900): #zatrzymuje statek przy prawej krawedzi
            self.x=900
class pocisk():
    def __init__(self):
        self.x=500
        self.y=830
        self.right=0
        self.left=0
        self.up = 0
    def display(self):
        rect(self.x,self.y,5,20)
    def update(self):
        global resetpocisku #zmienna ktora resetuje nam y pocisku po trafieniu w przeciwnika
        if (resetpocisku==1):
            self.y=830
            resetpocisku=0
            p.up=0 #sprawia ze pocisk nie leci 2 raz
        if (self.y>=800):
            self.x=pozycjastatku+50
        if not (self.x>=0):
            self.x=0
        if (self.x>=950): #zatrzymuje pocisk na srodku statku przy prawej krawedzi
            self.x=950
        if (self.x<=50): #zatrzymuje pocisk na stodku statku przy lewej krawedzi
            self.x=50
        self.y = self.y+self.up
        if (self.y<=-100):
            self.y=830
            p.up=0
        global pociskX
        global pociskY
        pociskX=self.x
        pociskY=self.y
class enemy():
    def __init__(self, x, y):
        self.hit=0
        self.x=x+100
        self.y=y+200
    def display(self):
        rect(self.x,self.y,50,50)
    def update(self):
        global score
        global resetpocisku
        global wysokoscprzeciwnika
        if not (self.hit==1):
            global przeciwnikX
            global przeciwnikY
            przeciwnikX=self.x
            przeciwnikY=self.y
            if (self.x<750):
                self.x=self.x+2
                if (score>=5):
                    self.x=self.x+1
                if (score>=10):
                    self.x=self.x+1
                if (score>=15):
                    self.x=self.x+1
            else:
                self.y=self.y+100
                self.x=100
            if (pociskY<przeciwnikY) and ((pociskX<=przeciwnikX+50)):
                if (pociskX<przeciwnikX):
                    pass
                else:
                    self.hit=1
                    score=score+1
                    resetpocisku=1
            else:
                pass
            if (self.y>840):
                wysokoscprzeciwnika=1
        else:
            self.y=-20000


def setup():
    size(1000,1000)
    background(50)
    global wygrana
    global score
    global resetpocisku
    global wysokoscprzeciwnika
    global s #statek
    global p #pocisk
    #rzadek nr 1
    global e1 #przeciwnik i jego nr
    global e2
    global e3
    global e4
    global e5
    #rzadek nr 2
    global e6
    global e7
    global e8
    global e9
    global e10
    #rzadek nr 3
    global e11
    global e12
    global e13
    global e14
    global e15
    #rzadek nr 4
    global e16
    global e17
    global e18
    global e19
    global e20
    wysokoscprzeciwnika=0
    wygrana=0
    resetpocisku=0
    score=0
    s=statek()
    p=pocisk()
    #rzadek 1
    e1=enemy(50,100)
    e2=enemy(150,100)
    e3=enemy(250,100)
    e4=enemy(350,100)
    e5=enemy(450,100)
    #rzadek 2
    e6=enemy(50,0)
    e7=enemy(150,0)
    e8=enemy(250,0)
    e9=enemy(350,0)
    e10=enemy(450,0)
    #rzadek 3
    e11=enemy(50,-100)
    e12=enemy(150,-100)
    e13=enemy(250,-100)
    e14=enemy(350,-100)
    e15=enemy(450,-100)
    #rzadek 4
    e16=enemy(50,-200)
    e17=enemy(150,-200)
    e18=enemy(250,-200)
    e19=enemy(350,-200)
    e20=enemy(450,-200)
def draw():
    global wygrana
    global wysokoscprzeciwnika
    background(50)
    fill(255)
    s.display()
    s.update()
    p.display()
    p.update()
    #rzadek 1
    fill(0,255,0)
    e1.display()
    e1.update()
    e2.display()
    e2.update()
    e3.display()
    e3.update()
    e4.display()
    e4.update()
    e5.display()
    e5.update()
    #rzadek 2
    fill(0,0,255)
    e6.display()
    e6.update()
    e7.display()
    e7.update()
    e8.display()
    e8.update()
    e9.display()
    e9.update()
    e10.display()
    e10.update()
    #rzadek 3
    fill(0,255,255)
    e11.display()
    e11.update()
    e12.display()
    e12.update()
    e13.display()
    e13.update()
    e14.display()
    e14.update()
    e15.display()
    e15.update()
    #rzadek 4
    fill(124,124,222)
    e16.display()
    e16.update()
    e17.display()
    e17.update()
    e18.display()
    e18.update()
    e19.display()
    e19.update()
    e20.display()
    e20.update()
    print(pociskX, ' ' , pociskY) #wyswietlanie pozycji pocisku
    print(score) #wyswietla wynik
    #WYNIKI
    if (score==0):
        img=loadImage("punkt0.png")
        image(img,0,0)
    if (score==1):
        img=loadImage("punkt1.png")
        image(img,0,0)
    if (score==2):
        img=loadImage("punkt2.png")
        image(img,0,0)
    if (score==3):
        img=loadImage("punkt3.png")
        image(img,0,0)
    if (score==4):
        img=loadImage("punkt4.png")
        image(img,0,0)
    if (score==5):
        img=loadImage("punkt5.png")
        image(img,0,0)
    if (score==6):
        img=loadImage("punkt6.png")
        image(img,0,0)
    if (score==7):
        img=loadImage("punkt7.png")
        image(img,0,0)
    if (score==8):
        img=loadImage("punkt8.png")
        image(img,0,0)
    if (score==9):
        img=loadImage("punkt9.png")
        image(img,0,0)
    if (score==10):
        img=loadImage("punkt10.png")
        image(img,0,0)
    if (score==11):
        img=loadImage("punkt11.png")
        image(img,0,0)
    if (score==12):
        img=loadImage("punkt12.png")
        image(img,0,0)
    if (score==13):
        img=loadImage("punkt13.png")
        image(img,0,0)
    if (score==14):
        img=loadImage("punkt14.png")
        image(img,0,0)
    if (score==15):
        img=loadImage("punkt15.png")
        image(img,0,0)
    if (score==16):
        img=loadImage("punkt16.png")
        image(img,0,0)
    if (score==17):
        img=loadImage("punkt17.png")
        image(img,0,0)
    if (score==18):
        img=loadImage("punkt18.png")
        image(img,0,0)
    if (score==19):
        img=loadImage("punkt19.png")
        image(img,0,0)
    if (score==20):
        wygrana=1
    if (wygrana==1):
        background(255)
        img2=loadImage("wygrana.png")
        image(img2,0,0)
        noLoop()
    if (wysokoscprzeciwnika==1):
        background(255)
        img3=loadImage("przegrana.png")
        image(img3,0,0)
        noLoop()
#sterowanie
def keyPressed():
    if keyCode == RIGHT:
        s.right=10
        p.right=10
    if keyCode == LEFT:
        s.left=10
        p.left=10
    if keyCode == UP:
        p.up = -30
def keyReleased():
    if keyCode == RIGHT:
        s.right=0
        p.right=0
    if keyCode == LEFT:
        s.left=0
        p.left=0.
