#/usr/bin/python3
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

def read_data(path):
    # open excel file, and obtain sheet object
    work_book = xlrd.open_workbook(path)
    sheet = work_book.sheet_by_index(0)
    
    # obtain datas by first column
    all_data = sheet.col_values(0)
    
    return all_data

NCOUNT = 0

# handle the first column values
def del_duplication(data):
    mylist = []
    for ds in data:
        mylist.append(ds)

    mymap = {}
    for item in mylist:
        if item in mymap:
            mymap[item] += 1
        else:
            mymap[item] = 1
    
    return mymap
    
# write the processing data to outputData.xls
def write_data(mymap, path):
    work_book = xlwt.Workbook()
    sheet = work_book.add_sheet("unique data")
    
    i = 0
    for key in mymap:
        sheet.write(i,0, key)
        sheet.write(i,1,mymap[key])
        i += 1
        
    outResultPath = path + "/OutResults/" 
    if (os.path.exists(outResultPath) == False):
        os.mkdir(outResultPath)
    
    print("output data path: " + outResultPath)
    work_book.save(outResultPath + "outputData.xls")
    
if __name__ == "__main__":
    curr_path = os.getcwd()
    print("input  data path: " + curr_path)
    filename = sys.argv[1]
    if filename == '':
        datas = read_data(curr_path + "/tmall_com_first1000.xls");
    else:
        datas = read_data(curr_path + "/" + filename);
    mymap = del_duplication(datas)
    write_data(mymap, curr_path)
    
    