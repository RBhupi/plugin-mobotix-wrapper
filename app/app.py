#!/usr/bin/env python3
"""
Created on Mon Dec 13 11:05:11 2021

1. Runs the Mobotix C++ sampler with the given arguments.
2. The .rgb files are too large, so we used ffmpeg to convert to JPG.
"""

import argparse
import sys
import time
import glob
import os
import subprocess
import re


from waggle.plugin import Plugin


def main(args):
    
    #create output directory if does not exist.
    if not os.path.exists(args.o):
        os.makedirs(args.o)
    os.chdir(args.o)
    
    print("running subprocess")
    # here we should run the c++ code
    subprocess.run(["/eventstreamclient/samples/thermal-raw/build/thermal-raw", 
                    args.ip])
    print("complete subprocess")
    
    
    
    # At this point should we only run the sampler only once or for continuouse
    # time period of say 5-30 min? We need to decide this based on the data 
    
    


    rgb_files = glob.glob("*.rgb")
    for f_rgb in rgb_files:
        # make JPEG file name
        f_jpg = f_rgb.replace(".rgb", ".jpg")
        
        # get the Width and Height of the image from filename
        match_str = re.search('\d\d\d\dx\d\d\d\d', f_rgb)
        image_dims = match_str.group()
        subprocess.run(['ffmpeg', '-f', 'rawvideo', '-pixel_format', 'bgra', 
                        '-video_size', image_dims, '-i', f_rgb, f_jpg])
        
        #ffmpeg -f rawvideo -pixel_format bgra -video_size image_dims -i f_rgb f_jpg

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''
                                     This program runs Mobotix sampler for raw 
                                     storing thermal data.''')
    parser.add_argument('--ip', type=str, 
                        help='Camera IP or URL', 
                        default="10.10.10.1")
    parser.add_argument('--id', type=str, 
                        help='Authenticator User ID.',
                        default="admin")
    parser.add_argument('--pw', type=str,
                        help='Authenticator Password.', default="password")
    parser.add_argument('--o', type=str, 
                        help='Output directory', default="./data/")
    parser.add_argument('--i', type=int,
                        help='Interval [sec]', default=1)
    
    args = parser.parse_args()
    main(args)


