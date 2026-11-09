class ARP_RARP_Simulator:

    def __init__(self):

        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18"
        }

        self.rarp_table = {
            v: k for k, v in self.arp_table.items()
        }

    def arp_request(self, ip):

        mac = self.arp_table.get(ip)

        if mac:
            print("IP Address:", ip)
            print("MAC Address:", mac)
        else:
            print("IP Address not found")

    def rarp_request(self, mac):

        ip = self.rarp_table.get(mac)

        if ip:
            print("MAC Address:", mac)
            print("IP Address:", ip)
        else:
            print("MAC Address not found")


simulator = ARP_RARP_Simulator()

simulator.arp_request("192.168.1.1")

simulator.rarp_request("00:0a:95:9d:68:16")