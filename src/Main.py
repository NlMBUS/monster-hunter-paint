#basicPaint.py
from pygame import *
from math import *
from tkinter import *
from tkinter import filedialog
#required for open and save tool to remove unnecessary window
root = Tk()
root.withdraw()
#required to initiate use of fonts
font.init()
init()#Initiates music
musicTime = [366,311,315,"6:06","5:10","5:14","Nergigante's Theme","Velkhana's Theme","Title Screen Theme"]#List of length of songs in seconds,length of songs in minutes:seconds, name of the songs
#Makes a list of songs to loop through
musicList = []
musicList.append("nergiganteTheme.mp3")
musicList.append("velkhanaTheme.mp3")
musicList.append("titleTheme.mp3")
music = 2#Default song is 3rd song in the list(Title Screen Theme)
mixer.music.load(musicList[music])#Loads the music
mixer.music.play(-1)#Allows songs to be played as many times possible since -1 is the amount of loops and -1 is infinite
seconds = mixer.music.get_pos()//1000#Finds how many seconds have passed since the song started in seconds instead of milliseconds
#Creates a 1100x600 pixels window 
width,height=1100,600
screen=display.set_mode((width,height))
#List of preset colors in RGB
RED=(255,0,0,10)
GREY=(127,127,127,10)
BLACK=(0,0,0,10)
BLUE=(14,138,231,10)
GREEN=(0,255,0,10)
YELLOW=(255,255,0,10)
WHITE=(255,255,255,10)
PURPLE=(131,39,205)
col=(BLACK)#Sets default color to black
#Loads the "Monster Hunter" font and sets the font size
subtitleFont = font.Font("monsterhunter.ttf", 18)
musicFont = font.Font("monsterhunter.ttf", 12)
#Renders the text
thicknessText=subtitleFont.render("Thickness",True,RED)
colorText=subtitleFont.render("Color",True,RED)
stampsText=subtitleFont.render("Stamps",True,RED)
toolsText=subtitleFont.render("Tools",True,RED)
musicText1=subtitleFont.render("Music",True,RED)
musicText2=subtitleFont.render("Currently playing:",True,RED)
#Makes a list of stamps and appends the stamps to the list
stampList=[]
brachydios=image.load("Brachydios.png")
stampList.append(transform.scale(brachydios,(110,67)))
deviljho=image.load("Deviljho.png")
stampList.append(transform.scale(deviljho,(110,67)))
nergigante=image.load("Nergigante.png")
stampList.append(transform.scale(nergigante,(110,71)))
rathalos=image.load("Rathalos.png")
stampList.append(transform.scale(rathalos,(110,86)))
tigrex=image.load("Tigrex.png")
stampList.append(transform.scale(tigrex,(110,61)))
velkhana=image.load("Velkhana.png")
stampList.append(transform.scale(velkhana,(110,95)))
#Sets the parameters for all the rectangles 
pencilRect=Rect(10,100,40,40)
eraserRect=Rect(60,100,40,40)
highlighterRect=Rect(10,150,40,40)
lineRect=Rect(60,150,40,40)
rectRect=Rect(10,200,40,40)
ellipseRect=Rect(60,200,40,40)
polygonRect=Rect(10,250,40,40)
resetRect=Rect(60,250,40,40)
saveRect=Rect(10,340,50,50)
openRect=Rect(80,340,50,50)
undoRect=Rect(10,415,50,50)
redoRect=Rect(80,415,50,50)
brachydiosRect=Rect(440,10,110,67)
deviljhoRect=Rect(550,10,110,67)
nergiganteRect=Rect(660,10,110,71)
rathalosRect=Rect(770,10,110,86)
tigrexRect=Rect(880,10,110,61)
velkhanaRect=Rect(990,10,120,88)
eyedropRect=Rect(396,40,40,40)
canvasRect=Rect(450,110,600,450)
thickRect=Rect(10,25,90,40)
previousRect=Rect(220,510,40,40)
pauseRect=Rect(260,500,60,60)
nextRect=Rect(320,510,40,40)
colorRect=Rect(260,40,136,40)
lightRect=Rect(260,80,176,40)
sliderRect=Rect(175,578,200,5)
#A list of parameters for rectangle of the tools
toolsList=[pencilRect,eraserRect,highlighterRect,lineRect,rectRect,ellipseRect,polygonRect,resetRect,saveRect,openRect,undoRect,redoRect,eyedropRect,previousRect,pauseRect,nextRect]
#Loads the background for the theme and blits it
background=image.load("Background.png")
screen.blit(background,(0,0))
#Copies part of the background so if something is blitted twice, it doesn't overlap
pauseTransparency = screen.subsurface(pauseRect).copy()
musicTransparency = screen.subsurface(0,535,220,65).copy()
draw.circle(screen,WHITE,(180,80),60)#Draws filled circle at center of color palette since middle is transparent
#Loads and blits images
wheel=image.load("Wheel.png")
screen.blit(wheel,(110,10))
light=image.load("Light.png")
screen.blit(light,(260,80))
screen.blit(light,(348,80))
screen.blit(stampList[0],canvasRect)
banner=image.load("Banner.png")
screen.blit(banner,(450,565))
pencil=image.load("Pencil.png")
screen.blit(pencil,(10,100))
eraser=image.load("Eraser.png")
screen.blit(eraser,(60,100))
highlighter=image.load("Highlighter.png")
screen.blit(highlighter,(10,150))
line=image.load("Line.png")
screen.blit(line,(60,150))
rect=image.load("Rectangle.png")
screen.blit(rect,(10,200))
ellipse=image.load("Ellipse.png")
screen.blit(ellipse,(60,200))
polygon=image.load("Polygon.png")
screen.blit(polygon,(10,250))
reset=image.load("Reset.png")
screen.blit(reset,(60,250))
eyedrop=image.load("Eyedrop.png")
screen.blit(eyedrop,(396,40))
previous=image.load("Previous.png")
screen.blit(previous,(220,512))
nextPic=image.load("Next.png")
screen.blit(nextPic,(320,512))
pause=image.load("Pause.png")
screen.blit(pause,(260,500))
play=image.load("Play.png")
save=image.load("Save.png")
screen.blit(save,(10,340))
load=image.load("Load.png")
screen.blit(load,(80,340))
undoPic=image.load("Undo.png")
screen.blit(undoPic,(10,415))
redoPic=image.load("Redo.png")
screen.blit(redoPic,(80,415))

