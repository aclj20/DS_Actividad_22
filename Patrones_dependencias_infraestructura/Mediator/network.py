from dependency import DependsOn

class NetworkFactoryModule:
    def build(self):
        return {
            "resource": {
                "null_resource": {
                    "network": {
                        "triggers": {
                            "name": "hello-world-network"
                        }
                    }
                }
            }
        }

    def outputs(self):
        return DependsOn("null_resource", "network", {"name": "hello-world-network"})

# Fase 5
# Método que simula el estado de Network
def check_network_status():
    return {"status": "active", "ip": "192.168.0.1"}
