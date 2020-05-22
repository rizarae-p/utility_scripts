import glob

def parse_vgg(line):
	line = line.replace('"{""name"":""rect"",""x"":','').replace('""y"":','').replace('""width"":','').replace('""height"":','').replace('}","{}"','').replace('"{}",','').split(",")
	folder = line[0][:-8]
	line = [folder+'/'+line[0]]+line[4:]
	return line

labels_list = glob.glob("../frames/LABELS/*.csv")
all_labels = []
for label_fname in labels_list:
	with open(label_fname) as labels:
		labels = [parse_vgg(x.strip()) for x in labels.readlines() if '"{}",0,0,"{}","{}"' not in x and 'filename,file_size,file_attributes' not in x]
	all_labels+=labels

with open('label_masterlist','w') as outfile:
	outfile.write('\n'.join([' '.join(x) for x in all_labels]))