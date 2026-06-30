import os

class IssueTracker:
    def __init__(self):
        # Seeded with some mock data
        self.issues = {
            101: {"title": "Raw material variance on dock 2", "rca_attached": None},
            102: {"title": "Component-X Tensile Strength Failure", "rca_attached": None},
            103: {"title": "Label printer calibration error", "rca_attached": None}
        }
        self.next_id = 104

    def display_issues(self):
        print("\n=== CURRENT QUALITY ISSUES ===")
        print(f"{'ID':<6} | {'Issue Title':<45} | {'RCA Linked?'}")
        print("-" * 70)
        for issue_id, details in self.issues.items():
            rca_status = f"✅ Yes ({details['rca_attached']})" if details['rca_attached'] else "❌ No"
            print(f"{issue_id:<6} | {details['title']:<45} | {rca_status}")
        print("=" * 70)

    def create_issue(self):
        print("\n--- Create New Issue ---")
        title = input("Enter issue description/title: ").strip()
        if title:
            self.issues[self.next_id] = {"title": title, "rca_attached": None}
            print(f"🎉 Success: Created Issue ID {self.next_id}")
            self.next_id += 1
        else:
            print("⚠ Error: Issue title cannot be empty.")

    def attach_rca(self):
        print("\n--- Link RCA Document ---")
        try:
            issue_id = int(input("Enter Issue ID to link template to: "))
            if issue_id not in self.issues:
                print("⚠ Error: Issue ID not found.")
                return
            
            file_path = input("Enter path to the RCA Markdown file (e.g., rca_template.md): ").strip()
            
            if os.path.exists(file_path):
                self.issues[issue_id]["rca_attached"] = os.path.basename(file_path)
                print(f"🎉 Success: Successfully linked '{os.path.basename(file_path)}' to Issue ID {issue_id}!")
            else:
                print(f"⚠ Error: File '{file_path}' could not be located. Please verify path.")
        except ValueError:
            print("⚠ Error: Please enter a valid numerical Issue ID.")

    def run(self):
        while True:
            self.display_issues()
            print("\nOptions Menu:")
            print("1. Create New Issue")
            print("2. Link/Attach RCA Template to Issue")
            print("3. Exit System")
            choice = input("Select an option (1-3): ").strip()

            if choice == '1':
                self.create_issue()
            elif choice == '2':
                self.attach_rca()
            elif choice == '3':
                print("\nExiting Quality Management Mock Tracker. Goodbye!")
                break
            else:
                print("⚠ Invalid option selection. Try again.")

if __name__ == "__main__":
    tracker = IssueTracker()
    tracker.run()