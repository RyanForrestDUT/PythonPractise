
import xlrd
import xlwt
import os
import sys
import shutil

#######################################################################
# Author: ryan
# Date: Oct 17
# Note: remove the reduplicative strings from excel by rules 
#       whether the content of first column in each row is unique 
#       and then obtain the correspondent frequencies.
#######################################################################

curr_path = os.getcwd()
outResultPath = curr_path + "/OutResults/" 
DICT_NAME = "word_dict.txt"
FILENAME = "/testText.xlsx"

def read_data(filename):
	# open excel file, and obtain sheet object
	work_book = xlrd.open_workbook(filename)
	sheet = work_book.sheet_by_index(0)
	
	# obtain datas by first column
	all_data = sheet.col_values(0)
	
	# transform the data to list 
	mylist = []
	for ds in all_data:
		mylist.append(ds)
		
	return mylist

NCOUNT = 0

# handle the first column values
def get_map_ncount(mylist):
	mymap = {}
	for item in mylist:
		if item in mymap:
			mymap[item] += 1
		else:
			mymap[item] = 1
	
	return mymap
	
# write the processing data to outputData.xls
def write_data(mymap, filename, bOutput = False):
	work_book = xlwt.Workbook()
	sheet = work_book.add_sheet("unique data")
	
	f = open(DICT_NAME, "a", encoding="utf-8")
	if(bOutput):
		f.writelines("*************************************** START:  append unmatched words to the word_dict ******************************" + "\n")
	
	i = 0
	for key in mymap:
		sheet.write(i,0, key)
		sheet.write(i,1,mymap[key])
		i += 1
		if (bOutput):
			f.writelines(key + "\n")
	
	if(bOutput):		
		f.writelines("*************************************** FINISH: append unmatched words to the word_dict ******************************" + "\n")	
	f.close()
	
	if (os.path.exists(outResultPath) == False):
		os.mkdir(outResultPath)
	
	print("output data path: " + outResultPath)
	work_book.save(outResultPath + filename)
	
	
def load_dict(filename):
	word_dict = set()
	f = open(filename, "r", encoding="utf-8")
	for line in f:
#		word = unicode(line.strip(), "utf-8")
		word = str(line.strip())
		word_dict.add(word)
		
	print("word_dict  func --------------------- \n", word_dict, "\n")
	return word_dict
	 
def handle_datas(DICT_NAME):
	datas_pre = read_data(curr_path + FILENAME)
	word_dict = load_dict(DICT_NAME)
	
	print("word_dict--------------------- \n", word_dict, "\n")
	
	mymap = {}
	for data in datas_pre:
		if data not in word_dict:
			if data in mymap:
				mymap[data] += 1
			else:
				mymap[data] = 1
				
	return mymap
	
	   
if __name__ == "__main__":
	print("input  data path: " + curr_path)
	filename = ""
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	if filename == '':
		datas = read_data(curr_path + FILENAME);
	else:
		datas = read_data(curr_path + "/" + filename);
		
	mymap = get_map_ncount(datas)
	write_data(mymap, "outputData.xls")
	
	result_map = handle_datas(DICT_NAME)
	write_data(result_map, "handledata.xls", True)
	
	
	
	
	
