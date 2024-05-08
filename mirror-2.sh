#!/bin/sh
echo "Qt Mirror Full: $(date)" >> /tmp/qt-mirror.log
/home/qtmirrorbot/bin/qtproject-mirror.py --full 2>&1 >> /tmp/qt-mirror.log
echo "Qt Mirror Full Successful: $(date)" >> /tmp/qt-mirror.log
