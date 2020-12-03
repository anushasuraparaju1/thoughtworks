dist=int(input())
mini=0
sedan=0
suv=0
if dist<=75:
    if dist<=18:
        mini+=50+(10*(dist-3))
    else:
        mini+=50+(15*10)+(dist-18)*8
else:
    mini+=8*dist
#print(mini)
if dist<=100:
    if dist<=20:
        sedan+=80+(12*(dist-5))
    else:
        sedan+=80+(15*12)+(dist-20)*10
else:
    sedan+=10*dist
#print(sedan)
if dist<=20:
        suv+=100+(15*(dist-5))
else:
        suv+=100+(15*15)+(dist-20)*12
#print(suv)
print("Mini- Rs. "+str(mini)+","+"Sedan-Rs. "+str(sedan)+","+"SUV-Rs. "+str(suv))
