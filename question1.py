import sys
import io
def parsefile(test):
    try:
        f = io.open(test, 'r', encoding='utf-8')
        lines = f.readlines()
    except IOError as e:
        print e
        return
    else:
        print 'File opened successfully!'
        cnt=0
        sum=0.0
        for line in lines:           
            # print line
            res=line.split()
            for ele in res:
                sum = sum+float(ele)
                cnt=cnt+1
        print 'The total count is:'+str(cnt)
        print 'The total value is:'+str(sum)
        f.close()
        if f.closed==True:
            print 'The file has been closed'
        else:
            print 'The file is being processed.'
        return
if __name__ == '__main__':
    parsefile(sys.argv[1])
