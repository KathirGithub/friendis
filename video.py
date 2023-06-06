import os
import cv2

path = 'Images'

images=[]

for file in os.listdir(path):
    root,extension=os.path.splitext(file)
    if extension in ['.gif','.jpg','.jpeg','.webp','.png','.jfif']:
        filename=path+'/'+file
        images.append(filename)

count=len(images)

frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)

out=cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()
print('done')
