

def digital_root(n):
    digits = [int(x) for x in str(n)]
    total = 0
    for n in digits:
     total+=n
    # print(digits)
    # print(total)
    length = len([int(x) for x in str(total)])
    # print(length)
    go_into = False
    if length > 1:
     go_into = True
    # print(go_into)
    
    while go_into:
     cont_num = [int(x) for x in str(total)]
     total_whi = 0
     for n in cont_num:
      total_whi+=n
     length_whi = len([int(x) for x in str(total_whi)])
     total_whi = total
     if length_whi == 1:
      go_into = False
    print(total)
    
    
    
digital_root(942)