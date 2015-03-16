import sys
def parsefile(test):
    try:
        f = open(test,'r')
        lines = f.readlines()
    except IOError as e:
        print e
    else:
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
if __name__ == '__main__':
    parsefile('/Users/zhileiyue/Desktop/1.txt')
