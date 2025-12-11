import mysql.connector

# -------------------------
# DATABASE CONNECTION
# -------------------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # Add your MySQL password if needed
    database="hospital_db"
)

cursor = db.cursor()

print("✔ Connected to hospital_db")


# ---------------------------------------------------
# ADD DATA FUNCTIONS
# ---------------------------------------------------

def add_patient():
    print("\n--- Add Patient ---")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender (Male/Female): ")
    phone = input("Phone: ")
    address = input("Address: ")

    query = """
        INSERT INTO patients (name, age, gender, phone, address)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (name, age, gender, phone, address)
    cursor.execute(query, values)
    db.commit()
    print("✔ Patient Added!\n")


def add_doctor():
    print("\n--- Add Doctor ---")
    name = input("Name: ")
    specialization = input("Specialization: ")
    phone = input("Phone: ")
    email = input("Email: ")

    query = """
        INSERT INTO doctors (name, specialization, phone, email)
        VALUES (%s, %s, %s, %s)
    """
    values = (name, specialization, phone, email)
    cursor.execute(query, values)
    db.commit()
    print("✔ Doctor Added!\n")


def add_appointment():
    print("\n--- Add Appointment ---")
    patient_id = input("Patient ID: ")
    doctor_id = input("Doctor ID: ")
    date = input("Appointment Date (YYYY-MM-DD HH:MM:SS): ")
    reason = input("Reason: ")

    query = """
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason)
        VALUES (%s, %s, %s, %s)
    """
    values = (patient_id, doctor_id, date, reason)
    cursor.execute(query, values)
    db.commit()
    print("✔ Appointment Added!\n")


def add_treatment():
    print("\n--- Add Treatment ---")
    patient_id = input("Patient ID: ")
    doctor_id = input("Doctor ID: ")
    diagnosis = input("Diagnosis: ")
    medicines = input("Medicines: ")

    query = """
        INSERT INTO treatments (patient_id, doctor_id, diagnosis, medicines)
        VALUES (%s, %s, %s, %s)
    """
    values = (patient_id, doctor_id, diagnosis, medicines)
    cursor.execute(query, values)
    db.commit()
    print("✔ Treatment Added!\n")


def add_room():
    print("\n--- Add Room ---")
    room_number = input("Room Number: ")
    room_type = input("Room Type (General/ICU/Private): ")
    price = input("Price per day: ")

    query = """
        INSERT INTO rooms (room_number, room_type, price_per_day)
        VALUES (%s, %s, %s)
    """
    values = (room_number, room_type, price)
    cursor.execute(query, values)
    db.commit()
    print("✔ Room Added!\n")


def admit_patient():
    print("\n--- Admit Patient ---")
    patient_id = input("Patient ID: ")
    room_id = input("Room ID: ")

    # Mark room as unavailable
    cursor.execute("UPDATE rooms SET is_available = FALSE WHERE room_id = %s", (room_id,))
    
    query = """
        INSERT INTO admissions (patient_id, room_id)
        VALUES (%s, %s)
    """
    cursor.execute(query, (patient_id, room_id))
    db.commit()
    print("✔ Patient Admitted!\n")


# ---------------------------------------------------
# VIEW FUNCTIONS
# ---------------------------------------------------

def view_table(table_name):
    print(f"\n--- {table_name.upper()} ---")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print()


# ---------------------------------------------------
# UPDATE FUNCTIONS
# ---------------------------------------------------

def update_patient():
    patient_id = input("Enter Patient ID: ")

    print("1. Name")
    print("2. Age")
    print("3. Phone")
    print("4. Address")
    choice = input("Choose field: ")

    columns = {
        "1": "name",
        "2": "age",
        "3": "phone",
        "4": "address"
    }

    if choice in columns:
        new_value = input("Enter new value: ")
        column = columns[choice]
        query = f"UPDATE patients SET {column} = %s WHERE patient_id = %s"
        cursor.execute(query, (new_value, patient_id))
        db.commit()
        print("✔ Patient Updated!\n")
    else:
        print("❌ Invalid choice")


# ---------------------------------------------------
# DELETE FUNCTIONS
# ---------------------------------------------------

def delete_record(table, id_column):
    record_id = input(f"Enter {table} ID: ")
    cursor.execute(f"DELETE FROM {table} WHERE {id_column} = %s", (record_id,))
    db.commit()
    print("🗑 Record Deleted!\n")


# ---------------------------------------------------
# MAIN MENU
# ---------------------------------------------------

def main():
    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Add Appointment")
        print("4. Add Treatment")
        print("5. Add Room")
        print("6. Admit Patient")
        print("7. View Patients")
        print("8. View Doctors")
        print("9. View Appointments")
        print("10. View Treatments")
        print("11. View Rooms")
        print("12. View Admissions")
        print("13. Update Patient")
        print("14. Delete Patient")
        print("15. Exit")

        choice = input("Choose an option: ")

        if choice == "1": add_patient()
        elif choice == "2": add_doctor()
        elif choice == "3": add_appointment()
        elif choice == "4": add_treatment()
        elif choice == "5": add_room()
        elif choice == "6": admit_patient()
        elif choice == "7": view_table("patients")
        elif choice == "8": view_table("doctors")
        elif choice == "9": view_table("appointments")
        elif choice == "10": view_table("treatments")
        elif choice == "11": view_table("rooms")
        elif choice == "12": view_table("admissions")
        elif choice == "13": update_patient()
        elif choice == "14": delete_record("patients", "patient_id")
        elif choice == "15":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid Option")


main()
