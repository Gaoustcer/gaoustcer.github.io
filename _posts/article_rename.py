import os
import datetime
import time
import sys

today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
file_name = os.listdir('.')
outputfilename = list()
originfilename = list()
for element in file_name:
    if (element[0]>='0' and element[0]<='9') or element.endswith('py') or element=='img':
        pass
    else:
        newelement = today +'-' + element
        outputfilename.append(newelement)
        originfilename.append(element)
print(originfilename)
for i in range(len(originfilename)):

    originfilename[i] = originfilename[i].split('.')[0]
print(originfilename)


for i in range(1,len(originfilename)):
    lines = list()
    head_info = '''
    ---
    layout:     post
    title:      {0}
    subtitle:   {1}
    date:       {2}
    author:     Haihan Gao
    header-img: img/post-bg-swift2.jpg
    catalog: true
    tags:
        - Operation system
    ---

    '''.format(originfilename[i],originfilename[i],today)
     
    with open(originfilename[i]+'.md',"r",encoding="utf-8") as fp:
        for line in fp:
            lines.append(line)
        
        
        with open(outputfilename[i],'a+',encoding='utf-8') as output:
            print(outputfilename[i])
            output.write(head_info)
            output.close()
        with open(outputfilename[i],'a+',encoding='utf-8') as output:
            output.write(''.join(lines))
            output.close()
        
    print(i,'is end')

print("Everthing is OK")     
