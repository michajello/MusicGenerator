from random import randint
from Image_converter import Image_converter
class Music_Generator:


    def __init__(self, beats_number,filename,narcotic_rate,length):
        self.__beats_number=beats_number
        self.__beat_iterator=0
        self.__filename=filename
        self.__narcotic_rate=narcotic_rate
        self.__length=length


    def generate_part(self, beats_number_part, narcotic_rate,notes_list):
        x = 1
        notes_per_second =randint(1,narcotic_rate)
        delayment=1/notes_per_second

        while x <= beats_number_part:
            x+=1
            for i in range (0,notes_per_second):
                notes_list.append([self.__beat_iterator+delayment*i,randint(0,237),randint(0,127),1])

            self.__beat_iterator += 1

    def generate_music(self,  narcotic_rate):
       notes_list = []
       if self.__filename !=None:
            image_generator=Image_converter(self.__filename,self.__beats_number,self.__length)
            notes_list=image_generator.get_list_notes()

       else:
            x = 1
            part_length=int(self.__beats_number/narcotic_rate)

            while x<=narcotic_rate:
                 self.generate_part(part_length,narcotic_rate,notes_list)
                 x+=1

            generated_music_beats=x*part_length
            if generated_music_beats < self.__beats_number:
                x+=1

       return notes_list





