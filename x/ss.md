---
theme: ./
colorSchema: dark
layout: cover
background: /assets/images/girl.jpg
title: Acoustic
---

# Acoustic
<div class="uppercase text-sm tracking-widest">
Jamie John
</div>

<div class="abs-bl mx-14 my-12 flex">
  <img src="/assets/images/logo.png" class="h-8">
  <div class="ml-3 flex flex-col text-left">
        <div><b>Discover Cyber</b></div>
    <div class="text-sm opacity-50">13 August 2021</div>
  </div>
</div>

<!--
Opening screen
-->

---
layout: image-right
image: /assets/images/girl.jpg
---

Introduction:

* Background
* Non-Conformal Malware Attacks
* Applications needing microphone access
* Attack Anatomy
* Stem Demo

---
layout: cover
background: /assets/images/Supplay2020.png
---
f

---
layout: cover
background: /assets/images/c3apsule.png
---
f

---
layout: cover
background: /assets/images/bitwhisper.png
---
---
layout: cover
background: /assets/images/gsmem.png
---
---
layout: image-right
image: /assets/images/girl.jpg
---

# What

Encode data in audio waves using audible or inaudible tones that takes place with no network connection.


<br>
<br>

- 🔐 **Secure** - focus on security
- 🧑‍💻 **Developer Friendly** - multiply languages
- 🎧 **Transfer** - send using your speakers
- 🎤 **Receive** - listens continuously via mic
- 📤 **Portable** - C++, Mobile, Arm, Python
- 🛠 **Hackable** - anything is possible

<br>
<br>

<!--
Developed in C/C++

Supports TLS
-->

---
layout: image-right
image: /assets/images/hacker.png
---

# Build

Tech

<br>

* Hardware - Inexpensive
  * Speaker 
  * Microphone

<br>


* Software
  * Python
  * C/C++
  * iOS/Android
  * Armv6 / 7

<!--
PortAudio
-->

---
layout: image-right
image: /assets/images/hacker.png
---

# Install

* python - 2/3
* pip - package manager
* pyAudio - drive sound
* microphone permissions

<div class="uppercase text-sm tracking-widest">

</div>

<div class="abs-bl mx-14 my-12 flex">
  <img src="/assets/images/logo.png" class="h-8">
  <div class="ml-3 flex flex-col text-left">
        <div><b>Discover Cyber</b></div>
    <div class="text-sm opacity-50">13 August 2021</div>
  </div>
</div>

---
layout: image-right
image: /assets/images/code.jpg
---

# Software

Python Example:

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


...
```
---
layout: image-right
image: /assets/images/code.jpg
---
# Software

Callback

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
# Software
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

# Software

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
image: /assets/images/debug.jpeg
---
Chellenge:

Send an encoded message that sends the wifi details and then send back a message to say done.

Recap to install the software

```bash
python3 -m pip install pyaudio, numpy, speechy
```
Dont forget to to turn the volume up!
---
layout: image-right
image: /assets/images/board.jpg
---
# Hardware


<video width="500" height="30" controls>
  <source src="/assets/media/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---
layout: image-right
image: /assets/images/debug.jpeg
---

# Send a message

<br>

  * We can send as far as the hearing range
  * It doesn’t need an active network or internet connection
  * Can you tweak it?

<br>
