

locks_pos - folder of positive lock images

locks_neg - folder of negative lock images

locks_pos.txt - file with filepaths to positive files. Each line has the filepath, followed by the number of rectangles, followed by the coordinates of each rectangle's opposite corners.

locks_neg.txt - file with filepaths to negative files (currently absolute, should be able to be made relative. I made them absolute during some troubleshooting)

locks_pos.vec - output of the samples from the positive images; vector file

locks_cascade - contains each iteration of the cascade training, with cascade.xml being the most up to date

locks_test - contains lock images to use to test model (may be some overlap with locks_pos though ideally there would not be)

cascadeutils.py - contains a neat function that generates locks_neg.txt

main.py - tests the model



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

opencv_annotation --annotations=locks_post.txt --images=locks_pos/

# Cycles through all images, allows you to draw boxes around them



/usr/local/opt/opencv@3/bin/opencv_createsamples -info locks_pos.txt -w 20 -h 20 -vec locks_pos.vec

# w and h refer to window size width and height. Maybe make a lot larger for our images?
# opencv_createsamples and opencv_traincascade both only are supported from older versions of opencv (3.4), so I have to call them from the absolute filepath.


/usr/local/opt/opencv@3/bin/opencv_traincascade -data cascade/ -vec locks_pos.vec -bg locks_neg.txt -w 20 -h 20 -numPos 80 -numNeg 40 -numStages 10

# numpos, numneg, and numstages are all values to play around with.
