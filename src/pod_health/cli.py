import argparse
from pod_health.k8s_client import get_core_v1_api

from pod_health.health_checker import get_namespace_pod_health
from pod_health.formatting import print_health_report

def main():

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--namespace")

    args = parser.parse_args()

    namespace = args.namespace

    core_v1 = get_core_v1_api()


    report = get_namespace_pod_health(namespace, core_v1)

    #print(report["unhealthy_count"])
    # print(""
    # ""
    # ""
    # ""
    # ""
    # ""
    # ""
    # ""
    # "")

    # if (report.get("unhealthy_count") != 0):
    #     print("Namespace:", report["namespace"])
    #     print("Total pods:", report["total_pods"])
    #     print("Unhealthy:", report["unhealthy_pods"])
    # pass
    
    print_health_report(report)

if __name__ == "__main__":
    main()