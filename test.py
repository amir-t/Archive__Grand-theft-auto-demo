import pygame, sys
from pygame.locals import *
import math
import threading
pygame.init()
GUI = True
counth = 0
countv = 0
argent = 100
#              R    G    B
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
DGREY      = ( 40,  40,  40)
GREY       = (186, 186, 186)
decalx,decaly = 0,0
selfx , selfy = 0,0
v = 2
comptvitess = 0
x , y = 0,0
j = 0
i = 0
q = 0
step = 0
EDGX, EDGY = 600,375
TEMPEDGX,TEMPEDGY = 600,375
bgx,bgy = 0,0
move = 1
mission1=0              #Variable d'état de chaque mission
mission2=-1
mission3=-1
comptaffmiss=0          #Compteur Affichage Mission
affmiss=1               #Variable Etat Affichage Mission
tempo=150               #Temporisation entre les textes de mission
stillx,stilly = 400,120
clock = pygame.time.Clock()
pygame.key.set_repeat(0, 2000)
bg = pygame.image.load('bg2.png')
GUN = pygame.image.load('gun.png')
surface = pygame.display.set_mode((1200,750))
pygame.display.set_caption("p'tit theaft auto 1")
car = pygame.image.load('car.png')
dude = pygame.image.load('per.png')
dead1 = pygame.image.load('per1.png')
dead2 = pygame.image.load('per2.png')
deaddead = pygame.image.load('per2mort.png').convert()
dead3 = pygame.image.load('per3.png')
dead4 = pygame.image.load('per4.png')
dead5 = pygame.image.load('per5.png')
dead6 = pygame.image.load('per6.png')
dead7 = pygame.image.load('per7.png')
dead8 = pygame.image.load('per8.png')
dead9 = pygame.image.load('per9.png')
blank = pygame.image.load('blank.png')
arr1 = pygame.image.load('blank.png')
imagesv=pygame.image.load("symbvie.jpg").convert()          #Symbole vie
imagesa=pygame.image.load("symbarg.png").convert()          #Symbole Argent
imagesp=pygame.image.load("symbpoing.png").convert()        #Symbole Poing
imagesm=pygame.image.load("symbmit.png").convert()          #Symbole Mitrailette
caricon = pygame.image.load("caricon.png")
imagespis=pygame.image.load("symbpis.png").convert()        #Symbole Pistolet
imagemm = pygame.image.load("minimap.png").convert()
imageposho = pygame.image.load("posho.png").convert()
imageposmiss = pygame.image.load("posmiss.png").convert()
logo = pygame.image.load('logo.png')
end  = pygame.image.load('end.png')
imageposmiss.set_colorkey((255,255,255))
imageposho.set_colorkey((255,255,255))
deaddead.set_colorkey((255,255,255))
dead0 = 0
somme = 0
mode = 1
size2 = 100
shot = False
gun = False
angle = 0
cenx = EDGX
ceny = EDGY
carleft = -1000
carright = -1000
carup = -1000
cardown = -1000
#wallleft =  ["x",carleft ,0   ,539 ,789 ,789 ,789 ,0   ,0   ,1865]
#wallright = ["x",carright,540 ,1875,1875,1875,1875,540 ,540 ,2000]
#wallup =    ["y",carup   ,0    ,0   ,581 ,1650,3120,3120,1650,0  ]
#walldown =  ["y",cardown ,1390,323 ,1390,2865,3750,3750,2863,3750]
hdirleft =  [653 ,1964,4730,7950,3070,685 ,1920,3072,4363,4747,6450,3070,4363,6577,8165,8165,675 ,2521,6567]
hdirright = [1827,4604,7814,9231,4225,1813,2920,4220,4600,6306,7806,4225,4600,8013,9225,9225,2373,6727,9221]
hdirup =    [300 ,300 ,300 ,300 ,1955,2617,2627,1960,1960,1960,1960,4535,4535,4535,4535,3825,6000,6000,6000]
hdirdown =  [620 ,620 ,620 ,620 ,2125,2780,2780,2120,2120,2120,2120,4700,4700,4700,4700,3990,6320,6320,6320]
vdirleft =  [340 ,340 ,1810,2915,2915,2365,4208,6290,8000,8000,7800,4580,6410,9220,9220]
vdirright = [667 ,667 ,1980,3090,3090,2530,4378,6465,8172,8172,7970,4750,6580,9541,9541]
vdirup =    [610 ,2777,610 ,2120,2780,4695,2120,2120,2120,3980,610 ,610 ,4692,621 ,3980]
vdirdown =  [2623,6001,2623,2630,4539,6000,4539,4539,3828,4737,1958,1958,6000,3826,6000]
def walls(int,list,m):
    wallright[m]-= 5
    if list[0] == "x":
        for j in (-5,5):
            if   list[m]+x+j-5 < int < list[m]+x+j+5:
                wallright[m]+= 5
                return True
        wallright[m]+= 5
        return False
    if list[0] == "y":
        int += 60
        for j in (-10,0):
            if int < list[m]+y+j+5:
                wallright[m]+= 5
                int -= 60
                return True
        int -= 60
        wallright[m]+= 5
        return False
def wall(int,list,m):
    wallleft[m]-= 60
    if list[0] == "x":
        for j in (-5,5):
            if  int < list[m]+x+j-5:
                wallleft[m]+= 60
                return True
        wallleft[m]+= 60
        return False
    if list[0] == "y":
        for j in (-10,0):
            if list[m]+y+j-5 < int < list[m]+y+j + 5 :
                wallleft[m]+= 60
                return True
        wallleft[m]+= 60
        return False
