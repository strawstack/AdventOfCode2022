gif = None
packed_fields = ["0", "0", "0", "0", "0", "0", "0", "0"]

def write(b):
    gif.write(b)

def pad(s, size): # pad
    return "0" * (size - len(s)) + s

def baseTenToBytesLE(baseTenNum):
    hexDigits = pad(hex(baseTenNum)[2:], 4)
    return bytearray([int(hexDigits[2:], 16), int(hexDigits[:2], 16)])

def gif(filename):
    global gif

    # Clear file
    gif = open(f"{filename}.gif", "w")
    gif.close()

    # Open for reading
    gif = open(f"{filename}.gif", 'ab')

def GIF89a():
    write(b'\x47\x49\x46\x38\x39\x61')

def width(baseTenNum):
    write(baseTenToBytesLE(baseTenNum))

def height(baseTenNum):
    write(baseTenToBytesLE(baseTenNum))

def global_color_table_flag(booleanFlag):
    global packed_fields
    packed_fields[0] = "1" if booleanFlag else "0"

def color_resolution(baseTenNum):
    global packed_fields
    binNumberStr = pad(bin(baseTenNum)[2:], 3)
    packed_fields[1] = binNumberStr[0]
    packed_fields[2] = binNumberStr[1]
    packed_fields[3] = binNumberStr[2]

def table_sort_flag(booleanFlag):
    global packed_fields
    packed_fields[4] = "1" if booleanFlag else "0"

def size_of_global_color_table(baseTenNum):
    global packed_fields
    binNumberStr = pad(bin(baseTenNum)[2:], 3)
    packed_fields[5] = binNumberStr[0] 
    packed_fields[6] = binNumberStr[1]
    packed_fields[7] = binNumberStr[2]
    write(bytearray([int("".join(packed_fields), 2)]))

    # Clear buffer
    for i in range(len(packed_fields)):
        packed_fields[i] = "0"

def background_color_index(baseTenNum):
    write(bytearray([baseTenNum]))

def pixel_aspect_ratio(baseTenNum):
    write(bytearray([baseTenNum]))

def global_color_table_color(colorTuple):
    write(bytearray(colorTuple))

def application_extension():
    write(b'\x21\xFF')

def block_size(baseTenNum):
    write(bytearray([baseTenNum]))

def application_name(stringName):
    lst = [ord(x) for x in stringName]
    write(bytearray(lst))

def index_of_block(baseTenNum):
    write(bytearray([baseTenNum]))

def number_of_repetitions(baseTenNum):
    write(baseTenToBytesLE(baseTenNum))

def end_block():
    write(b'\x00')

def graphic_control_extension():
    write(b'\x21\xF9')

def reserved(baseTenNum):
    binNumberStr = pad(bin(baseTenNum)[2:], 3)
    packed_fields[0] = binNumberStr[0]
    packed_fields[1] = binNumberStr[1]
    packed_fields[2] = binNumberStr[2]

def disposal_method(baseTenNum):
    binNumberStr = pad(bin(baseTenNum)[2:], 3)
    packed_fields[3] = binNumberStr[0]
    packed_fields[4] = binNumberStr[1]
    packed_fields[5] = binNumberStr[2]

def user_input_flag(booleanFlag):
    packed_fields[6] = "1" if booleanFlag else "0"

def transparent_color_flag(booleanFlag):
    packed_fields[7] = "1" if booleanFlag else "0"
    write(bytearray([int("".join(packed_fields), 2)]))

    # Clear buffer
    for i in range(len(packed_fields)):
        packed_fields[i] = "0"

def delay_time(baseTenNum):
    write(baseTenToBytesLE(baseTenNum))

def transparent_color_index(baseTenNum):
    write(bytearray([baseTenNum]))

def image_separator():
    write(b'\x2C')

def image_left(baseTenNum):
    write(baseTenToBytesLE(baseTenNum))

def image_top(baseTenNum):
    write(baseTenToBytesLE(baseTenNum))

def local_color_table_flag(booleanFlag):
    packed_fields[0] = "1" if booleanFlag else "0"

def interlace_flag(booleanFlag):
    packed_fields[1] = "1" if booleanFlag else "0"

def sort_flag(booleanFlag):
    packed_fields[2] = "1" if booleanFlag else "0"

def reserved(baseTenNum):
    binNumberStr = pad(bin(baseTenNum)[2:], 2)
    packed_fields[3] = binNumberStr[0]
    packed_fields[4] = binNumberStr[1]

def size_of_local_color_table(baseTenNum):
    binNumberStr = pad(bin(baseTenNum)[2:], 3)
    packed_fields[5] = binNumberStr[0]
    packed_fields[6] = binNumberStr[1]
    packed_fields[7] = binNumberStr[2]
    write(bytearray([int("".join(packed_fields), 2)]))

    # Clear buffer
    for i in range(len(packed_fields)):
        packed_fields[i] = "0"

def LZW_minimum_code_size(baseTenNum):
    write(bytearray([baseTenNum]))

def clear_command():
    write(b'\x80')

def color_lookup_value(baseTenNum):
    write(bytearray([baseTenNum]))

def end_file():
    write(b'\x00')
    gif.close()

def plain_text_label():
    write(b'\x21\x01')

def text_grid_left(baseTenNum):
    image_left(baseTenNum)

def text_grid_top(baseTenNum):
    image_top(baseTenNum) 

def character_cell_width(baseTenNum):
    write(bytearray([baseTenNum]))

def character_cell_height(baseTenNum):
    write(bytearray([baseTenNum]))

def text_foreground_color_index(baseTenNum):
    write(bytearray([baseTenNum]))

def text_background_color_index(baseTenNum):
    write(bytearray([baseTenNum]))

def characters(stringCharacters):
    write(bytearray([ord(x) for x in stringCharacters]))

# Sources
# https://www.w3.org/Graphics/GIF/spec-gif89a.txt
# https://en.wikipedia.org/wiki/GIF