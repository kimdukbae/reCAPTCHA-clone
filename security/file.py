import os

dataset_dir = 'tmp\\captcha\\test_photos2'
#directories = []
photo_filenames = []

for filename in os.listdir(dataset_dir):
    path = os.path.join(dataset_dir, filename)
    photo_filenames.append(path)
photo_filenames.sort()
#  if filename == 'normal' or filename == 'adenoma':
#  path = os.path.join(dataset_dir, filename)
#  if os.path.isdir(path):
#    directories.append(path)
#  else:
#    path1=os.path.join(dataset_dir, filename)
#    for filename2 in os.listdir(path1):
#      path2=os.path.join(path1, filename2)
#      if os.path.isdir(path2):
#        directories.append(path2)

#for directory in directories:
#  for filename in os.listdir(directory):
#    path = os.path.join(directory, filename)
#    photo_filenames.append(path)
   
f = open("tmp\\captcha\\test2.txt", "w")
for i in photo_filenames:
    f.write(i + "\n")
f.close()