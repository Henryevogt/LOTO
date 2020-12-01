from PIL import Image, ImageDraw, ImageFilter
import os
import random

def create_training_imgs():



    #
    tag = Image.open('tag.png') # Replace with Tag File Location
    #f = open() # open the xml or txt file where the image location data will be stored

    for filename in os.listdir('backgrounds'): # for all the images in the background image folder

        bg = Image.open('backgrounds/' + filename)
        if bg.size[0] < tag.width or bg.size[1] < tag.height:
            continue
        synth = bg.copy()
        x = random.randint(0, synth.size[0] - tag.width)
        y = random.randint(0, synth.size[1] - tag.height)
        synth.paste(tag, (x, y), tag)
        synth.save("synth/" + filename)
        labelimg(filename, tag, x, y)
        label_cascade(filename, tag, x, y)


    return

def labelimg(img_name, tag, x, y):
    f = open("yololabels/" + img_name[:-3] + 'txt', 'w+')
    f.write("1 "  + str(x) + " " + str(y) + " " + str(tag.width) + " " + str(tag.height) + "\n")
    # tag = 1
    # hasp = 0
    # lock = 2

def label_cascade(img_name, tag, x, y):
    f = open('tags_cascade.txt', 'a+')
    f.write("synth/" + img_name + " 1 " + str(x) + " " + str(y) + " " + str(tag.width) + " " + str(tag.height) + "\n")

def create_negatives(num = 1000):
    n = 0
    for filename in os.listdir('backgrounds'):
        if n == num:
            break

        f = Image.open('backgrounds/' + filename)
        negative = f.copy()
        negative.save('synth_neg/' + filename)

        n += 1

    return

def copy_desired_imgs():

    f = open("bgImgList.txt")
    line = f.readline()[:-1]
    while(line):
        img = Image.open("validation/" + line)
        img.save('backgrounds/' + line)
        line = f.readline()[:-1]


def generate_negative_description_file(objname):
    # Creates a .txt file in the proper structure for training the negative images

    with open(objname + '_neg.txt', 'w') as f:

        for filename in os.listdir('synth_neg'):
            f.write('/Users/henryevogt/projects/AI/SyntheticDataset/synth_neg/' + filename + '\n')


#copy_desired_imgs()
#create_training_imgs()
#create_negatives()
generate_negative_description_file('tags')

#if __name__ == "__main__":
#    main()