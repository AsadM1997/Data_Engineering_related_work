def func(m,n):
    return m+n;

print(__name__)

# now code will not executed because of main 
if __name__=="__main__":
    print(func(2,3))
    print("this is python learning module going on ")
