from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '11263666'
API_KEY = '8BKNttikPjgLQv0S8hqevv9b'
SECRET_KEY = '6424687cee1fcf31a4fa7919cfc60515'

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def RecoLocalWav():
	client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
	res = client.asr(get_file_content('01.wav'), 'wav', 8000, {
	    'dev_pid': 1536,
	})

	print (res.get("result"))
	return res.get("result")

RecoLocalWav()