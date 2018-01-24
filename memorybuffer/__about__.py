# Copyright (c) 2012-2017 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

__all__ = ('__title__', '__summary__', '__uri__', '__version_info__',
           '__version__', '__author__', '__email__', '__copyright__',
           '__license__')

__title__        = "memorybuffer"
__summary__      = "Python buffer protocol"
__uri__          = "http://pypi.python.org/pypi/memorybuffer/"
__version_info__ = type("version_info", (), dict(serial=2,
                        major=0, minor=2, micro=1, releaselevel="alpha"))
__version__      = "{0.major}.{0.minor}.{0.micro}{1}{2}".format(__version_info__,
                   dict(final="", alpha="a", beta="b", rc="rc")[__version_info__.releaselevel],
                   "" if __version_info__.releaselevel == "final" else __version_info__.serial)
__author__       = "Adam Karpierz"
__email__        = "python@python.pl"
__copyright__    = "Copyright (c) 2012-2017 {0}".format(__author__)
__license__      = "zlib/libpng License ; {0}".format(
                   "http://opensource.org/licenses/zlib")