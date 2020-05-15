import pandas as pd
import urllib.request
import os
import sys
from pydub import AudioSegment


class GetAudio:

    def __init__(self, csv_filepath, destination_folder='audio/', wait=1.5, debug=False):

        self.csv_filepath = csv_filepath
        self.audio_df = pd.read_csv(csv_filepath)
        self.url = 'http://chnm.gmu.edu/accent/soundtracks/{}.mp3'
        self.destination_folder = destination_folder
        self.wait = wait
        self.debug = False

    def check_path(self):

        if not os.path.exists(self.destination_folder):
            if self.debug:
                print('{} does not exist, creating'.format(
                    self.destination_folder))
            os.makedirs('../' + self.destination_folder)

    def get_audio(self):

        self.check_path()

        counter = 0

        for lang_num in self.audio_df['language_num']:
            if not os.path.exists(self.destination_folder + '{}.wav'.format(lang_num)):
                if self.debug:
                    print('downloading {}'.format(lang_num))
                (filename, headers) = urllib.request.urlretrieve(
                    self.url.format(lang_num))
                sound = AudioSegment.from_mp3(filename)
                sound.export('../' + self.destination_folder +
                             "{}.wav".format(lang_num), format="wav")
                counter += 1

        return counter


if __name__ == '__main__':

    csv_file = sys.argv[1]
    ga = GetAudio(csv_filepath=csv_file)
    ga.get_audio()
