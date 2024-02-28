from db import district_list

def create(dictionary):
    """
    Function to add a dictionary to the district_list.
    """
    largest_id = max(item['id'] for item in district_list)
    new_id = largest_id + 1
    dictionary['id'] = new_id
    district_list.append(dictionary)
    print(district_list)

def retrieve(id):
    """
    Function to retrieve a dictionary with the given id.
    """
    for item in district_list:
        if item['id'] == id:
            return item
    return None

def update(id, name):
    """
    Function to update the name of a dictionary with the given id.
    """
    for item in district_list:
        if item['id'] == id:
            item['name'] = name
            break
    print(district_list)

def delete(id):
    """
    Function to delete a dictionary with the given id.
    """
    for item in district_list:
        if item['id'] == id:
            district_list.remove(item)
            break
    print(district_list)