# ScanSphere

> **AI-Powered Document Scanning, Enhancement & OCR Platform**

ScanSphere is a full-stack document digitization application that converts scanned images and PDF documents into clean, editable digital documents.

It provides a complete workflow for uploading documents, previewing pages, enhancing document images, extracting text using OCR, reviewing the processed pages, managing pages, and generating downloadable digital documents.

The application is designed with a temporary-session architecture: uploaded documents and generated files are retained only for a limited period and are automatically removed after **15 minutes**.

---

## ✨ Features

### 📤 Document Upload

* Upload individual images.
* Upload multi-page PDF documents.
* Support multiple pages in a single session.
* Automatic PDF page extraction.
* File and page validation.
* Session-based temporary storage.

### 👁️ Page Preview

* Preview uploaded pages before processing.
* View individual document pages.
* Maintain page order.
* Delete unwanted pages.
* Replace individual pages.
* Refresh previews after page replacement.

### 🖼️ Image Enhancement

ScanSphere processes document images through an enhancement pipeline designed to improve OCR quality.

The enhancement pipeline can include:

* Grayscale conversion
* Noise reduction
* Contrast improvement
* Thresholding
* Document cleanup
* Black-and-white conversion
* Other preprocessing operations required by the OCR pipeline

### 🔍 OCR

ScanSphere converts document images into machine-readable text using OCR processing.

The OCR pipeline is designed primarily for **printed documents**.

The extracted text can then be used to generate editable digital documents.

> Handwritten OCR is intentionally not part of the current version.

### 📄 Document Generation

Processed documents can be exported into digital formats including:

* DOCX
* PDF

Generated files remain temporarily available so that the user can download and inspect them before the session expires.

### 🗂️ Page Management

Users can manage pages during the scanning workflow:

* Reorder pages
* Delete pages
* Replace pages
* Preview pages
* Process selected pages
* Review enhanced pages

### ⏱️ Temporary Session Storage

ScanSphere does not permanently store user documents.

Each processing session receives a unique session directory.

```text
temp/
└── session_<UUID>/
    ├── input/
    ├── pages/
    ├── enhanced/
    ├── ocr/
    ├── output/
    └── metadata.json
```

The complete session is automatically deleted after **15 minutes**.

This includes:

* Original uploaded files
* Extracted PDF pages
* Enhanced images
* OCR results
* Generated DOCX files
* Generated PDF files
* Session metadata

---

# 🏗️ Architecture

ScanSphere follows a full-stack client-server architecture.

```text
                    ┌──────────────────────┐
                    │        User          │
                    │      Web Browser     │
                    └──────────┬───────────┘
                               │
                               │ HTTP
                               ▼
                    ┌──────────────────────┐
                    │   React Frontend     │
                    │        + Vite        │
                    └──────────┬───────────┘
                               │
                               │ REST API
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
       ┌───────────┐    ┌─────────────┐    ┌───────────┐
       │    PDF    │    │ Enhancement │    │    OCR    │
       │ Processing│    │   Pipeline  │    │  Pipeline │
       └───────────┘    └─────────────┘    └───────────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Temporary Session    │
                    │      Storage         │
                    └──────────┬───────────┘
                               │
                         15 Minute TTL
                               │
                               ▼
                         Automatic Cleanup
```

---

# 🛠️ Technology Stack

## Frontend

* React
* Vite
* JavaScript
* HTML5
* CSS3

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

## Document Processing

* PDF processing
* Image processing
* OpenCV-based enhancement pipeline

## OCR

* Tesseract OCR / configured OCR engine
* OCR preprocessing pipeline

## Document Generation

* DOCX generation
* PDF generation

## Development Tools

* Git
* GitHub
* VS Code
* Python Virtual Environment
* Node.js
* npm

---

# 📁 Project Structure

```text
ScanSphere/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── ...
│   │   │
│   │   ├── core/
│   │   │   └── ...
│   │   │
│   │   ├── enhancement/
│   │   │   └── ...
│   │   │
│   │   ├── ocr/
│   │   │   └── ...
│   │   │
│   │   ├── pdf/
│   │   │   └── ...
│   │   │
│   │   ├── document/
│   │   │   └── ...
│   │   │
│   │   └── utils/
│   │       └── ...
│   │
│   ├── temp/
│   │   └── uploads/
│   │
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── enhancement/
│   │   │   └── ...
│   │   │
│   │   ├── hooks/
│   │   │   ├── useEnhancementReviewActions.js
│   │   │   └── ...
│   │   │
│   │   ├── pages/
│   │   ├── services/
│   │   └── ...
│   │
│   ├── package.json
│   └── ...
│
├── .gitignore
├── README.md
└── ...
```