def dirh(edgx,edgy):
    for m in range(len(hdirleft)):
        if edgx >= hdirleft[m]+x and edgx+128 <= hdirright[m]+x and edgy <= hdirdown[m]+y and edgy >= hdirup[m]+y:
            return True
    return False
def dirv(edgx,edgy):
    for m in range(len(vdirleft)):
        if edgx >= vdirleft[m]+x and edgx+60 <= vdirright[m]+x and edgy <= vdirdown[m]+y and edgy >= vdirup[m]+y:
            return True
    return False
def wallr(edgx,edgy):
    for m in range(1,len(wallup)):
        if not (not walls(edgx    ,wallright,m) or ( walls(edgx    ,wallright,m) and ( walls(edgy,wallup,m) or not walls(edgy,walldown,m)))):
            return (not walls(edgx,wallright,m) or ( walls(edgx,wallright,m) and ( walls(edgy,wallup,m) or not walls(edgy,walldown,m))))
    return True
def walll(edgx,edgy):
    for m in range(1,len(wallleft)):
        if not (not walls(edgx,wallleft ,m) or ( walls(edgx,wallleft ,m) and ( walls(edgy,wallup,m) or not walls(edgy,walldown,m)))):
            return (not walls(edgx,wallleft ,m) or ( walls(edgx,wallleft ,m) and ( walls(edgy,wallup,m) or not walls(edgy,walldown,m))))
        if not walls(edgx,wallleft,m) and 20 < -(edgx - wallleft[m]-x) < 64 and not ( walls(edgy,wallup,m) or not walls(edgy,walldown,m)):
            return False
    return True
def walld(edgx,edgy):
    for m in range(1,len(wallup)):
        if not ( not wall(edgy,walldown,m) or ( wall(edgy,walldown,m) and ( wall(edgx,wallleft,m) or not wall(edgx,wallright,m)))):
            return ( not wall(edgy,walldown,m) and ( not wall(edgx,wallleft,m) and wall(edgx,wallright,m)))
    return True
def wallu(edgx,edgy):
    for m in range(1,len(wallup)):
        if not ( not wall(edgy,wallup,m) or ( wall(edgy,wallup,m) and ( wall(edgx,wallleft,m) or not wall(edgx,wallright,m)))):
            return False
        if  not wall(edgy,wallup,m) and 20 < -(edgy - wallup[m]-y) < 64 and not (wall(edgx,wallleft,m) or not wall(edgx,wallright,m)):
            return False
    return True
wayv = 0
wayh = 0
wv = 0
wh = 2
def hpep():
    global counth
    global wayh
    global wh
    if wayh == 0:
        counth += 3
    if wayh == 1:
        counth -= 3
    if counth % 900 == 0:
        if wayh == 1:
            wh = 2
            wayh = 0
        elif wayh == 0:
            wh = 1
            wayh = 1
    t = threading.Timer(0.2, hpep)
    t.start()

def vpep():
    global countv
    global wayv
    global wv
    if wayv == 0:
        countv += 3
    if wayv == 1:
        countv -= 3
    if countv % 900 == 0:
        if wayv == 1:
            wv = 0
            wayv = 0
        elif wayv == 0:
            wv = 3
            wayv = 1
    t = threading.Timer(0.2, vpep)
    t.start()
def timer():
    global q
    global step
    q += 1
    step = q%4
    t = threading.Timer(0.2, timer)
    t.start()
