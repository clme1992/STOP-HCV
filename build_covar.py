#get the covariates of age
import re
import sys
import statistics
impute = 0
if len(sys.argv) > 1 and sys.argv[1] == 'impute':
    impute = 1

med = None
age_lst = list()
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
            age_lst.append(age)
        covar_dict[ID] = age
if impute == 1:
    med = statistics.median(age_lst)

wrt_file_name = ""
if impute == 1:
    wrt_file_name = prefix + "test/August2016.covar.impute"
else:
    wrt_file_name = prefix + "test/August2016.covar"
wrt_file = open(wrt_file_name, 'w')
file_name = prefix + "test/August2016.fam"
missing_num = 0
with open(file_name, 'r') as read_file:
    for line in read_file:
        line = line.rstrip().split(' ')
        ID_lst = re.split('[-_]', line[0])
        ID = ""
        for item in ID_lst:
            if len(item) == 10:
                ID = item
                break
        if (ID in covar_dict) and (covar_dict[ID] != None):
            string = '1' + '\t' + str(covar_dict[ID])
        else:
            missing_num = missing_num + 1
            if (impute == 1):
                string = '1' + '\t' + str(med)
            else:
                string = '1' + '\t'
        print(string, file=wrt_file)
        print(missing_num)