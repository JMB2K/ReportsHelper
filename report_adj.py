
import os, time
import pandas as pd
from collections import OrderedDict as OD

file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'reports.csv')
reports = pd.read_csv(file_path)
labels = reports["Label"]

working_dict = OD()

def get_job_num(file):
    """
    This is splitting the data
    to get the plp job number
    """
    x = file.split('\\')
    return x[3]


def main():
    """
    So much looping!  But this is
    sorting through all files and
    organizing by PLP job number,
    then adding all files printed
    in that job to a list and counting
    how many times the first file name
    appears in that list to show how
    many sets were printed, and returning
    that info in a dict.
    """
    temp_dict = OD()
    for jobs in labels:  # Going through labels and pulling the PLP job number, then adding to dict
        job_num=get_job_num(jobs)
        if not job_num in temp_dict:
            temp_dict[job_num] = []

    for job_nums in temp_dict:  # Going through the temp dict getting the PLP job numbers
        temp_list = []
        for x in labels:  # Going through labels and putting all files from PLP job number into a list
            if get_job_num(x) == job_nums:
                temp_list.append(x)
        temp_dict[job_nums] = temp_list  # The PLP job number is the key and the list of files printed is the value
    for job_nums in temp_dict:
        count = 0
        checker = temp_dict[job_nums][0]  # The first file in the list is set as a check point
        for last_one in temp_dict[job_nums]:  # Itterating the list value and checking how many times the first file shows up
            if last_one == checker:
                count += 1
        working_dict[job_nums] = count  # The PLP job number is the key and the number of sets printed is the value
    final_dict = OD()
    for key, value in working_dict.items():
        if value > 1:
            final_dict[key] = value
    return final_dict


if __name__ == "__main__":
    start = time.time()
    final_dict = main()
    new_line = 0
    to_print = ''
    for key, value in sorted(final_dict.items()):
        print("{} - {} sets".format(key, value), end='\t')
        to_print = to_print + "{} - {} sets".format(key, value) + '\t\t\t'
        new_line += 1
        if new_line % 3 == 0:
            print('\n')
            to_print = to_print + '\n'
    elapsed = time.time() - start
    print("\nThere are {} jobs, sorted in {:.2f} seconds".format(len(final_dict), elapsed))
    to_print = to_print + "\nThere are {} jobs, sorted in {:.2f} seconds".format(len(final_dict), elapsed)
    with open('C:\\Users\\00015\\Desktop\\MultiSets.txt', 'w') as f:
        f.write(to_print)


