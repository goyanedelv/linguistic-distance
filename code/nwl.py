from numpy import full, zeros

def score_match(nt1,nt2,scoring_matrix):
    """Return the score for a substitution between nt1 and nt2 based on the scoring matrix
    nt1 -- a string representing the first nucleotide 
    nt2 -- a string representing the second nucleotide
    scoring_matrix -- an N x N numpy array, where N is
      the number of the alphabet  
    """

    if (nt1 == " ") & (nt2 == " "):
        return 0
    elif nt1 == " ":
        return 3
    elif nt2 == " ":
        return 3
    else:
        if (nt1, nt2) not in scoring_matrix.keys():
            return 3
        else:
            return scoring_matrix[(nt1, nt2)]

# Needleman-Wunsch Like
def nwl(seq1,seq2, scoring_matrix,\
  scoring_function=score_match, gap_penalty = -3):
    """Perform Needleman Wunsch global alignment on two sequences
    seq1 -- a sequence as a string
    seq2 -- a sequence as a string
    gap_penalty -- a function that takes no parameters and returns the score for a gap
    scoring_function -- a function that takes two letters and returns a score
    """
    #build an array of zeroes 
    n_rows = len(seq1) + 1 #need an extra row up top
    n_columns = len(seq2) + 1 #need an extra column on the left
    scoring_array = full([n_rows,n_columns],0)

   
    #iterate over columns first because we want to do 
    # all the columns for row 1 before row 2
    for row in range(n_rows):
        for col in range(n_columns):  
            if row == 0 and col == 0:
                #We're in the upper right corner
                score = 0
            elif row == 0:
                #We're on the first row
                #but NOT in the corner

                #Look up the score of the previous cell (to the left) in the score array\
                previous_score = scoring_array[row,col - 1]
                # add the gap penalty to it's score
                score = previous_score + gap_penalty
            elif col == 0:
                #We're on the first column but not in the first row
                previous_score = scoring_array[row -1,col]
                score = previous_score + gap_penalty
            else: 
                #We're in a 'middle' cell of the alignment

                #Calculate the scores for coming from above,
                #from the left, (representing an insertion into seq1)
                cell_to_the_left = scoring_array[row,col-1]
                from_left_score = cell_to_the_left + gap_penalty

                #or from above (representing an insertion into seq2)
                above_cell = scoring_array[row-1,col]
                from_above_score = above_cell + gap_penalty

                #diagonal cell, representing a substitution (e.g. A --> T)
               
                diagonal_left_cell = scoring_array[row-1,col-1]

                #Since the table has an extra row and column (the blank ones), 
                #when indexing back to the sequence we want row -1 and col - 1.
                #since row 1 represents character 0 of the sequence.
                curr_nt_seq1 = seq1[row-1]
                curr_nt_seq2 = seq2[col-1]
                
                #the scoring matrix will tell us the score for matches,
                #transitions and transversions
                diagonal_left_cell_score = diagonal_left_cell - \
                  score_match(curr_nt_seq1,curr_nt_seq2,scoring_matrix)
                score = max([from_left_score,from_above_score,diagonal_left_cell_score]) 

            scoring_array[row,col] = score

    return scoring_array[n_rows - 1, n_columns - 1]


