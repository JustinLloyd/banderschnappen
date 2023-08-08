import copy
import json
import os


def prune_structure(d):
    if not isinstance(d, dict):
        return d
    return {k: prune_structure(v) for k, v in d.items() if v and prune_structure(v)}


def merge_structures(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_structures(result[key], value)
        else:
            result[key] = value

    return result


def make_quoted_prompt(data, prefix=None):
    return f'"""{make_prompt(data, prefix)}"""'

def make_delimited_prompt(data, prefix=None):
    return f'<data>\n{make_prompt(data, prefix)}\n</data>'


def make_prompt(data, prefix=None):
    if not data:
        raise ValueError("No data supplied, this is probably an internal error")

    # Recursive function to check if list contains only strings
    def is_list(lst):
        for item in lst:
            if isinstance(item, list):
                if not is_list(item):
                    return False
            elif not isinstance(item, str):
                return False
        return True

    if isinstance(data, list) and is_list(data):
        output = '\n'.join(data) + '\n'
    else:
        output = json.dumps(data)

    if prefix:
        output = f'{{\n"{prefix}": {output}\n}}'

    return output


def save_state_data(state_name, data_obj):
    try:
        ensure_state_data_directory_exists()
        with open(f'state-data/{state_name}.json', 'w') as file:
            json.dump(data_obj, file)
    except Exception as e:
        raise SaveDataError(f"Error saving state data for '{state_name}': {str(e)}")


def load_state_data(state_name):
    try:
        ensure_state_data_directory_exists()
        if not os.path.exists(f'state-data/{state_name}.json'):
            return {}

        with open(f'state-data/{state_name}.json') as file:
            return json.load(file)
    except Exception as e:
        raise LoadDataError(f"Error loading state data for '{state_name}': {str(e)}")


def ensure_state_data_directory_exists():
    try:
        if not os.path.exists('state-data'):
            os.makedirs('state-data')
    except Exception as e:
        raise DirectoryCreationError(f"Error creating 'state-data' directory: {str(e)}")


def load_prompt(prompt_file):
    with open(f"prompts/{prompt_file}.prompt") as file:
        return json.load(file)


def strip_descriptions(entity):
    stripped_entity = copy.deepcopy(entity)
    if 'class' in stripped_entity and 'description' in stripped_entity['class']:
        stripped_entity['class']['description'] = ''
    if 'background' in stripped_entity and 'description' in stripped_entity['background']:
        stripped_entity['background']['description'] = ''
    if 'abilities' in stripped_entity:
        for ability in stripped_entity['abilities']:
            if 'description' in ability:
                ability['description'] = ''
    if 'traits' in stripped_entity:
        for trait in stripped_entity['traits']:
            if 'description' in trait:
                trait['description'] = ''
    if 'skills' in stripped_entity:
        for skill in stripped_entity['skills']:
            if 'description' in skill:
                skill['description'] = ''

    return stripped_entity


class SaveDataError(Exception):
    pass


class LoadDataError(Exception):
    pass


class DirectoryCreationError(Exception):
    pass
