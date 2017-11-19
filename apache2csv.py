#!/usr/bin/env python
import sys

FIELD_NAMES = [
    'ip', 
    'datetime', 
    'method', 
    'url', 
    'protocol', 
    'response_code', 
    'content_length'
]

def split_line(line):
    Line_dict={}
    lineTab=[x.strip() for x in line.split(' ')]
    #print line
    try:
        Line_dict = {
            'ip' : lineTab[0],
            'datetime' : lineTab[3][1:]+' '+lineTab[4][:-1],
            'method' : lineTab[5],
            'url' : lineTab[6],
            'protocol' : lineTab[7],
            'response_code' : lineTab[8],
            'content_length' : lineTab[9]
        }
    except IndexError:
        Line_dict={}
    return Line_dict  

def run(input_filename, output_filename):
    if (input_filename is not None):
        input = open(input_filename, 'r')
    else:
        input=sys.stdin
    if (output_filename is not None):
        outputStream =open(output_filename,'w')
    else:
        outputStream=sys.stdout
    try:
        for line in input.readlines():
            if len(line.strip()) == 0 :
                break
            RcvDic=split_line(line)
            strOut=''
            for record in FIELD_NAMES:
                strOut+= RcvDic[record]+','
            outputStream.write(strOut[:-1]+'\n')
        input.close()
    except KeyboardInterrupt:
        pass
    except KeyError:
        pass
    finally:
        input.close()
        outputStream.close()
        return
    return

def main(args):
    if len(args)==3:
        run(args[1], args[2])
    elif len(args)==1:
        run(None,None)
    elif len(args)==2:
        run(args[1],None)
    else:
        print('Usage: apache2csv.py input_filename output_filename')

if __name__ == "__main__":
    main(sys.argv)
