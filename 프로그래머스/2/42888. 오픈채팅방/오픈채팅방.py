def solution(record):
    id_name_dic = {}
    for item in record:
        action_id_name = item.split()

        if action_id_name[0] == "Leave":
            continue

        _, user_id, username = action_id_name

        id_name_dic[user_id] = username

    result = []

    for item in record:
        action_id_name = item.split()

        action = action_id_name[0]

        if action == "Change":
            continue

        action = action_id_name[0]
        user_id = action_id_name[1]
        result.append(f"{id_name_dic[user_id]}님이 " + ("들어왔습니다." if action == "Enter" else "나갔습니다."))

    return result
