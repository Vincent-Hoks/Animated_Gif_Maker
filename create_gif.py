import imageio.v3 as iio

filenames = ['image1.jpg','image2.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

output_name = input('Input The Gift Name(Dont Use .Gif)....')
iio.imwrite(output_name+'.gif',images,duration = 500,loop = 0)
print(f'Your {output_name}.gif Has Succesfully Created')
