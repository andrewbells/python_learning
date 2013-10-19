import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile
# from os import path
# import datetime
# from datetime import date, time, timedelta
# import time

def main():
    
    if path.exists('newfile.txt'):
        src = path.realpath('newfile.txt')
        
#         head, tail = path.split(src)
#         print ('path: ' + head)
#         print ('file: ' + tail)
#         
#         dst = src + '.bak'
#         shutil.copy(src, dst)
#         shutil.copystat(src, dst)
#         os.rename('file.txt', 'newfile.txt')

        #=======================================================================
        # root_dir, tail = path.split(src)
        # shutil.make_archive('archive', 'zip', root_dir)
        #=======================================================================
        with ZipFile('testzip.zip', 'w') as newzip:
            newzip.write('newfile.txt')
            newzip.write('file.txt.bak')
    #===========================================================================
    # #===========================================================================
    # # #f = open('file.txt', 'w+')
    # # f = open('file.txt', 'a+')
    # # for i in range(10):
    # #     f.write('this is line %d\r\n' % (i + 1))
    # # f.close()
    # # 
    # #===========================================================================
    # f = open('file.txt', 'r')
    # if f.mode == 'r':
    #     #contents = f.read()
    #     #print (contents)
    #     fl = f.readlines()
    #     for x in fl:
    #         print (x, end = '')
    #===========================================================================
    #===========================================================================
    # print (os.name)
    # print ('item exists: ' + str(path.exists('file.txt')))
    # print ('item is a file: ' + str(path.isfile('file.txt')))
    # print ('item is a directory: ' + str(path.isdir('file.txt')))
    #===========================================================================
    #===========================================================================
    # print ("item's path: " + str(path.realpath('file.txt')))
    # print ("item's path and name: " + str(path.split(path.realpath('file.txt'))))
    #===========================================================================
    #===========================================================================
    # t = time.ctime(path.getmtime('file.txt'))
    # print (t)
    # print (datetime.datetime.fromtimestamp(path.getmtime('file.txt')))
    #===========================================================================
    #===========================================================================
    # td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('file.txt'))
    # print ('it has been ' + str(td) + ' the file was modified')
    # print ('Or, ' + str(td.total_seconds()) + ' seconds')
    #===========================================================================

if __name__ == '__main__':
    main()
    