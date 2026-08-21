from app.enhancement.enhance import enhance_session
from app.utils.session_manager import SessionManager

class EnhancementService:

    def enhance(self, session_id: str):

        total = enhance_session(session_id)

        manager = SessionManager(session_id)
        manager.update_status("enhanced")
        

        metadata = manager.read_metadata()

        pages = manager.list_pages()

        return {
            "session_id": session_id,
            "status": metadata["status"],
            "document_type": metadata["document_type"],
            "original_file": metadata["original_file"],
            "total_pages": metadata["total_pages"],
            "pages": pages,
        }