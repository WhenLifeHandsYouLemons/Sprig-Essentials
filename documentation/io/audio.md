### `audio` module

#### Initialisation

```py
import board
from sprig_essentials.io import audio

audio_device = audio.Audio()
```

- **Parameters:**
  - `bit_clock_pin`: Pin number for the bit clock (default: `board.GP10`)
  - `word_select_pin`: Pin number for word select (default: `board.GP11`)
  - `data_pin`: Pin number for data (default: `board.GP9`)
- **Returns:** `Audio` object.

The `Audio` class manages audio output via the I2S interface. The initialization functions in this class don't have to be called if you are using this with a Sprig.

---

#### `createI2S`

Creates an I2S output object.

- **Parameters:**
  - `bit_clock_pin`: Pin number for the bit clock
  - `word_select_pin`: Pin number for word select
  - `data_pin`: Pin number for data
- **Returns:** `audiobusio__i2s` object.

Example:

```py
i2s_output = audio_device.createI2S(board.GP10, board.GP11, board.GP9)
```

---

#### `playWaveFile`

Plays a .wav file directly without additional lines.

- **Parameters:**
  - `wave_filename`: Filename of the .wav file
  - `loop`: Boolean for looped playback (default: `False`)
- **Returns:** `None`.

Example:

```py
audio_device.playWaveFile("example.wav", loop=True)
```

---

#### `playMP3File`

Plays an .mp3 file directly without additional lines.

- **Parameters:**
  - `mp3_filename`: Filename of the .mp3 file
  - `loop`: Boolean for looped playback (default: `False`)
- **Returns:** `None`.

Example:

```py
audio_device.playMP3File("example.mp3")
```

---

#### `playAudio`

Plays audio received from `createAudioSample` or `openWaveFile`.

- **Parameters:**
  - `audio`: Audio sample object (could be from [`createAudioSample`](#createaudiosample) or [`openWaveFile`](#openwavefile) or [`openMP3File`](#openmp3file))
  - `loop`: Boolean for looped playback (default: `False`)
- **Returns:** `None`.

Example:

```py
audio_device.playAudio(audio_sample, loop=True)
```

---

#### `isPlaying`

Checks if audio is currently playing.

- **Parameters:** `None`
- **Returns:** `bool`.

Example:

```py
playing = audio_device.isPlaying()
```

---

#### `stopAudio`

Stops all audio playback.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
audio_device.stopAudio()
```

---

#### `pauseAudio`

Pauses current audio playback.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
audio_device.pauseAudio()
```

---

#### `resumeAudio`

Resumes paused audio playback.

- **Parameters:** `None`
- **Returns:** `None`.

Example:

```py
audio_device.resumeAudio()
```

---

#### `createAudioSample`

Creates an audio sample from an input buffer for use with [`playAudio`](#playaudio).

- **Parameters:**
  - `audio_buffer`: [Input audio buffer](#createsinewave) (as `list` object with `int` values)
  - `sample_rate`: Sample rate (default: `8000`)
- **Returns:** `circuitpython_typing__AudioSample` object.

Example:

```py
audio_sample = createAudioSample(audio_buffer, sample_rate=16000)
```

---

#### `openWaveFile`

Opens 8-bit unsigned or 16-bit signed .wav files as samples.

- **Parameters:**
  - `wave_filename`: Filename of the .wav file
- **Returns:** `circuitpython_typing__AudioSample` object.

Example:

```py
wav_sample = openWaveFile("example.wav")
```

---

#### `openMP3File`

Opens .mp3 files as samples.

- **Parameters:**
  - `mp3_filename`: Filename of the .mp3 file
- **Returns:** `circuitpython_typing__AudioSample` object.

Example:

```py
mp3_sample = openMP3File("example.mp3")
```

---

#### `createSineWave`

Generates one period of a sine wave. Used as an example to show how an audio buffer can be created.

- **Parameters:** `None`
- **Returns:** `list[int]`.

Example:

```py
audio_buffer = createSineWave()
```

---
