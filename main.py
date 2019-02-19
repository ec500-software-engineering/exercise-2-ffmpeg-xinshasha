import threading
import time
import os
import queue

q1 = queue.Queue()
q2 = queue.Queue()

def thread720p():
	global q1,q2
	thread_stop = False
	count = 0
	while thread_stop is False:
		try:
			video = q1.get()
			if video == 'q':
				break
			count += 1
			os.system("ffmpeg -i "+video+" -b 2M -r 30 -f mp4 -s 1280x720 -loglevel quiet "+str(video[:-4])+"_720p_"+str(count)+".mp4")
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
			os.system("ffmpeg -i "+video+" -b 2M -r 30 -f mp4 -s 640x480 -loglevel quiet "+str(video[:-4])+"_480p_"+str(count)+".mp4")
			print("480p "+video + 'Converted.')
		except IOError:
			time.sleep(1)
	print('480p Thread Stop')

def main():
	global q1,q2
	HD_convert = threading.Thread(target=thread720p)
	LD_convert = threading.Thread(target=thread480p)
	HD_convert.start()
	LD_convert.start()
	while True:
		file_name = input()
		q1.put(file_name)
		q2.put(file_name)
		if file_name == 'q':
			break
		time.sleep(1)



	

if __name__ == '__main__':
	main()