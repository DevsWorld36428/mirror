#!/bin/sh
echo "Qt Mirror: $(date)" >> /tmp/qt-mirror.log
/home/qtmirrorbot/bin/qtproject-mirror.py 2>&1 >> /tmp/qt-mirror.log
echo "Qt Mirror Successful: $(date)" >> /tmp/qt-mirror.log
