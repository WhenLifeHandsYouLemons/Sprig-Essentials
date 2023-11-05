import board
import displayio, audiobusio, audiocore
import array
import math

# Reset all pins to allow new connections
displayio.release_displays()

# To show return tooltips for functions
class pin_number:pass
class audiobusio__i2s:pass
class audiocore__rawsample:pass
class audiocore__wavefile:pass

def createI2S(bit_clock_pin: pin_number,
              word_select_pin: pin_number,
              data_pin: pin_number) -> audiobusio__i2s:
    i2s = audiobusio.I2SOut(bit_clock_pin, word_select_pin, data_pin)
    return i2s

# Automates audio bus creation, assumes you're using a Sprig
def quickStartAudio() -> audiobusio__i2s:
    i2s = createI2S(board.GP10, board.GP11, board.GP9)
    return i2s

# Generate one period of sine wave.
def createSineWave():
    length = 8000 // 440
    sine_wave = array.array("H", [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15) + 2 ** 15)

# Creates an audio sample from an input buffer and can be used with the playAudio function
def createAudioSample(audio_buffer,
                      sample_rate = 8000) -> audiocore__rawsample:
    audio_sample = audiocore.RawSample(audio_buffer, sample_rate=sample_rate)
    return audio_sample

# Samples must be 8-bit unsigned or 16-bit signed .wav files
def openWaveFile(wave_filename: str) -> audiocore__wavefile:
    wave_file = audiocore.WaveFile(wave_filename)
    return wave_file

# Plays audio returned from createAudioSample or openWaveFile
def playAudio(i2s: audiobusio__i2s,
              audio,
              loop: bool = False) -> None:
    i2s.play(audio, loop=loop)

def playWaveFile(wave_filename: str,
                 i2s: audiobusio__i2s,
                 loop: bool = False) -> None:
    playAudio(i2s, openWaveFile(wave_filename), loop)

# Checks if sound is being played
def isPlaying(i2s: audiobusio__i2s) -> bool:
    if i2s.playing:
        return True
    return False

# Stop all audio from playing on the inputted audio bus
def stopAudio(i2s: audiobusio__i2s) -> None:
    i2s.stop()
