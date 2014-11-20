import os
import sys
def sub():
    file_name = sys.argv[1]
    file_hand = open(file_name,"r")
    content  = file_hand.read()
    dialogues = content.split("\r\n\r\n")
    script = []
    for each in dialogues[0:2]:
        splitsvilla = each.split('\r\n')
        seq = splitsvilla[0]
        start_time,end_time = splitsvilla[1].split("-->")
        dialogue = ' '.join(splitsvilla[2:])
        script.append((seq,start_time,end_time,dialogue))
    return script           
print sub()

        
        
        


