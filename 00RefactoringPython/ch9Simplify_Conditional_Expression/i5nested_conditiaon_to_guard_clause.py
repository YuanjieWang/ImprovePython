from mycolor import show

is_dead = False
is_seperate = True
is_retired = False
def dead_amount():
    return 100000

def seperate_amount():
    return 50000

def retire_amount():
    return 20000

def normal_amount():
    return 10000

def get_pay_amount_old():
    result = None
    if is_dead:
        result = dead_amount()
    else:
        if is_seperate:
            result = seperate_amount()
        else:
            if is_retired:
                result = retire_amount()
            else:
                result = normal_amount()

    return result

t = get_pay_amount_old()
print(show(t))

print('函数种条件逻辑让人非常难以看清楚正常的执行路径 ' + 
      ' 使用卫语句表现所有特殊情况')
print('- · - - · - - · - - · - ')

def get_pay_amount():
    if is_dead:
        return dead_amount()
    if is_seperate:
        return seperate_amount()
    if is_retired:
        return retire_amount()
    return normal_amount()

n = get_pay_amount()
print(show(n, 'red'))