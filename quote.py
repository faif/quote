#    quote.py Print a random quote from an input file
#    Copyright (C) 2010 Sakis Kasampalis <faif at dtek period gr> 

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random, os

FILE = '.qotd'             # quote of the day ;)
SEP = '\t'                 # quote/author separator


# Count lines. Assume that the
# stream is open and running.
#
# fin: input stream
# return: the total number of lines
def lcount(fin):
    count = 0
    for line  in fin:
        count += 1
    return count    


# Get a specified line. Assume that the
# stream is open and running.
#
# fin: input stream
# n: the line number
# return: the line content as a string,
# or None if the line doesn't exist
def nline(fin, n):
    count = 0
    for line in fin:
        if count == n:
            return line
        count += 1
    return None


# Show a string in the output, after
# splitting it using the given token.
#
# rline: the input string
# sep: the string token (separator)
# pref: a prefix for the 2nd string
def showstr(rline, sep, pref=None):
    first, _, sec = rline.partition(SEP)
    print(first, end=' ')
    if len(sec) > 1:
        print(pref, sec, end=' ')


# Try to open a file for reading.
#
# infile: the file name
def fopen(infile):
    try:
        fin = open(infile, 'r')
        return fin
    except IOError as e:
        print(e)
        exit(-1)
    except:
        print('unusual error, aborting...')
        fin.close()
        exit(-1)


# starting place...
def main():
    fin = fopen(FILE)

    # get a random line number
    linenum = int(random.random() * lcount(fin) + 1)

    # go to the beginning of the file
    fin.seek(os.SEEK_SET)

    # save the random line
    rline = nline(fin, linenum)

    # show the random quote
    showstr(rline, SEP, '  --')

    fin.close()


if __name__ == '__main__':
    main()
