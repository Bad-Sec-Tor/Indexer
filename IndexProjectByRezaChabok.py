
#start project
def File(a,b,c,p,i):
    for line in p:
        line=line.replace("."," ")#bejaye . space.
        line=line.replace(","," ")#bejaye , space.
        line=line.lower()#kalmati ke dakhel khat qrar darand ra lowercase mikonad (baraye ngozashtan faeq min lowercase v uppercase.
        line=line.rstrip()
        for word in line.split():#kalamat dakhel khat ra mishekanad.
            if word in c:#agr kalame ie ke behesh residi az qabl dar dictionary c vojod dasht:
                      b=""+str(i) #list b a yekbar khali va meqdar string shomare khat ra be an ezafe kon.
                      a=','+b #meqdar shomare khat ra dar a zakhire mikonad.
                      if b in c[word]:#baraye inke yek kalame momken ast dar yek khat tekrar shode bashad bayad sharti bgozarim ke agar meqdar khat az ghabl dar valiue an kalame boud :
                            continue#anra darnzr ngir.
                      else:c[word]=c[word]+a#dargheir in sourat valiue c ra brozresani kon . 
            else:c[word]=str(i)#baraye dafe aval ke kalame dar dictionary vojod ndarad bayad ebteda anra dar dictionary ezafe konad. 
            #end of for.
        if line != "":i+=1#har dafe ke halghe tekrar beshavad yak khat ezafe mishavad.
        #end of for
def sortwords(x,y):#sort words indexes in file:
    flag=False
    for k ,v in sorted(c.items()):
     if len(k)>=4:#kalamati ke daraye 4 harf v bishtar hastand chap mishavand.
      if k[0]==x or k[0]==y:#agar ebtedaye klme ba x ya y shoro shode bod :
          if flag==False :print(x+":") #harf aval klme ra chap kon.
          flag = True#baraye inke harf aval klme fqt yek bar chap shavad.
          print(k,":",v,".")
while True:
        try:
                        print("***************************** ")
                        print("||What do you want to do?  || ")
                        print("||*************************||  \n||1.show index of file.    ||\n||2.Exit.                  ||\n*****************************")
                        n =(input("Please Enter the number of button:"))
                        if n == "2":
                                print("---------------------------------------------------------------------------------------------------\n°•○●•°•○●---Made by Reza Chabok Shahroudi---●○•°•●○•°")
                                break
                        if n == "1":
                                print("---------------------------------------------------------------------------------------------------\n")
                                address=str(input("Enter The Address Of Your File With .txt(C:\\filename.txt):"))
                                p=open(address)#file ra mikhanad.
                                a=list()#list a
                                b=list()#list b
                                c=dict()#dictionary c
                                i=1#avalin khat meqdarash braber ba1 ast.
                                File(a,b,c,p,i)
                        #morattab karadn word ha bar asas horof alefba(english uppercase):
                                print("INDEX OF WORDS IN THIS FILE:")
                                for i in range(26):
                                    sortwords(chr(i+65),chr(i+65+32))
                                print("----------------------------------------------------------------------------")
                        else:print("This button not exist!!!\n")
        except IOError as e:
                print("*********************************************************************\n*Something bad as %s happened!*\n*********************************************************************"%e)
        #end project.