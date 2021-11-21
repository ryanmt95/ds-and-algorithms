# http://www.usaco.org/index.php?page=viewproblem2&cpid=1012
# run file with command: 
# python3 mad_scientist.py

def mad_scientist(num, cows_a, cows_b):
    count = 0
    match = True

    for i in range(num):
        if cows_a[i] == cows_b[i]:
            match = True
        else:
            if match: count += 1
            match = False

    return count

if __name__ == "__main__":
    f = open("breedflip.in",'r',encoding = 'utf-8')
    num = int(f.readline())
    cows_a = f.readline()
    cows_b = f.readline()
    
    result = mad_scientist(num, cows_a, cows_b)
    print(result)
    with open("breedflip.out",'w',encoding = 'utf-8') as f:
        f.write(str(result))
