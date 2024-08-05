"""Common functions that can be used multiple times.
   Open yml file."""
import os
import yaml

def read_conf():
    """Read the configuration"""
    mainpath =  os.getcwd()
    with open("{0}/config.yaml".format(mainpath), 'r') as file:
        print(file)
        prime_service = yaml.safe_load(file)
    return prime_service

def get_uri():
    """Reads the root host/domain from configuration (config.yml)"""
    conf = read_conf()
    domain_name = conf["host"]
    port = conf["port"]
    protocol = conf["protocol"]
    return "{0}://{1}:{2}".format(protocol, domain_name, port)

def get_websocket_uri():
    """Reads the websocket uri from configuration (config.yml)"""
    conf = read_conf()
    ip = conf["websockets"]["mousemove"]["ip"]
    port = conf["websockets"]["mousemove"]["port"]
    return (ip, port)
