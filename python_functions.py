def convert_dictionary_to_dataframe(dictionary, name_key="key", name_value="value"):
    return pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dictionary.items()])).melt().dropna().rename(
        columns={"variable": name_key, "value": name_value})


def display_gif(fn):
    '''Source: https://github.com/ipython/ipython/issues/10045'''
    from IPython import display
    return display.HTML('<img src="{}">'.format(fn))


def filter_dictionary(dictionary, key_list):
    return {key: dictionary[key] for key in key_list}


def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def read_dictionary_from_file(file):
    with open(file, "rb") as f:
        dictionary = json.load(f)
    return dictionary


def unique(input_list):
    return list(set(input_list))