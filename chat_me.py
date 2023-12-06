#First we import some installed libs

import speech_recognition as sr 
import pyaudio
import pywhatkit
import os
from gtts import gTTS
from playsound import playsound

while True: #to keep the prgram loop

	print ("Recording...") #announce user the begin of rec

	l = sr.Recognizer() #now we perform speech recognition

	with sr.Microphone() as mic: #shortcut for me
		voice = l.listen(mic)    #make it start rec
		com = l.recognize_google(voice) #transcribes our audio
		com = com.lower()	#make it small to reduce confusion

		print(com) #print the transcribe audio unnecssary but to check

		if ("computer") in com : #now we set the name of the model that will use to call it
			com=com.replace("computer","") #we remove it from the order 
			
			if ("play") in com : #set play order to run YT videos
				com=com.replace("play","")
				pywhatkit.playonyt (com) #use pywhatkit to write it on YT
			if ("say") in com : #set say order to repeat speech
				com=com.replace("say","") 
				sound = gTTS(text = com ) #now we convert it to audio
				#now we save sound in mp3 file
				file = 'sound.mp3' #name the file
				sound.save(file)   #save it 
				playsound (file)	#use playsound to run the saved sound
				os.remove(file) #remove it to repeat
			if ("stop") in com : #define stop as quite of loop
				break 
