class Map:
    def __init__(self, canv, charpos):
        self.c = canv
        self.charpos = charpos
        self.max_width = 220
        self.max_height = 180
        self.dim1 = 150
        self.dim2 = 90
        self.dim3 = 80
        self.dim4 = 80
        self.dim5 = 120
        self.dim6 = 50
        self.dim7 = 70
        self.dim8 = 60
        self.x1 = (self.max_width-self.dim1)/2
        self.y1 = (self.max_height-self.dim2)/2
        self.x2 = (self.max_width-self.dim3)/2
        self.y2 = (self.max_height-self.dim4)/2
        self.x3 = (self.max_width-self.dim5)/2
        self.y3 = (self.max_height-self.dim6)/2
        self.x4 = (self.max_width-self.dim7)/2
        self.y4 = (self.max_height-self.dim8)/2
        self.r1 = [self.x1, self.y1, self.x1+30, self.y1, self.x1+30, self.y1+20, self.x1, self.y1+20]
        self.r2 = [self.x1, self.y1+20, self.x1+30, self.y1+20, self.x1+30, self.y1+60, self.x1, self.y1+60]
        self.r3 = [self.x1, self.y1+60, self.x1+30, self.y1+60, self.x1+30, self.y1+90, self.x1, self.y1+90]
        self.r4 = [self.x1+30, self.y1, self.x1+60, self.y1, self.x1+60, self.y1+20, self.x1+30, self.y1+20]
        self.r5 = [self.x1+30, self.y1+20, self.x1+60, self.y1+20, self.x1+60, self.y1+50, self.x1+30, self.y1+50]
        self.r6 = [self.x1+30, self.y1+50, self.x1+90, self.y1+50, self.x1+90, self.y1+90, self.x1+30, self.y1+90]
        self.r7 = [self.x1+60, self.y1, self.x1+110, self.y1, self.x1+110, self.y1+20, self.x1+60, self.y1+20]
        self.r8 = [self.x1+60, self.y1+20, self.x1+110, self.y1+20, self.x1+110, self.y1+50, self.x1+60, self.y1+50]
        self.r9 = [self.x1+90, self.y1+50, self.x1+110, self.y1+50, self.x1+110, self.y1+90, self.x1+90, self.y1+90]
        self.r10 = [self.x1+110, self.y1, self.x1+150, self.y1, self.x1+150, self.y1+30, self.x1+110, self.y1+30]
        self.r11 = [self.x1+110, self.y1+30, self.x1+150, self.y1+30, self.x1+150, self.y1+50, self.x1+110, self.y1+50]
        self.r12 = [self.x1+110, self.y1+50, self.x1+150, self.y1+50, self.x1+150, self.y1+90, self.x1+110, self.y1+90]
        self.r13 = [self.x2, self.y2, self.x2+40, self.y2, self.x2+40, self.y2+40, self.x2, self.y2+40]
        self.r14 = [self.x2, self.y2+40, self.x2+40, self.y2+40, self.x2+40, self.y2+80, self.x2, self.y2+80]
        self.r15 = [self.x2+40, self.y2+40, self.x2+80, self.y2+40, self.x2+80, self.y2+80, self.x2+40, self.y2+80]
        self.r16 = [self.x3, self.y3, self.x3+20, self.y3, self.x3+20, self.y3+30, self.x3, self.y3+30]
        self.r17 = [self.x3+20, self.y3, self.x3+50, self.y3, self.x3+50, self.y3+30, self.x3+20, self.y3+30]
        self.r18 = [self.x3+50, self.y3, self.x3+90, self.y3, self.x3+90, self.y3+30, self.x3+50, self.y3+30]
        self.r19 = [self.x3+90, self.y3, self.x3+120, self.y3, self.x3+120, self.y3+30, self.x3+90, self.y3+30]
        self.r20 = [self.x3, self.y3+30, self.x3+20, self.y3+30, self.x3+20, self.y3+50, self.x3, self.y3+50]
        self.r21 = [self.x3+100, self.y3+30, self.x3+120, self.y3+30, self.x3+120, self.y3+50, self.x3+100, self.y3+50]
        self.r22 = [self.x4+20, self.y4, self.x4+40, self.y4, self.x4+40, self.y4+40, self.x4+20, self.y4+40]
        self.r23 = [self.x4, self.y4+40, self.x4+60, self.y4+40, self.x4+60, self.y4+70, self.x4, self.y4+70]
        self.p0 = [self.r13, self.r14, self.r15]
        self.p1 = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9, self.r10, self.r11, self.r12]
        self.p2 = [self.r16, self.r17, self.r18, self.r19, self.r20, self.r21]
        self.p3 = [self.r22, self.r23]
        self.visited = [self.r6]
        self.create_plane(self.c, self.getplane(self.charpos))
        self.mylocation(self.c, self.getroomid(self.charpos))

    def create_plane(self, cv, val):
            for i in range(len(val)):
                if val[i] not in self.visited:
		    pass
                    # cv.create_polygon(val[i], outline="green", fill="red")
                else:
                    cv.create_polygon(val[i], outline="green", fill="black")

    def getroomid(self, pos):
        if pos <= 12:
            t = pos-1
            return self.p1[t]
        elif (pos > 12) and (pos <= 15):
            t = pos-13
            return self.p0[t]
        elif (pos > 15) and (pos <= 21):
            t = pos-16
            return self.p2[t]
        elif pos > 21:
            t = pos-22
            return self.p3[t]

    def getplane(self, pos):
        if pos <= 12:
            return self.p1
        elif (pos > 12) and (pos <= 15):
            return self.p0
        elif (pos > 15) and (pos <= 21):
            return self.p2
        elif pos > 21:
            return self.p3

    def mylocation(self, cv, room):
        cv.create_polygon(room, outline="green", fill="blue")




