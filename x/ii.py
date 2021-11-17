from OxySDK import *
import pyaudio
import numpy as np
import time





class SetupAudio:
    #constructor, self ref to instance of class
    def __init__(self, sample_rate, buffer, mode, channels):
        self.sample_rate = sample_rate
        self.buffer = buffer
        self.mode = mode
        self.channels = channels
        
        OXY_Configure(mode, sample_rate, buffer, mCore)
        
    def callback(self, in_data, frame_count, time_info, status):
        self.message = in_data
        frames = []
        frames.append(np.frombuffer(in_data, dtype=np.float32))
        numpydata = np.hstack(frames)
        ret = OXY_PyDecodeAudioBuffer(numpydata, frame_count, mCore)
        
        print(ret)
        
        
        
        
    def start(self):
        stream = p.open(format=pyaudio.paFloat32,
                        channels=self.channels,
                        rate=self.sample_rate,
                        input=True,
                        output=False,
                        stream_callback=self.callback)
                

        stream.start_stream()

        while stream.is_active():
            time.sleep(0.1)

        stream.stop_stream()
        stream.close()

        p.terminate()
        return (in_data, pyaudio.paContinue)
                



p = pyaudio.PyAudio()
mCore = OXY_Create()

x = SetupAudio(44100, 1024, 3, 1)
x.start()
