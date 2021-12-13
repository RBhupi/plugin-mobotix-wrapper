import argparse
import sys
import time

from waggle.plugin import Plugin


def main(args):
    print(args)



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


