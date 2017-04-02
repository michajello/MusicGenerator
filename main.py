from argparse import ArgumentParser
from miditime.miditime import MIDITime

from Music_Generator import Music_Generator


parser = ArgumentParser(description='Program generates narcotic sounds.')
parser.add_argument('-f', '--filename', type=str, default='sample.midi', help='Name of output file')
parser.add_argument('-l', '--length', type=int, default=30, help='Length of song in seconds')
parser.add_argument('-s', '--speed', type=int, default=120, help='Beats per minute')
parser.add_argument('-r', '--rate', type=int, choices=[1,2,3,4,5,6],default=1, help='Narkotic rate; allowed values:[1,2,3,4,5,6]')
parser.add_argument('-i', '--image' ,type=str ,help='Image to convert into music')

arguments = parser.parse_args()
filename = arguments.filename
image=arguments.image
narcotic_rate=arguments.rate


length=arguments.length
speed = arguments.speed
beats_number=speed*length/60


mymidi = MIDITime(speed, filename)
# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
note_list = []
music_creator= Music_Generator(beats_number, image, narcotic_rate, length)


# Add a track with those notes
note_list=music_creator.generate_music(narcotic_rate)
mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()
