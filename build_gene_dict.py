# built ID dict
import re
from csv import reader
def build_ID_dict(local=0):
    clinic2gene = dict()
    equal_ID = dict()
    prefix = "/data/jaga/stophcv/steven/August2016/"
    file_name = prefix + "clinical_data/Data_Registry_Dataset_Sep_2017.csv"
    if local == 1:
        file_name = "/Users/stevenlin/OneDrive - OnTheHub - The University of Oxford/clinical_data/STOP-HCV_Data_Registry_Will.csv"
    prim_col = 0
    ID_col = [0,6,8,9,12,13,19,22]
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

    return [equal_ID, to_prim_key]

def build_cleanID_dict(local=0):
    cleanID_dict = dict()
    prefix = "/data/jaga/stophcv/steven/August2016/"
    if local == 1:
        prefix = "/Users/stevenlin/OneDrive - OnTheHub - The University of Oxford/"
    file_name = prefix + "cleanID_map.tsv"
    with open(file_name, 'r') as read_file:
        for line in read_file:
            line = line.rstrip().split('\t')
            cleanID_dict[line[0]] = line[1]
    return cleanID_dict