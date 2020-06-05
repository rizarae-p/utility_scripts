import glob

def parse_vgg(line):
	line = line.replace('"{""name"":""rect"",""x"":','').replace('""y"":','').replace('""width"":','').replace('""height"":','').replace('}","{}"','').replace('"{}",','').split(",")
	coords = ['0' if int(x)<0 else x for x in line[4:]]
	folder = line[0][:-8].strip("_").replace("_1","").replace("_2","").replace("_3","").replace("_4","").replace("_5","").replace("_6","").replace("_7","")
	line = [folder+'/'+line[0]]+coords
	return line

labels_list = glob.glob("../frames/YOUTUBE/LABELS/*.csv")
# labels_list = ["../frames/YOUTUBE/LABELS/JapaneseMacaques.csv"]

all_labels = []
for label_fname in labels_list:
	with open(label_fname) as labels:
		labels = [parse_vgg(x.strip()) for x in labels.readlines() if '"{}",0,0,"{}","{}"' not in x and 'filename,file_size,file_attributes' not in x and "(1)" not in x]
	all_labels+=labels

with open('label_masterlist_youtube','w') as outfile:
	outfile.write('\n'.join([' '.join(x) for x in all_labels]))