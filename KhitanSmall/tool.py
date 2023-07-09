def compare(num1: list[int], num2: list[int]) -> bool:
    for i in range(min(len(num1), len(num2))):
        if num1[i] < num2[i]:
            return True
        if num1[i] > num2[i]:
            return False
    if len(num1) < len(num2):
        return True
    return False


def number_to_string(nums: list[str]) -> list[str]:
    results = []
    import yaml
    mapping = yaml.load('serial-mapping.yaml', yaml.CFullLoader)
    for word in nums:
        array_char = word.split("-")
        result = ""
        for char in array_char:
            result += mapping[int(char)]
        results.append(result)
    return results


def pua_to_string(string: str) -> str:
    import yaml
    with open('menksoft-mapping.yaml', 'r', encoding='utf-8') as f_m:
        with open('serial-mapping.yaml', 'r', encoding='utf-8') as f_s:
            pua = yaml.load(f_m, yaml.CFullLoader)
            pua = {v: k for k, v in pua.items() if v != False}
            uni = yaml.load(f_s, yaml.CFullLoader)

            lst = list(string)
            result = [uni[pua[ord(char)]] if ord(char) in pua else char for char in lst]
            return "".join(result)


def shuffle(string: str) -> str:
    if len(string) == 1:
        return string[0]
    elif len(string) == 2:
        return string[1] + string[0]
    elif len(string) == 3:
        return string[1] + string[0] + string[2]
    elif len(string) == 4:
        return string[2] + string[0] + string[3] + string[1]
    elif len(string) == 5:
        return string[2] + string[0] + string[3] + string[1] + string[4]
    elif len(string) == 6:
        return string[3] + string[0] + string[4] + string[1] + string[5] + string[2]
    elif len(string) == 7:
        return string[3] + string[0] + string[4] + string[1] + string[5] + string[2] + string[6]
    elif len(string) == 8:
        return string[4] + string[0] + string[5] + string[1] + string[6] + string[2] + string[7] + string[3]
    else:
        return string


def pua_parser(string: str) -> str:
    list = string.split(' ')
    # new_list = [shuffle(st) for st in list]
    new_list = [st for st in list]
    res = pua_to_string(" ".join(new_list))
    return res


def check_order():
    with open('khitan-words.txt', 'r', encoding='utf-8') as f:
        store_numbers = [0]
        while True:
            line = f.readline()
            if not line:
                break
            _, sequence, *_ = line.strip().split('\t')
            numbers = sequence.split('-')
            numbers_int = [int(num) for num in numbers]
            if not compare(store_numbers, numbers_int):
                print('-'.join([str(num) for num in store_numbers]) + '\t' + '-'.join(numbers))
            store_numbers = numbers_int


if __name__ == '__main__':
    while True:
        inp = input()
        print(pua_parser(inp))