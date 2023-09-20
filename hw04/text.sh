# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 72 \
      -size $SIZE \
      label:'Clark' \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font
