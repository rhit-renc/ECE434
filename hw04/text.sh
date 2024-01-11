# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.gif
source=./media/boris.png

# From: http://www.imagemagick.org/Usage/text/
convert $source -rotate 90 -size $SIZE \
      -pointsize 72 -gravity South -splice 0x18 \
      -annotate +0+2 'Cat' -append \
      $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

# convert -list font