timer()
vpep()
hpep()
way = 0
effect = 50
som = 0
start = 0
blanc =  (255,255,255)
noir = (0,0,0)
FONT1 = pygame.font.SysFont("comicsansms", 20)
while GUI:
    if start == 0:
        logopic = surface.blit(logo,(0,0))
        X, Y = pygame.mouse.get_pos()
        load = str("run demo ")
        textSurf = FONT1.render(load, True, noir, blanc)
        textRect = textSurf.get_rect()
        if 950  < X < 1250 and 200 < Y < 250:
            pygame.draw.rect(surface, blanc, (950 - effect, 200, 300, 50))
            textRect.topleft = (1000 - effect, 205)
        else:
            pygame.draw.rect(surface, blanc, (950, 200, 300, 50))
            textRect.topleft = (1000, 205)
        surface.blit(textSurf, textRect)
        eight = str("quit")
        textSurf = FONT1.render(eight, True, noir, blanc)
        textRect = textSurf.get_rect()
        X, Y = pygame.mouse.get_pos()
        if 950 < X < 1250 and 400 < Y < 450:
            pygame.draw.rect(surface, blanc, (950 - 50, 400, 300, 50))
            textRect.topleft = (1000 - effect, 405)
        else:
            pygame.draw.rect(surface, blanc, (950, 400, 300, 50))
            textRect.topleft = (1000, 405)
        surface.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                # procedure boutton charger
                X, Y = event.pos
                if 950 < X < 1250 and 200 < Y < 250:
                    start = 1
                if 950 < X < 1250 and 400 < Y < 450:
                    GUI = False
    if start == 1:
        keys = pygame.key.get_pressed()
        police = pygame.font.Font('freesansbold.ttf', 26)  # Police Texte
        texte50 = police.render(" + 50 $ ", True, GREY, BLACK)
        texteRect50 = texte50.get_rect()
        texteRect50.topleft = (500, 710)
        texte100 = police.render(" + 100 $ ", True, GREY, BLACK)
        texteRect100 = texte50.get_rect()
        texteRect100.topleft = (500, 710)
        texte150 = police.render(" + 150 $ ", True, GREY, BLACK)
        texteRect150 = texte50.get_rect()
        texteRect150.topleft = (500, 710)
        texteM1 = police.render("Enmenez la voiture de jean mouloud jusqu'a chez lui", True, GREY, BLACK)
        texteRectM1 = texteM1.get_rect()
        texteRectM1.topleft = (300, 710)
        texteM2 = police.render("reccuperez l'arme dans le parc !", True, GREY, BLACK)
        texteRectM2 = texteM1.get_rect()
        texteRectM2.topleft = (300, 710)
        texteM3 = police.render("tue le mec (pierre) qui surveille le parking !", True, GREY, BLACK)
        texteRectM3 = texteM1.get_rect()
        texteRectM3.topleft = (300, 710)
        texteMR = police.render("Mission Réussi", True, GREY, BLACK)
        texteRectMR = texteMR.get_rect()
        texteRectMR.topleft = (400, 710)
        texteArg = police.render(str(argent), True, GREY, DGREY)
        texteRectArg = texteArg.get_rect()
        texteRectArg.topleft = (977, 80)
        texteVie = police.render("100", True, GREY, DGREY)
        texteRectVie = texteVie.get_rect()
        texteRectVie.topleft = (977, 38)
        surface.blit(bg,(bgx+x,bgy+y))
        if mission1 == 0:
            if affmiss == 1:

                comptaffmiss += 1
                surface.blit(texteM1, texteRectM1)
                tempo = 0
                if comptaffmiss == 100:
                    affmiss = 0
                    comptaffmiss = 0

        if mission1 == 2:

            if tempo < 70:
                tempo += 1

            if tempo == 50:
                affmiss = 2

            if affmiss == 1:

                comptaffmiss += 1
                surface.blit(texteMR, texteRectMR)

                if comptaffmiss == 50:
                    affmiss = 0
                    comptaffmiss = 0

                if comptaffmiss == 0:
                    tempo = 0

            if affmiss == 2:

                comptaffmiss += 1
                surface.blit(texte50, texteRect50)
                if comptaffmiss == 70:
                    argent += 50
                    affmiss = 1
                    comptaffmiss = 0
                    tempo = 0
                    mission1 = 3
                    mission2 = 0
        if mission2 == 0:
            if affmiss == 1:
                comptaffmiss += 1
                if comptaffmiss > 20:
                    surface.blit(texteM2, texteRectM2)
                if comptaffmiss == 120:
                    affmiss = 0
                    comptaffmiss = 0
        if mission2 == 2:

            if tempo < 70:
                tempo += 1

            if tempo == 50:
                affmiss = 2

            if affmiss == 1:

                comptaffmiss += 1
                surface.blit(texteMR, texteRectMR)

                if comptaffmiss == 75:
                    affmiss = 0
                    comptaffmiss = 0

                if comptaffmiss == 0:
                    tempo = 0

            if affmiss == 2:

                comptaffmiss += 1
                surface.blit(texte100, texteRect100)
                if comptaffmiss == 70:
                    argent += 100
                    affmiss = 1
                    tempo = 0
                    mission2 = 3
                    mission3 = 0
                    comptaffmiss = 0
        if mission3 == 0:
            if affmiss == 1:
                comptaffmiss += 1
                if comptaffmiss > 20:
                    surface.blit(texteM3, texteRectM3)
                if comptaffmiss == 130:
                    affmiss = 0
                    comptaffmiss = 0
        if mission3 == 2:

            if tempo < 70:
                tempo += 1

            if tempo == 50:
                affmiss = 2

            if affmiss == 1:

                comptaffmiss += 1
                surface.blit(texteMR, texteRectMR)

                if comptaffmiss == 75:
                    affmiss = 0
                    comptaffmiss = 0

                if comptaffmiss == 0:
                    tempo = 0

            if affmiss == 2:

                comptaffmiss += 1
                surface.blit(texte100, texteRect100)
                if comptaffmiss == 100:
                    argent += 100
                    affmiss = 1
                    comptaffmiss = 0
                    tempo = 0
                    mission3 = 3
                    start = 2
        if mode == 0:
            wallleft = ["x", 0, 0, 652, 1970, 1971, 4747, 7957, 8135, 9532, 3076,
                        4367, 6450, 656, 656, 2521, 6573, 8160, 0]
            wallright = ["x", 346, 10000, 1825, 4605, 2930, 7810, 9224, 9224,
                         10000, 4217, 6305, 8010, 2926, 2373, 6422, 9224, 9224, 98880]
            wallup = ["y", 0, 0, 612, 612, 1975, 612, 612, 1970, 0, 2116, 2116, 2116, 2777,
                      4540, 4693, 4693, 3980, 6310]
            walldown = ["y", 7000, 308, 2630, 1975, 2628, 1965, 1967, 3832, 7000,
                        4540, 4540, 4540, 4540, 6002, 6002, 6002, 4693, 7000]
            surface.blit(blank,(stillx,stilly))
            surface.blit(car,(EDGX,EDGY))
        if mode == 1:
            wallleft =  ["x", carleft - 2, carright - 5, carleft + 5]
            #,9682,870 ,2135,2220,2135,2220,2135,2245,2135,2085,2205,2755,2320,2485,2825,3150,3485,3825,4075,4240,4240,820 ,1790,2690,2630,2690,2600,2660,2000,1460,920 ,950 ,1355,1760,2130,2130,2100,820 ,935 ,1475,935 ,1475,1990,1990,1990,875 ,1345,1815,870 ,1540,2705,3560,4790,3620,3960,4270,4580,3810,4425,4140,5950,5950,6070,6070,6070,4515,5070,5205,5205,5650,4515,5515,4960,4960,6777,5710,5675,6125,6530,7420,7220,7430,7430,7430,7415,8140,8105,8105,8105,8105,8235,8375,8505,8640,8775,8970,8970,8970,8970,8255,8120,8055,8310,8310,8310,8310,8775,8775,8775,6860,8390,8620,8490,8350,8210,8070,8175,8035,7895,7520,7380,7245,7105,6965,6830,6830,6790,6790,6790,6790,6790,6790,6790,6790,6930,7070,7210,7345,7485,7620,7765,7900,8035,8280,8315,8315,6670,6705,6600,6600,6600,7755,7795,7795,7755,6600,6600,6600,6805,6930,7100,7305,6840,7220,6730,7110,7345,7625,6915,6895,6785,6935,7135,6825,7025,6945,6910,6835,6800,665 ,665 ,395 ,400 ,350 ,350 ,610 ,585 ,345 ,345 ,605 ,345 ,595 ,1135,1685,1935,2290,2935,5235,6740,7995,4000,4540,5225,5635,6140,6465,6895,7580,7940,8175,8730,9220,9485,9220,9490,9485,9220,9220]
            wallright = ["x", carleft + 2, carright + 5, carright - 10]
            #,200 ,1615,2245,2260,2245,2260,2245,2295,2245,2150,2255,2820,4215,2590,2930,3255,3590,3930,4150,4285,4285,930 ,1900,2800,2735,2800,2705,2765,2105,1565,1030,1060,1465,1870,2240,2240,2210,925 ,1275,1810,1275,2550,2550,2550,1210,1680,2150,1400,2075,3560,4790,5895,3735,4080,4385,4700,3920,4530,4215,5990,5990,6180,6180,6180,3295,5380,6155,5520,6155,6155,6155,7365,5545,5547,7353,5780,6230,6640,7460,7460,7540,7540,7540,7460,8940,8175,8140,8140,8140,8275,8410,8545,8675,8810,9015,9015,9015,9015,9060,8925,8610,8610,8610,8435,9075,9075,9075,9040,9040,8900,8765,8865,8730,8585,8450,8315,7930,7795,7655,7760,7620,7485,7345,7210,7070,6930,6830,6830,6830,6830,6830,6830,6965,7105,7245,7385,7520,7660,7795,7935,8070,8315,8355,8355,8355,8560,8315,8485,7865,7865,7865,7865,7865,7865,6705,6670,6920,7040,7205,7415,7535,7740,7425,7630,7455,7735,7020,7090,7660,6975,7415,7410,7305,7690,7420,7580,7310,7360,7720,7250,7610,610 ,610 ,660 ,665 ,395 ,395 ,660 ,400 ,660 ,1255,1810,2050,2410,3065,5365,6860,8120,4190,4650,5340,3755,6255,6715,7010,7700,8050,8300,8845,9290,9535,9275,9535,9540,9295,9275,9535,9275]
            wallup =    ["y", carup + 10, carup + 10, carup       ]
            #,6460,800 ,780 ,935 ,1090,1240,1400,1550,1705,1945,1950,1950,875 ,710 ,710 ,710 ,710 ,710 ,790 ,935 ,1575,2910,2910,2880,3150,3525,3925,4300,4365,4365,4365,5180,5180,5180,5080,5355,5800,5800,3030,3030,3775,3775,3030,3475,3950,4520,4520,4520,5395,5395,4845,4915,4845,5745,3745,3745,3745,5795,5795,5745,5040,5530,4890,5260,5700,2265,3070,2265,2745,2745,4005,4005,1245,765 ,765 ,1065,710 ,710 ,710 ,975 ,1530,1120,1400,1670,1275,765 ,1270,1175,1005,835 ,695 ,695 ,695 ,695 ,695 ,835 ,1005,1175,1270,1470,1600,1765,1720,2410,3110,2980,1720,2415,3110,4875,4220,5850,5850,5850,5850,5850,5850,5850,5850,5850,5850,5850,5850,5850,5850,5850,5645,5510,4975,5245,5110,4975,4840,4805,4805,4805,4805,4805,4805,4805,4805,4805,4805,4700,4570,4435,4155,3965,4025,4295,4025,3965,3715,2265,2265,2265,3715,4100,3955,4150,4140,3940,3920,3605,3595,3570,3485,3460,3255,3215,2935,2925,2825,2760,2725,2690,2455,2420,2370,1030,1580,1830,2180,2865,3500,3960,4305,4540,5225,5685,6005,6005,6230,6260,6005,6250,6000,6260,550 ,300 ,565 ,300 ,300 ,540 ,565 ,305 ,305 ,565 ,565 ,1125,1660,2345,2580,3085,3415,4020,4705,5300]
            walldown =  ["y", carup + 100, carup + 100, cardown + 25]
            #,155 ,2480,900 ,1050,1210,1355,1520,1625,1825,2075,2070,2080,1750,830 ,830 ,830 ,830 ,830 ,835 ,1050,1695,3030,3030,3000,3270,3645,4045,4420,4485,4485,4485,5305,5305,5305,5200,5475,5915,5915,3575,3575,4320,4320,3345,3815,4290,5080,5080,5080,5750,5750,5775,5720,5775,5790,3790,3790,3790,5915,5915,5790,5155,5645,5010,5380,5820,3745,3745,2745,2935,2935,5460,3070,1725,1245,1245,1065,830 ,830 ,830 ,1090,1645,1240,1520,1790,1350,1455,1390,1215,1040,950 ,735 ,735 ,735 ,735 ,735 ,950 ,1040,1210,1385,1590,1720,1885,2295,2980,3680,3110,2295,2985,3680,5820,5820,5885,5885,5885,5885,5885,5885,5885,5885,5885,5885,5885,5885,5885,5885,5885,5685,5545,5010,5285,5150,5010,4880,4845,4845,4845,4845,4845,4845,4845,4845,4845,4845,4735,4605,4470,4200,4025,4395,4395,4395,4025,3775,3715,2365,3715,3775,4205,4060,4255,4245,4040,4025,3705,3700,3675,3590,3565,3355,3320,3035,3025,2925,2865,2830,2795,2555,2525,2470,1150,1700,1940,2295,2980,3745,4075,4425,4655,5330,5870,6055,6055,6320,6320,6065,6315,6055,6315,620 ,355 ,615 ,350 ,350 ,615 ,615 ,355 ,350 ,615 ,620 ,1315,1775,2465,2700,3195,3665,4135,4820,5425]
            surface.blit(dude, (EDGX+decalx,EDGY+decaly), (32 * j, 48 * i,32,48))
            surface.blit(car,(stillx+TEMPEDGX+x,stilly+TEMPEDGY+y))
            if angle == 0 or angle == 180:
                carleft = stillx + TEMPEDGX + 30
                carright = stillx + TEMPEDGX + 120
                carup = stilly + TEMPEDGY
                cardown = stilly + TEMPEDGY + 40
            if angle == 90 or angle == 270:
                carleft = stillx + TEMPEDGX + 30
                carright = stillx + TEMPEDGX + 38
                carup = stilly + TEMPEDGY
                cardown = stilly + TEMPEDGY + 95
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                GUI = False
            if event.type == MOUSEBUTTONDOWN:
                if mode == 1 :
                    cenx = EDGX + 25 +decalx
                    ceny = EDGY + 35 +decaly
                    hyp = round(math.sqrt(abs(EDGX+25+decalx - selfx)**2 + abs(EDGY+35+decaly - selfy)**2))
                    changex = ((EDGX+25+decalx - selfx)/hyp)*50
                    changey = ((EDGY+35+decaly - selfy)/hyp)*50
                    shot = True
        keys = pygame.key.get_pressed()
        selfx , selfy = pygame.mouse.get_pos()
        angle = angle%360
        if (keys[K_f]):
            if  stillx-80 < -x < stillx+120 and stilly-90 < -y < stilly+130 :
                x,y = -stillx,-stilly
                carleft = -1000
                carright = -1000
                carup = -1000
                cardown = -1000
                if mission1 == 0:
                    mission1 = 1
                mode = 0
        if (keys[K_g]):
            if mode == 0:
                if 5200 < EDGX - x < 6100 and 300 < EDGY - y < 800:
                    if mission1 == 1:
                        mission1 = 2
                        affmiss = 1
                stillx,stilly= -x,-y
                TEMPEDGX,TEMPEDGY = EDGX,EDGY
                if angle == 90 :
                    decalx,decaly = -50, 0
                if angle == 270 :
                    decalx,decaly = 50, 0
                if angle == 180 :
                    decalx,decaly = 0, 65
                if angle == 0 :
                    decalx,decaly = 0, -65
                mode = 1
        if (3690-25 < -x+TEMPEDGX+decalx < 3690+10 and 2830-15 < -y+TEMPEDGY+decaly < 2830+10) :
            gun = True
            if mission2 == 0:
                mission2 = 2
                affmiss = 1
            GUN = pygame.image.load('blank.png')
        if mode == 1:
                if keys[K_RIGHT]:
                        if EDGX >= 600 and x > -(9888-1250) and walll(EDGX+decalx,EDGY+decaly):
                            x -= 3
                        if 600 >= EDGX >= 0 and walll(EDGX+decalx,EDGY+decaly):
                            EDGX += 1
                        elif 1200-128 > EDGX >= 600 and x <= -(9888-1250) and walll(EDGX+decalx,EDGY+decaly):
                            EDGX +=1
                        i = 2
                elif keys[K_DOWN]:
                    if wallu(EDGX+decalx,EDGY+decaly):
                        if EDGY >= 300 and y > -(6608 - 750):
                            y -= 3
                        if 300 > EDGY:
                            EDGY +=1
                        elif 750-128 >= EDGY >= 300 and y <= -(6608 - 800):
                            EDGY +=1
                        i = 0
                elif keys[K_LEFT]:
                    if wallr(EDGX+decalx,EDGY+decaly):
                        if EDGX < 600 and x < 0 and wallr(EDGX+decalx,EDGY+decaly):
                            x += 3
                        if 600 <= EDGX < 1200 and wallr(EDGX+decalx,EDGY+decaly):
                            EDGX -= 1
                        elif 600 >= EDGX > 0 and - 12 < x < 12 and wallr(EDGX+decalx,EDGY+decaly):
                            EDGX -= 1
                        i = 1
                elif keys[K_UP] :
                        if EDGY < 375 and y < 0 and walld(EDGX+decalx,EDGY+decaly):
                            y += 3
                        if 375 <= EDGY < 750 and walld(EDGX+decalx,EDGY+decaly):
                            EDGY -=  1
                        elif 375 >= EDGY >= 0 and - 12 < x < 12 and walld(EDGX+decalx,EDGY+decaly):
                            EDGY -= 1
                        i = 3
                if keys[K_UP] or keys[K_RIGHT] or keys[K_DOWN] or keys[K_LEFT]:
                    j = step
                else:
                    j = 0
        if mode == 0:
            if not dirh(EDGX, EDGY) and not dirv(EDGX, EDGY):
                if keys[K_RIGHT]:
                    if walll(EDGX, EDGY):
                        if angle == 90:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if angle == 270:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                        if EDGX >= 600 and x > -(9888 - 1250) and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                x -= 6
                            if vitesse == 1:
                                x -= 10
                            if vitesse == 2:
                                x -= 14
                        if 600 >= EDGX >= 0 and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX += 6
                            if vitesse == 1:
                                EDGX += 10
                            if vitesse == 2:
                                EDGX += 14
                        elif 1200 - 128 > EDGX >= 600 and x <= -(9888 - 1250) and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX += 6
                            if vitesse == 1:
                                EDGX += 10
                            if vitesse == 2:
                                EDGX += 14
                elif keys[K_DOWN]:
                    if wallu(EDGX, EDGY):
                        if angle == 180:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                        if angle == 0:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if EDGY >= 300 and y > -(6608 - 750):
                            comptvitess += 1
                            if vitesse == 0:
                                y -= 6
                            if vitesse == 1:
                                y -= 10
                            if vitesse == 2:
                                y -= 12
                        if 300 > EDGY:
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                        elif 750 - 128 >= EDGY >= 300 and y <= -(6608 - 800):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                elif keys[K_LEFT]:
                    if wallr(EDGX, EDGY):
                        if angle == 90:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                        elif angle == 270:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if EDGX < 600 and x < 0 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                x += 6
                            if vitesse == 1:
                                x += 10
                            if vitesse == 2:
                                x += 14
                        if 600 <= EDGX < 1200 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX -= 6
                            if vitesse == 1:
                                EDGX -= 10
                            if vitesse == 2:
                                EDGX -= 14
                        elif 600 >= EDGX > 0 and - 12 < x < 12 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX -= 6
                            if vitesse == 1:
                                EDGX -= 10
                            if vitesse == 2:
                                EDGX -= 14
                elif keys[K_UP]:
                    if walld(EDGX, EDGY):
                        if angle == 180:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if angle == 0:
                            angle += 90
                            car = pygame.transform.rotate(car, +90)
                        if EDGY < 375 and y < 0 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                y += 6
                            if vitesse == 1:
                                y += 10
                            if vitesse == 2:
                                y += 14
                        if 375 <= EDGY < 750 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14

                        elif 375 >= EDGY >= 0 and - 12 < y < 12 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14
            elif dirv(EDGX, EDGY):
                if keys[K_UP] and (angle == 270 or angle == 90):
                    if walld(EDGX, EDGY):
                        if angle == 180:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if angle == 0:
                            angle += 90
                            car = pygame.transform.rotate(car, +90)
                        if EDGY < 375 and y < 0 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                y += 6
                            if vitesse == 1:
                                y += 10
                            if vitesse == 2:
                                y += 14
                        if 375 <= EDGY < 750 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14

                        elif 375 >= EDGY >= 0 and - 12 < y < 12 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14
                if keys[K_LEFT] and (keys[K_DOWN] and angle == 270 and EDGY != 627 or keys[K_UP] and angle == 90):
                    if wallr(EDGX, EDGY):
                        if EDGX < 600 and x < 0 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                x += 6
                            if vitesse == 1:
                                x += 10
                            if vitesse == 2:
                                x += 14
                        if 600 <= EDGX < 1200 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX -= 6
                            if vitesse == 1:
                                EDGX -= 10
                            if vitesse == 2:
                                EDGX -= 14
                        elif 600 >= EDGX > 0 and - 12 < x < 12 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX -= 6
                            if vitesse == 1:
                                EDGX -= 10
                            if vitesse == 2:
                                EDGX -= 14
                elif keys[K_RIGHT] and keys[K_UP]:
                    if wallu(EDGX, EDGY):
                        if angle == 270:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                elif keys[K_LEFT] and keys[K_UP]:
                    if wallu(EDGX, EDGY):
                        if angle == 270:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                if keys[K_DOWN] and (angle == 90 or angle == 270):
                    if wallu(EDGX, EDGY):
                        if angle == 180:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                        if angle == 0:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if EDGY >= 300 and y > -(6608 - 750):
                            comptvitess += 1
                            if vitesse == 0:
                                y -= 6
                            if vitesse == 1:
                                y -= 10
                            if vitesse == 2:
                                y -= 14
                        if 300 > EDGY:
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                        elif 750 - 128 >= EDGY >= 300 and y <= -(6608 - 800):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                if keys[K_RIGHT] and (keys[K_UP] and angle == 90 or keys[K_DOWN] and angle == 270 and EDGY != 627):
                    if walll(EDGX, EDGY):
                        if EDGX >= 600 and x > -(9888 - 1250) and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                x -= 6
                            if vitesse == 1:
                                x -= 10
                            if vitesse == 2:
                                x -= 14
                        if 600 >= EDGX >= 0 and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX += 6
                            if vitesse == 1:
                                EDGX += 10
                            if vitesse == 2:
                                EDGX += 14
                        elif 1200 - 128 > EDGX >= 600 and x <= -(9888 - 1250) and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX += 6
                            if vitesse == 1:
                                EDGX += 10
                            if vitesse == 2:
                                EDGX += 14
                elif keys[K_RIGHT] and keys[K_DOWN]:
                    if wallu(EDGX, EDGY):
                        if angle == 90:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                elif keys[K_LEFT] and keys[K_DOWN]:
                    if wallu(EDGX, EDGY):
                        if angle == 90:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                if ((keys[K_DOWN]) and not (keys[K_RIGHT])) and ((keys[K_DOWN]) and not (keys[K_LEFT])):
                    if angle == 180:
                        angle += 90
                        car = pygame.transform.rotate(car, 90)
                    if angle == 0:
                        angle -= 90
                        car = pygame.transform.rotate(car, -90)
                if ((keys[K_UP]) and not (keys[K_RIGHT])) and ((keys[K_UP]) and not (keys[K_LEFT])):
                    if angle == 180:
                        angle -= 90
                        car = pygame.transform.rotate(car, -90)
                    if angle == 0:
                        angle += 90
                        car = pygame.transform.rotate(car, 90)
            elif dirh(EDGX, EDGY):
                if keys[K_RIGHT] and (angle == 180 or angle == 0):
                    if walll(EDGX, EDGY):
                        if angle == 90:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if EDGX >= 600 and x > -(9888 - 1250) and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                x -= 6
                            if vitesse == 1:
                                x -= 10
                            if vitesse == 2:
                                x -= 14
                        if 600 >= EDGX >= 0 and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX += 6
                            if vitesse == 1:
                                EDGX += 10
                            if vitesse == 2:
                                EDGX += 14
                        elif 1200 - 128 > EDGX >= 600 and x <= -(9888 - 1250) and walll(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX += 6
                            if vitesse == 1:
                                EDGX += 10
                            if vitesse == 2:
                                EDGX += 14
                if keys[K_DOWN] and (keys[K_LEFT] and angle == 180 and EDGX != 0 or keys[K_RIGHT] and angle == 0):
                    if wallu(EDGX, EDGY):
                        if EDGY >= 300 and y > -(6608 - 750):
                            comptvitess += 1
                            if vitesse == 0:
                                y -= 6
                            if vitesse == 1:
                                y -= 10
                            if vitesse == 2:
                                y -= 14
                        if 300 > EDGY:
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                        elif 750 - 128 >= EDGY >= 300 and y <= -(6608 - 800):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                elif keys[K_DOWN] and (angle == 90 or angle == 270):
                    if wallu(EDGX, EDGY):
                        if EDGY >= 300 and y > -(6608 - 750):
                            comptvitess += 1
                            if vitesse == 0:
                                y -= 6
                            if vitesse == 1:
                                y -= 10
                            if vitesse == 2:
                                y -= 14
                        if 300 > EDGY:
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                        elif 750 - 128 >= EDGY >= 300 and y <= -(6608 - 800):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY += 6
                            if vitesse == 1:
                                EDGY += 10
                            if vitesse == 2:
                                EDGY += 14
                elif keys[K_RIGHT] and keys[K_UP]:
                    if wallu(EDGX, EDGY):
                        if angle == 180:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                elif keys[K_RIGHT] and keys[K_DOWN]:
                    if walld(EDGX, EDGY):
                        if angle == 180:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                if keys[K_LEFT] and (angle == 0 or angle == 180):
                    if wallr(EDGX, EDGY):
                        if angle == 90:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                        elif angle == 270:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                        if EDGX < 600 and x < 0 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                x += 6
                            if vitesse == 1:
                                x += 10
                            if vitesse == 2:
                                x += 14
                        if 600 <= EDGX < 1200 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX -= 6
                            if vitesse == 1:
                                EDGX -= 10
                            if vitesse == 2:
                                EDGX -= 14
                        elif 600 >= EDGX > 0 and - 12 < x < 12 and wallr(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGX -= 6
                            if vitesse == 1:
                                EDGX -= 10
                            if vitesse == 2:
                                EDGX -= 14
                if keys[K_UP] and (keys[K_LEFT] and angle == 180 and EDGX != 0 or keys[K_RIGHT] and angle == 0):
                    if walld(EDGX, EDGY):
                        if EDGY < 375 and y < 0 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                y += 6
                            if vitesse == 1:
                                y += 10
                            if vitesse == 2:
                                y += 14
                        if 375 <= EDGY < 750 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14

                        elif 375 >= EDGY >= 0 and - 12 < x < 12 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14
                elif keys[K_UP] and (angle == 90 or angle == 270):
                    if walld(EDGX, EDGY):
                        if EDGY < 375 and y < 0 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                y += 6
                            if vitesse == 1:
                                y += 10
                            if vitesse == 2:
                                y += 14
                        if 375 <= EDGY < 750 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14

                        elif 375 >= EDGY >= 0 and - 12 < x < 12 and walld(EDGX, EDGY):
                            comptvitess += 1
                            if vitesse == 0:
                                EDGY -= 6
                            if vitesse == 1:
                                EDGY -= 10
                            if vitesse == 2:
                                EDGY -= 14

                elif keys[K_LEFT] and keys[K_UP]:
                    if walld(EDGX, EDGY):
                        if angle == 0:
                            angle -= 90
                            car = pygame.transform.rotate(car, -90)
                elif keys[K_LEFT] and keys[K_DOWN]:
                    if walld(EDGX, EDGY):
                        if angle == 0:
                            angle += 90
                            car = pygame.transform.rotate(car, 90)
                if ((keys[K_RIGHT]) and not (keys[K_UP])) and ((keys[K_RIGHT]) and not (keys[K_DOWN])):
                    if angle == 270:
                        angle += 90
                        car = pygame.transform.rotate(car, 90)
                    if angle == 90:
                        angle -= 90
                        car = pygame.transform.rotate(car, -90)
                if ((keys[K_LEFT]) and not (keys[K_UP])) and ((keys[K_LEFT]) and not (keys[K_DOWN])):
                    if angle == 270:
                        angle -= 90
                        car = pygame.transform.rotate(car, -90)
                    if angle == 90:
                        angle += 90
                        car = pygame.transform.rotate(car, 90)
        if not keys[K_LEFT] and not keys[K_UP] and not keys[K_RIGHT] and not keys[K_DOWN] :
                comptvitess = 0
        if comptvitess < 30:
            vitesse = 0
        elif comptvitess < 80 and comptvitess > 29:
            vitesse = 1
        elif  comptvitess >= 80 :
            vitesse = 2
        if gun:
            surface.blit(imagespis, (1090, 27))
        if shot and gun :
            selfx , selfy = pygame.mouse.get_pos()
            cenx -= changex
            ceny -= changey
            pygame.draw.rect(surface,(0,0,0),(cenx,ceny,5,5))
            if cenx > 1200 or  0 > cenx or ceny > 700 or 0 > ceny:
                cenx , ceny = 600 ,375
                shot = False
        posx , posy = pygame.mouse.get_pos()
        #pygame.draw.line(surface,(0,0,0),(EDGX+25,EDGY+44),(posx,posy))
        surface.blit(dead1, (701  + counth  + x, 661  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead2, (4444 + counth  + x, 4444 + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead3, (4800 + counth  + x, 1850 + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead4, (360   + counth  + x, 209  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead5, (360   + counth  + x, 209  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead6, (1600  + counth  + x, 209  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead7, (2800  + counth  + x, 209  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead8, (4000  + counth  + x, 209  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead9, (5200  + counth  + x, 209  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead1, (6500  + counth  + x, 209  + y), (32 * step, 48 * wh, 32, 48))
        surface.blit(dead3, (4444 + x, 850  + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead4, (1680 + x, 750  + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead5, (4097 + x, 2280 + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead6, (4825 + x, 705  + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead8, (4097 + x, 2280 + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead7, (2000 + x, 1433 + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead9, (2825 + x, 2825 + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead1, (2825 + x, 2825 + countv  + y), (32 * step, 48 * wv, 32, 48))
        surface.blit(dead2, (4810 + x, 713  + countv  + y), (32 * step, 48 * wv, 32, 48))
        if dead0 < 1:
            XDEAD,YDEAD = 2015 + counth , 2088
            surface.blit(dead2, (2015 + counth + x, 2088 + y), (32 * step, 48 * wh, 32, 48))
        else:
            surface.blit(deaddead, (XDEAD+x, YDEAD+y))
            if mission3 == 0:
                mission3 = 2
                affmiss = 1
        if 2047 + counth + x > cenx > 2015 + counth + x and 2136 + y > ceny > 2088 + y and dead0 < 1:
            pox,poy = cenx,ceny
            dead0+=1
            pygame.draw.rect(surface,(255,255,255),(pox+x,poy+y,10,10))
            cenx , ceny = 1250 , 750
        surface.blit(arr1, (995 + x, 400 + y))
        surface.blit(GUN, (3677 + x, 2847 + y))
        pygame.draw.rect(surface, BLACK, (925, 20, 235, 100))
        pygame.draw.rect(surface, DGREY, (927, 22, 231, 96))
        surface.blit(imagesv, (932, 27))
        surface.blit(imagesa, (932, 70))
        surface.blit(texteArg, texteRectArg)
        surface.blit(texteVie, texteRectVie)
        surface.blit(imagesp, (1090, 27))
        if keys[K_c]:
            surface.blit(imagemm, (50, 50))
            surface.blit(imageposho, (-((x // 11) - 85), -((y // 11) - 30)))
            if mission1 == 0 or mission1 == 1 or mission1 == 2:
                surface.blit(imageposmiss, (550, 90))
            if mission2 == 0 or mission2 == 1 or mission2 == 2:
                surface.blit(imageposmiss, (30 + 3677 // 11, 10 + 2847 // 11))
            if mission3 == 0 or mission3 == 1 or mission3 == 2:
                surface.blit(imageposmiss, (30 + 2433 // 11, 10 + 2165 // 11))
            if mode == 1:
                surface.blit(caricon, (50 + (stillx + TEMPEDGX) // 11, 50 - 32 + (stilly + TEMPEDGY) // 11))
        if mission3 == 3:
            start == 2
    if start == 2:
            logopic = surface.blit(end, (0, 0))
            if event.type == QUIT:
                inprogress = False
    pygame.display.flip()