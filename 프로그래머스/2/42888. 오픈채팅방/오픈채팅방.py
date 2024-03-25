def solution(record):
    id_name_dic = {}
    for item in record:
        action_id_name = item.split()

        if action_id_name[0] == "Leave":
            continue

        action, id, name = action_id_name

        id_name_dic[id] = name

    result = []

    for item in record:
        action_id_name = item.split()
        if action_id_name[0] == "Leave":
            action, id = action_id_name
            result.append(f"{id_name_dic[id]}님이 나갔습니다.")
        elif action_id_name[0] == "Enter":
            result.append(f"{id_name_dic[action_id_name[1]]}님이 들어왔습니다.")

    return result
