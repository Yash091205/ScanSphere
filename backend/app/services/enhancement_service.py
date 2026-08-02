from app.enhancement.enhance import enhance_session
from app.utils.session_manager import SessionManager

class EnhancementService:

    def enhance(self, session_id: str):

        total = enhance_session(session_id)

        manager = SessionManager(session_id)
        manager.update_status("enhanced")
        


        return {
            "session_id": session_id,
            "status": "enhanced",
            "enhanced_pages": total,
        }