day = 'Moderating'

results = day + '\\moderating_results.txt'
with open(results,'w') as cr:
    cr.write('')

angles = [0,1,3,5,10]

for angle in angles:
    angle =str(angle)
    print(angle)
    inpo = day+'\\'+angle+'mm\\MsNB.inpo'
    try:
        with open(inpo,'r') as output, open(results,'a') as cr:
            out = output.readlines()
            cr.write(angle)
            cr.write('\n')
            try:
                for i in range(0,len(out)):
                    if 'final result' in out[i]:
                        cr.write(out[i-4])
                        cr.write(out[i])
                        break
            except:
                        cr.write('there was an error with this file\n')

            cr.write('_________________________________________________________________________________________________________________________\n')
    except:
        with open(results,'a') as cr:
            cr.write(angle)
            cr.write('   File does not exist\n')
            cr.write('_________________________________________________________________________________________________________________________\n')
