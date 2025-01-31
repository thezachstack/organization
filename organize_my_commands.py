#This script provides a list of Cisco and Juniper CLI troubleshooting commands in alphabetical order

#Provide a list of Cisco CLI troubleshooting commands
cisco_commands = [
  "show ip interface brief",
  "show version",
  "show running-config",
  "show startup-config",
  "show log",
  "debug ip packet",
  "show ip route",
  "show arp",
  "show mac address-table",
  "ping",
  "traceroute",
  "show cdp neighbors detail",
  "show ip protocols",
  "show spanning-tree",
  "show interfaces",
  "show interface status",
  "show ip ospf neighbor",
  "show ip bgp summary",
  "show processes cpu",
  "show processes memory",
  "show flash",
  "show environment",
  "show controllers",
  "clear counters",
  "show service-module",
  "debug ip ospf events",
  "show mls qos interface",
  "show vlan",
  "show etherchannel summary",
  "show ip nat translations",
  "show ip access-list",
  "show ip dhcp binding",
  "show ip flow top-talkers",
  "show vtp status",
  "show policy-map",
]

#Provide a list of Juniper CLI troubleshooting commands
juniper_commands = [
  "show interfaces terse",
  "show interfaces extensive",
  "show configuration",
  "show system uptime",
  "show system information",
  "show system processes extensive",
  "show system storage",
  "show route",
  "show route summary",
  "ping",
  "traceroute",
  "show arp",
  "show spanning-tree bridge",
  "show ethernet-switching table",
  "show chassis environment",
  "show chassis alarms",
  "show system alarms",
  "show bgp summary",
  "show ospf neighbor",
  "show isis adjacency",
  "show log messages",
  "show log <filename>",
  "clear log messages",
  "show system buffers",
  "show firewall",
  "show security policies",
  "show security flow session summary",
  "show route forwarding-table",
  "show dhcp server binding",
  "show system users",
  "show chassis hardware",
  "show configuration | compare",
  "show route receive-protocol bgp <neighbor>",
  "show system commit",
  "show class-of-service interfaces",
  "show security nat source summary",
  "show vlans",
  "show ethernet-switching interfaces",
  "monitor traffic interface <interface>",
  "request support information",
]

#Create a function that displays the lists alphabetically
def display_switch_commands(commands):
  print("\nUse this tool to organize your troubleshooting commands")
  for command in sorted(commands):
      print(command)

#Define the main program
def main():
  print("Welcome to the switching CLI command organizer")
  
  while True:
    print("\nOptions:")
    print("1. Cisco commands")
    print("2. Juniper commands")
    print("3. Exit")

    choice = input("\nChoose an option 1/2/3:\n").strip()
    if choice == "1":
      display_switch_commands(cisco_commands)
    elif choice == "2":
      display_switch_commands(juniper_commands)
    elif choice == "3": 
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

main()