#Blits text
screen.blit(thicknessText,(0,0))
screen.blit(colorText,(320,0))
screen.blit(stampsText,(720,85))
screen.blit(toolsText,(30,75))
screen.blit(musicText1,(0,475))
screen.blit(musicText2,(0,505))


draw.rect(screen,WHITE,canvasRect)#draws canvas before loop starts
#Blits the stamps in a loop for efficiency
for i in range(6):
    screen.blit(stampList[i],(440+(i*110),10))
#Makes undo and redo list, undo has a screenshot of canvas to redo if only one action on canvas is done
undo = [screen.subsurface(canvasRect).copy()]
redo=[]
def shades(col):#Makes function for light scale 
    #Since the middle of the light scale is not the same as the current color, blit image again to prevent the r or g or b from accumatively increasing
    if screen.get_at((348,81))!=(min(255,col[0]+1),min(255,col[1]+1),min(255,col[2]+1),255):
        screen.blit(light,(260,80))
        screen.blit(light,(348,80))
    if screen.get_at((348,81))!=col:
        screen.blit(light,(348,80))
    #Makes first half of light scale white to current color by adding current r,g,b to previous scale and if any value goes over 255, stay 255
    for x in range(260,348):
        for y in range(80,120):
            r,g,b,a=screen.get_at((x,y))
            nr = min(255,col[0]+r)
            ng = min(255,col[1]+g)
            nb = min(255,col[2]+b)
            screen.set_at((x,y),(r,g,b))
            screen.set_at((x,y),(nr,ng,nb))
    #Makes second half of light scale current color to black by multiplying current r,g,b to r,g,b multiplied percentage of the values out of the maximum possible value(255)
    for x in range(348,436):
        for y in range(80,120):
            r,g,b,a=screen.get_at((x,y))
            nr = min(255,col[0]/255*r)
            ng = min(255,col[1]/255*g)
            nb = min(255,col[2]/255*b)
            screen.set_at((x,y),(r,g,b))
            screen.set_at((x,y),(nr,ng,nb))
