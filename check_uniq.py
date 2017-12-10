'''check if the first column really is the unique identifier to link to the genetic data'''
import re
prefix = "/data/jaga/stophcv/steven/August2016/"
file_name = prefix + "clinical_data/TR000402_STOP-HCV_Data_Registry_Dataset.txt2"
ID_dict = dict()
prim_col = 0
ID_col = [0,1,2,3,5,6]
with open(file_name, 'r') as read_file:
    for line in read_file:
        line = line.rstrip().split('\t')
        ID_dict[line[prim_col]] = [None]*len(alt_col)
        for i,col in enumerate(alt_col):
            if (len(line) >= col+1) and (line[col] != ""):
                ID_dict[line[prim_col]][i] = line[col]

gene_ID_lst = list()
file_naem = prefix + "test/August2016.fam"
with open(file_name) as read_file:
    for line in read_file:
        line = line.rstrip().split(' ')
        ID_lst = re.split('_-', line[0])
        for item in ID_lst:
            if len(item) == 10:
                gene_ID_lst.append(ID)

uniq_cnt_lst = list()
for prim_ID in ID_dict:
    ID_lst = ID_dict[prim_ID]
    uniq_cnt = -1
    for ID in ID_lst:
        if ID in gene_ID_lst:
            uniq_cnt = uniq_cnt + 1
    uniq_cnt_lst.append(uniq_cnt)

for item in uniq_cnt_lst:
    if item >= 0:
        print(item)