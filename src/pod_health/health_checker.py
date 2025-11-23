from pod_health.k8s_client import get_core_v1_api
import json


def get_namespace_pod_health(namespace: str, core_v1):
   
    ret = core_v1.list_namespaced_pod(namespace)
    pods = ret.items
    total_pods = len(pods)
    unhealthy_pods = []
    unhealthy_count = 0
    for i in pods:
        name = i.metadata.name
        phase = i.status.phase
        
        if phase != "Running":
            unhealthy_count += 1
            unhealthy_pods.append({
                "name": name,
                "phase": phase
            })
    return {
        "namespace": namespace,
        "total_pods": total_pods,
        "unhealthy_count": unhealthy_count, 
        "unhealthy_pods": unhealthy_pods
    }

def pod_health_tool(namespace:str) -> dict:
    
    core_v1 = get_core_v1_api()
    report = get_namespace_pod_health(namespace, core_v1)
    return report


    pass

if __name__ == "__main__":
    print(json.dumps(pod_health_tool("xxxx"), indent=2))
