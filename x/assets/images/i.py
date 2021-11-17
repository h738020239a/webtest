from OxySDK import *
import time
import pyaudio
import numpy as np

CHANNELS = 1  # Mono
SAMPLE_RATE = 44100  # Hz
CHUNKSIZE = 1024

mDecodedString = ""  # char array

""" Setup """
p = pyaudio.PyAudio()
mCore = OXY_Create()
OXY_Configure(3, SAMPLE_RATE, 1024, mCore)

""" Audio Processing """


def callback(in_data, frame_count, time_info, status):
    frames = [np.frombuffer(in_data, dtype=np.float32)]  # A python-list of chunks(numpy.ndarray)
    # Convert the list of numpy-arrays into a 1D array (column-wise)
    numpydata = np.hstack(frames)
    ret = OXY_PyDecodeAudioBuffer(numpydata, frame_count, mCore)

    # Debug Process ret
    if ret == -2:
        print("Decode started")
    elif ret >= 0:
        print(ret)
    elif ret == -3:
        energy_vol = OXY_GetReceivedOxysVolume(mCore)
        print(energy_vol)
        size_a = OXY_GetDecodedData(mDecodedString, mCore)
        print(size_a)

    return in_data, pyaudio.paContinue

    # Scaled floating point representation (paFloat32) uses +1.0 and -1.0 as the maximum and minimum respectively.


stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()
