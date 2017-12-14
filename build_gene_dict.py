# built ID dict
import re
from csv import reader
def build_ID_dict():
    clinic2gene = dict()
    gene2clinic = dict()
    equal_ID = dict()
    prefix = "/data/jaga/stophcv/steven/August2016/"
    file_name = prefix + "clinical_data/Data_Registry_Dataset_Sep_2017.csv"
    prim_col = 0
    ID_col = [0,1,2,3,5,6]
    to_prim_key = dict()
    clinic_ID_lst = list()
    with open(file_name, 'r', encoding='latin-1') as read_file:
        for line in reader(read_file):
            #line = line.rstrip().split('\t')
            equal_ID[line[prim_col]] = [None]*len(ID_col)
            for i,col in enumerate(ID_col):
                if (len(line) >= col+1) and (line[col] != ""):
                    equal_ID[line[prim_col]][i] = line[col]
                    to_prim_key[line[col]] = line[prim_col]
                    clinic_ID_lst.append(line[col])
    
    for file_name in [prefix + "clinical_data/TR000384_Enrolment2", prefix + "clinical_data/TR000384_Additional_Enrolment2"]:
        with open(file_name, 'r', encoding='latin-1') as read_file:
            for line in read_file:
                line = line.rstrip().split('\t')
                ID = line[prim_col]
                if ID not in to_prim_key:
                    equal_ID[ID] = ID
                    to_prim_key[ID] = ID

    gene_ID_lst = list()
    file_name = prefix + "test/August2016.fam"
    with open(file_name,'r', encoding='latin-1') as read_file:
        for line in read_file:
            line = line.rstrip().split(' ')
            ID_lst = re.split('[_\-\.]', line[0])
            for item in ID_lst:
                if len(item) == 10:
                    gene_ID_lst.append(item)

    for prim_ID in equal_ID:
        gene_exit = 0
        ID_lst = equal_ID[prim_ID]
        for i,ID in enumerate(ID_lst):
            if ID in gene_ID_lst:
                gene_exit = 1
                gene2clinic[ID] = prim_ID

    return [equal_ID, to_prim_key]