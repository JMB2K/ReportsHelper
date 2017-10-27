#!python3

import pandas as pd

reports = pd.read_csv("/Users/jb/Desktop/reports.CSV")
labels = reports["Label"]
proj_dict = {}

def get_b(r):
    """
    this is getting the page numbers
    from the job file, so we can use
    it to count sets - it just gets
    passed a splice when used here
    """
    b = ''
    for s in r:
        if s.isdigit():
            b=b+s
    if b == '':
        b = 0
    else:
        b = int(b)
    return b


def clean_up(dict):
    """
    this is cleaning the single-sheets
    jobs out of the dict - if they were
    printed more than once I'm not concerned
    """
    singles = []
    for i in dict:
        if dict[i] == [0, 0]:
            singles.append(i)
    for x in singles:
        del dict[x]
    return dict


def sort_jobs(file):
    """
    this is going through the csv file and
    sorting the needed data into a dict with
    plp job num as the key and [num of pages, sets]
    as the value - the sets are set to 0 for now
    """
    for i in file:
        a = i[19:27]
        b = get_b(i[-6:])
        x = [a, b]
        if a in proj_dict:
            if proj_dict[a] == 0:
                pass
            if b > proj_dict[a][0]:
                proj_dict[a][0] = b
        else:
            proj_dict[a] = [b, 0]
    clean_up(proj_dict)
    return proj_dict


def count_sets(file, dict):
    """
    this is going through the csv
    and every time it sees the high
    page num for a plp job num, it
    adds 1 to the sets printed
    """
    for i in file:
        a = i[19:27]
        b = get_b(i[-6:])
        if not a in dict:
            pass
        else:
            if dict[a][0] == b:
                dict[a][1] = dict[a][1] + 1
    return dict


def clean_out(dict):
    """
    the is cleaning out any job
    that only printed one set
    """
    outs = []
    for i in dict:
        if dict[i][1] == 1:
            outs.append(i)
    for x in outs:
        del dict[x]
    return dict



test = sort_jobs(labels)
answer = count_sets(labels, test)
result = clean_out(answer)
for i in result:
    print(i, proj_dict[i])
