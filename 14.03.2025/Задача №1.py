from typing import List, Set

def is_valid(x: int, y: int, visited: List[List[bool]], M: int, L: int) -> bool:
    return 0 <= x < M and 0 <= y < L and not visited[x][y]

def search_word(board: List[List[str]], word: str, x: int, y: int, index: int, visited: List[List[bool]], M: int, L: int) -> bool:
    if index == len(word):
        return True
    
    if not is_valid(x, y, visited, M, L) or board[x][y] != word[index]:
        return False
    
    visited[x][y] = True
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for dx, dy in directions:
        if search_word(board, word, x + dx, y + dy, index + 1, visited, M, L):
            return True
    
    visited[x][y] = False
    return False

def find_words_on_board(dictionary: Set[str], board: List[List[str]], M: int, L: int) -> List[str]:
    found_words = set()
    
    for word in dictionary:
        for i in range(M):
            for j in range(L):
                visited = [[False] * L for _ in range(M)]
                if search_word(board, word, i, j, 0, visited, M, L):
                    found_words.add(word)
    
    return sorted(found_words)

def main():
    N = int(input().strip())
    dictionary = set(input().strip().split())
    M, L = map(int, input().strip().split())
    board = [input().strip().split() for _ in range(M)]
    
    result = find_words_on_board(dictionary, board, M, L)
    print(" ".join(result))

main()