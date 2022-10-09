import enum
from objc_util import ObjCClass


class AVAudioQuality(enum.Enum):
  AVAudioQualityMin = 0
  AVAudioQualityLow = 32
  AVAudioQualityMedium = 64
  AVAudioQualityHigh = 96
  AVAudioQualityMax = 127


# [Core Audio その２ AudioStreamBasicDescription | objective-audio](https://objective-audio.jp/2008/03/30/core-audio-audiostreambasicdes/)
class AVFormatIDKey(enum.Enum):  #UInt32
  kAudioFormatLinearPCM = 1819304813
  kAudioFormatAppleIMA4 = 1768775988
  kAudioFormatMPEG4AAC = 1633772320
  kAudioFormatMACE3 = 1296122675
  kAudioFormatMACE6 = 1296122678
  kAudioFormatULaw = 1970037111
  kAudioFormatALaw = 1634492791
  kAudioFormatMPEGLayer1 = 778924081
  kAudioFormatMPEGLayer2 = 778924082
  kAudioFormatMPEGLayer3 = 778924083
  kAudioFormatAppleLossless = 1634492771


AVAudioSession = ObjCClass('AVAudioSession')
AVAudioRecorder = ObjCClass('AVAudioRecorder')

# xxx: `objc_util` では、設定済み？
# NSURL = ObjCClass('NSURL')


def avaudio_recorder_record(
    file_name,
    duration,
    AVFormatIDKey=AVFormatIDKey.kAudioFormatLinearPCM,
    AVSampleRateKey=44100.00,
    AVNumberOfChannelsKey=2,
    AVEncoderAudioQualityKey=AVAudioQuality.AVAudioQualityMedium):
  pass


if __name__ == '__main__':
  avaudio_recorder_record(file_name='./outPut/record.wav', duration=3)

