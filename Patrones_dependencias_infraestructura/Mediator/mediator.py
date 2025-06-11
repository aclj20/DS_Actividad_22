import json
from network import check_network_status
from server import check_server_status
from firewall import check_firewall_status
from dependency import create_dependency_graph

class Mediator:
    """
    Clase Mediator que orquestra las relaciones entre componentes.
    Los componentes no se comunican entre ellos, solo conocen de
    la existencia de Mediator.
    """
    def __init__(self):
        self.network_status = None
        self.server_status = None
        self.firewall_status = None

    def check_all_statuses(self):
        # Revisión de estados
        self.network_status = check_network_status()
        self.server_status = check_server_status()
        self.firewall_status = check_firewall_status()
        print("Estados revisados.")

    def generate_main(self):
        # Generación de main.tf.json
        main_tf = {
            "resource": {
                "network": self.network_status,
                "server": self.server_status,
                "firewall": self.firewall_status,
            },
            "dependency_graph": create_dependency_graph()
        }
        with open("main.tf.json", "w") as f:
            json.dump(main_tf, f, indent=2)
        print("main.tf.json generated.")

def main():
    mediator = Mediator()
    mediator.check_all_statuses()
    mediator.generate_main()

if __name__ == "__main__":
    main()
