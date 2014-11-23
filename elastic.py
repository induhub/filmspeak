import os
import subprocess
movies = open('srt_files.txt','r')
for each in movies.readlines():
    print each
    subprocess.Popen(['python','opensub.py','/home/ubuntu/'+each.replace('\n','')])
    
