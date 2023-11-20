rooms = {
    '101': {'status': 'available', 'guest': None},
    '102': {'status': 'available', 'guest': None},
    '103': {'status': 'available', 'guest': None},
}

staff = []

def display_available_rooms():
    print("Available Rooms:")
    for room, info in rooms.items():
        if info['status'] == 'available':
            print(f"Room {room}")


def book_room():
    room_number = input("Enter room number to book: ")
    if room_number in rooms:
        if rooms[room_number]['status'] == 'available':
            guest_name = input("Enter guest name: ")
            rooms[room_number]['status'] = 'occupied'
            rooms[room_number]['guest'] = guest_name
            print(f"Room {room_number} booked for {guest_name}.")
        else:
            print(f"Room {room_number} is already occupied.")
    else:
        print("Invalid room number.")

def cancel_booking():
    room_number = input("Enter room number to cancel booking: ")
    if room_number in rooms:
        if rooms[room_number]['status'] == 'occupied':
            guest_name = rooms[room_number]['guest']
            rooms[room_number]['status'] = 'available'
            rooms[room_number]['guest'] = None
            print(f"Booking for {guest_name} in Room {room_number} canceled.")
        else:
            print(f"Room {room_number} is not occupied.")
    else:
        print("Invalid room number.")

def display_occupied_rooms():
    print("Occupied Rooms:")
    for room, info in rooms.items():
        if info['status'] == 'occupied':
            guest_name = info['guest']
            print(f"Room {room} - Guest: {guest_name}")

def add_staff():
    staff_name = input("Enter staff name: ")
    staff.append(staff_name)
    print(f"{staff_name} added to staff.")

def view_staff():
    print("Staff List:")
    for s in staff:
        print(s)

def update_staff():
    old_name = input("Enter staff name to update: ")
    if old_name in staff:
        new_name = input("Enter new name: ")
        staff[staff.index(old_name)] = new_name
        print(f"{old_name} updated to {new_name} in staff.")
    else:
        print("Staff not found.")

def delete_staff():
    staff_name = input("Enter staff name to delete: ")
    if staff_name in staff:
        staff.remove(staff_name)
        print(f"{staff_name} removed from staff.")
    else:
        print("Staff not found.")

def search_staff():
    search_name = input("Enter staff name to search: ")
    if search_name in staff:
        print(f"{search_name} found in staff.")
    else:
        print(f"{search_name} not found in staff.")

while True:
    print("\nHotel Management System")
    print("-----------------------")
    print("1. Display Available Rooms")
    print("2. Book a Room")
    print("3. Cancel Booking")
    print("4. Display Occupied Rooms")
    print("5. Add Staff")
    print("6. View Staff")
    print("7. Update Staff")
    print("8. Delete Staff")
    print("9. Search Staff")
    print("10. Quit")
    
    choice = input("Enter your choice (1-10): ")
    
    if choice == '1':
        display_available_rooms()
    elif choice == '2':
        book_room()
    elif choice == '3':
        cancel_booking()
    elif choice == '4':
        display_occupied_rooms()
    elif choice == '5':
        add_staff()
    elif choice == '6':
        view_staff()
    elif choice == '7':
        update_staff()
    elif choice == '8':
        delete_staff()
    elif choice == '9':
        search_staff()
    elif choice == '10':
        print("Exiting the Hotel Management System. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        