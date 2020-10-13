# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:58:16 2018

@author: Hayreen
"""
def printok(ts = 0.13):
    
    import time
    print(' '*8,'** *')
    time.sleep(ts-0.02)
    print(' '*6,'**','   ','*',' '*9,'*')
    time.sleep(ts)
    print(' '*5,'*',' '*6,'*',' '*8,'*',' '*6,'*')
    time.sleep(ts)
    print(' '*4,'*',' '*8,'*',' '*7,'*',' '*4,'*')
    time.sleep(ts)
    print(' '*3,'*',' '*10,'*',' '*6,'*',' '*2,'*')
    time.sleep(ts)
    print(' '*2,'*',' '*12,'*',' '*5,'*','*')
    time.sleep(ts)
    print(' '*3,'*',' '*10,'*',' '*6,'*',' '*2,'*')   
    time.sleep(ts)
    print(' '*4,'*',' '*8,'*',' '*7,'*',' '*4,'*')
    time.sleep(ts)
    print(' '*5,'*',' '*6,'*',' '*8,'*',' '*6,'*')
    time.sleep(ts)
    print(' '*6,'**','   ','*',' '*9,'*',' '*8,'*')
    time.sleep(ts+0.02)
    print(' '*8,'** *',' '*11,'*',' '*10,'*')

if __name__ == '__main__':
    printok()
