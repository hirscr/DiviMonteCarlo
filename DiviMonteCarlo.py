# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from math import sin,radians,cos,sqrt
from pprint import pprint
from random import randint, random

from graphics import *

pi=3.1415926

tierlist=["diamond","platinum","gold","silver","copper"]
tiers= {"diamond" : {"allocated" : 10000000,
                     "nodes" :     33,
                     "radius" :  0.0,
                     "area" : 0.0,
                     "weight" : 12000,
                     "chance" : 0,
                     "circle" : Circle(Point(0,0),0),
                     "count" : 0,
                     "color" : "LightSteelBlue1",
                     "textcolor" : "black"},

        "platinum" : {"allocated" : 3000000,
                     "nodes" :     100,
                     "radius" :  0.0,
                     "area" : 0.0,
                     "weight" : 3450,
                     "chance" : 0,
                     "circle" : Circle(Point(0,0),0),
                     "count" : 0,
                     "color" : "gray90",
                     "textcolor" : "black"},

        "gold" : {"allocated" : 1000000,
                     "nodes" :     249,
                     "radius" :  0.0,
                     "area" : 0.0,
                     "weight" : 1100,
                     "chance" : 0,
                     "circle" : Circle(Point(0,0),0),
                     "count" : 0,
                     "color" : "gold",
                     "textcolor" : "black"},

        "silver" : {"allocated" : 300000,
                     "nodes" :     557,
                     "radius" :  0.0,
                     "area" : 0.0,
                     "weight": 315,
                     "chance" : 0,
                     "circle" : Circle(Point(0,0),0),
                     "count" : 0,
                     "color" : "gray70",
                     "textcolor" : "white"},

        "copper" : {"allocated" : 100000,
                     "nodes" :     701,
                     "radius" :  0.0,
                     "area" : 0.0,
                     "weight": 100,
                     "chance" : 0,
                     "circle" : Circle(Point(0,0),0),
                     "count" : 0,
                     "color" : "sienna3",
                     "textcolor" : "white"}
        }

maxR = 500
maxWin = 1000
center=maxWin/2
maxA = pi * maxR ** 2

def Rad2Cart(r,theta):
    x = r * cos(radians(theta)) + center
    y = r * sin(radians(theta)) + center
    return Point(x,y)



def main():
    global tiers

    totalStakes=10080*12
    tiers["diamond"]["area"] = maxA
    win = GraphWin('target', maxWin,maxWin,autoflush=False) # give title and dimensions

    totalWeight =0

    for tier in tiers:  #get the total weight of nodes
        tiers[tier]["coins"] = tiers[tier]['allocated'] * tiers[tier]['nodes']
        totalWeight += tiers[tier]["weight"] * tiers[tier]["nodes"]

    for tier in tiers:
        tiers[tier]["chance"] = tiers[tier]["weight"] / totalWeight  #chance for a single masternode to get a reward

    #work out temporary areas starting with copper then scale
    tiers["copper"]["area"]=tiers["copper"]["chance"]*tiers["copper"]["nodes"]
    tiers["copper"]["radius"]=sqrt(tiers["copper"]["area"]/pi)
    lastR=tiers["copper"]["radius"]
    
#get the radii for circles
    for tier in tierlist[::-1]:
        if tier != "copper":
            tiers[tier]["area"]=tiers[tier]["chance"]*tiers[tier]["nodes"]
            tiers[tier]['radius']=sqrt(tiers[tier]["area"]/pi+lastR**2)
        lastR=tiers[tier]['radius']
        print(tier + " radius: " + str(tiers[tier]["radius"]))

    scale=maxR/tiers["diamond"]['radius']

#scale radii to full screen
    for tier in tierlist:
        tiers[tier]['radius']=tiers[tier]['radius']*scale
        print(tier + " radius: " + str(tiers[tier]["radius"]))

    for tier in tierlist:
        tiers[tier]['circle']=Circle(Point(center,center), tiers[tier]['radius'])
        print(tier +" area: "+ str(tiers[tier]["area"]))
        tiers[tier]['circle'].setFill(tiers[tier]['color'])
        tiers[tier]['circle'].draw(win)
        for line in range(1, tiers[tier]["nodes"]+1):
            l = Line(Point(center, center), Rad2Cart(tiers[tier]['radius'], 360 / tiers[tier]["nodes"] * line+.5))
            l.draw(win)
        message = Text(Point(maxR, maxR-tiers[tier]['radius'] + 20), tier)
        message.setTextColor(tiers[tier]["textcolor"])
        message.setStyle("bold")
        #message.draw(win)

    for dot in range(1,totalStakes):
        r=maxR*sqrt(random())
        if r<tiers["copper"]["radius"]:
            tiers["copper"]["count"] +=1
        elif r<tiers["silver"]["radius"]:
            tiers["silver"]["count"] += 1
        elif r<tiers["gold"]["radius"]:
            tiers["gold"]["count"] += 1
        elif r<tiers["platinum"]["radius"]:
            tiers["platinum"]["count"] += 1
        else:
            tiers["diamond"]["count"] += 1

        theta=randint(1,360)
        p=Rad2Cart(r,theta)
        p.draw(win)

    update()
    label = Text(Point(100, 120), 'Divi Masternode Target')
    for tier in tierlist:
        s=" {tier} total = {total} each = {each:.2f}".format(tier=tier,total=tiers[tier]["count"],each=tiers[tier]["count"]/tiers[tier]["nodes"])
        message = Text(Point(maxR, maxR - tiers[tier]['radius'] + 20), s)
        message.setTextColor(tiers[tier]["textcolor"])
        message.setStyle("bold")
        message.draw(win)

    label.draw(win)
    pprint(tiers)
    win.getMouse()
    win.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
