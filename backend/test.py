from app.utils.session_manager import SessionManager

session_id = input("Session ID: ")

manager = SessionManager(session_id)

print("\nBefore:")
print(manager.list_pages())

manager.reorder_pages([3, 1, 4, 2])

print("\nAfter:")
print(manager.list_pages())