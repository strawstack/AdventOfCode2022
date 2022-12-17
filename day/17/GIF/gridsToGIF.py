from gif import *

def makeFrame(HEIGHT, WIDTH, pixelSize, grid, delay=100):
    # Graphic Control Extension
    graphic_control_extension()

    block_size(4)

    # Packed Byte Field
    reserved(0)
    disposal_method(1)
    user_input_flag(False)
    transparent_color_flag(False)

    # Hundreds of seconds
    delay_time(delay)

    transparent_color_index(0)

    end_block()

    # Image frame
    image_separator()

    image_left(0)
    image_top(0)

    width(WIDTH)
    height(HEIGHT)

    # Packed Byte Field
    local_color_table_flag(False)
    interlace_flag(False)
    sort_flag(False)
    reserved(0)
    size_of_local_color_table(0)

    LZW_minimum_code_size(7)

    packet = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pos = (x // pixelSize, y // pixelSize)
            if pos not in grid:
                packet.append(0)
            else:
                packet.append(grid[pos])

            if len(packet) == 4:
                block_size(5)
                clear_command()
                for n in packet:
                    color_lookup_value(n)
                packet = []

    end_block()

# Grid is a dict
# (x, y) -> color index 
def gridsToGIF(fileName, HEIGHT, WIDTH, pixelSize, gridList, opts):
    gif(fileName)

    HEIGHT = HEIGHT * pixelSize
    WIDTH = WIDTH * pixelSize

    GIF89a()

    width(WIDTH)
    height(HEIGHT)

    # Packed Fields
    global_color_table_flag(True)
    color_resolution(7)
    table_sort_flag(False)
    size_of_global_color_table(2) # 2**3 = 8

    background_color_index(0)

    pixel_aspect_ratio(0)

    # Add colors to the color table
    for color in opts["COLORS"]:
        global_color_table_color(color)

    # Application Extension
    application_extension()

    block_size(11)

    application_name("NETSCAPE2.0")

    block_size(3)

    index_of_block(1)

    # 0 for infinite
    number_of_repetitions(0)

    end_block()

    for grid in gridList:
        makeFrame(HEIGHT, WIDTH, pixelSize, grid, opts["DELAY"])

    end_file()