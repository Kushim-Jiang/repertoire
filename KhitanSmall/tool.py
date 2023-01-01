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
                print('-'.join([str(num) for num in store_numbers]) + '\t' +
                      '-'.join(numbers))
            store_numbers = numbers_int
