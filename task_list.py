#This script is used to generate and view a list of tasks

#This is a list of my personal tasks
tasks = [
    "Obtain Microsoft Certified Azure Fundamentals Certification",
    "Obtain Microsoft Certified: Dynamics 365 Fundamentals (CRM)",
    "ObtainMicrosoft Certified: Dynamics 365 Fundamentals (ERP)",
    "Obtain Amazon Web Services Certified Cloud Practitioner Certification",
    "Obtain Google Associate Cloud Engineer Certification",
    "Obtain Microsoft Certified Azure Artificial Intelligence Fundamentals Certification",
    "Obtain Certified Entry-Level Python Programmer Certification",
    "Obtain Splunk Core Certified User Certification",
    "Obtain Linux Plus Certification",
    "Obtain Security Onion Certified Professional Certification",
    "Obtain Wireshark Certified Network Analyst (WCNA) Certification",
    "Obtain Kubernetes and Cloud Native Associate Certification",
    "Obtain Certified Security Operations Center Analyst Certification",
    "Obtain Docker Certified Associate Certification",
    "Obtain F5 Certified BIG-IP Administrator Certification",
    "Obtain Cisco Certified Network Associate in Routing and Switching Certification",
    "Obtain Juniper Networks Certified Associate Certification",
    "Obtain Palo Alto Networks Certified Cybersecurity Associate Certification",
    "Obtain VMware Certified Technical Associate Certification",
    "Obtain Gigamon Certified Professional Certification",
    "Obtain Red Hat Certified System Administrator Certification",
    "Obtain Red Hat Certified Specialist in Ansible Automation Certification",
    "Obtain Cisco Certified DevNet Associate Certification",
    "Obtain Amazon Web Services Certified Machine Learning Specialty Certification",
    "Obtain Google Artificial Intelligence Essentials Certification",
    "Obtain Microsoft Certified Azure Database Administrator Associate Certification",
    "Obtain SolarWinds Certified Professional Exam Certification",
    "Obtain Cisco 300-415 Implementing Cisco SD-WAN Solutions Certification",
    "Obtain Cisco 300-425 Designing Cisco Enterprise Wireless Networks Certification",
    "Obtain Cisco 300-430 Implementing Cisco Enterprise Wireless Networks Certification",
    "Obtain Cisco 300-620 Implementing Cisco Application Centric Infrastructure Certification",
    "Obtain Cisco 300-715 Implementing and Configuring Cisco Identity Services Engine Certification",
    "Obtain Cisco 300-725 Securing the Web with Cisco Secure Web Appliance Certification",
    "Obtain Cisco 300-730 Implementing Secure Solutions with Virtual Private Networks Certification",
    "Obtain Cisco 350-701 Implementing and Operating Cisco Security Core Technologies Certification",
    "Obtain Cisco Certified Design Expert Certification\n"
]

#This function is used to display the tasks in the list
def view_tasks():
  if not tasks:
    print("\nNo tasks available.")
  else:
    print("\nYour current task list:\n")
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")

#This function is used to add a task to the list
def add_task():
  new_task = input("Enter a new task:\n").strip()
  if new_task and new_task not in tasks:
    tasks.append(new_task)
    print("Your task was successfully added.")
  else:
    print("Your task could not be added to the list.")

#This function is used to remove a task from the list
def remove_task():
  old_task = input("Remove an existing task:\n").strip()
  if old_task and old_task in tasks:
    tasks.remove(old_task)
    print("Your task was successfully removed.")
  else:
    print("Your task could not be removed from the list.")

#This loop is used display options and ask for user input
while True:
  print("Use the options below to view or update your current tasks:")
  print("\n1. View Tasks")
  print("2. Add Task")
  print("3. Remove Task")
  print("4. Exit\n")
  choice = input()
  if choice == "1":
    view_tasks()
  elif choice == "2":
    add_task()
  elif choice == "3":
    remove_task()
  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice, please try again.")
