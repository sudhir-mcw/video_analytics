from perfetto.trace_processor import TraceProcessor
import sys

# if log file name not provided exit
if len(sys.argv) == 0:
    sys.exit(0)

if __name__ == "__main__":
    tp = TraceProcessor(trace=sys.argv[1])

    QUERY = (
    """
    select   t.cpu, avg(value) as frequency, scp.name as event_name, avg(scp.duration) as avg_time  from counter as c
    left join cpu_counter_track as t on c.track_id = t.id,
    (select s.name as name , sc.cpu as cpu,avg(sc.dur) as duration from slice s,sched sc where s.name='pre process' or s.name='post process'  and sc.dur = s.dur group by cpu,s.name) scp
    where t.cpu = scp.cpu and  t.name = 'cpufreq' group by scp.name,t.cpu
    """
    )
    pre_process = {
        'duration':[],
        'frequency':[]
    }
    post_process = {
        'duration':[],
        'frequency':[]
    }
    qr_it = tp.query(QUERY)

    for row in qr_it:
        if row.event_name=='pre process':
            pre_process['duration'].append(row.avg_time)
            pre_process['frequency'].append(row.frequency)   
        elif row.event_name=='post process':
            post_process['duration'].append(row.avg_time)
            post_process['frequency'].append(row.frequency) 

    pre_process_avg_time = sum(pre_process['duration'])/len(pre_process['duration'])
    pre_process_avg_frequency = sum(pre_process['frequency'])/len(pre_process['frequency'])
    post_process_avg_time = sum(post_process['duration'])/len(post_process['duration'])
    post_process_avg_frequency = sum(post_process['frequency'])/len(post_process['frequency'])
    print('Average PreProcess Timing : ',pre_process_avg_time/(10**6),'ms')
    print('Average PostProcess Timing : ',post_process_avg_time/(10**6),'ms')
    print('Pre Process Average Frequency',pre_process_avg_frequency/(10**6),'GHz')
    print('Post Process Average Frequency',post_process_avg_frequency/(10**6),'GHz')
    print('Pre Process Clock Cycles : ',(pre_process_avg_time/(10**9))*(pre_process_avg_frequency*1000))
    print('Post Process Clock Cycles : ',(post_process_avg_time/(10**9))*(post_process_avg_frequency*1000))
