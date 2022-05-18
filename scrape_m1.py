
results = 'm1_results.txt'
with open(results,'w') as mr:
    mr.write('')

days = [2,4,6,8,10,12]

for day in days:
    day ='Month'+str(day)
    #print(day)
    inp = day+'\\Broad\\0\\MsNB.inp'
    print(inp)
    try:
        with open(inp,'r') as inputfile, open(results,'a') as mr:
            input = inputfile.readlines()
            mr.write(day)
            mr.write('\n')
            try:
                for i in range(0,len(input)):
                    if 'M1' in input[i]:
                        mr.write(input[i])
                        mr.write(input[i+5])
                        mr.write(input[i+2])
                        mr.write(input[i+3])
                        mr.write(input[i+1])
                        mr.write(input[i+4])
                        mr.write(input[i+8])
                        mr.write(input[i+7])
                        mr.write(input[i+6])
                        mr.write(input[i+9])
                        mr.write(input[i+10])
                        mr.write(input[i+12])
                        mr.write(input[i+11])
                        mr.write(input[i+13])
                        mr.write(input[i+14])
                        mr.write(input[i+15])
                        mr.write(input[i+16])
                        mr.write(input[i+17])
                        mr.write(input[i+18])
                        break
            except:
                        mr.write('there was an error with this file\n')

            mr.write('_________________________________________________________________________________________________________________________\n')
    except:
        with open(results,'a') as mr:
            mr.write(day)
            mr.write('   File does not exist\n')
            mr.write('_________________________________________________________________________________________________________________________\n')
