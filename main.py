import threading
import time
import subprocess
import queue

q1 = queue.Queue()
q2 = queue.Queue()
def thread720p():
	global q1,q2,end2
	thread_stop = False
	count = 0
	while thread_stop is False:
		try:
			video = q1.get()
			if video == 'q':
				break
			count += 1
			subprocess.Popen(['ffmpeg','-i',video,'-y','-b','2M','-r','30','-f','avi','-s','1280x720','-loglevel','quiet',str(video[:-4])+"_720p.avi"])
			time.sleep(3)
			print("720p "+video + 'Converted.')
		except IOError:
			time.sleep(1)
	print('HD Thread Stop')

def thread480p():
	global q1,q2
	thread_stop = False
	count = 0
	while thread_stop is False:
		try:
			video = q2.get()
			if video == 'q':
				break
			count += 1
			subprocess.Popen(['ffmpeg','-i',video,'-y','-b','1M','-r','30','-f','avi','-s','640x480','-loglevel','quiet',str(video[:-4])+"_480p.avi"])
			time.sleep(3)
			print("480p "+video + 'Converted.')
		except IOError:
			time.sleep(1)
	print('480p Thread Stop')

def ConvertVideo(video_list):
	global q1,q2,end1,end2
	out_queue = queue.Queue()
	HD_convert = threading.Thread(target=thread720p)
	LD_convert = threading.Thread(target=thread480p)
	HD_convert.start()
	LD_convert.start()
	while not video_list.empty():
		a = video_list.get()
		q1.put(a)
		q2.put(a)
		out_queue.put(a)
		time.sleep(1)
	return out_queue
	

