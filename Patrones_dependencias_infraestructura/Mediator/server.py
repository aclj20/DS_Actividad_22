from dependency import DependsOn

class ServerFactoryModule:
    def __init__(self, depends=None):
        self.depends = depends

    def build(self):
        triggers = {"name": "hello-world-server"}
        if self.depends:
            triggers["depends_on"] = f"{self.depends.resource_type}.{self.depends.resource_id}"
        return {
            "resource": {
                "null_resource": {
                    "server": {"triggers": triggers}
                }
            }
        }

    def outputs(self):
        return DependsOn("null_resource", "server", {"name": "hello-world-server"})

# Fase 5
# Método que simula el estado de Server
def check_server_status():
    return {"status": "active", "ip": "192.168.0.1"}
