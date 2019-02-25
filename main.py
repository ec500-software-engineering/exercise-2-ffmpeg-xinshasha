import threading
import time
import os
import queue

q1 = queue.Queue()
q2 = queue.Queue()
end1 = 0
end2 = 0
def thread720p():
	global q1,q2,end2
	thread_stop = False
	count = 0
	while thread_stop is False:
		try:
			video = q1.get()
			if video == 'q':
				end2 = 1
				break
			count += 1
			os.system("ffmpeg -i "+video+" -y -b 2M -r 30 -f mp4 -s 1280x720 -loglevel quiet "+str(video[:-4])+"_720p"+".mp4")
			print("720p "+video + 'Converted.')
		except IOError:
			time.sleep(1)
	print('HD Thread Stop')

def thread480p():
	global q1,q2,end1
	thread_stop = False
	count = 0
	while thread_stop is False:
		try:
			video = q2.get()
			if video == 'q':
				end1 = 1
				break
			count += 1
			os.system("ffmpeg -i "+video+" -y -b 2M -r 30 -f mp4 -s 640x480 -loglevel quiet "+str(video[:-4])+"_480p"+".mp4")
			print("480p "+video + 'Converted.')
		except IOError:
			time.sleep(1)
	print('480p Thread Stop')

def main():
	global q1,q2,end1,end2
	HD_convert = threading.Thread(target=thread720p)
	LD_convert = threading.Thread(target=thread480p)
	HD_convert.start()
	LD_convert.start()
	q1.put('video.mp4')
	q2.put('video.mp4')
	q1.put('q')
	q2.put('q')
	while(True):
		if end1 and end2:
			return 0
	"""
	while True:
		file_name = input()
		q1.put(file_name)
		q2.put(file_name)
		if file_name == 'q':
			break
		time.sleep(1)
	"""



	

if __name__ == '__main__':
	main()