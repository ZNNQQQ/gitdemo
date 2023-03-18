[1mdiff --git a/fileinfo.py b/fileinfo.py[m
[1mindex 2792531..76f4bf8 100644[m
[1m--- a/fileinfo.py[m
[1m+++ b/fileinfo.py[m
[36m@@ -6,3 +6,30 @@[m
 # Modifications     :[m
 [m
 # Description           : Show file information for a given file加上注释[m
[32m+[m
[32m+[m[32m# get file information using os.stat()[m
[32m+[m[32m# tested with Python24 vegsaeat 25sep2006[m
[32m+[m[32mfrom __future__ import print_function[m
[32m+[m
[32m+[m[32mimport os[m
[32m+[m[32mimport stat  # index constants for os.stat()[m
[32m+[m[32mimport sys[m
[32m+[m[32mimport time[m
[32m+[m
[32m+[m[32mif sys.version_info >= (3, 0):[m
[32m+[m[32m    raw_input = input[m
[32m+[m
[32m+[m[32mfile_name = raw_input("Enter a file name: ")  # pick a file you have[m
[32m+[m[32mcount = 0[m
[32m+[m[32mt_char = 0[m
[32m+[m[32mtry:[m
[32m+[m[32m    with open(file_name) as f:[m
[32m+[m[32m        line = f.readline()[m
[32m+[m[32m        t_char += len(line)[m
[32m+[m[32m        while line:[m
[32m+[m[32m            count += 1[m
[32m+[m[32m            line = f.readline()[m
[32m+[m[32m            t_char += len(line)[m
[32m+[m[32mexcept FileNotFoundError as e:[m
[32m+[m[32m    print(e)[m
[32m+[m[32m    sys.exit()[m
