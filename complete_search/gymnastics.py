# http://www.usaco.org/index.php?page=viewproblem2&cpid=963
# run file with command: 
# python3 gymnastics.py

def cow_gymnastics(practices, cows, rankings):
    consistent_pairs = set()
    for i in range(cows):
        for j in range(i+1, cows):
            consistent_pairs.add((i+1, j+1))
    
    pair_map = dict()
    first_ranking = rankings[0]
    for i, rank1 in enumerate(first_ranking):
        for rank2 in first_ranking[i+1:]:
            pair = tuple(sorted([rank1, rank2]))
            pair_map[pair] = rank1
    
    for ranking in rankings[1:]:
        for i, rank1 in enumerate(ranking):
            for rank2 in ranking[i+1:]:
                pair = tuple(sorted([rank1, rank2]))
                if pair_map[pair] != rank1 and pair in consistent_pairs:
                    consistent_pairs.remove(pair)

    return len(consistent_pairs)

if __name__ == "__main__":
    f = open("gymnastics.in",'r',encoding = 'utf-8')
    input = f.readline()
    practices, cows = tuple(map(int, input.split(" ")))
    rankings = []

    for line in f:
        ranking = tuple(map(int, line.split(" ")))
        rankings.append(ranking)
    
    result = cow_gymnastics(practices, cows, rankings)
    print(result)
    with open("gymnastics.out",'w',encoding = 'utf-8') as f:
        f.write(str(result))
