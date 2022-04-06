#C-style parser for command line options

import getopt

optlist, args = getopt.getopt(args, 'abc:d:')
print(optlist)

