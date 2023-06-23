class Device:
    def __init__(self, ip, name, version):
        self.ip = ip
        self.name = name
        self.version = version
        
    # getter and setter methods
    def get_ip(self):
        return self.ip
    
    def set_ip(self, ip):
        self.ip = ip
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_version(self):
        return self.version
    
    def set_version(self, version):
        self.version = version
        
    def __str__(self):
        return f"IP: {self.ip}, Name: {self.name}, Version: {self.version}"
    
    def __repr__(self):
        return f"IP: {self.ip}, Name: {self.name}, Version: {self.version}"