def ellipseThick(x1,x2,y1,y2,thick):#Makes function for empty ellipse
     #Normal ellipse has white dots on it, so draw an eclipse for what the thickness is, makes different formula for every direction the mouse moves, the values are changed depending on if initial click or mouse position is bigger
     if thick > 1:
        for i in range(0,thick):
            draw.ellipse(screen,col,(x1-i,y1-i,x2-x1+i*2,y2-y1+i*2),1)
            draw.ellipse(screen,col,(x1-i+1,y1-i+1,x2-x1+i*2,y2-y1+i*2),1)
            draw.ellipse(screen,col,(x1-i-1,y1-i-1,x2-x1+i*2,y2-y1+i*2),1)
            draw.ellipse(screen,col,(x1-i+1,y1-i-1,x2-x1+i*2,y2-y1+i*2),1)
            draw.ellipse(screen,col,(x1-i-1,y1-i+1,x2-x1+i*2,y2-y1+i*2),1)
    #Making multiple ellipses is useless if thickness is only one
     else:
        draw.ellipse(screen,col,(x1-i,y1-i,x2-x1+i*2,y2-y1+i*2),1)
omx,omy,mx,my=0,0,0,0#Old mouse position and mouse position is set to 0 or else it won't run


running=True#The boolean is set to true for the while loop
tool="no tool"#There is no default 