---

# 🔄 Application Workflow

The complete ScanSphere workflow is:

```text
1. Upload Document
        ↓
2. Create Processing Session
        ↓
3. Validate Upload
        ↓
4. Convert PDF to Individual Pages
        ↓
5. Generate Page Previews
        ↓
6. Manage Pages
   ├── Reorder
   ├── Delete
   └── Replace
        ↓
7. Enhance Document Images
        ↓
8. Review Enhanced Pages
        ↓
9. OCR Processing
        ↓
10. Generate Digital Document
        ↓
11. Download DOCX / PDF
        ↓
12. Session Remains Available
        ↓
13. Automatic Cleanup After 15 Minutes
```

---

# 🔐 Temporary Storage & Privacy

ScanSphere follows a temporary-processing model.

No permanent document storage is required.

When a document is uploaded, ScanSphere creates a unique session:

```text
session_<UUID>
```

All files belonging to that session are stored inside the session directory.

For example:

```text
temp/
└── session_8d2f.../
    ├── input/
    ├── pages/
    ├── enhanced/
    ├── ocr/
    └── output/
```

The complete directory is automatically removed after the session reaches its 15-minute lifetime.

### Why 15 minutes?

The user may need to:

* Download the generated DOCX.
* Open and inspect the document.
* Identify an OCR or formatting issue.
* Re-download the document.
* Review enhanced images.
* Access generated output again.

Keeping the complete session temporarily makes this workflow possible without permanent storage.

---

# ⏳ Session Lifecycle

```text
                 Upload
                   │
                   ▼
          Create Session UUID
                   │
                   ▼
          Store Processing Data
                   │
                   ▼
          Enhancement + OCR
                   │
                   ▼
          Generate DOCX / PDF
                   │
                   ▼
        User Reviews / Downloads
                   │
                   ▼
            15 Minute Limit
                   │
                   ▼
          Delete Session Folder
                   │
                   ▼
              Data Removed
```

---

# 🚀 Running the Project Locally

## Prerequisites

Make sure the following are installed:

* Python 3.11+
* Node.js
* npm
* Git
* Tesseract OCR
* Required Python dependencies
* Required frontend dependencies

---

## 1. Clone the Repository

```bash
git clone https://github.com/Yash091205/ScanSphere.git
cd ScanSphere
```

---

# 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

API base path:

```text
/api/v1
```

---

# ⚛️ Frontend Setup

Open another terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# 🔌 API

The backend exposes REST APIs under:

```text
/api/v1
```

The API is responsible for:

* Health checking
* File uploads
* Session management
* PDF processing
* Page management
* Image enhancement
* OCR processing
* Document generation
* Temporary file handling

FastAPI also provides interactive API documentation.

After starting the backend, open:

```text
http://127.0.0.1:8000/docs
```

to inspect and test the available API endpoints.

---

# 📄 Supported Input

ScanSphere is designed to process:

### Images

Common image formats such as:

```text
JPG
JPEG
PNG
```

### PDF

Multi-page PDF documents can be uploaded and converted into individual page images for processing.

---

# 📤 Output

The application can generate:

```text
DOCX
PDF
```

The generated documents are temporarily stored within the active processing session.

---

# ⚙️ Processing Pipeline

## 1. Upload

The frontend sends the selected document to the FastAPI backend.

The backend validates the file and creates a unique session.

## 2. PDF Conversion

For PDF input, individual pages are extracted and stored as page images.

```text
document.pdf
      ↓
page_1.png
page_2.png
page_3.png
...
```

## 3. Enhancement

Each page is processed through the image enhancement pipeline.

The objective is to produce a cleaner image suitable for OCR and document viewing.

## 4. OCR

The enhanced document images are passed through the OCR pipeline.

The extracted text is structured for subsequent document generation.

## 5. Document Generation

OCR results and processed pages are used to generate the requested digital output.

## 6. Temporary Cleanup

Once the session reaches 15 minutes, all session data is removed.

---

# 🎯 Design Goals

ScanSphere was designed around the following principles:

### Simplicity

The system avoids unnecessary infrastructure and services.

### Temporary Processing

Documents are processed without requiring permanent document storage.

### Modular Architecture

PDF processing, enhancement, OCR, and document generation are separated into dedicated modules.

### User Control

Users can preview and manage pages before generating the final document.

### Extensibility

The architecture allows future OCR engines, enhancement algorithms, and document formats to be added without rebuilding the entire application.

---

# 🔮 Future Improvements

Possible future versions can include:

