#try this
import time 
import tracemalloc
import pandas as pd
from flashtext import KeywordProcessor
import csv
begin = time.time() 
tracemalloc.start()
keyword_dictionary = pd.read_csv('french_dictionary.csv', header=None, index_col=1, squeeze=True).to_dict()
keyword_processor = KeywordProcessor()
for i,v in keyword_dictionary.items():
    keyword_dictionary[i] = list(v.split())

with open('find_words.txt','r') as f:
    listl=[]
    for line in f:
        strip_lines=line.strip()
        listli=strip_lines.split()
        m=listl.append(''.join(listli))

    keyword_dictionary1={}
    for i,v in keyword_dictionary.items():
        if v[0] in listl:
            keyword_dictionary1[i]=v
        #frequency.csv
        header = ['English word','French word','Frequency']
        with open('frequency.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            with open('/content/data.txt','r') as f:
                for word in listl:
                    count=0
                    for line in f:
                        for i in line.split():
                            if(i==word):
                                count+=1
                    value =""
                    for a,b in keyword_dictionary1.items():
                        if b[0] == word:
                            value = a
                    data = [word,value,count]
                    writer.writerow(data)
        keyword_processor.add_keywords_from_dict(keyword_dictionary1)
        with open('t8.shakespeare.txt', 'r+') as file:
                content = file.read()
                new_content = keyword_processor.replace_keywords(content)
                file.seek(0)
                file.truncate()
                file.write(new_content)

first_size, first_peak = tracemalloc.get_traced_memory()
peak = first_peak/(1024*1024)
print(peak)
tracemalloc.stop()
time.sleep(1)
end = time.time()
print(end-begin)