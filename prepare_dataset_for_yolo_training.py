import glob
import shutil
import cv2

def get_center(ux,uy,w,h):
	return (ux+int(w/2),uy+(h/2))

def generate_yolo_label(x,y,width,height,img_h,img_w):
	center = get_center(x,y,width,height)
	return (center[0]/img_w,center[1]/img_h,width/img_w,height/img_h)

labels_masterlist_fname = 'label_masterlist_youtube'
# labels_masterlist_fname = 'label_masterlist_youtube_japanesemacaques'
images_folder_dir = '../frames/YOUTUBE_DATASET_FIXED/images/'
labels_folder_dir = '../frames/YOUTUBE_DATASET_FIXED/labels/'
cropped_folder_dir = '../frames/YOUTUBE_DATASET_FIXED/cropped_images_gt/'
master_imgs_dir = '../frames/YOUTUBE/'
labels_master = []

with open(labels_masterlist_fname) as labels_master:
	labels_master = [x.strip().split(" ") for x in labels_master.readlines()]

count = 0
prev = ''
for label in labels_master:
	img = cv2.imread(master_imgs_dir+label[0])
	print(label[0])
	x,y,width,height = [int(x) for x in label[1:]]
	img_h,img_w,img_c = img.shape
	foldername,filename = label[0].split("/")
	shutil.copy(master_imgs_dir+label[0], images_folder_dir+filename)
	cropped = img[y:y+height,x:x+width]
	if prev == filename:
		count+=1
	else:
		count = 0
	cv2.imwrite(cropped_folder_dir+filename[:-4]+"_"+str(count)+".jpg",cropped)

	prev = filename
	with open(labels_folder_dir+filename.replace(".jpg",'.txt'),'a') as outfile:
		outfile.write("0 "+" ".join([str(a) for a in generate_yolo_label(x,y,width,height,img_h,img_w)])+"\n")



