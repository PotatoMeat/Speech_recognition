from pydub import AudioSegment
import os


class converter:

    def __init__(self):
        pass

    def convert_to_wav(self, input):
        split_tup = os.path.splitext(input)
        path = split_tup[0]
        ext = split_tup[1]

        if ext =='.wav':
            return input

        audio = AudioSegment.from_file(input)
        audio.export(path+'.wav', format='wav')

    def convert_to_mp3(self, input):
        split_tup = os.path.splitext(input)
        path = split_tup[0]
        ext = split_tup[1]

        if ext == '.mp3':
            return input

        print((path + '.mp3'))
        print(type(path))

        audio = AudioSegment.from_file(input)
        audio.export((path + '.mp3'), format='mp3')
