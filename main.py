import controller

def main():
    while True:
        print("\n📌 Job Application Tracker")
        print("1️⃣ Add a Job")
        print("2️⃣ View Jobs")
        print("3️⃣ Update Job Status")
        print("4️⃣ Delete a Job")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            company = input("Enter Company Name: ")
            position = input("Enter Job Position: ")
            status = input("Enter Job Status (Applied/In Review/Interviewed/Rejected/Hired): ")
            controller.add_job(company, position, status)

        elif choice == "2":
            jobs = controller.view_jobs()
            print("\n📌 Saved Jobs:")
            if jobs:
                for job in jobs:
                    print(f"🆔 {job[0]} | 🏢 {job[1]} | 💼 {job[2]} | 📌 {job[3]}")
            else:
                print("❌ No jobs found.")

        elif choice == "3":
            job_id = input("Enter Job ID to update: ")
            new_status = input("Enter new status: ")
            controller.update_job_status(job_id, new_status)

        elif choice == "4":
            job_id = input("Enter Job ID to delete: ")
            controller.delete_job(job_id)

        elif choice == "5":
            print("🚀 Exiting... Have a great day!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
