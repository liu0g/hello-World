__author__ = 'lg'

def sum_num(li):
    sum = 0
    for i in li:
        sum += i
    print('the sum is:%d'%sum)

def aver_num(li):
    sum = 0
    for i in li:
        sum += i
    aver = float(sum)/len(li)
    print('the average is:%.2f'%aver)

def main():
    str = '''
        (1)get sum of the 5 numbers
        (2)get average of the 5 numbers
        (X)exit'''
    list = [2,3,4,5,5]
    print(str)
    in_put = -1
    while True:
        in_put = raw_input('slect the number:')
        if in_put == '1':
            sum_num(list)
        elif in_put == '2':
            aver_num(list)
        elif in_put == 'X':
            break
        else:
            print('input error')

if __name__ == '__main__':
    main()