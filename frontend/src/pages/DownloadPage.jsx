import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import {
    generateDocument,
    getDownloadUrl,
} from "../services/documentService";
import { getSession } from "../utils/session";

export default function DownloadPage() {

    const [loading, setLoading] = useState(false);
    const [generated, setGenerated] = useState(false);
    const [error, setError] = useState("");

    async function handleGenerate() {

        try {

            setLoading(true);
            setError("");

            const sessionId = getSession();

            if (!sessionId) {
                throw new Error("No active session found.");
            }

            await generateDocument(sessionId);

            setGenerated(true);

        } catch (error) {

            console.error(error);

            setError(
                error.response?.data?.detail ||
                error.message ||
                "Failed to generate document."
            );

        } finally {

            setLoading(false);

        }
    }

    function handleDownload() {

        const sessionId = getSession();

        if (!sessionId) {
            setError("No active session found.");
            return;
        }

        window.open(
            getDownloadUrl(sessionId),
            "_blank"
        );
    }

    return (

        <MainLayout>

            <div className="max-w-3xl mx-auto">

                <h1 className="text-4xl font-bold mb-8">
                    Document Export
                </h1>

                {!generated && (

                    <div className="
                        bg-white
                        rounded-2xl
                        shadow-md
                        p-8
                        text-center
                    ">

                        <h2 className="text-2xl font-bold mb-3">
                            Your document is ready to generate
                        </h2>

                        <p className="text-slate-600 mb-8">
                            Generate a DOCX document using your reviewed OCR text.
                        </p>

                        <button
                            onClick={handleGenerate}
                            disabled={loading}
                            className="
                                bg-indigo-600
                                hover:bg-indigo-700
                                disabled:opacity-50
                                text-white
                                px-8
                                py-3
                                rounded-xl
                                font-semibold
                            "
                        >
                            {loading
                                ? "Generating..."
                                : "Generate Document"
                            }
                        </button>

                    </div>

                )}

                {generated && (

                    <div className="
                        bg-white
                        rounded-2xl
                        shadow-md
                        p-8
                        text-center
                    ">

                        <div className="text-5xl mb-4">
                            📄
                        </div>

                        <h2 className="text-2xl font-bold mb-3">
                            Document Generated
                        </h2>

                        <p className="text-slate-600 mb-8">
                            Your reviewed OCR text has been converted into a DOCX document.
                        </p>

                        <button
                            onClick={handleDownload}
                            className="
                                bg-emerald-600
                                hover:bg-emerald-700
                                text-white
                                px-8
                                py-3
                                rounded-xl
                                font-semibold
                            "
                        >
                            Download DOCX
                        </button>

                    </div>

                )}

                {error && (

                    <div className="
                        mt-6
                        p-4
                        rounded-xl
                        bg-red-100
                        text-red-700
                    ">
                        {error}
                    </div>

                )}

            </div>

        </MainLayout>

    );
}