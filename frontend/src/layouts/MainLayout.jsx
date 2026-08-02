import { Link } from "react-router-dom";

export default function MainLayout({ children }) {
  return (
    <div className="min-h-screen bg-slate-100 flex flex-col">

      {/* Header */}
      <header className="bg-white shadow-sm border-b">

        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">

          <h1 className="text-2xl font-bold text-emerald-600">
            📄 ScanSphere
          </h1>

          <nav className="flex gap-6">

            <Link to="/">Home</Link>

            <Link to="/upload">Upload</Link>

            <Link to="/review">Review</Link>

            <Link to="/ocr">OCR</Link>

            <Link to="/download">Download</Link>

          </nav>

        </div>

      </header>

      {/* Main */}

      <main className="flex-1 max-w-7xl w-full mx-auto px-6 py-10">

        {children}

      </main>

      {/* Footer */}

      <footer className="bg-white border-t py-4 text-center text-gray-500">

        © 2026 ScanSphere

      </footer>

    </div>
  );
}