from PIL import Image
import os
import glob
import argparse
import numpy as np
import time

parser = argparse.ArgumentParser()
parser.add_argument('--type_num', type=int, default=0, help='type_num')
args = parser.parse_args()
n=0

while n<20:
    try:
        im=Image.open('./result.jpg')
        makeups = glob.glob(os.path.join('imgs', 'makeup', '*.*'))
        num=len(makeups)+1
        img_size=int(im.size[0]/num)
        im1 = im.crop((args.type_num*img_size,0, (args.type_num+1)*img_size, img_size)) 
        im1.show()


        #wait click ok

        # im1.save('cut.jpg') 
        break
        
        
    except:
        print('圖片製作中')
        n+=1

        time.sleep(1)