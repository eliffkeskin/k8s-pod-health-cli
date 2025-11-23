from kubernetes import client, config

def get_core_v1_api():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    return v1