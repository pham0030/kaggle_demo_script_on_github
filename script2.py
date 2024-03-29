def function2():
    print('this is seconde python script')

    with open('function2_output.txt', 'a') as of:
        of.write('this is second python script' + '\n')