#this is a script to organize your favorite links alphabetically!

#provide a list of favorite links
favorite_links = [
  "https://www.coursera.org",
  "https://youtube.com",    
  "https://brilliant.org",
  "https://www.deeplerning.ai",
  "https://www.codecademy.com",
  "https://huggingface.co",
  "https://quizlet.com",
  "https://learningnetwork.cisco.com",
  "https://u.cisco.com",
  "https://github.com",
  "https://www.codewars.com",
  "https://www.executeprogram.com",
  "https://learningportal.juniper.net",
  "https://www.w3schools.com",
  "https://training.linuxfoundation.org",
  "https://www.splunk.com",
  "https://pythoninstitute.org",
  "https://learn.microsoft.com",
  "https://d1.awsstatic.com",
  "https://cloud.google.com/learn",
  "https://www.vmware.com/topic",
  "https://www.f5.com",
  "https://docs.ansible.com/ansible",
  "https://www.docker.com",
  "https://developer.cisco.com",
  "https://www.ciscopress.com",
  "https://www.paloaltonetworks.com",
  "https://www.redhat.com",
  "https://www.isc2.org",
  "https://blogs.cisco.com",
  "https://codefinity.com",
]

#define a function that displays the list alphabetically
def display_sorted_links(links):
  print("\nYour favorite links, organized alphabetically:")
  for link in sorted(links):
    print(link)
  
#define the main program
def main():
  print("Welcome to the Favorite Links Organizer!")

  while True:
    print("\nOptions:")
    print("1. View links")
    print("2. Add a new link")
    print("3. Exit")

    choice = input("Choose an option 1/2/3:\n").strip()
    if choice == "1":
      display_sorted_links(favorite_links)
    elif choice == "2":
      new_link = input("Enter the URL of the new link:\n").strip()
      if new_link and new_link not in favorite_links:
        favorite_links.append(new_link)
        print(f"Added: {new_link}")
      else:
        print("Invalid or duplicate link")
    elif choice == "3":
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

main()
