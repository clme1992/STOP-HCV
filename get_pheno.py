import re
pheno_file_name1 = "/data/jaga/stophcv/steven/clinical_data/TR000384_ID"
pheno_file_name2 = "/data/jaga/stophcv/steven/clinical_data/TR000402_noCirrhosis_ID"
file_name = "/data/jaga/stophcv/steven/August2016/test/August2016.fam"
wrt_file_name = "August2016.fam.temp"
wrt_file = open(wrt_file_name, 'w')
case_ID = list()
control_ID = list()
with open(pheno_file_name1, 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        case_ID.append(line)
with open(pheno_file_name2, 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        control_ID.append(line)

with open (file_name, 'r') as read_file:
    for line in read_file:
        line = line.rstrip().split(' ')[0]
        line_lst = re.split('[-_]', line)
        ID = ""
        for item in line_lst:
            if len(item) == 10:
                ID = item
                break
        if ID in case_ID:
            line[5] = 2
        elif ID in control_ID:
            line[5] = 1
        else:
            line[5] = 0
        print(' '.join(line), file=wrt_file)


