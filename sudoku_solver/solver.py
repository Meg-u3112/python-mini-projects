def find_empty(board):
  
  for row in range(len(board)):
    for column in range(len(board[row])):
      if board[row][column] == 0:
          return row,column        
  return None    


def is_valid(board,num,row,column):
  box_row = (row//3)*3
  box_column =(column//3)*3

  for i in range(len(board[row])):
    if board[row][i] == num:
      return False
    if board[i][column] == num:
      return False
  for r in range(box_row, box_row + 3):
    for c in range(box_column, box_column + 3):
      if board[r][c] == num:
        return False
  return True



def solve(board):
  empty = find_empty(board)

  if not empty:
    return True
  row,column = empty
  
  for num in range(1,10):
    if is_valid(board,num,row,column):
      board[row][column] = num
      if solve(board):
        return True
      board[row][column] = 0
  return False    
      

