# https://codeforces.com/gym/102951/problem/A
# run file with command: 
# python3 max_distance.py < max_distance.txt

def max_distance(num, x_coords, y_coords):

    max_sq_distance = 0

    for i in range(num):
        for j in range(i+1, num):
            p1 = (x_coords[i], y_coords[i])
            p2 = (x_coords[j], y_coords[j])

            sq_distance = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
            max_sq_distance = max(max_sq_distance, sq_distance)
    
    return max_sq_distance


if __name__ == "__main__":
    num = int(input())
    x_coords = list(map(int, input().split(" ")))
    y_coords = list(map(int, input().split(" ")))
    
    result = max_distance(num, x_coords, y_coords)
    print(result)