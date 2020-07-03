import hashlib


def check_json_data(json):
    if {'email', 'password', 'profile_id'} <= json.keys():
        return True
    else:
        return False


def generate_unique_key(json):
    email = json.get('email')
    result = hashlib.md5(email.encode())
    encoded_email = result.hexdigest()
    return encoded_email