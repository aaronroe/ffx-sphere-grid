import json


def load_nodes(graph='international-hd-remaster'):
	return load_data('nodes', graph=graph)


def load_characters(graph='international-hd-remaster'):
	return load_data('characters', graph=graph)


def load_abilities(graph='international-hd-remaster'):
	return load_data('abilities', graph=graph)


def load_data(data_type, graph='international-hd-remaster'):
	filepath = './data/{graph}/{data_type}.json'.format(graph=graph, data_type=data_type)
	return _data_from_file(filepath)


def _data_from_file(filepath):
	with open(filepath) as f:
		json_blob = f.read()
		return json.loads(json_blob)
