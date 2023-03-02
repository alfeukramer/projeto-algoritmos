def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0].lower() < right[0].lower():
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) == 0:
        result += right
    else:
        result += left
    return result


def merge_sort(string):
    if len(string) <= 1 or not string:
        return string

    list = [lt for lt in string]

    left = merge_sort(list[:len(list) // 2])
    right = merge_sort(list[len(list) // 2:])

    return merge(left, right)


def is_anagram(first_string, second_string):

    first_word = ''.join(merge_sort(list(first_string.lower())))
    second_word = ''.join(merge_sort(list(second_string.lower())))

    verify = False
    
    if first_word == second_word:
        verify = True

    result = (first_word, second_word, verify)

    return result
