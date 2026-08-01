from app.enhancement.enhance import enhance_session


class EnhancementService:

    def enhance(self, session_id: str):

        total = enhance_session(session_id)

        return {
            "session_id": session_id,
            "status": "enhanced",
            "enhanced_pages": total,
        }