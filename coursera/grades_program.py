import tkinter.filedialog
import grades1

al_filename = tkinter.filedialog.askopenfilename()
al_file = open(al_filename, 'r')

al_histfilename = tkinter.filedialog.asksaveasfilename()
al_histfile = open(al_histfilename, 'w+')



#for line in al_file:
#    print (line)

#read the grades into a list
grades = grades1.read_grades(al_file)
#count the grades per range
range_counts = grades1.count_grade_ranges(grades)

#print(range_counts)
#write the histogram to the file
grades1.write_histogram(range_counts, al_histfile)

al_file.close()
al_histfile.close()

'''
0-9:   *
10-19: *
20-29: **
..
..
90-99: ***
100:   *
'''
