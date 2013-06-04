# This works with python >2.5. If you are using 2.4, you'll need to use
# md5

import hashlib

class FilterModule(object):
    ''' Custom filters are loaded by FilterModule objects '''

    def filters(self):
        ''' FilterModule objects return a dict mapping filter names to
            filter functions. '''
        return {
            'md5': self.gen_md5,
        }

    def gen_md5(self, value):
        return hashlib.md5(value).hexdigest()
