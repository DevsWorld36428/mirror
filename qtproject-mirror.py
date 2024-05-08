#!/usr/bin/python

import ConfigParser
import os, sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--full', action='store_true')
args = parser.parse_args()
#print args

cfg = ''
cfg1 = '/home/qtmirrorbot/bin/config.cfg'
cfg2 = '/home/qtmirrorbot/bin/full.cfg'
if args.full:
    cfg = cfg2
else:
    cfg = cfg1
config = ConfigParser.RawConfigParser()
config.read(cfg)

path_prefix = config.get('general', 'path_prefix')
src_prefix= config.get('general', 'src_prefix')
dst_prefix = config.get('general', 'dst_prefix')
projects_string = config.get('general', 'projects').strip()
projects = []
if len(projects_string) > 0:
    projects = projects_string.split(',')
else:
    projects = config.sections()
    if 'general' in projects:
        projects.remove('general')

#cfgneedwrite = False

for p in projects:
    inited = config.getboolean(p, 'inited')
    source = p
    destination = config.get(p, 'destination')
    src = src_prefix + source
    dst = dst_prefix + destination
    path = path_prefix + p
    if (inited):
#       print path_prefix
#       os.chdir(path_prefix)
#       os.system('git clone --mirror ' + src + ' ' + p)
#       print 'mirror finished ' + p
#       print path
        os.chdir(path)
#       os.system('git config remote.origin.fetch \'+refs/heads/*:refs/heads/*\' heads')
#       os.system('git config remote.origin.fetch \'+refs/tags/*:refs/tags/*\' tags')
#       os.system('git config remote.origin.fetch \'+refs/staging/*:refs/staging/*\' staging')
#       os.system('git config remote.origin.url "ssh://codereview.qt-project.org:29418/$i.git"')
#       os.system('git fetch -p -q -u')
#       print 'fetch finished'
#       os.system('git push --mirror ' + dst)
        os.system('git push --all --force ' + dst)
        os.system('git push --tags --force ' + dst)
#       print 'push finished'

#if cfgneedwrite == True:
#    with open('/home/qtmirrorbot/bin/config.cfg', 'wb') as configfile:
#        config.write(configfile)
