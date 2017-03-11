import pyaudio
import wave
import sys

#CHUNK = 1024
CHUNK = 256
FILE = "output.wav"
if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s fileneame.wav" % sys.argv[0])
    #sys.exit(-1)

#wf = wave.open(sys.argv[1], 'rb')
wf = wave.open(FILE, 'rb')


p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

print len(data)
while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()