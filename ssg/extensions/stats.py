from ssg import hooks
import time
start_time=None
total_written=0

def start_build():
    global start_time
    start_time=time.localtime()

def written():
    global total_written
    total_written+=1

def stats():
        final_time=time.localtime()-start_time
        average= final_time/total_written if total_written!=0
        report="Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"
        print(report.format(total_written,final_time,average))
