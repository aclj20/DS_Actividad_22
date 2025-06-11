class DependsOn:
    def __init__(self, resource_type, resource_id, attributes=None):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.attributes = attributes or {}

# Establece dependencias entre recursos
def create_dependency_graph():
    return {
        "network": ["server", "firewall"],
        "server": [],
        "firewall": ["network"]
    }
