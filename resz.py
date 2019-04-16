
import cv2
import glob
import os
import math

def resizefld(infld, outfld):
    nms = glob.glob(os.path.join(infld, '*.jpg'))
    cnt = 0

    for nm in nms:
        img = cv2.imread(nm)
        h, w, c = img.shape
        alpha = 400.0 / math.sqrt(h*w)
        sized = cv2.resize(img, None, fx=alpha, fy=alpha)
        cv2.imwrite(nm.replace(infld, outfld), sized)
        cnt = cnt+1
        print('progress {:.2f}% ({:d} of {:d})'.format(100.0*cnt/len(nms), cnt, len(nms)) )

infld = 't100l'
outfld = 't100'
resizefld(infld, outfld)

