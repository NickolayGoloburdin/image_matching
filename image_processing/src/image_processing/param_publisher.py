#!/usr/bin/env python3  
import rospy
import os
import yaml

def load_params():
    data_path = find_path_to_config()
    if data_path is None:
        home = os.getenv("HOME")
        data_path = home+'/copa5/config/config.yaml'
        print("NO EXTEND PARAM FILE, USE DEFAULT")
    else:
        print("USE EXTEND PARAM FILE", data_path)
    with open(data_path) as file:
        params = yaml.full_load(file)
    return params

def find_path_to_config():
    name = 'config.yaml'
    path = '/media/'
    for root, dirs, files in os.walk(path+os.getlogin()):
        if name in files:
            return os.path.join(root, name)
    return None

if __name__ == '__main__':
    rospy.init_node('book_action_client_py')
    params = load_params()
    for key in params:
        rospy.set_param(key, params[key])    
    