#!/usr/bin/env python
# coding: UTF-8
import sys
import os.path

os.system("E:")
os.system("cd visual studio 2017/Target Intelligent Recognition/"
          "Image Classification/Image Classification/Data Set/dataset1/train")
os.system("dir /b/s *.pgm *.jpg >at.txt")

if __name__ == "__main__":

    # if len(sys.argv) != 2:
    #    print "usage: create_csv <base_path>"
    #    sys.exit(1)
    # BASE_PATH=sys.argv[1]
    BASE_PATH = "E:/visual studio 2017/Target Intelligent Recognition/" \
                "Image Classification/Image Classification/Data Set/dataset1/train"
    SEPARATOR = ";"
    fh = open("E:/visual studio 2017/Target Intelligent Recognition"
              "/Image Classification/Image Classification/Data Set//dataset1/train/at.txt", 'w')

    label = 1
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                #print
                #"%s%s%d" % (abs_path, SEPARATOR, label)
                fh.write(abs_path)
                fh.write(SEPARATOR)
                fh.write(str(label))
                fh.write("\n")
            label = label + 1
    fh.close()

    os.system("E:")
    os.system("cd visual studio 2017/Target Intelligent Recognition/"
              "Image Classification/Image Classification/Data Set/dataset1/test")
    os.system("dir /b/s *.pgm *.jpg >at.txt")

    if __name__ == "__main__":

        # if len(sys.argv) != 2:
        #    print "usage: create_csv <base_path>"
        #    sys.exit(1)
        # BASE_PATH=sys.argv[1]
        BASE_PATH = "E:/visual studio 2017/Target Intelligent Recognition/" \
                    "Image Classification/Image Classification/Data Set/dataset1/test"
        SEPARATOR = ";"
        fh = open("E:/visual studio 2017/Target Intelligent Recognition"
                  "/Image Classification/Image Classification/Data Set//dataset1/test/at.txt", 'w')

        label = 1
        for dirname, dirnames, filenames in os.walk(BASE_PATH):
            for subdirname in dirnames:
                subject_path = os.path.join(dirname, subdirname)
                for filename in os.listdir(subject_path):
                    abs_path = "%s/%s" % (subject_path, filename)
                    # print
                    # "%s%s%d" % (abs_path, SEPARATOR, label)
                    fh.write(abs_path)
                    fh.write(SEPARATOR)
                    fh.write(str(label))
                    fh.write("\n")
                label = label + 1
        fh.close()