from manager.memory import Memory
from posting.packet import Packet
from posting.twitterposter import TwitterPoster

from picker.pickerManager import PickerManager, PickerType
from frames.frameManager import FrameManager, FrameType

from format.formatter import Formatter

n = 2

# Pick a colour picker and then get n colours
picker = PickerManager.getPicker(PickerType.SCHEME, n)
colours = picker.getColours()

# Get a frame for n colours of a particular type
frame = FrameManager.getRandomFrame(FrameType.ALL, n)

# Print the method of picking colours
# and the frame used
print(f'Picker: {picker.ptype}')
print(f'Picker subtype: {picker.subtype}')
print(f'Number of colours: {picker.num}')
print(f'Frame type: {frame.style}')
print(f'Frame name: {frame.name}')

# Print the colours used
print(colours)

f = Formatter(frame)

clean, full = f.getImages(colours)

# Save the image
clean.save("clean.png")
full.save("full.png")

tp = TwitterPoster()

packet = Packet(picker, frame, colours)

media = tp.post(packet)

print(media)