shades(BLACK)#The shades function (light scale) is applied to the default color
thick=5#Default thickness is 5
screenCap=screen.subsurface(canvasRect).copy()#Takes screenshot of canvasRect since sometimes the changes on the canvas aren't applied 
resetScreen=screen.subsurface(canvasRect).copy()#taking a screen shot of the "canvasRect" only#Just a white screen that doesn't change for reset tool
points=[]#List of points for polygon tool
while running:#While loop so you can constantly interact with the program
    for evt in event.get():
	#Sets the position for the initial position when the canvas is clicked
        if evt.type==MOUSEBUTTONDOWN and canvasRect.collidepoint(mx,my):
            sx,sy=evt.pos
	#Every action that is done is appended to the undo list
        if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
            undo.append(screen.subsurface(canvasRect).copy())
	#If pause button is left clicked, pause, if right click, unpause
        if evt.type==MOUSEBUTTONUP and pauseRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,(450,565,600,30))
            eraserText=subtitleFont.render("Pause:stop the music temporarily, unpause with right click",True,BLACK)
            screen.blit(eraserText,(450,565))
            if mb[0]==1 and pauseRect.collidepoint(mx,my):
                mixer.music.pause()
                screen.blit(pauseTransparency,(260,500))
                screen.blit(play,(260,500))
            if mb[2]==1 and pauseRect.collidepoint(mx,my):
                screen.blit(pauseTransparency,(260,500))
                screen.blit(pause,(260,500))
                mixer.music.unpause()
	#If anywhere on the slider is clicked, sets the song to a specific part based off of the percentage of the slider to the overall grey rectangle played multiplied by the seconds in the song
        if evt.type==MOUSEBUTTONUP and sliderRect.collidepoint(mx,my):
            mixer.music.set_pos(((mx-175)/200)*musicTime[music])
            draw.rect(screen,WHITE,(170,565,270,30))
            draw.rect(screen,GREY,sliderRect)
            seconds = int(((mx-175)/200)*(musicTime[music]+mixer.music.get_pos()/1000))#Makes a variable for the seconds that would pass if the slider was clicked
	#If the previous button is pressed, go to the previous song in the list and if it's zero, it goes back to the second song
        if evt.type==MOUSEBUTTONUP and previousRect.collidepoint(mx,my):
            if music == 0:
                music = 2
            else:
                music -= 1
            mixer.music.load(musicList[music])
            mixer.music.play(-1)
            seconds = 0
	#Does the reverse or the seconds passed is more than the length of the song
        if evt.type==MOUSEBUTTONUP and nextRect.collidepoint(mx,my) or seconds+mixer.music.get_pos()//1000>musicTime[music]:
            if music == 2:
                music =0
            else:
                music += 1
            mixer.music.load(musicList[music])
            mixer.music.play(-1)
            seconds = 0
        #If touches color wheel or scale, change color unless eraser
        if (mx-200)**2+(my-80)**2<=70**2 and evt.type==MOUSEBUTTONUP or lightRect.collidepoint(mx,my)and evt.type==MOUSEBUTTONUP:#(x – h)^2 + (y – k)^2 <= r^2
            if tool != "eraser":
                col = (screen.get_at((mx,my)))
                shades(col)
            screen.set_clip(None)
        shades(col)
        screen.set_clip(None)
        #Blits previous screenshots
        if evt.type==MOUSEBUTTONDOWN and undoRect.collidepoint(mx,my):
            if len(undo)>1:
                redo.append(undo.pop())
                screen.blit(undo[-1],(450,110))
                if len(undo)==0:
                    draw.rect(screen,WHITE,canvasRext)
            screenCap=screen.subsurface(canvasRect).copy()
        #Blits screenshots you undid
        if evt.type==MOUSEBUTTONDOWN and redoRect.collidepoint(mx,my):
            if len(redo)>0:
                screen.blit(redo[-1],(450,110))
                undo.append(redo.pop())
            screenCap=screen.subsurface(canvasRect).copy()
        #Blits the stamps
        if tool=="brachydios":
            draw.rect(screen,WHITE,(450,565,600,30))
            eraserText=subtitleFont.render("Brachydios: Blit the slimey Brachydios",True,BLACK)
            screen.blit(eraserText,(450,565))
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                if mb[0]==1 and canvasRect.collidepoint(mx,my):
                    screen.blit(stampList[0],(mx,my))
                screenCap=screen.subsurface(canvasRect).copy()
        if tool=="deviljho":
            draw.rect(screen,WHITE,(450,565,600,30))
            eraserText=subtitleFont.render("Deviljho:Blit the forever hungry Deviljho",True,BLACK)
            screen.blit(eraserText,(450,565))
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                if mb[0]==1 and canvasRect.collidepoint(mx,my):
                    screen.blit(stampList[1],(mx,my))
                screenCap=screen.subsurface(canvasRect).copy()
        if tool=="nergigante":
            draw.rect(screen,WHITE,(450,565,600,30))
            eraserText=subtitleFont.render("Nergigante:Blit the aggressive, Nergigante",True,BLACK)
            screen.blit(eraserText,(450,565))
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                if mb[0]==1 and canvasRect.collidepoint(mx,my):
                    screen.blit(stampList[2],(mx,my))
                screenCap=screen.subsurface(canvasRect).copy()
        if tool=="rathalos":
            draw.rect(screen,WHITE,(450,565,600,30))
            eraserText=subtitleFont.render("Rathalos:Blit the fire breathing dragon Rathalos",True,BLACK)
            screen.blit(eraserText,(450,565))
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                if mb[0]==1 and canvasRect.collidepoint(mx,my):
                    screen.blit(stampList[3],(mx,my))
                screenCap=screen.subsurface(canvasRect).copy()
        if tool=="tigrex":
            draw.rect(screen,WHITE,(450,565,600,30))
            eraserText=subtitleFont.render("Tigrex:Blit the brute Tigrex",True,BLACK)
            screen.blit(eraserText,(450,565))
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                if mb[0]==1 and canvasRect.collidepoint(mx,my):
                    screen.blit(stampList[4],(mx,my))
                screenCap=screen.subsurface(canvasRect).copy()
        if tool=="velkhana":
            draw.rect(screen,WHITE,(450,565,600,30))
            eraserText=subtitleFont.render("Velkhana:Blit the freezing Velkhana",True,BLACK)
            screen.blit(eraserText,(450,565))
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                if mb[0]==1 and canvasRect.collidepoint(mx,my):
                    screen.blit(stampList[5],(mx,my))
                screenCap=screen.subsurface(canvasRect).copy()
        if tool=="line":
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                screen.blit(screenCap,canvasRect)
                draw.line(screen,col,(sx,sy),(mx,my),thick)#adding 1 more line
                screenCap=screen.subsurface(canvasRect).copy()
        #Makes a rect 
        if tool=="rect":
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                screen.blit(screenCap,canvasRect)
                if mb[0]==1 and canvasRect.collidepoint(mx,my):
                    for i in range(0,thick):
                        if mx-sx>0 and my-sy>0 or mx-sx<0 and my-sy<0:
                            draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),2)
                        elif mx-sx>0 and my-sy<0:
                            draw.rect(screen,col,(sx-i,sy+i,mx-sx+i*2,my-sy-i*2),2)
                        else:
                            draw.rect(screen,col,(sx+i,sy-i,mx-sx-i*2,my-sy+i*2),2)
                if mb[2]==1 and canvasRect.collidepoint(mx,my):
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy))
                screenCap=screen.subsurface(canvasRect).copy()
        #Makes an ellipse
        if tool=="ellipse":
            if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
                try:
                    if mb[0]==1 and canvasRect.collidepoint(mx,my):
                        for i in range(0,thick):
                            if mx>sx and my>sy:
                                ellipseThick(sx,mx,sy,my,thick)
                            if mx>sx and sy>my:
                                ellipseThick(sx,mx,my,sy,thick)
                            if sx>mx and my>sy:
                                ellipseThick(mx,sx,sy,my,thick)
                            if sx>mx and sy>my:
                                ellipseThick(mx,sx,my,sy,thick)
                    if mb[2]==1 and canvasRect.collidepoint(mx,my):
                        if mx>sx and my>sy:
                            draw.ellipse(screen,col,(sx,sy,mx-sx,my-sy))
                        if mx>sx and sy>my:
                            draw.ellipse(screen,col,(mx-(mx-sx),my,mx-sx,sy-my))
                        if sx>mx and my>sy:
                            draw.ellipse(screen,col,(mx,my-(my-sy),sx-mx,my-sy))
                        if sx>mx and sy>my:
                            draw.ellipse(screen,col,(mx,my,sx-mx,sy-my))
                except:
                    print("a")
                screenCap=screen.subsurface(canvasRect).copy()
        #Makes a polygon from the points
        if tool=="polygon":
            screen.blit(screenCap,canvasRect)
            if mb[0]==1 and canvasRect.collidepoint(mx,my):
                points.append((sx,sy))
                if len(points)>1:
                    draw.line(screen,col,points[-2],points[-1],thick)
                else:
                    draw.rect(screen,col,(sx,sy,1,1),2)
            if mb[1]==1 and canvasRect.collidepoint(mx,my):
                if len(points)>1:
                    draw.line(screen,col,points[0],points[-1],thick)
                points=[]
            if mb[2]==1 and canvasRect.collidepoint(mx,my):
                if len(points)>1:
                    draw.polygon(screen,col,points)
                points=[]
            screenCap=screen.subsurface(canvasRect).copy()
        if evt.type==QUIT:
            running=False

    
    mx,my=mouse.get_pos()#current mouse position
    mb=mouse.get_pressed()#If mouse buttons is pressed
    draw.circle(screen,BLACK,(180,80),71,2)


    #drawing all tools


    for i in toolsList:
        draw.rect(screen,BLUE,i,2)
        if i.collidepoint(mx,my):
            draw.rect(screen,PURPLE,i,2)

    draw.rect(screen,col,colorRect)
    draw.polygon(screen,col,[(10,45), (100,25), (100,65)])
   

       

    #selecting the tools
    if (mx-200)**2+(my-80)**2<=70**2 and mb[0]==1 or lightRect.collidepoint(mx,my)and mb[0]==1:#(x – h)^2 + (y – k)^2 <= r^2
        if tool == "eraser":
            col = WHITE
        else:
            col = (screen.get_at((mx,my)))
    if mb[0]==1 and brachydiosRect.collidepoint(mx,my):
        tool="brachydios"
    if mb[0]==1 and deviljhoRect.collidepoint(mx,my):
        tool="deviljho"
    if mb[0]==1 and nergiganteRect.collidepoint(mx,my):
        tool="nergigante"
    if mb[0]==1 and rathalosRect.collidepoint(mx,my):
        tool="rathalos"
    if mb[0]==1 and tigrexRect.collidepoint(mx,my):
        tool="tigrex"
    if mb[0]==1 and velkhanaRect.collidepoint(mx,my):
        tool="velkhana"
    if mb[0]==1 and pencilRect.collidepoint(mx,my):
        tool="pencil"
        draw.rect(screen,WHITE,(450,565,600,30))
        pencilText=subtitleFont.render("Pencil:Draw whatever colour or thickness you want",True,BLACK)
        screen.blit(pencilText,(450,565))
    if mb[0]==1 and thickRect.collidepoint(mx,my):
        thick=((mx-10)//4)+1
    if mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool="eraser"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Eraser:Erase in any thickness you want",True,BLACK)
        screen.blit(eraserText,(450,565))
        col=WHITE
    if mb[0]==1 and highlighterRect.collidepoint(mx,my):
        tool="highlighter"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Highlighter:Draw a translucent line and stay in spot to increase opacity",True,BLACK)
        screen.blit(eraserText,(450,565))
    if mb[0]==1 and lineRect.collidepoint(mx,my):
        tool="line"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Line:Make a line from where you originaly clicked to where you let go",True,BLACK)
        screen.blit(eraserText,(450,565))
    if mb[0]==1 and resetRect.collidepoint(mx,my):
        tool="reset"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Reset:Set the canvas to its original state",True,BLACK)
        screen.blit(eraserText,(450,565))
    if mb[0]==1 and rectRect.collidepoint(mx,my):
        tool="rect"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Rect:Make a rectangle (click->let go) right click is filled",True,BLACK)
        screen.blit(eraserText,(450,565))
    if mb[0]==1 and ellipseRect.collidepoint(mx,my):
        tool="ellipse"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Ellipse:Make an ellipse (click->let go) right click is filled",True,BLACK)
        screen.blit(eraserText,(450,565))
    if mb[0]==1 and eyedropRect.collidepoint(mx,my):
        tool="eyedrop"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Eyedrop:Get whatever color you want",True,BLACK)
        screen.blit(eraserText,(450,565))
    if mb[0]==1 and polygonRect.collidepoint(mx,my):
        tool="polygon"
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Make a polygon by clciking points, right click is filled, middle is no fill",True,BLACK)
        screen.blit(eraserText,(450,565))
    #Opens directory and blits image
    if mb[0]==1 and openRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Open: Opens an image from the folder",True,BLACK)
        screen.blit(eraserText,(450,565))
        try:
            fname=filedialog.askopenfilename()#fname is a string that has the full path to the selected file
            mypic=image.load(fname)
            if mypic.get_rect().size[0]>600 or mypic.get_rect().size[1]>450:
                mypic=transform.scale(mypic,(600,450))
            screen.blit(mypic,(450,110))
            undo.append(screen.subsurface(canvasRect).copy())
        except:
            print("Load error")
    #Saves image
    if mb[0]==1 and saveRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,(450,565,600,30))
        eraserText=subtitleFont.render("Save:Save your drawing to a .png file",True,BLACK)
        screen.blit(eraserText,(450,565))
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            image.save(screenCap, fname)
        except:
            print("Saving error")
    #If the image is pencil or eraser use pythagorean to draw line conenct to previous point
    def drawing(col,thick):
        if mb[0]==1:
            dx=mx-omx #run
            dy=my-omy #rise
            dist=sqrt(dx**2+dy**2)
            for i in range(1,int(dist)):
                cx=int(omx+i*dx/dist)
                cy=int(omy+i*dy/dist)
                draw.circle(screen,col,(cx,cy),thick)
            draw.circle(screen,col,(mx,my),thick)
    #using the tools
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)#only the canvas area can be "updated"
        if tool=="pencil" or tool=="eraser":
            drawing(col,thick)

            screenCap=screen.subsurface(canvasRect).copy()
        if tool=="highlighter":
            brushHead = Surface((20,20),SRCALPHA)
            draw.circle(brushHead,(col[0],col[1],col[2],10),(10,10),10)
            if mx!=omx or my!=omy:
                if mb[0]==1:
                    screen.blit(brushHead,(mx-10,my-10))
            screenCap=screen.subsurface(canvasRect).copy()
        if tool=="eyedrop":
            col=(screen.get_at((mx,my)))
            tool="pencil"
            print(col,tool)
            screenCap=screen.subsurface(canvasRect).copy()
    if tool=="reset":
        screen.blit(resetScreen,canvasRect)
        screenCap=screen.subsurface(canvasRect).copy()
    if tool=="line":
        screen.blit(screenCap,canvasRect)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            draw.line(screen,col,(sx,sy),(mx,my),thick)
    if tool=="rect":
        screen.blit(screenCap,canvasRect)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            for i in range(0,thick):
                if mx-sx>0 and my-sy>0 or mx-sx<0 and my-sy<0:
                    draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),2)
                elif mx-sx>0 and my-sy<0:
                    draw.rect(screen,col,(sx-i,sy+i,mx-sx+i*2,my-sy-i*2),2)
                else:
                    draw.rect(screen,col,(sx+i,sy-i,mx-sx-i*2,my-sy+i*2),2)
        if mb[2]==1 and canvasRect.collidepoint(mx,my):
            draw.rect(screen,col,(sx,sy,mx-sx,my-sy))
    if tool=="ellipse":
        screen.blit(screenCap,canvasRect)
        try:
            if mb[0]==1 and canvasRect.collidepoint(mx,my):
                for i in range(0,thick):
                    if mx>sx and my>sy:
                        ellipseThick(sx,mx,sy,my,thick)
                    if mx>sx and sy>my:
                        ellipseThick(sx,mx,my,sy,thick)
                    if sx>mx and my>sy:
                        ellipseThick(mx,sx,sy,my,thick)
                    if sx>mx and sy>my:
                        ellipseThick(mx,sx,my,sy,thick)
            if mb[2]==1 and canvasRect.collidepoint(mx,my):
                if mx>sx and my>sy:
                    draw.ellipse(screen,col,(sx,sy,mx-sx,my-sy))
                if mx>sx and sy>my:
                    draw.ellipse(screen,col,(mx-(mx-sx),my,mx-sx,sy-my))
                if sx>mx and my>sy:
                    draw.ellipse(screen,col,(mx,my-(my-sy),sx-mx,my-sy))
                if sx>mx and sy>my:
                    draw.ellipse(screen,col,(mx,my,sx-mx,sy-my))
                screen.set_clip(None)

        except:
            print("a")
    #Makes music minutes:seconds and blits as text
    screen.blit(musicTransparency,(0,535))
    musicText3=subtitleFont.render("%s" % musicTime[music+6],True,RED)
    screen.blit(musicText3,(0,535))
    if mb[0]==1 and sliderRect.collidepoint(mx,my):
        mixer.music.play(-1)
    rectLength = (seconds/musicTime[music]+mixer.music.get_pos()/1000/musicTime[music])*200
    musicMinutes = int((seconds+mixer.music.get_pos()/1000)/60)
    musicSeconds = int((seconds+mixer.music.get_pos()/1000)%60)
    draw.rect(screen,WHITE,(170,565,270,30))
    if musicSeconds < 10:        
        musicCurrent = "%i:0%i" % (musicMinutes,musicSeconds)
    elif musicSeconds > 9:
        musicCurrent = "%i:%i" % (musicMinutes,musicSeconds)
    musicText4=musicFont.render("%s / %s" % (musicCurrent,musicTime[music+3]),True,BLACK)
    screen.blit(musicText4,(378,575))
    draw.rect(screen,GREY,sliderRect)
    draw.rect(screen,BLACK,(175,578,rectLength,5))
    #If song ends, play next song
    if rectLength>200:
        if music == 2:
            music =0
        else:
            music += 1
        mixer.music.load(musicList[music])
        mixer.music.play(-1)
        seconds = 0

    display.flip()
    omx,omy=mx,my





quit()
