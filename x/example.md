---
theme: ./
colorSchema: dark
layout: cover
background: /assets/images/school.jpg
title: Speechy
---

# Speechy

Science, Technology, Engineering and Mathematics
<div class="uppercase text-sm tracking-widest">
Jamie John
</div>

<div class="abs-bl mx-14 my-12 flex">
  <img src="/assets/images/logo.png" class="h-8">
  <div class="ml-3 flex flex-col text-left">
        <div><b>Discover Cyber</b></div>
    <div class="text-sm opacity-50">22 Sept 2021</div>
  </div>
</div>

<!--
Opening screen
-->

---
layout: image-right
image: /assets/images/folk.jpg
---

# What is Speechy?

Allows data to be encoded inside of audio waves using audible or inaudible ultrasound tones to a receiver 

<br>
<br>

- 🔐 **Security** - focus on security
- 🧑‍💻 **Developer Friendly** - multiply languages
- 🎧 **Transfer** - only requires a speaker
- 🎤 **Receive** - listens continuously
- 📤 **Portable** - runs on any device
- 🛠 **Hackable** - anything is possible

<br>
<br>

<!--
Developed in C/C++

Supports TLS
-->

---
layout: image-right
image: /assets/images/code.jpg
---

# Requirements

A computer with a microphone and speakers

* Software
  * python 3
  * pip
  * pyAudio
  * numpy
  * speechy

<!--
PortAudio
-->

---
layout: cover
background: /assets/images/python.jpeg
---

# Install
https://www.python.org/

<div class="uppercase text-sm tracking-widest">
  
</div>

<div class="abs-bl mx-14 my-12 flex">
  <img src="/assets/images/logo.png" class="h-8">
  <div class="ml-3 flex flex-col text-left">
        <div><b>Speechy</b></div>
    <div class="text-sm opacity-50">22 Sept 2021</div>
  </div>
</div>

<!--
The first contact with a programming language should be as simple as possible. And Python is an easy-to-learn programming language that has some really useful features for a beginning programmer. The code is quite easy to read when compared to other programming languages, and it has an interactive shell into which you can enter your programs and see them run.
In addition to its simple language structure and an interactive shell with which to experiment, Python has some features that greatly augment the learning process and allow you to put together simple animations for creating your own games.
For example, with one line of code, it possible to create a “Hello World” program and in two lines it is possible to create a code in which the computer requests the user’s name and returns it with a length — or any other simple operation with the user’s name string. If that same code is written in Java, C or Pascal, you must use eight or nine lines of code.
Another good reason is that Kids Won’t Outgrow Python. Scientists use Python to work with large data sets. Software engineers build neural networks and other forms of artificial intelligence with this versatile language.
Also most popular kid's games, like Minecraft and Roblox, provide a good Python API that allows more advanced users to extend the game’s capabilities and resources, offering new game experiences, which, in my particular case, has increased curiosity and desire of my son learning Python.
-->

---
layout: image-right
image: /assets/images/kid.jpeg
---

# Install

Few things to get us up and running
* pyaudio allows to use the audio device
* numpy allows us to do calculations on the audio
* speechy is the software that send and recieves audio data


```bash
python3 -m pip install pyaudio, numpy, speechy
```


<div class="uppercase text-sm tracking-widest">
  
</div>

<div class="abs-bl mx-14 my-12 flex">
  <img src="/assets/images/logo.png" class="h-8">
  <div class="ml-3 flex flex-col text-left">
        <div><b>Speechy</b></div>
    <div class="text-sm opacity-50">22 Sept 2021</div>
  </div>
</div>

---
layout: image-right
image: /assets/images/code.jpg
---

# Receive

```py
from OxySDK import *
import time
import pyaudio
import numpy as np

CHANNELS = 1 # Mono
SAMPLE_RATE = 44100 # Hz
CHUNKSIZE = 1024

p = pyaudio.PyAudio()
m = OXY_Create()
OXY_Configure(3, SAMPLE_RATE, 1024, m)
```

[<img src="/assets/images/board.jpg" class="m-20 h-20 rounded shadow" />](/assets/images/i.py)

---
layout: image-right
image: /assets/images/code.jpg
---
# Receive
```py
def callback(in_data, frame_count, time_info, status):
    frames = []
    frames.append(np.frombuffer(in_data, dtype=np.float32))
    numpydata = np.hstack(frames)
    ret = OXY_PyDecodeAudioBuffer(numpydata, frame_count, m)
    if (ret == -3):
        out, mDecodedString = OXY_PyGetDecodedData(m)
        if (mDecodedString[:9] == "sk98b12a"):
            print("Mr Robot is online!")
        else:
            print(mDecodedString)

    return (in_data, pyaudio.paContinue)
```
---
layout: image-right
image: /assets/images/code.jpg
---
# Receive
```py
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
```
---
layout: image-right
image: /assets/images/code.jpg
---

# Send a message

Send an encoded message

```py
""" Send data """
def snd(name):
    cmd = './speak -dk ' + name + ' -sp 1 -o demo.wav -m 0'
    os.system(cmd)
```

Output:

<audio controls>
  <source src="/assets/media/code.wav" type="audio/wav">
Your browser does not support the audio element.
</audio>
---
layout: image-right
image: /assets/images/v.png
---
Vigenere cipher

```bash
import itertools

table = "0123456789ABCDEFGHIJKLMNOPQRSTUV"

def encrypt(clear_text, key_str):
    global table
    key = itertools.cycle(key_str)
    cipher_text = bytearray()
    for ch in clear_text:
        if ch in table:
            row_offset = table.find(ch)
            col_offset = table.find(next(key))
            cipher_text.append(ord(table[(row_offset+col_offset)%30]))
        else:
            cipher_text.append(ord(ch))

    return cipher_text.decode('utf-8')
```

---
layout: image-right
image: /assets/images/debug.jpeg
---

# Few tips

<br>

  * We can send as far as the hearing range
  * We don’t need an active network or internet connection
  * We can encrypt our communications
  * Explore and have fun
<br>

---
layout: image-right
image: /assets/images/debug.jpeg
---
Chellenge:

Listen for our message that's contionously playing and decipher it!

<br>
<br>
Recap to install the software

```bash
python3 -m pip install pyaudio, numpy, speechy
```

<br>
Dont forget to to turn the volume up!
---
layout: image-right
image: /assets/images/code.jpg
---
# Demo


<video width="500" height="30" controls>
  <source src="/assets/media/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


