import sys
fil=sys.argv[1]
csvfilename = open(fil, 'r').readlines()
file = 1
for j in range(len(csvfilename)):
    if j % 2000 == 0:
        open(str(fil)+ str(file) + '.csv', 'w+').writelines(csvfilename[j:j+2000])
    file += 1
