def planets(p):

    for i in range(0,len(circle)):
        if p ==circle[i]:
            return i

    return p + " is not a circle"



    circle = ["mercury", "venus", "earth", "mars", "juipter", "saturn", "uranus", "neptune"]
    print (planets("earth"))



    
