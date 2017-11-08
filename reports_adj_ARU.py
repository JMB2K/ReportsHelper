
import pandas as pd
import time, os

file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'ARU.log')
reader = pd.read_csv(file_path, low_memory=False)
data = reader[["JOB_FILENAME", "IMAGE_FILENAME"]]  # Get the only data we need
data_dict=dict()

def organize(data):
    """
    This is putting everything into a dict
    with the job number as the key and
    every file printed as a list for the
    value
    """
    temp=[]
    for file in data.iterrows():
        jobname=file[1]["JOB_FILENAME"][:-4]
        temp.append([jobname, file[1]['IMAGE_FILENAME']])
        if not jobname in data_dict:
            data_dict[jobname] = []  # creating keys in dict
    for plp in data_dict:
        temp2=[]  # Making a list of all files printed in job
        for jobs in temp:
            if jobs[0] == plp:
                temp2.append(jobs[1])
        data_dict[plp]=temp2  # Job number = list of files printed
    return data_dict


def count_sets(data_dict):
    """
    Here we just iterate through the
    job numbers, then lists of files.
    Everytime the first file is repeated
    we up the set count - then throw the
    job number and set count into another
    dict
    """
    final_dict=dict()
    for job in data_dict:  #  Iterate job numbers
        count = 0
        checkfile = data_dict[job][0]  # Anytime this shows up, that's one set printed
        for file in data_dict[job]:  # Iterate files for above job number
            if file == checkfile:
                count+=1
        if count > 1:
            final_dict[job]=count
    return final_dict


if __name__ == '__main__':
    """
    Just a bunch of bs to get it to print
    and write to a file so I can easily
    see it to make my changes in Argos
    """
    start=time.time()
    first=organize(data)
    result=count_sets(first)
    new_line = 0
    to_print = ''
    for key, value in sorted(result.items()):
        print(key, '-', value, 'sets', end='\t')
        to_print = to_print + "{} - {} sets".format(key, value) + '\t\t\t'
        new_line += 1
        if new_line % 3 == 0:
            print('\n')
            to_print = to_print + '\n'
    elapsed = time.time() - start
    print("\nThere are {} jobs, sorted in {:.2f} seconds".format(len(result), elapsed))
    to_print = to_print + "\nThere are {} jobs, sorted in {:.2f} seconds".format(len(result), elapsed)
    with open('C:\\Users\\00015\\Desktop\\MultiSets.txt', 'w') as f:
        f.write(to_print)
