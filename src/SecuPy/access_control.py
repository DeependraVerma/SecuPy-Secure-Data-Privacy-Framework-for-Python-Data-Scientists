class AccessControl:
    def __init__(self, roles=None):
        self.roles = roles if roles else {}

    def add_role(self, role_name, permissions):
        self.roles[role_name] = permissions

    def check_permission(self, role_name, permission):
        if role_name in self.roles:
            return permission in self.roles[role_name]
        else:
            return False
