import MainLayout from "../layouts/MainLayout";
import ReviewGallery from "../components/review/ReviewGallery";
import useReviewActions from "../hooks/useReviewActions";

export default function ReviewPage() {
    const {
        loading,
        actionLoading,
        session,
        error,
        handleDelete,
        handleReplace,
        handleAppend,
        handleMove,
        handleProceed,
    } = useReviewActions();

    if (loading) {
        return (
            <MainLayout>
                <div className="flex items-center justify-center min-h-[400px]">
                    <div className="flex flex-col items-center gap-3">
                        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin"></div>
                        <p className="text-slate-500 font-medium">Loading session pages...</p>
                    </div>
                </div>
            </MainLayout>
        );
    }

    if (error) {
        return (
            <MainLayout>
                <div className="max-w-md mx-auto text-center py-12 space-y-4">
                    <div className="p-4 bg-rose-50 text-rose-700 rounded-2xl border border-rose-200">
                        {error}
                    </div>
                    <a href="/upload" className="inline-block px-6 py-2.5 bg-indigo-600 text-white rounded-xl font-medium">
                        Go to Upload
                    </a>
                </div>
            </MainLayout>
        );
    }

    return (
        <MainLayout>
            <div className="max-w-6xl mx-auto space-y-8">
                <div>
                    <h1 className="text-4xl font-extrabold text-slate-900 tracking-tight">
                        Review & Manage Pages
                    </h1>
                    <p className="text-slate-500 mt-2">
                        Inspect, replace, reorder, or add pages before processing image enhancements and OCR text extraction.
                    </p>
                </div>

                <ReviewGallery
                    session={session}
                    onDelete={handleDelete}
                    onReplace={handleReplace}
                    onAppend={handleAppend}
                    onMove={handleMove}
                    onProceed={handleProceed}
                    actionLoading={actionLoading}
                />
            </div>
        </MainLayout>
    );
}