import MainLayout from "../layouts/MainLayout";
import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <MainLayout>

      <section className="text-center py-20">

        <h1 className="text-6xl font-extrabold text-slate-900">
          ScanSphere
        </h1>

        <p className="mt-6 text-xl text-slate-600 max-w-3xl mx-auto">
          Convert scanned PDFs and images into editable Microsoft Word
          documents using document detection, image enhancement and OCR.
        </p>

        <div className="mt-10 flex justify-center gap-4">

          <Link
            to="/upload"
            className="bg-emerald-600 hover:bg-emerald-700 text-white px-8 py-4 rounded-xl font-semibold transition"
          >
            Upload Document
          </Link>

          <a
            href="#features"
            className="border border-slate-300 hover:bg-slate-100 px-8 py-4 rounded-xl font-semibold transition"
          >
            Learn More
          </a>

        </div>

      </section>

      <section
        id="features"
        className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 pb-20"
      >

        <Feature
          title="Document Scanner"
          text="Automatically detects document boundaries and corrects perspective."
        />

        <Feature
          title="Image Enhancement"
          text="Improves readability using denoising, sharpening and adaptive thresholding."
        />

        <Feature
          title="OCR"
          text="Extracts editable text from English, Hindi and Marathi documents."
        />

        <Feature
          title="DOCX Export"
          text="Generate editable Microsoft Word documents with reviewed OCR text."
        />

      </section>

    </MainLayout>
  );
}

function Feature({ title, text }) {
  return (
    <div className="bg-white rounded-2xl shadow-md p-6">

      <h2 className="text-xl font-bold mb-3">
        {title}
      </h2>

      <p className="text-slate-600">
        {text}
      </p>

    </div>
  );
}