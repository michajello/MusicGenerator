import matplotlib.pylab
import math
import sys

class Image_converter:




    def __init__(self,filename,beats_number,length):
        self.__filename_=filename
        self.__beats_number=beats_number
        self.__image = matplotlib.pylab.imread(filename)
        self.__height = self.__image.shape[0]
        self.__width = self.__image.shape[1]
        self.__mask_size = int(math.floor(math.sqrt(self.__width* self.__height/beats_number)))
        if self.__mask_size > 2:
            self.__mask_size = int(self.__mask_size/2)
        self.__length = length
        self.__colors_number={'magenta': 0,
            'red': 0,
            'white': 0,
            'blue':0,
            'black': 0,
            'grey': 0,
            'yellow': 0,
            'green': 0,
            'cyan': 0
            }
        self.__colors_pointer_function = {'magenta': self.__is_magenta,
                                     'red': self.__is_red,
                                     'white':self.__is_white,
                                     'blue': self.__is_blue,
                                     'black': self.__is_black,
                                     'grey': self.__is_grey,
                                     'yellow': self.__is_yellow,
                                     'green': self.__is_green,
                                     'cyan': self.__is_cyan
                                          }

    __color_frequency={'magenta': 27.5,
            'red': 29.135,
            'white': 30.863,
            'blue':32.703,
            'black': 34.648,
            'grey': 36.708,
            'yellow': 41.203,
            'green': 43.654,
            'cyan': 49.000
            }

    #Use equation to combine note's pitch P =255 * Asin(2pi f t)


    def __obtain_note(self,color,counter):
        (color_name, saturation, value)=color
        pitch = abs(int(255 * value * math.sin(2*math.sin(math.pi * self.__color_frequency[color_name] *saturation))))
        return [counter,pitch,int(127),saturation]



    def get_list_notes(self):
        self.__image=self.__convert_rgb_to_hsv(self.__image)
        notes_list=[];
        counter=0
        sys.stdout.flush()
        while True:
            for i in range(0, self.__height - self.__mask_size, self.__mask_size):
                for j in range(0, self.__width - self.__mask_size, self.__mask_size):
                    color = self.__search_dominant_color_in_patch(i, j)
                    note = self.__obtain_note(color,counter)
                    notes_list.append(note)
                    counter+=color[1];
                    sys.stdout.write("\r%d%%" % (100*counter/self.__beats_number))
                    sys.stdout.flush()

                    if counter >self.__beats_number :
                        return notes_list


    def __convert_rgb_to_hsv(self,image):
        image = image / 255  # before converting to hsv is required to divided all RGB parameters
        return matplotlib.colors.rgb_to_hsv(image)

     # determines color using hsv parameters
     # indexes: 0 - hue 1 - saturation 2 - value

    def __is_black(self,i,j):
        if self.__image[i][j][2] <= 0.12:
            return True
        return False

    def __is_white(self,i,j):
        if self.__image[i][j][1] <= 0.1 and self.__image[i][j][2] >= 0.9:
            return True
        return False

    def __is_grey(self,i,j):
        if self.__image[i][j][1] <= 0.1 and  0.12 < self.__image[i][j][2] <= 0.9 :
            return True
        return False

    def __is_red(self,i,j):
        if self.__image[i][j][0] <0.0833 or self.__image[i][j][0] >= 0.9166:
            return True
        return False
    def __is_yellow(self,i,j):
        if 0.0833 <= self.__image[i][j][0] <0.25:
            return True
        return False

    def __is_green(self,i,j):
        if 0.25 <= self.__image[i][j][0] <0.4166:
            return True
        return False

    def __is_cyan(self,i,j):
        if 0.4166 <= self.__image[i][j][0] <0.5833:
            return True
        return False

    def __is_blue(self,i,j):
        if 0.5833 <= self.__image[i][j][0] <0.75:
            return True
        return False

    def __is_magenta(self,i,j):
        if 0.75 <= self.__image[i][j][0] <0.9166:
            return True
        return False



    def __determine_color(self,i,j):
        if self.__is_black(i,j):
            return 'black'
        if self.__is_white(i,j):
            return 'white'
        if self.__is_grey(i,j):
            return 'grey'
        if self.__is_red(i,j):
            return "red"
        if self.__is_yellow(i,j):
            return 'yellow'
        if self.__is_green(i,j):
            return 'green'
        if self.__is_cyan(i,j):
            return 'cyan'
        if self.__is_blue(i,j):
            return 'blue'
        if self.__is_magenta(i,j):
            return 'magenta'

    def __search_dominant_color_in_patch(self,y,x):

        for key in self.__colors_number:
            self.__colors_number[key]=0

        for i in range(y,y+self.__mask_size):
            if i>=self.__height:
                break
            for j in range(x,x+self.__mask_size):
                if j>=self.__width:
                    break
                color_name=self.__determine_color(i,j)
                self.__colors_number[color_name]+=1

        dominant_color = max(self.__colors_number, key=self.__colors_number.get)
        average_saturation = 0
        average_value = 0
        f=self.__colors_pointer_function[dominant_color];
        counter=0
        for i in range(y,y+self.__mask_size):
            if i>=self.__height:
                break
            for j in range(x,x+self.__mask_size):
                if j>=self.__width:
                    break
                if f(i,j) :
                    average_value+=self.__image[i][j][2]
                    average_saturation+=self.__image[i][j][1]
                    counter+=1;
        return (dominant_color,average_saturation/counter,average_value/counter)

