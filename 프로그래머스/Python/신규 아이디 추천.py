def remove_non_valid_char(new_id):
    return ''.join(list(filter(lambda x: True if x.isalnum() or x in ["-", "_", "."] else False, new_id)))

def remove_continuous_dots(new_id):
    while new_id.find("..") != -1:
        new_id = new_id.replace("..", ".")
    return new_id

def remove_start_and_end_dot(new_id: str):
    new_id = new_id[1:] if new_id.startswith('.') else new_id
    new_id = new_id[:-1] if new_id.endswith('.') else new_id
    return new_id


def add_a_if_new_id_is_empty(new_id):
    if not new_id:
        new_id = 'a'
    return new_id


def add_last_char_if_too_short(new_id):
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    return new_id


def solution(new_id: str):
    new_id = new_id.lower()
    new_id = remove_non_valid_char(new_id)
    new_id = remove_continuous_dots(new_id)
    new_id = remove_start_and_end_dot(new_id)
    new_id = add_a_if_new_id_is_empty(new_id)
    new_id = new_id[:15]
    new_id = remove_start_and_end_dot(new_id)
    new_id = add_last_char_if_too_short(new_id)
    return new_id
