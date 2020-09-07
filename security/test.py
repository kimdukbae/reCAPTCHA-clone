from matplotlib import pyplot as plt
import numpy as np
import os
import tensorflow as tf
import random
import seaborn as sns
import pandas as pd
#import level2
from nets import densenet
from preprocessing import densenet_preprocessing
os.environ["CUDA_VISIBLE_DEVICES"]="0"
checkpoints_dir = 'tmp\\train_logs'
slim = tf.contrib.slim
image_size = densenet.densenet121.default_image_size
num = 1
correct = 0.0
accuracy = 0.0
threshold = 0.0
sample_num = 9
column = 0
photo_filenames=[]
#level_2 = []
compare = {'bus' : 0, 'car' : 1, 'cat' : 2, 'dog' : 3, 'ship' : 4}
classes = ['bus', 'car', 'cat', 'dog', 'ship']
CMatrix = [ [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0] ]
with tf.Graph().as_default():
    class0=[]
    class1=[]
    class2=[]
    class3=[]
    class4=[]
    user_images = []  
    user_processed_images = []
#    image_names = []
    image_files = []
#    GT_dict = {}
    GT_num = {} 
    f = open("tmp\\captcha\\test2.txt", "r")
    while(1):
      data = f.readline()
      if not data:
        break
      image_files.append(data[:-1])
#    image_files = random.sample(image_names, sample_num)
    for i in image_files:
#        GT_dict[i] = i.split('/')[3]
        GT_num[i] = i.split('\\')[3]
        image_input = tf.read_file(i)
        image = tf.image.decode_jpeg(image_input, channels=3)
        user_images.append(image)
        processed_image = densenet_preprocessing.preprocess_image(image, image_size, image_size, is_training=False)
        user_processed_images.append(processed_image)

    processed_images = tf.expand_dims(processed_image, 0)

    with slim.arg_scope(densenet.densenet_arg_scope()):
        logits, _ = densenet.densenet121(user_processed_images, num_classes=5, is_training=False)
    probabilities = tf.nn.softmax(logits)

    init_fn = slim.assign_from_checkpoint_fn(
        os.path.join(checkpoints_dir, 'model.ckpt-21031'),
        slim.get_model_variables('densenet121'))
        
    with tf.Session() as sess:
        init_fn(sess)
        probabilities = sess.run(probabilities)

#    names = os.listdir("tmp/captcha/test_photos2")
    names = ['bus', 'car', 'cat', 'dog', 'ship']
    names.sort()
    #names=['normal', 'adenoma', 'adenocarcinoma']
    for files in range(sample_num):
        prob = probabilities[files ,0 ,0, 0:]
        sorted_inds = [n[0] for n in sorted(enumerate(-prob), key=lambda x: x[1])]
#        if GT_dict[image_files[files]] == names[sorted_inds[0]]:
#            correct += 1
        
#        if prob[sorted_inds[0]] >= threshold:
#            if compare[GT_dict[image_files[files]]] == 2 and compare[names[sorted_inds[0]]] == 2:
#              photo_filenames.append(image_files[files])
#              column += 1
            #    pass
            #else:
#            CMatrix[compare[GT_dict[image_files[files]]]][compare[names[sorted_inds[0]]]] += 1
        
#        else:
#        print("No. %d" % (num))
        print('Prediction : ', names[sorted_inds[0]], ', Image_name : ', GT_num[image_files[files]])
        for p in range(5):
          index = sorted_inds[p]
          print('Probability %0.2f%% => [%s]' % (prob[index], names[index]))

        if compare[names[sorted_inds[0]]] == 0:
          class0.append(GT_num[image_files[files]])
        elif compare[names[sorted_inds[0]]] == 1:
          class1.append(GT_num[image_files[files]])
        elif compare[names[sorted_inds[0]]] == 2:
          class2.append(GT_num[image_files[files]])
        elif compare[names[sorted_inds[0]]] == 3:
          class3.append(GT_num[image_files[files]])  
        elif compare[names[sorted_inds[0]]] == 4:
          class4.append(GT_num[image_files[files]])

        num += 1
        
    print("bus : ", class0)
    print("car : ", class1)
    print("cat : ", class2)
    print("dog : ", class3)
    print("ship : ", class4)
                
#    print("Total Accuracy : %0.2f%%" % (correct / sample_num))
#    print(CMatrix)
    #level2

#    total = np.sum(CMatrix, axis=1)
#    CMatrix = CMatrix / total[:,None]
#    cm = pd.DataFrame(CMatrix, index=classes, columns=classes)
#    plt.title('Confusion Matrix')
#    sns.heatmap(cm, annot=True)
#    plt.show()
    
#f1 = open("tmp/colon/test2.txt", "w")
#for i in photo_filenames:
#  f1.write(i + "\n")
#f1.close()

#f2 = open("tmp/colon/test3.txt", "w")
#f2.write('%d\n' %column)
#for i in range(0,3):
#  for j in range (0,3):
#    f2.write('%d\n' %CMatrix[i][j])
#f2.write('%.1f' %threshold)
#f2.close()
