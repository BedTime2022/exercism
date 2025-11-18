def is_valid(isbn):
    cool_isbn = isbn.replace("-","")
    if len(cool_isbn) != 10:
      return False  
    else:
        if cool_isbn[0:8].isdigit(): 
            set_isbn  = [(int(cool_isbn[0]) * 10),
                         (int(cool_isbn[1]) * 9),
                         (int(cool_isbn[2]) * 8),
                         (int(cool_isbn[3]) * 7),
                         (int(cool_isbn[4]) * 6),
                         (int(cool_isbn[5]) * 5),
                         (int(cool_isbn[6]) * 4),
                         (int(cool_isbn[7]) * 3),
                         (int(cool_isbn[8]) * 2)]

            if not (cool_isbn[9].isdigit() or cool_isbn[9] == "X"):
                return False
    
            elif cool_isbn[9] == "X":
                checker_set_isbn = int(10)
            else:
                checker_set_isbn = (int(cool_isbn[9]) * 1)
        
            return (int(sum(set_isbn)) + checker_set_isbn) % 11 == 0 
        else: return False
    
