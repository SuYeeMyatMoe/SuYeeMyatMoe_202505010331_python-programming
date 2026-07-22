def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    student_name = input("Student Name : ")
    student_id = input("Student ID   : ")
    issue = input("Issue        : ")
    location = input("Location     : ")
    priority = input("Priority (High/Medium/Low): ")

    # Determine assigned technician based on priority
    priority_lower = priority.strip().lower()
    if priority_lower == "high":
        technician = "Ahmad"
    elif priority_lower == "medium":
        technician = "Siti"
    elif priority_lower == "low":
        technician = "Ali"
    else:
        technician = "Unassigned"

    status = "Pending"

    # Return ticket data as a dictionary 
    return {
        "name": student_name,
        "id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": status,
    }