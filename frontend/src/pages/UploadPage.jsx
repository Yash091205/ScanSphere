import MainLayout from "../layouts/MainLayout";
import UploadOptions from "../components/upload/UploadOptions";

export default function UploadPage() {
    return (
        <MainLayout>

            <div className="max-w-3xl mx-auto">

                <h1 className="text-5xl font-bold text-center">
                    Upload Document
                </h1>

                <p className="text-center text-slate-600 mt-4 mb-10">
                    Choose how you want to import your document.
                </p>

                <UploadOptions />

            </div>

        </MainLayout>
    );
}