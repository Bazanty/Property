import bcrypt
import getpass
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from property.database import init_db, SessionLocal
from property.models import Agent, Property, Room, Client, Payment
from datetime import datetime

init_db()

def signup():
    """Register a new agent with password confirmation."""
    name = input('Your name: ')
    email = input('Your email: ')

    # Ask for password and confirm it, hiding the input for both
    while True:
        password = getpass.getpass('Your password: ')  # Hides the password input
        confirm_password = getpass.getpass('Repeat your password: ')  # Hides the confirmation password input
        
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db = SessionLocal()
    try:
        # Create and add the new agent
        agent = Agent(name=name, email=email, hashed_password=hashed_password)
        db.add(agent)
        db.commit()
        print(f"Agent {name} registered and logged in successfully!")
    except IntegrityError:
        db.rollback()
        print("Email already exists. Please try a different email.")
    finally:
        db.close()

def login():
    """Log in an existing agent."""
    email = input('Your email: ')
    password = getpass.getpass('Your password: ')  # Hides the password input
    db = SessionLocal()
    try:
        agent = db.query(Agent).filter(Agent.email == email).first()
        if agent and bcrypt.checkpw(password.encode('utf-8'), agent.hashed_password):
            print(f"Logged in successfully as {agent.name}!")
        else:
            print("Invalid email or password. Please try again.")
    finally:
        db.close()

def add_property():
    """Add a new property."""
    address = input('Property address: ')
    location = input('Property location: ')
    agent_id = int(input('Agent ID: '))
    db = SessionLocal()
    try:
        property = Property(address=address, location=location, agent_id=agent_id)
        db.add(property)
        db.commit()
        print(f"Property at {address} added successfully!")
    except IntegrityError:
        db.rollback()
        print("Failed to add property. Please check the provided details.")
    finally:
        db.close()

def add_client():
    """Add a new client."""
    name = input('Client name: ')
    email = input('Client email: ')
    password = getpass.getpass('Client password: ')  # Hides the password input
    agent_id = int(input('Agent ID: '))
    property_id = int(input('Property ID: '))
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db = SessionLocal()
    try:
        client = Client(name=name, email=email, hashed_password=hashed_password, agent_id=agent_id, property_id=property_id)
        db.add(client)
        db.commit()
        print(f"Client {name} added successfully!")
    except IntegrityError:
        db.rollback()
        print("Failed to add client. Please check the provided details.")
    finally:
        db.close()

def add_room():
    """Add a new room to a property."""
    type = input('Room type: ')
    size = float(input('Room size: '))
    property_id = int(input('Property ID: '))
    db = SessionLocal()
    try:
        room = Room(type=type, size=size, property_id=property_id)
        db.add(room)
        db.commit()
        print(f"Room of type {type} with size {size} added successfully to property ID {property_id}!")
    except IntegrityError:
        db.rollback()
        print("Failed to add room. Please check the provided details.")
    finally:
        db.close()

def add_payment():
    """Add a new payment for a client."""
    amount = float(input('Payment amount: '))
    date = input('Payment date (YYYY-MM-DD or DD/MM/YYYY): ')
    client_id = int(input('Client ID: '))
    db = SessionLocal()
    try:
        try:
            payment_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            payment_date = datetime.strptime(date, '%d/%m/%Y').date()
        payment = Payment(amount=amount, date=payment_date, client_id=client_id)
        db.add(payment)
        db.commit()
        print(f"Payment of {amount} on {payment_date} added successfully for client ID {client_id}!")
    except IntegrityError:
        db.rollback()
        print("Failed to add payment. Please check the provided details.")
    except ValueError:
        print("Invalid date format. Please use either YYYY-MM-DD or DD/MM/YYYY.")
    finally:
        db.close()

def list_clients():
    """List all clients."""
    db = SessionLocal()
    clients = db.query(Client).all()
    for client in clients:
        print(f"Client ID: {client.id}, Name: {client.name}, Email: {client.email}")
    db.close()

def list_properties():
    """List all properties."""
    db = SessionLocal()
    properties = db.query(Property).all()
    for property in properties:
        print(f"Property ID: {property.id}, Address: {property.address}, Location: {property.location}")
    db.close()

def list_rooms():
    """List all rooms."""
    db = SessionLocal()
    rooms = db.query(Room).all()
    for room in rooms:
        print(f"Room ID: {room.id}, Type: {room.type}, Size: {room.size}, Property ID: {room.property_id}")
    db.close()

def update_property():
    """Update an existing property."""
    property_id = int(input('Property ID: '))
    new_address = input('New address: ')
    new_location = input('New location: ')
    db = SessionLocal()
    property = db.query(Property).filter(Property.id == property_id).first()
    if property:
        property.address = new_address
        property.location = new_location
        db.commit()
        print(f"Property ID {property_id} updated successfully!")
    else:
        print(f"Property ID {property_id} not found.")
    db.close()

def update_client():
    """Update an existing client."""
    client_id = int(input('Client ID: '))
    name = input('New name: ')
    email = input('New email: ')
    db = SessionLocal()
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        client.name = name
        client.email = email
        db.commit()
        print(f"Client ID {client_id} updated successfully!")
    else:
        print(f"Client ID {client_id} not found.")
    db.close()

def delete_client():
    """Delete an existing client."""
    client_id = int(input('Client ID: '))
    db = SessionLocal()
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
        print(f"Client ID {client_id} deleted successfully!")
    else:
        print(f"Client ID {client_id} not found.")
    db.close()

def delete_room():
    """Delete an existing room."""
    room_id = int(input('Room ID: '))
    db = SessionLocal()
    room = db.query(Room).filter(Room.id == room_id).first()
    if room:
        db.delete(room)
        db.commit()
        print(f"Room ID {room_id} deleted successfully!")
    else:
        print(f"Room ID {room_id} not found.")
    db.close()

def search_client():
    """Search for a client by name."""
    name = input('Client name to search for: ')
    db = SessionLocal()
    clients = db.query(Client).filter(Client.name.ilike(f"%{name}%")).all()
    if clients:
        for client in clients:
            print(f"Client ID: {client.id}, Name: {client.name}, Email: {client.email}")
    else:
        print(f"No clients found with the name '{name}'.")
    db.close()

def cli():
    while True:
        print("\nMenu:")
        print("1. Signup")
        print("2. Login")
        print("3. Add Property")
        print("4. Add Client")
        print("5. Add Room")
        print("6. Add Payment")
        print("7. List Clients")
        print("8. List Properties")
        print("9. List Rooms")
        print("10. Update Property")
        print("11. Update Client")
        print("12. Delete Client")
        print("13. Delete Room")
        print("14. Search Client")
        print("15. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            signup()
        elif choice == 2:
            login()
        elif choice == 3:
            add_property()
        elif choice == 4:
            add_client()
        elif choice == 5:
            add_room()
        elif choice == 6:
            add_payment()
        elif choice == 7:
            list_clients()
        elif choice == 8:
            list_properties()
        elif choice == 9:
            list_rooms()
        elif choice == 10:
            update_property()
        elif choice == 11:
            update_client()
        elif choice == 12:
            delete_client()
        elif choice == 13:
            delete_room()
        elif choice == 14:
            search_client()
        elif choice == 15:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli()
