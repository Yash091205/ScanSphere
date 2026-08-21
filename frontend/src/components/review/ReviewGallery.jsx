import React, { useRef } from "react";

const BASE_URL = "http://127.0.0.1:8000";

export default function ReviewGallery({
    session,
    onDelete,
    onReplace,
    onAppend,
    onMove,
    onProceed,
    actionLoading,
}) {
    const appendInputRef = useRef(null);
    const replaceInputRefs = useRef({});

    if (!session || !session.pages) {
        return (
            <div className="text-center py-12 text-slate-500">
                No session data available.
            </div>
        );
    }

    const pages = session.pages;

    const handleAppendChange = (e) => {
        if (e.target.files && e.target.files.length > 0) {
            onAppend(e.target.files);
            e.target.value = "";
        }
    };

    const handleReplaceChange = (pageId, e) => {
        if (e.target.files && e.target.files[0]) {
            onReplace(pageId, e.target.files[0]);
            e.target.value = "";
        }
    };

    return (
        <div className="space-y-6">
            {/* Header Control Banner */}
            <div className="bg-white rounded-2xl shadow-sm border border-slate-100 p-6 flex flex-wrap items-center justify-between gap-4">
                <div className="flex items-center gap-3 flex-wrap">
                    <span className="px-3 py-1 bg-indigo-50 text-indigo-700 font-semibold rounded-full text-sm">
                        Session: {session.session_id}
                    </span>
                    <span className="px-3 py-1 bg-emerald-50 text-emerald-700 font-medium rounded-full text-sm uppercase">
                        Type: {session.document_type || "Images"}
                    </span>
                    <span className="px-3 py-1 bg-slate-100 text-slate-700 font-medium rounded-full text-sm">
                        Total Pages: {pages.length}
                    </span>
                </div>

                <div className="flex items-center gap-3">
                    {/* Hidden input for append */}
                    <input
                        type="file"
                        ref={appendInputRef}
                        onChange={handleAppendChange}
                        multiple
                        accept="image/png, image/jpeg, image/webp"
                        className="hidden"
                    />
                    <button
                        onClick={() => appendInputRef.current?.click()}
                        disabled={actionLoading}
                        className="px-4 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-800 font-medium rounded-xl transition flex items-center gap-2 text-sm disabled:opacity-50 cursor-pointer"
                    >
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 4v16m8-8H4" />
                        </svg>
                        Add Pages
                    </button>

                    <button
                        onClick={onProceed}
                        disabled={actionLoading || pages.length === 0}
                        className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl transition shadow-md shadow-indigo-200 flex items-center gap-2 text-sm disabled:opacity-50 cursor-pointer"
                    >
                        {actionLoading ? "Processing..." : "Proceed to Enhancement →"}
                    </button>
                </div>
            </div>

            {/* Gallery Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {pages.map((page, index) => {
                    const pageId = page.page_id || page.id;
                    return (
                        <div
                            key={pageId}
                            className="bg-white rounded-2xl border border-slate-200/80 shadow-sm hover:shadow-md transition overflow-hidden flex flex-col justify-between group"
                        >
                            {/* Card Top / Preview Header */}
                            <div className="p-4 space-y-3">
                                <div className="flex items-center justify-between">
                                    <span className="font-bold text-slate-800 text-base">
                                        Page {page.page_number}
                                    </span>
                                    <span className="text-xs text-slate-400 truncate max-w-[150px]">
                                        {page.original_name}
                                    </span>
                                </div>

                                <div className="relative aspect-[3/4] bg-slate-50 rounded-xl overflow-hidden border border-slate-100 flex items-center justify-center">
                                    <img
                                        src={`${BASE_URL}${page.preview_url}`}
                                        alt={page.original_name}
                                        className="w-full h-full object-contain p-2"
                                    />
                                </div>
                            </div>

                            {/* Card Actions Footer */}
                            <div className="p-4 bg-slate-50/50 border-t border-slate-100 flex items-center justify-between gap-2">
                                {/* Move Left / Right */}
                                <div className="flex items-center gap-1">
                                    <button
                                        onClick={() => onMove(pageId, "left")}
                                        disabled={index === 0 || actionLoading}
                                        title="Move Left"
                                        className="p-2 text-slate-600 hover:bg-slate-200/70 rounded-lg disabled:opacity-30 disabled:hover:bg-transparent transition cursor-pointer"
                                    >
                                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7" />
                                        </svg>
                                    </button>

                                    <button
                                        onClick={() => onMove(pageId, "right")}
                                        disabled={index === pages.length - 1 || actionLoading}
                                        title="Move Right"
                                        className="p-2 text-slate-600 hover:bg-slate-200/70 rounded-lg disabled:opacity-30 disabled:hover:bg-transparent transition cursor-pointer"
                                    >
                                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </button>
                                </div>

                                {/* Replace Button */}
                                <div>
                                    <input
                                        type="file"
                                        ref={(el) => (replaceInputRefs.current[pageId] = el)}
                                        onChange={(e) => handleReplaceChange(pageId, e)}
                                        accept="image/png, image/jpeg, image/webp"
                                        className="hidden"
                                    />
                                    <button
                                        onClick={() => replaceInputRefs.current[pageId]?.click()}
                                        disabled={actionLoading}
                                        title="Replace Page"
                                        className="px-3 py-1.5 bg-amber-50 hover:bg-amber-100 text-amber-700 text-xs font-semibold rounded-lg transition border border-amber-200/60 flex items-center gap-1 cursor-pointer disabled:opacity-50"
                                    >
                                        <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                                        </svg>
                                        Replace
                                    </button>
                                </div>

                                {/* Delete Button */}
                                <button
                                    onClick={() => onDelete(pageId)}
                                    disabled={actionLoading}
                                    title="Delete Page"
                                    className="p-2 text-rose-600 hover:bg-rose-50 rounded-lg transition cursor-pointer disabled:opacity-50"
                                >
                                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    );
                })}

                {/* Append Card Slot */}
                <div
                    onClick={() => appendInputRef.current?.click()}
                    className="border-2 border-dashed border-slate-200 hover:border-indigo-400 bg-slate-50/50 hover:bg-indigo-50/30 rounded-2xl min-h-[280px] flex flex-col items-center justify-center p-6 transition cursor-pointer group text-slate-400 hover:text-indigo-600"
                >
                    <div className="p-3 bg-white group-hover:bg-indigo-100 rounded-full shadow-sm transition mb-3">
                        <svg className="w-6 h-6 text-slate-500 group-hover:text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 4v16m8-8H4" />
                        </svg>
                    </div>
                    <span className="font-semibold text-sm">Append More Pages</span>
                    <span className="text-xs text-slate-400 mt-1">PNG, JPG, WEBP</span>
                </div>
            </div>
        </div>
    );
}