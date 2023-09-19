from PIL import Image
input_path = 'nbs/ML/images/RLHF/Untitled 2.png'
output_path = input_path
# output_path = '_docs/ML/images/RLHF/graph.png'
size = 760
foo = Image.open(input_path)  # My image is a 200x374 jpeg that is 102kb large
# image size to 500 width and keep the aspect ratio
foo = foo.resize((size, int(size * foo.size[1] / foo.size[0])), Image.ANTIALIAS)
foo.save(output_path, optimize=True, quality=95)  # The saved downsized image size is 22.9kb