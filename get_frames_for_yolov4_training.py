import random

train_videos_fname = "video_train.txt"
test_videos_fname = "video_test.txt"
valid_videos_fname = "video_valid.txt"
frame_masterlist_fname = "frame_masterlist.txt"

train_videos = []
test_videos = []
valid_videos = []
frame_masterlist = []

train_frames = []
test_frames = []
valid_frames = []
with open(train_videos_fname) as training_videos:
	train_videos = [x.strip()[:-4] for x in training_videos.readlines()]

with open(test_videos_fname) as testing_videos:
	test_videos = [x.strip()[:-4] for x in testing_videos.readlines()]

with open(valid_videos_fname) as validation_videos:
	valid_videos = [x.strip()[:-4] for x in validation_videos.readlines()]

with open(frame_masterlist_fname) as all_frames:
	frame_masterlist = [x.strip() for x in all_frames.readlines()]

for i in frame_masterlist:
	key = "_".join(i[:-4].replace("data/monkey/","").split("_")[0:-1])
	if key in train_videos:
		train_frames.append(i)
	elif key in test_videos:
		test_frames.append(i)
	elif key in valid_videos:
		valid_frames.append(i)

# print(train_frames)
random.shuffle(train_frames)
random.shuffle(test_frames)
random.shuffle(valid_frames)

with open("30may_yolov4/video_train_frames.txt","w") as outfile:
	outfile.write("\n".join(train_frames))

with open("30may_yolov4/video_test_frames.txt","w") as outfile:
	outfile.write("\n".join(test_frames))

with open("30may_yolov4/video_valid_frames.txt","w") as outfile:
	outfile.write("\n".join(valid_frames))
