from socket import  *
from pygame import mixer

def playMusic(songToPlay):
	mixer.init()
	mixer.music.load("/home/pi/Desktop/" + songToPlay + ".mp3")
	mixer.music.play(0)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print ("The Server is ready to receive")
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode("utf-8")
	playMusic(modifiedMessage)

