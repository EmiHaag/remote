def gridChallenge(grid):
    sorted_grid = [sorted(s) for s in grid ]
    for c in range(len(sorted_grid[0])):    # <- for non-square test cases
        for r in range(len(grid)-1):
            if sorted_grid[r+1][c] < sorted_grid[r][c]: return 'NO'
    return 'YES'
    
    


print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))


