from app.enhancement.enhance import enhance_session

session_id = input("Session ID: ")

count = enhance_session(session_id)

print(f"{count} pages enhanced successfully.")