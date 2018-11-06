import ImageProcessor
import sys

def print_usage():
    print("""
        Usage: {0} <image> <destination> [sorting length] [sorting axis]

        Sorts pixel rows/collumns of the given image <image>.
        Each line of sorted pixels is [sorting_length] long and defaults to 0 for stopping at the picture ends.
        [Sorting axis] toggles on which axis the sorting is done. Defaults to vertical.
        """.format(sys.argv[0]))


if len(sys.argv) < 2:
    print_usage()
    exit(0)
if sys.argv[1] == "-h":
    print_usage()
    exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]
sorting_length = 0 if len(sys.argv) < 4 else sys.argv[3]
sort_direction = True if len(sys.argv) < 5 else sys.argv[4]


assert(isinstance(input_file, str))
assert(isinstance(output_file, str))
assert(isinstance(sorting_length, int) and sorting_length >= 0)
assert(isinstance(sort_direction, bool) or isinstance(sort_direction, str))

if sort_direction.lower() == "true":
    sort_direction = True
elif sort_direction.lower() == "false":
    sort_direction = False
else:
    print("Did not recognize parameter [sorting axis]! Defaulting to True for vertical.")
    sort_direction = True

ImageProcessor.glitchsort(input_file, output_file, sorting_length, sort_direction)
