def function1():
    print('this is first python script')

    with open('function1_output.txt', 'a') as of:
        of.write('this is first python script' + '\n')
