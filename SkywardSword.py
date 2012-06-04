from PIL import ImageDraw, Image
import glob, os, sys, re
def convert(a):
    a = re.sub("[^a-zA-Z]",'',a)
    if(a==""):
        return "null"
    return a
def translate(name,text):
    text = re.sub("[dD]","w",text)
    text = re.sub("[eE]","k",text)
    text = re.sub("[gG]","q",text)
    text = re.sub("[iI]","x",text)
    text = re.sub("[oO]","z",text)
    text = re.sub("[pP]","t",text)
    path = sys.path[0]+"\SS\\"
    im = Image.open(path+"a.bmp")
    line = text.split("@")
    length = 0
    for i in line:
        if len(i) > length:
            length = len(i)
    height = len(line)
    length *= 35
    height *= 27
    diagram = Image.new("RGBA",(length,height),(255,255,255))
    longest = 0
    for i in range(0,len(line)):
        letters = []
        pos = 0
        for j in range(0,len(line[i])):
            temp = convert(line[i][j])
            if(temp != "null"):
                letters.append(temp)
        for j in range(0,len(letters)):
            im = Image.open(path+letters[j]+".bmp")
            (le,up,ri,bo) = im.getbbox()
            diagram.paste(im,(pos,i*27,pos+ri,(i+1)*27))
            pos+=ri
        pos = pos
        if(pos > longest):
            longest = pos
    diagram = diagram.crop((0,0,longest,len(line)*27))
    diagram.save(path+name+".png")
    diagram.show()
translate("lol","message from the heavens: @skyward sword")