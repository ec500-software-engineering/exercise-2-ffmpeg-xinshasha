import subprocess
import json
import main
import time
import queue
from pytest import approx
class TestCase:
	def test_duration(self):
		q1 = queue.Queue()
		q1.put('v1.avi')
		q1.put('v2.avi')
		q1.put('q')
		v_list=main.ConvertVideo(q1)
		time.sleep(5)
		while not v_list.empty():
			vi = v_list.get()
			if vi == 'q':
				break
			origin = get_duration(vi)
			video480 = get_duration(vi[:-4]+'_480p.avi')
			video720 = get_duration(vi[:-4]+'_720p.avi')
			assert(origin == approx(video480,abs=0.1))
			assert(origin == approx(video720,abs=0.1))


def get_duration(path):
	return float(json.loads(subprocess.check_output(['ffprobe','-print_format','json','-show_format',path]))['format']['duration'])
