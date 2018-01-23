import sys,getopt

opts,args = getopt.getopt(sys.argv[1:],"hi:o:")
input_file=""
output_file=""
for op,value in opts:
    if op == "-i":
       input_file = value
       with open(value,'r') as f:
          chars = f.read()
          chars = chars.replace('\r',' ').replace('\n',' ')
    elif op == "-o":
       output_file = value
       with open(value,'w') as wf:
          wf.write(chars)
    elif op == "-h":
       usage = "-i filename -o filename"
       print(usage)
       sys.exit()
