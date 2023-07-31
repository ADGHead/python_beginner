def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(raise_to_power(3, 4))

def power_up(base_num, power_num):
    result = base_num**power_num
    return result

print(power_up(3,4))