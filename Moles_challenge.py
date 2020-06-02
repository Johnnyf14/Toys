import platform
import sys
import time
import random
import numpy as np

def beep(freq, dur):
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(freq, dur)  # freq [Hz] / dur  [ms]
    else:
        # for mac
        import os
        os.system('play -n synth %s sin %s' % (dur/1000, freq))
def l(): #long
    beep(2000, 500)
def s(): # short
    beep(2000, 100)
def A():
    s()
    l()
def B():
    l()
    s()
    s()
    s()
def C():
    l()
    s()
    l()
    s()
def D():
    l()
    s()
    s()
def E():
    s()
def F():
    s()
    s()
    l()
    s()
def G():
    l()
    l()
    s()
def H():
    s()
    s()
    s()
    s()
def I():
    s()
    s()
def J():
    s()
    l()
    l()
    l()
def K():
    l()
    s()
    l()
def L():
    s()
    l()
    s()
    s()
def M():
    l()
    l()
def N():
    l()
    s()
def O():
    l()
    l()
    l()
def P():
    s()
    l()
    l()
    s()
def Q():
    l()
    l()
    s()
    l()
def R():
    s()
    l()
    s()
def S():
    s()
    s()
    s()
def T():
    l()
def U():
    s()
    s()
    l()
def V():
    s()
    s()
    s()
    l()
def W():
    s()
    l()
    l()
def X():
    l()
    s()
    s()
    l()
def Y():
    l()
    s()
    l()
    l()
def Z():
    l()
    l()
    s()
    s()
def N1():
    s()
    l()
    l()
    l()
    l()
def N2():
    s()
    s()
    l()
    l()
    l()
def N3():
    s()
    s()
    s()
    l()
    l()
def N4():
    s()
    s()
    s()
    s()
    l()
def N5():
    s()
    s()
    s()
    s()
    s()
def N6():
    l()
    s()
    s()
    s()
    s()
def N7():
    l()
    l()
    s()
    s()
    s()
def N8():
    l()
    l()
    l()
    s()
    s()
def N9():
    l()
    l()
    l()
    l()
    s()
def N0():
    l()
    l()
    l()
    l()
    l()
def Quest(k):
    if k ==0 :
        A()
    elif k ==1 :
        B()
    elif k == 2:
        C()
    elif k ==3 :
       D()
    elif k ==4 :
        E()
    elif k ==5 :
        F()
    elif k ==6 :
        G()
    elif k ==7 :
        H()
    elif k ==8 :
        I()
    elif k ==9 :
        J()
    elif k ==10 :
        K()
    elif k == 11:
        L()
    elif k == 12:
        M()
    elif k == 13:
        N()
    elif k == 14:
        O()
    elif k == 15:
        P()
    elif k == 16:
        Q()
    elif k == 17:
        R()
    elif k == 18:
        S()
    elif k == 19:
        T()
    elif k == 20:
        U()
    elif k == 21:
        V()
    elif k == 22:
        W()
    elif k == 23:
        X()
    elif k == 24:
        Y()
    elif k == 25:
        Z()
    elif k == 26:
        N1()
    elif k == 27:
        N2()
    elif k == 28:
        N3()
    elif k == 29:
        N4()
    elif k == 30:
        N5()
    elif k == 31:
        N6()
    elif k == 32:
        N7()
    elif k == 33:
        N8()
    elif k == 34:
        N9()
    elif k == 35:
        N0()
    else:
        print("error wrong number")


if __name__ == '__main__':
    table = np.arange(0,35)
    dictionary = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",\
                  16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",\
                  26:1,27:2,28:3,29:4,30:5,31:6,32:7,33:8,34:9,35:0}
    print("how many questions (type in your answer) ?")
    number = input()
    print("starting ",int(number)," questions !\n" )
    time.sleep(1)
    no =0
    while no <= int(number)-1:
        print("\nQuestion no" , no+1)
        # do
        print("listen ! ")
        time.sleep(1)
        print("....3..")
        time.sleep(1)
        print("....2..")
        time.sleep(1)
        print("....1..")
        time.sleep(1)
        key = int(random.choices(table)[0])
        # print("TESTTTT",int(key))
        Quest(key)
        answer = dictionary[key]
        print("what was it (type in your answer) ?")
        typed = input()
        print("typed is ..[", typed, "]   ", end="")
        print("answer is ..[", answer, "]   ", end="")
        if typed == answer:
            print(" ... FUCKIN' CORRECT !")
        else:
            print(" ... BLOODY WRONG !")
        no+=1






