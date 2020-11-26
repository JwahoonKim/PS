def solution(board, moves):
    n = len(board[0])    
    bucket = []
    m = len(moves)
    count = 0
    for doll in moves:
        for j in range(n):
            if board[j][doll - 1] == 0: 
                continue
            bucket.append(board[j][doll - 1])
            board[j][doll - 1] = 0
            break
        
        if len(bucket) == 0 or len(bucket) == 1:
            continue
        if bucket[-1] == bucket[-2]:
            count += 2
            del bucket[-1]
            del bucket[-1]        
    return count
