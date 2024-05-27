import re

preprocess_time = []
postprocess_time = []
post_process_time =[]

fp=open('output.log','r')

for line in fp.read().strip().split('\n'):
    if line=='':
        break
    if "pre processing" in line:
        time = float(line.split(":")[1].strip())
        preprocess_time.append(time)
    elif "post processing" in line:
        time = float(line.split(":")[1].strip())
        post_process_time.append(time)
fp.close()



print('total entries',len(preprocess_time),len(post_process_time))
print('preprocess',sum(preprocess_time)/len(preprocess_time))
print('postprocess',sum(post_process_time)/len(preprocess_time))
