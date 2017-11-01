#Input File

file1 = input("First file name: ")
f = open(file1, 'r')

f.read(0)

local = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

var = '000000'
glob = {var:0}

selector = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

file2 = input("Second file name: ")
#Output File
target = open(file2, 'w')

total = 0
loc_hit = 0
glob_hit = 0
select_hit = 0

for line in f:
    total = total + 1

    #Local Predictor
    exp = line[1]
    indx = int(line[0])
    
    if local[indx] <= 1:
        loc_pred = 'n'
    else:
        loc_pred = 't'
    target.write(str(indx))
    target.write(loc_pred)

    if exp == 'n':
        if local[indx] > 0: 
            local[indx] = local[indx] - 1
    else:
        if local[indx] < 3:
            local[indx] = local[indx] + 1

    if loc_pred == exp:
        loc_hit = loc_hit + 1

    #Global Predictor

    if exp == 'n':
        curr = '0'
    else:
        curr = '1'
      
    if var in glob:

        if glob[var]<= 1:
            glob_pred = 'n'        glob_hit = glob_hit + 1

        else:
            glob_pred = 't'

        if curr == '0':
            if glob[var] > 0: 
                glob[var] = glob[var] - 1
        else:
            if glob[var] < 3: 
                glob[var] = glob[var] + 1
        
    else:
        glob_hit = glob_hit + 1
        if curr == '0':
            glob[var] = 0
        else:
            glob[var] = 1

        glob_pred = 'n'
        
    if glob_pred == exp:
        glob_hit = glob_hit + 1

    target.write(str(glob_pred))
    
    var = var[1:] + curr


    #Selector and Tournament Predictor
    if loc_pred != glob_pred:
        if loc_pred == exp:
            if selector[indx] > 0:
                selector[indx] = selector[indx] - 1
        elif glob_pred == exp:
            if selector[indx] < 3:
                selector[indx] = selector[indx] + 1

    if selector[indx]<= 1:
        selection = 'l'
        select_pred = loc_pred
    else:
        selection = 'g'
        select_pred = glob_pred

    if select_pred == exp:
        select_hit = select_hit + 1
        
    target.write(selection)
    target.write(select_pred)
    target.write(exp)
    target.write("\n")

target.close()
