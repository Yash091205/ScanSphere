import { useState } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";
import useEnhancementReviewActions from "../hooks/useEnhancementReviewActions";
import EnhancementGallery from "../components/enhancement/EnhancementGallery";

import { processOCR } from "../services/ocrService";
import { getSession as getStoredSession } from "../utils/session";

export default function EnhancementReviewPage() {

    const {
        loading,
        session,
        error,
    } = useEnhancementReviewActions();

    const navigate = useNavigate();

    const [selectedVersions, setSelectedVersions] = useState({});

    // Change Original / Enhanced selection
    function handleSelectionChange(pageId, version) {

        setSelectedVersions((prev) => ({
            ...prev,
            [pageId]: version,
        }));

    }

    // Continue to OCR
    async function handleContinueToOCR() {

        try {

            const sessionId = getStoredSession();

            const pages = session.pages.map((page) => ({
                page_id: page.page_id,
                source: selectedVersions[page.page_id] || "enhanced",
            }));

            await processOCR(
                sessionId,
                pages,
            );

            navigate("/ocr");

        } catch (error) {

            console.error(error);

            alert(
                error.response?.data?.detail ||
                "Failed to process OCR."
            );

        }

    }

    if (loading) {

        return (
            <MainLayout>

                <div className="flex items-center justify-center min-h-[400px]">

                    <div className="flex flex-col items-center gap-3">

                        <div className="
                            w-10
                            h-10
                            border-4
                            border-indigo-600
                            border-t-transparent
                            rounded-full
                            animate-spin
                        "></div>

                        <p className="text-slate-500 font-medium">
                            Loading enhancement review...
                        </p>

                    </div>

                </div>

            </MainLayout>
        );

    }

    if (error) {

        return (
            <MainLayout>

                <div className="max-w-md mx-auto text-center py-12">

                    <div className="
                        p-4
                        bg-rose-50
                        text-rose-700
                        rounded-2xl
                        border
                        border-rose-200
                    ">
                        {error}
                    </div>

                </div>

            </MainLayout>
        );

    }

    if (!session || !session.pages) {

        return (
            <MainLayout>

                <div className="text-center py-12">

                    <p className="text-slate-500">
                        No pages available for enhancement review.
                    </p>

                </div>

            </MainLayout>
        );

    }

    return (

        <MainLayout>

            <div className="max-w-6xl mx-auto space-y-8">

                <div>

                    <h1 className="
                        text-4xl
                        font-extrabold
                        text-slate-900
                        tracking-tight
                    ">
                        Enhancement Review
                    </h1>

                    <p className="text-slate-500 mt-2">
                        Choose the original or enhanced version of each page
                        before sending the document for OCR.
                    </p>

                </div>

                <EnhancementGallery
                    pages={session.pages}
                    selectedVersions={selectedVersions}
                    onSelectionChange={handleSelectionChange}
                />

                <div className="flex justify-end pt-4">

                    <button
                        onClick={handleContinueToOCR}
                        className="
                            bg-indigo-600
                            hover:bg-indigo-700
                            text-white
                            px-8
                            py-3
                            rounded-xl
                            font-semibold
                            transition
                        "
                    >
                        Continue to OCR →
                    </button>

                </div>

            </div>

        </MainLayout>

    );

}