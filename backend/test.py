from app.utils.session_manager import SessionManager

session = input("Session ID: ")


manager = SessionManager(session)

manager.update_total_pages()
print(" successfully.")