file_name = "/Users/stevenlin/OneDrive - OnTheHub - The University of Oxford/clinical_data/TR000402_STOP-HCV_Data_Registry_Dataset.txt2"

with open(file_name, 'r') as read_file:
    for line in read_file:
        line = line.rstrip().split('\t')