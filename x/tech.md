---
theme: ./
colorSchema: dark
layout: cover
background: /assets/images/backmario.gif
title: Technical
---

# Mario JS

https://github.com
<div class="uppercase text-sm tracking-widest">
Jamie John
</div>

<div class="abs-bl mx-14 my-12 flex">
  <img src="/assets/images/logo.png" class="h-8">
  <div class="ml-3 flex flex-col text-left">
        <div><b>Game</b></div>
    <div class="text-sm opacity-50">27 July 2021</div>
  </div>
</div>

<!--
Opening screen
-->

---
layout: intro
---

# technology

kaboom.js is a JavaScript library that helps us make games fast and fun!

<video width="480" height="340" controls>
  <source src="/assets/media/kaboom.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<br>
<br>

<!--
Developed in C/C++

Supports TLS
-->

---
layout: cover
background: /assets/images/i.jpg
---

# Teach machines to sing

What you will need


<!--
PortAudio
-->

---
---

# html

```html
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Mario</title>
    <style>
      body {
        margin: 0;
        overflow: hidden;
      }
    </style>
  </head>
  <body>
    <script src="https://kaboomjs.com/lib/0.5.0/kaboom.js"></script>
    <script src="game.js"></script>
  </body>
</html>
```
---
---

# javascript

```js
kaboom({
  global: true,
  fullscreen: true,
  scale: 2,
  debug: true,
  clearColor: [0, 0, 0, 1],
})

```


---
---
# Javascript - Speed

```js
const MOVE_SPEED = 120
const JUMP_FORCE = 360
const BIG_JUMP_FORCE = 550
let CURRENT_JUMP_FORCE = JUMP_FORCE
const FALL_DEATH = 400
const ENEMY_SPEED = 20

```
<img src="assets/images/mariospeed.jpg" class="h-68">

---
---
# Controls


### Keyboard Shortcuts

|     |     |
| --- | --- |
| <kbd>left</kbd> <kbd>right</kbd> | move left and right |
| <kbd>spacebar</kbd> | jump |

---
layout: intro 
---
<iframe srcdoc="
<html lang=]'en'>
  <head>
    <meta charset='utf-8' />
    <title>Mario Kaboom.js</title>
    <style>
      body {
        margin: 0;
        overflow: hidden;
      }
    </style>
  </head>
  <body>
    <script src='https://kaboomjs.com/lib/0.5.0/kaboom.js'></script>
    <script src='game.js'></script>
  </body>
</html>
" width="100%" height="300"></iframe>
---
layout: intro
---
```js
loadRoot('http://127.0.0.1:8080/')
loadSprite('coin', 'wbKxhcd.png')
loadSprite('evil-shroom', 'KPO3fR9.png')
loadSprite('brick', 'pogC9x5.png')
loadSprite('block', 'M6rwarW.png')
loadSprite('mario', 'Wb1qfhK.png')
loadSprite('mushroom', '0wMd92p.png')
loadSprite('surprise', 'gesQ1KP.png')
loadSprite('unboxed', 'bdrLpi6.png')
loadSprite('pipe-top-left', 'ReTPiWY.png')
loadSprite('pipe-top-right', 'hj2GK4n.png')
loadSprite('pipe-bottom-left', 'c1cYSbt.png')
loadSprite('pipe-bottom-right', 'nqQ79eI.png')

loadSprite('blue-block', 'fVscIbn.png')
loadSprite('blue-brick', '3e5YRQd.png')
loadSprite('blue-steel', 'gqVoI2b.png')
loadSprite('blue-evil-shroom', 'SvV4ueD.png')
loadSprite('blue-surprise', 'RMqCc1G.png')
```
---
layout: intro
---
```js
const maps = [
    [
      '                                      ',
      '                                      ',
      '                                      ',
      '                                      ',
      '                                      ',
      '     %   =*=%=                        ',
      '                                      ',
      '                            -+        ',
      '                    ^   ^   ()        ',
      '==============================   =====',
    ],
    [
      '£                                       £',
      '£                                       £',
      '£                                       £',
      '£                                       £',
      '£                                       £',
      '£        @@@@@@              x x        £',
      '£                          x x x        £',
      '£                        x x x x  x   -+£',
      '£               z   z  x x x x x  x   ()£',
      '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ]
```
---
layout: intro
---

