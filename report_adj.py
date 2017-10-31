
import pandas as pd

reports = pd.read_csv("C:\\Users\\00015\\Desktop\\reports.CSV")
labels = reports["Label"]

working_dict = dict()

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
	temp_dict = dict()
	for jobs in labels:  # Going through labels and pulling the PLP job number, then adding to dict
		job_num=get_job_num(jobs)
		if not jobs in temp_dict:
			temp_dict[job_num] = []
	for job_nums in temp_dict:  # Going through the temp dict getting the PLP job numbers
		temp_list = []
		for x in labels:  # Going through labels and putting all files from PLP job number into a list
			if get_job_num(x) == job_nums:
				temp_list.append(x)
		temp_dict[job_nums] = temp_list  # The PLP job number is the key and the list of files printed is the value
	for inst in temp_dict:
		count = 0
		checker = temp_dict[inst][0]  # The first file in the list is set as a check point
		for last_one in temp_dict[inst]:  # Itterating the list and checking how many times the first file shows up
			if last_one == checker:
				count += 1
		working_dict[inst] = count  # The PLP job number is the key and the number of sets printed is the value
	return working_dict
