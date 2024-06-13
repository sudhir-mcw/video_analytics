import pandas as pd
import sys 
import os 

# provide the report folder path as cmdline argument 
path = sys.argv[1]
BASE_PATH = path
df = pd.read_csv(os.path.join(BASE_PATH,'log.csv'),skiprows=4)
metrics_df = pd.read_csv(os.path.join(BASE_PATH,'timeline.csv'),skiprows=4) 
 
preprocess_times = []
postprocess_times = []
pre_process_clock_cycles=[]
post_process_clock_cycles=[]

i=0
while i<len(df)-1 :
    if "pre process start" in df.iloc[i]['Message'] and "pre process end" in  df.iloc[i+1]['Message']:
        time1 = (df.iloc[i]['When (s)'])
        time2 = (df.iloc[i+1]['When (s)'])
        try:
            time1 = float(time1)
        except ValueError:
            mins = int(time1.split(':')[0])
            mins *=60
            secs = float(time1.split(':')[1])
            secs +=mins
            time1 = secs
        try:
            time2 = float(time2)
        except ValueError:
            mins = int(time2.split(':')[0])
            mins *=60
            secs = float(time2.split(':')[1])
            secs +=mins
            time2 = secs
        preprocess_times.append(abs(time1-time2))    
        index = int(time1 * 1000)
        index = index/1000
        index2 = int(time2 * 1000)
        index2 = index2/1000
        start_index = metrics_df.columns.get_loc('Cycles:CPU Cycles [0]')
        end_index = metrics_df.columns.get_loc('Cycles:CPU Cycles [31]')
        row = metrics_df[(metrics_df['Index (s)'] >= index) & (metrics_df['Index (s)'] <= index2)]
        cpu_cycles_mean = row.iloc[:,start_index:end_index+1].mean(axis=1)
        if i==0:
            print(row.iloc[:,start_index:end_index+1])
        pre_process_clock_cycles.append(cpu_cycles_mean.iloc[-1])
    elif "post process start" in df.iloc[i]['Message'] and "post process end" in  df.iloc[i+1]['Message']:
        time1 = (df.iloc[i]['When (s)'])
        time2 = (df.iloc[i+1]['When (s)'])
        try:
            time1 = float(time1)
        except ValueError:
            mins = int(time1.split(':')[0])
            mins *=60
            secs = float(time1.split(':')[1])
            secs +=mins
            time1 = secs

        try:
            time2 = float(time2)
        except ValueError:
            mins = int(time2.split(':')[0])
            mins *=60
            secs = float(time2.split(':')[1])
            secs +=mins
            time2 = secs
        postprocess_times.append(abs(time1-time2))        
        index = int(time1 * 1000)
        index = index/1000
        index2 = int(time2 * 1000)
        index2 = index2/1000
        start_index = metrics_df.columns.get_loc('Cycles:CPU Cycles [0]')
        end_index = metrics_df.columns.get_loc('Cycles:CPU Cycles [31]')
        row = metrics_df[(metrics_df['Index (s)'] >= index) & (metrics_df['Index (s)'] <= index2)]
        cpu_cycles_mean = row.iloc[:,start_index:end_index+1].mean(axis=1)
        
        cpu_cycles_mean   = row.iloc[:,start_index:end_index+1].mean(axis=1) 
        post_process_clock_cycles.append(cpu_cycles_mean.iloc[-1])
    i+=1

print("Avg Pre process cpu cycles ",sum(pre_process_clock_cycles)/len(pre_process_clock_cycles))
print("pre process : ",(sum(preprocess_times)/len(preprocess_times))*1000 ,'ms')
print("Avg Post process cpu cycles ",sum(post_process_clock_cycles)/len(post_process_clock_cycles))
print("post process : ",(sum(postprocess_times)/len(postprocess_times))*1000 ,'ms')