```js
  const levelCfg = {
    width: 20,
    height: 20,
    '=': [sprite('block'), solid()],
    '$': [sprite('coin'), 'coin'],
    '%': [sprite('surprise'), solid(), 'coin-surprise'],
    '*': [sprite('surprise'), solid(), 'mushroom-surprise'],
    '}': [sprite('unboxed'), solid()],
    '(': [sprite('pipe-bottom-left'), solid(), scale(0.5)],
    ')': [sprite('pipe-bottom-right'), solid(), scale(0.5)],
    '-': [sprite('pipe-top-left'), solid(), scale(0.5), 'pipe'],
    '+': [sprite('pipe-top-right'), solid(), scale(0.5), 'pipe'],
    '^': [sprite('evil-shroom'), solid(), 'dangerous'],
    '#': [sprite('mushroom'), solid(), 'mushroom', body()],
    '!': [sprite('blue-block'), solid(), scale(0.5)],
    '£': [sprite('blue-brick'), solid(), scale(0.5)],
    'z': [sprite('blue-evil-shroom'), solid(), scale(0.5), 'dangerous'],
    '@': [sprite('blue-surprise'), solid(), scale(0.5), 'coin-surprise'],
    'x': [sprite('blue-steel'), solid(), scale(0.5)],

  }
```
---
layout: intro
---
```js
 const gameLevel = addLevel(maps[level], levelCfg)

  const scoreLabel = add([
    text(score),
    pos(30, 6),
    layer('ui'),
    {
      value: score,
    }
  ])

  add([text('level ' + parseInt(level + 1) ), pos(40, 6)])
```
---
layout: intro
---
```js
function big() {
    let timer = 0
    let isBig = false
    return {
      update() {
        if (isBig) {
          CURRENT_JUMP_FORCE = BIG_JUMP_FORCE
          timer -= dt()
          if (timer <= 0) {
            this.smallify()
          }
        }
      },
      isBig() {
        return isBig
      },
      smallify() {
        this.scale = vec2(1)
        CURRENT_JUMP_FORCE = JUMP_FORCE
        timer = 0
        isBig = false
      },
      biggify(time) {
        this.scale = vec2(2)
        timer = time
        isBig = true
      }
    }
  }
```


---
layout: code
---

```py {monaco}
from OxySDK import *
import time
import pyaudio
import numpy as np

CHANNELS = 1 # Mono
SAMPLE_RATE = 44100 # Hz
CHUNKSIZE = 1024
WAVE_OUTPUT_FILENAME = "output.wav"

Wifipayload = []

""" Setup """
p = pyaudio.PyAudio()
mCore = OXY_Create()

OXY_Configure(3, SAMPLE_RATE, 1024, mCore)

""" Audio Processing """
def callback(in_data, frame_count, time_info, status):
    frames = [] # A python-list of chunks(numpy.ndarray)
    frames.append(np.frombuffer(in_data, dtype=np.float32))
    #Convert the list of numpy-arrays into a 1D array (column-wise)
    numpydata = np.hstack(frames)
    ret = OXY_PyDecodeAudioBuffer(numpydata, frame_count, mCore)

    if (ret == -3):
        EnergyVol = OXY_GetReceivedOxysVolume(mCore)
        print(EnergyVol)
        """ Processed data """
        out, mDecodedString = OXY_PyGetDecodedData(mCore)
        if (string == "sk98b12a238400767qq9pf96541burp54ere"):
            print("Mr Robot is online!")
        else:
            print(mDecodedString)
        

    return (in_data, pyaudio.paContinue)

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
