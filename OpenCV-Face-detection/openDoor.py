import get_arcsoft
import gethello
import time
import livecheck
import cv2
import handcheck
import playsound
import serialComu
import RecordWav2
import VoiceRecognition

cap = cv2.VideoCapture(0)

cache = '1' 
while(1):
	people =get_arcsoft.getPeople()  #从虹软获取识别的到的人编号

	name = gethello.getname(people)		#获取到该人对应目录下问好文件
	print(name)
	if name == 'stranger':
		gethello.opendoor('unqualified')
	# print(handcheck.gethand())
	else:
		
		ret, frame = cap.read()
		# show a frame
		#cv2.imshow("capture", frame)
		cv2.imwrite("cap.jpg", frame)
		#cap.release()
		#cv2.destroyAllWindows()
		#拍下当前摄像头前面一张图像
		live = livecheck.checklive()
		print(live)
		if live == None:
			print("live check return None")
		elif float(live) > 0.8:
			gethello.opendoor('VoiceTip')
			RecordWav2.my_record()
			print('Over!') 
			VoiceReturn = VoiceRecognition.RecoLocalWav()
			if VoiceReturn != None:
				VoiceText = VoiceReturn[0]
				if "开门" in VoiceText:
					print('opendoor') #这里应该在写读取’您具有开门资格的语音
					gethello.opendoor('Success')
					serialComu.arduino_opendoor()
			else:
				print("Sorry, Voice can't be recognizied!")
				gethello.opendoor('VoiceNot')
		#serialComu.arduino_opendoor()# 向arduino传递数据进行开门操作
		elif float(live) < 0.9:
			gethello.opendoor('notreal')
			print("It seems that the people infront of the door is not a real man")
			print("It's OK to opendoor!")
		
		#RecordWav2.play()
		#playsound.playsound("01.wav")
		
				
				

			#print(VoiceText)

		


	'''
		if handcheck.gethand() == True:
			print('hands on')
			live = livecheck.checklive('cap.jpg')
			print(live)

			if live == None:
				print("live check return None")
			elif float(live) > 0.9:
				print('opendoor') #这里应该在写读取’您具有开门资格的语音
				gethello.opendoor('qualified')
				#serialComu.arduino_opendoor()# 向arduino传递数据进行开门操作

			elif float(live) < 0.9:
				gethello.opendoor('notreal')
				print("It seems that the people infront of the door is not a real man")
	break #测试专用
	# cache = name
	'''
	
	

	