from pod_health.health_checker import get_namespace_pod_health
from pod_health.k8s_client import get_core_v1_api

def print_health_report(report: dict):

    core_v1 = get_core_v1_api()

    namespace = report["namespace"]
    total_pods = report["total_pods"]
    unhealthy_count = report["unhealthy_count"]

    print(""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    "")

    print("Namespace:", namespace)
    print("Total pods:", total_pods)
    print("Unhealthy:", unhealthy_count)
    print("-----------------------------------------")

    if unhealthy_count == 0:
        print("All pods are healthy ✅")
        return
    else:

        print("NAME\t\t\t\t\t\t\tPHASE")
        print("----------------------------------------------------------")
        unhealthy_pods = report["unhealthy_pods"]
        for pod in unhealthy_pods:
            name = pod["name"]
            phase = pod["phase"]
            print(name,"\t\t",phase)



