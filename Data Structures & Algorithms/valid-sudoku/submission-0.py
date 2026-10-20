class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #seen = set()
        #dictionary = {}
        #dictionary[0] = set()
        rows = {}
        cols = {}
        boxes = {} #3 dict

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue #skip cycle and start again
                
                if r not in rows:
                    rows[r] = set()

                if c not in cols:
                    cols[c] = set() #creat new sets for r/c that don't have one

                box = (r//3,c//3)
                if box not in boxes:
                    boxes[box] = set()


                if (num in rows[r] or num in cols[c] or num in boxes[box]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        return True        

