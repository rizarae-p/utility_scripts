from sklearn.model_selection import train_test_split

with open("videolist", "rb") as f:
	data = f.read().split('\n')
	x_train ,x_test = train_test_split(data,test_size=0.3)       #t
	x_test, x_valid = train_test_split(x_test,test_size=0.3)       #t
with open("video_train.txt","w") as ftrain:
	ftrain.write("\n".join(x_train))

with open("video_test.txt","w") as ftest:
	ftest.write("\n".join(x_test))

with open("video_valid.txt","w") as fvalid:
	fvalid.write("\n".join(x_valid))
