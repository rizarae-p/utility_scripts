#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np 
import glob
import os


vidext = ["wmv","mp4","avi","mov","mkv"]
vidextid = 1
fnames = glob.glob("../youtube/*."+vidext[vidextid])
output_dest = "../frames/YOUTUBE/"
for filename in fnames:
	filename = filename.strip()
	foldername = filename.split("/")[-1].replace("."+vidext[vidextid],"")
	outpath = output_dest+foldername
	if not(os.path.exists(outpath)):
	    os.mkdir(outpath)
	print(foldername)
	cap = cv2.VideoCapture(filename)
	count = 0
	while(cap.isOpened()):
	    ret,frame = cap.read()
	    if ret:
	    	if ((count%30)==0):
	        	cv2.imwrite(outpath+"/"+foldername+"_"+"0"*(3-len(str(count)))+str(count)+".jpg",frame)
	    	count+=1
	    else:
	        break
	cap.release()
