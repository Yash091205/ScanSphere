import MainLayout from "../layouts/MainLayout";
import useOCRReviewActions from "../hooks/useOCRReviewActions";

export default function OCRReviewPage() {

    const {
        pages,
        loading,
        saving,
        error,
        message,
        handleTextChange,
        saveReview,
    } = useOCRReviewActions();

    if (loading) {

        return (
            <MainLayout>
                <h2 className="text-xl font-semibold">
                    Loading OCR results...
                </h2>
            </MainLayout>
        );

    }

    if (error) {

        return (
            <MainLayout>
                <h2 className="text-xl font-semibold text-red-600">
                    {error}
                </h2>
            </MainLayout>
        );

    }

    return (

        <MainLayout>

            <div className="flex items-center justify-between mb-8">

                <h1 className="text-4xl font-bold">
                    OCR Review
                </h1>

                <button
                    onClick={saveReview}
                    disabled={saving}
                    className="
                        bg-indigo-600
                        hover:bg-indigo-700
                        disabled:opacity-50
                        text-white
                        px-6
                        py-3
                        rounded-xl
                        font-semibold
                    "
                >
                    {saving ? "Saving..." : "Save Review"}
                </button>

            </div>

            {message && (
                <div className="
                    mb-6
                    p-4
                    rounded-xl
                    bg-green-100
                    text-green-700
                ">
                    {message}
                </div>
            )}

            <div className="space-y-8">

                {pages.map((page, index) => (

                    <div
                        key={page.page}
                        className="
                            bg-white
                            rounded-2xl
                            shadow-md
                            p-6
                        "
                    >

                        <h2 className="text-xl font-bold mb-4">
                            Page {index + 1}
                        </h2>

                        <textarea
                            value={page.text}
                            onChange={(event) =>
                                handleTextChange(
                                    page.page,
                                    event.target.value
                                )
                            }
                            className="
                                w-full
                                min-h-[250px]
                                border
                                border-slate-300
                                rounded-xl
                                p-4
                                resize-y
                                focus:outline-none
                                focus:ring-2
                                focus:ring-indigo-500
                            "
                            placeholder="OCR text..."
                        />

                    </div>

                ))}

            </div>

            {pages.length === 0 && (
                <div className="
                    text-center
                    text-slate-500
                    py-12
                ">
                    No OCR results found.
                </div>
            )}

        </MainLayout>

    );
}