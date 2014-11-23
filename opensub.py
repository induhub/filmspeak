import os
import sys
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'54.172.239.130'}])
def index_subtitle():
    file_name = sys.argv[1]
    print file_name
    file_hand = open(file_name,"r")
    content  = file_hand.read()
    dialogues = content.split("\r\n\r\n")
    #script = []
    print len(dialogues)
    for each in dialogues[:-1]:
        print each
        try:
            splitsvilla = each.split('\r\n')
            seq = splitsvilla[0]
            start_time,end_time = splitsvilla[1].split("-->")
            dialogue = ' '.join(splitsvilla[2:])
        
            doc = {'seq_no':seq, 'start_time':start_time, 'end_time':end_time, 'dialogue':dialogue}
        
            es.index(index ="top_250",doc_type='subtitle',body=doc)
        except: 
            pass
    return           
index_subtitle()

        
        
        


