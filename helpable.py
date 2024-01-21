
import sys 

if len(sys.argv)==2:
    if sys.argv[1]=='--help' or sys.argv[1]=='-h':
        print("도움말")
        sys.exit()
print("안녕하세요")
    