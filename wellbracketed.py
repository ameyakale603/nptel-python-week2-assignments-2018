def bracket(str):
    depth=0
    for i in range(len(str)):
        if str[i]=="(":
            depth+=1
        elif str[i]==")":
            depth-=1
        print(depth)
    if depth == 0:
        return True
    else:
        print("wrong")



def main():
    bracket("ak()))")

if __name__=='__main__':
    main()