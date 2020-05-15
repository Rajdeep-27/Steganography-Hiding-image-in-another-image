import sys
import getopt
import cv2 as cv
import numpy as np

def combine(str):
    source=cv.imread(str[0],1)
    hidden=cv.imread(str[1],1)
    if source.shape[0]<hidden.shape[0] or source.shape[1]<hidden.shape[1]:
        raise ValueError("Image to be hidden cannot be larger")
    a=source.shape
    b=hidden.shape
    target=np.zeros(a)
    #print(target.shape)
    for i in range(a[0]):
        for j in range(a[1]):
            for k in range(a[2]):
                if i<b[0] and j<b[1]:
                    p=source[i][j][k] & 240
                    q=hidden[i][j][k] & 240
                    #print(q)
                    q=q>>4
                    target[i][j][k]=p+q
                                        
                else:
                    target[i][j][k]+=source[i][j][k] & 240
    #target[i][j]
    out=target/255.0
    cv.imwrite(str[2],target)
    print("SUCCESS!!")          
    cv.imshow('target',out)
    cv.imshow('source',source)
    cv.imshow('hidden',hidden)
    c=cv.waitKey(0)
    if c==27: cv.destroyAllWindows()                    

def separate(str):
    source=cv.imread(str[0],1)
    a=source.shape
    #print(source)
    target=np.zeros(a)
    for i in range(a[0]):
        for j in range(a[1]):
            for k in range(a[2]):
                m=source[i][j][k]&15
                m=m<<4
                
                target[i][j][k]=  m
    out=target/255.0
    cv.imwrite(str[1],target)
    print("SUCCESS!!")
    cv.imshow('extracted',out)
    cv.imshow('source',source)
    c=cv.waitKey(0)
    if c==27: cv.destroyAllWindows()           

def main():
    arguments=sys.argv[1:]
    options="m:e:"
    long_options=["Merge=","Extract="]
    try:
        str=[]
        args,vals=getopt.getopt(arguments,options,long_options)
        for curr_arg, curr_val in args:
            if curr_arg in ("-m","--Merge"):
                str=curr_val.split(",")
                combine(str)

            if curr_arg in ("-e","--Extract"):
                str=curr_val.split(",")
                separate(str)                                

    except getopt.error as err:
        print("Incorrect options/arguments")            

if __name__ == "__main__":  
    main()
