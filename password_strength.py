import re


def load_password_blacklist(filepath):
    with open(filepath, 'r') as data:
        data_bad_passwords = data.read()
    list_of_bad_passwords = re.findall(r'[\w]+', data_bad_passwords)
    return list_of_bad_passwords

def get_password_strength(password, filepath_to_list):
    if len(password) < 6:
        return 1
    else:
        password_strength = 1
        if len(password) > 12:  
            password_strength += 2
        if password.lower() != password and password.upper() != password: 
            password_strength += 1
        if password not in load_password_blacklist(filepath_to_list):
            password_strength += 3
        if re.findall(r'[\d]', password): 
            password_strength += 1
        if re.findall(r'[!@#$%^&*><}{]', password):
            password_strength += 2
        return (password_strength)


if __name__ == '__main__':
    password = input('Enter your password to get strength: ')
    filepath_to_blacklist = input('Enter filepath to blacklist:')
    print('{} {}'.format('Your password is', str(get_password_strength(password,filepath_to_blacklist)) + '/10'))
