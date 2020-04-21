#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np 
import glob
import os


vidext = ["wmv","mp4","avi","mov"]
vidextid = 0
fnames = glob.glob("../raw_data/*."+vidext[vidextid])
output_dest = "../frames/"
for filename in fnames:
	filename = filename.strip()
	foldername = filename.split("/")[-1].replace(".wmv","")
	outpath = output_dest+foldername
	if not(os.path.exists(outpath)):
	    os.mkdir(outpath)
	print(foldername)
	cap = cv2.VideoCapture(filename)
	count = 0
	while(True):
	    ret,frame = cap.read()
	    if ret:
	        if (count % 10) == 0:
	            cv2.imwrite(outpath+"/"+foldername+"_"+"0"*(3-len(str(count)))+str(count)+".jpg",frame)
	        count+=1
	    else:
	        break
	cap.release()
