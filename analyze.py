import pandas as pd
import sys 
import os 

path = sys.argv[1]

BASE_PATH = path


df = pd.read_csv(os.path.join(BASE_PATH,'log.csv'))
metrics_df = pd.read_csv(os.path.join(BASE_PATH,'timeline.csv')) 
pre_process_cpu_util =[]
post_process_cpu_util =[]
 
preprocess_times = []
postprocess_times = []

pre_process_clock_frequency=[]
post_process_clock_frequency=[]


pre_process_clock_cycles=[]
post_process_clock_cycles=[]

for i in range(0,len(df),2):
    # print(df.iloc[i]['Message'])
    if "pre process" in df.iloc[i]['Message'] and "pre process" in  df.iloc[i+1]['Message']:
        time1 = df.iloc[i]['When (s)']
        time2 = df.iloc[i+1]['When (s)']
        preprocess_times.append(abs(time1-time2))    

        index = int(time1 * 1000)
        index = index/1000
        # print("index : ",index)
        row = metrics_df[metrics_df['Index (s)'] == index]

        # row['cpu_percent'] = row.iloc[:, 1:33].mean(axis=1)
        cpu_percent = row.iloc[:, 1:33].mean(axis=1)
        pre_process_cpu_util.append(cpu_percent.iloc[-1])
        
        
        clock_freq  = row.iloc[:,129:160].mean(axis=1) 
        pre_process_clock_frequency.append(clock_freq.iloc[-1])   
       
        clock_cycle = row.iloc[:,161:192].mean(axis=1) 
        pre_process_clock_cycles.append(clock_cycle.iloc[-1])

    elif "post process" in df.iloc[i]['Message'] and "post process" in df.iloc[i+1]['Message']:
        time1 = df.iloc[i]['When (s)']
        time2 = df.iloc[i+1]['When (s)']
        postprocess_times.append(abs(time1-time2)) 

        index = int(time1 * 1000)
        index = index/1000
        # print("index : ",index)
        row = metrics_df[metrics_df['Index (s)'] == index]

        # row['cpu_percent'] = row.iloc[:, 1:33].mean(axis=1)
        cpu_percent = row.iloc[:, 1:33].mean(axis=1)
        post_process_cpu_util.append(cpu_percent.iloc[-1]) 

        clock_freq  = row.iloc[:,129:160].mean(axis=1) 
        post_process_clock_frequency.append(clock_freq.iloc[-1])   

        clock_cycle = row.iloc[:,161:192].mean(axis=1) 
        post_process_clock_cycles.append(clock_cycle.iloc[-1])

preprocess_df = pd.DataFrame({'Preprocess Time': preprocess_times})
postprocess_df = pd.DataFrame({'Postprocess Time': postprocess_times})

print("pre process : ",preprocess_df.mean().iloc[-1] ,'s')
print("post process : ",postprocess_df.mean().iloc[-1],'s')

print("pre process cpu utlization ",sum(pre_process_cpu_util)/len(pre_process_cpu_util))
print("post process cpu utlization ",sum(post_process_cpu_util)/len(post_process_cpu_util))


print("pre process cpu frequency ",sum(pre_process_clock_frequency)/len(pre_process_clock_frequency))
print("post process cpu frequency ",sum(post_process_clock_frequency)/len(post_process_clock_frequency))

print("Avg Pre process cpu cycles ",sum(pre_process_clock_cycles)/len(pre_process_clock_cycles))
print("Avg Post Process cpu cycles ",sum(post_process_clock_cycles)/len(post_process_clock_cycles))


