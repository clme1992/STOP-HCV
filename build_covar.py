#get the covariates of age
import re
prefix = "/data/jaga/stophcv/steven/August2016/"
covar_dict = dict()
file_name = prefix + "clinical_data/patient_lib.tsv"
with open(file_name, 'r') as read_file:
    line = read_file.readline()
    for line in read_file:
        line = line.rstrip().split('\t')
        ID = line[0]
        age = int(line[1])
        if age < 0:
            age = None
        else:
            age = 2017 - age
        covar_dict[ID] = age

wrt_file_name = prefix + "test/August2016.covar"
wrt_file = open(wrt_file_name, 'w')
file_name = prefix + "test/August2016.fam"
with open(file_name, 'r') as read_file:
    for line in read_file:
        line = line.rstrip().split(' ')
        ID_lst = re.split('[-_]', line[0])
        ID = ""
        for item in ID_lst:
            if len(item) == 10:
                ID = item
                break
        if ID in covar_dict:
            string = '1' + '\t' + str(covar_dict[ID])
        else:
            string = '1' + '\t'
        print(string, file=wrt_file)