import subprocess
import json
import main
from pytest import approx
def get_duration(path):
	return float(json.loads(subprocess.check_output(['ffprobe','-print_format','json','-show_format',path]))['format']['duration'])

def test_duration():
	origin = get_duration('video.mp4')
	main.main()
	video480 = get_duration('video_480p.mp4')
	video720 = get_duration('video_720p.mp4')
	assert(origin == approx(video480,abs=0.1))
	assert(origin == approx(video720,abs=0.1))
	print('Tests Passed.')

test_duration()