* Handwritten document OCR
* Additional OCR engines
* OCR confidence visualization
* Editable OCR text
* Side-by-side original/enhanced comparison
* Better document layout preservation
* Table detection
* Automatic document orientation correction
* Automatic page border detection
* Multi-language OCR
* More export formats
* Advanced document classification
* Background processing for large documents
* Progress tracking
* Improved document formatting
* User accounts and permanent storage as an optional feature

---

# ⚠️ Current Scope

The current version focuses on **printed document digitization**.

Handwritten OCR is intentionally outside the current scope.

The application is primarily designed for personal use, demonstration, and academic/project purposes rather than high-volume production workloads.

---

# 🧪 Project Status

```text
████████████████████████████████████████ 100%
```

**Status: Completed and Working**

The implemented system includes:

* [x] React frontend
* [x] FastAPI backend
* [x] File upload
* [x] PDF processing
* [x] Multi-page document handling
* [x] Page preview
* [x] Page reordering
* [x] Page deletion
* [x] Page replacement
* [x] Image enhancement
* [x] OCR processing
* [x] Document generation
* [x] Temporary session storage
* [x] 15-minute automatic data lifecycle
* [x] DOCX/PDF output
* [x] REST API architecture
* [x] Git/GitHub integration
* [x] Local development environment
* [x] Deployment-ready architecture

---

# 🌐 Deployment

ScanSphere can be deployed using a cloud application hosting platform such as Render.

A deployed architecture can run the backend processing remotely:

```text
User Browser
     │
     │ Internet
     ▼
Cloud Hosted Frontend
     │
     ▼
Cloud Hosted FastAPI Backend
     │
     ├── PDF Processing
     ├── Image Enhancement
     ├── OCR
     ├── DOCX/PDF Generation
     └── Temporary Storage
              │
              ▼
        15 Minute Cleanup
```

This means the user's computer does not need to run the Python backend or OCR engine after the application has been deployed.

---

# 💻 Local vs Cloud Processing

## Local Development

```text
Your Computer
├── React
├── FastAPI
├── OCR
├── Enhancement
└── Temporary Storage
```

## Deployed Version

```text
Your Browser
      │
      ▼
Cloud Server
├── FastAPI
├── OCR
├── Enhancement
├── PDF Processing
├── Document Generation
└── Temporary Storage
```

The processing workload is therefore handled by the backend server.

---

# 📌 Key Technical Decisions

| Decision               | Choice                         |
| ---------------------- | ------------------------------ |
| Frontend               | React + Vite                   |
| Backend                | FastAPI                        |
| Backend Server         | Uvicorn                        |
| Language               | Python                         |
| Frontend Language      | JavaScript                     |
| Image Processing       | OpenCV-based pipeline          |
| OCR                    | OCR engine integration         |
| PDF Processing         | Backend PDF pipeline           |
| Output                 | DOCX / PDF                     |
| Storage                | Temporary filesystem           |
| Session Lifetime       | 15 minutes                     |
| Permanent File Storage | No                             |
| Database               | Not required                   |
| Authentication         | Not required for current scope |
| Deployment Model       | Cloud-ready                    |
| Primary Use            | Personal / Academic Project    |

---

# 🧹 Data Cleanup Policy

ScanSphere follows a strict temporary-storage model.

Every processing session is associated with a unique directory and lifetime.

After 15 minutes, the session directory is removed.

```text
Session Created
      │
      ├── Original Files
      ├── Page Images
      ├── Enhanced Images
      ├── OCR Data
      └── Generated Documents
                │
                ▼
          15 Minutes
                │
                ▼
        Automatic Deletion
```

This prevents temporary files from accumulating indefinitely.

---

# 🛡️ Error Handling

The application is designed to handle common document-processing problems such as:

* Invalid file types
* Unsupported files
* Corrupted documents
* Invalid PDF files
* Processing failures
* Missing pages
* OCR failures
* Invalid session requests
* Missing temporary files

The frontend communicates processing states and errors to the user instead of silently failing.

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

* Full-stack web development
* React application development
* REST API design
* FastAPI backend development
* File upload handling
* PDF processing
* Image processing
* OCR integration
* Document generation
* Temporary storage management
* Session-based architecture
* Frontend/backend communication
* Git and GitHub workflow
* Cloud deployment architecture

---

# 👨‍💻 Author

**Yash Shirsath**

Artificial Intelligence & Data Science Engineering

---

# 📜 License

This project is intended primarily for educational, academic, and personal use.

If you plan to reuse, modify, or distribute the project, please review and add an appropriate license before doing so.

---

# ⭐ ScanSphere

**Scan. Enhance. Recognize. Digitize.**

A complete document digitization workflow built from the ground up using modern full-stack technologies.
