import os
import sys
import capture

path = 'tmp\\captcha\\test_photos2'

os.system('python {}.py'.format(capture))

os.system('move *.jpg {}'.format(path))
