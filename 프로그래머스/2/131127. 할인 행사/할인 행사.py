def solution(want, number, discount):
    count = sum(number)
    target = {want[i]: number[i] for i in range(len(want))}
    window = {}
    for i in range(count):
        add_item = discount[i]
        window[add_item] = window.get(add_item, 0) + 1

    delete_index = 0
    add_index = delete_index + count
    rt = 0
    while True:
        if all([w_k in target and target[w_k] == w_v for w_k, w_v in window.items()]):
            rt += 1

        if add_index >= len(discount):
            break

        delete_item = discount[delete_index]
        if window[delete_item] > 1:
            window[delete_item] -= 1
        else:
            window.pop(delete_item)

        add_item = discount[add_index]
        window[add_item] = window.get(add_item, 0) + 1

        delete_index += 1
        add_index += 1

    return rt

