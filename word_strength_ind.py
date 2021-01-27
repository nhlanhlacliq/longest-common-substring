print("======================================================")
print("Enter two words below so see how strongly they relate:")
print("======================================================")
word1 = input("Enter word 1\n> ")
word2 = input("Enter word 2\n> ")

def get_word_strength(word1, word2):
  # Create grid (2d array) using the words as columns and rows
  grid = [[0]*len(word2) for i in range(len(word1))]

  same_letters_count = 0
  for i in range(len(word1)):   #check letters of word 1 against..
    for j in range(len(word2)):   #..every letter of word 2
      if word1[i] == word2[j]:  
        grid[i][j] = (grid[i-1][j-1]) + 1 #if letters are ==, then that cell's value is previous cell + 1.. (adds onto the number of same letters found so far)
        same_letters_count += 1       #increment count
      else:
        grid[i][j] = max(grid[i-1][j], grid[i][j-1])  #if letters arent ==, set value to max between left / above cell (the max same letters so far)
        # basically keep memory of the longest number
  # print(grid)
  max_letters = (len(word1)+len(word2)) / 2   #max letters avail. is average of both words
  longest_subsqnce = grid[-1][-1]  #this is the same as max latters so far. since its a grid the max number will always* propagate to the very last cell
  strength = round((longest_subsqnce / max_letters)*100,2)

  return print(f"Max subsequence: {longest_subsqnce}\nSame letter count: {same_letters_count} \nWord strength: {strength}%")

print("======================================================")
get_word_strength(word1,word2)