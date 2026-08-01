class ScanSphereException(Exception):
    """
    Base exception for the ScanSphere application.
    """
    pass


class UploadException(ScanSphereException):
    """Raised when upload validation fails."""
    pass


class EnhancementException(ScanSphereException):
    """Raised when image enhancement fails."""
    pass


class OCRException(ScanSphereException):
    """Raised when OCR processing fails."""
    pass


class DocumentException(ScanSphereException):
    """Raised when DOCX generation fails."""
    pass