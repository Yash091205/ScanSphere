const BASE_URL = "http://127.0.0.1:8000";

export default function EnhancementCard({
    page,
    selectedVersion,
    onSelectionChange,
}) {

    return (

        <div className="bg-white rounded-2xl shadow-md p-6">

            <h2 className="text-xl font-semibold mb-5">
                Page {page.page_number}
            </h2>

            <div className="grid md:grid-cols-2 gap-6">

                <div>

                    <h3 className="font-medium mb-3 text-center">
                        Original
                    </h3>

                    <img
                        src={`${BASE_URL}${page.preview_url}`}
                        alt="Original"
                        className="rounded-xl border"
                    />

                </div>

                <div>

                    <h3 className="font-medium mb-3 text-center">
                        Enhanced
                    </h3>

                    <img
                        src={`${BASE_URL}${page.enhanced_preview_url}`}
                        alt="Enhanced"
                        className="rounded-xl border"
                    />

                </div>

            </div>

            <div className="flex gap-8 mt-6 justify-center">

                <label className="flex items-center gap-2 cursor-pointer">

                    <input
                        type="radio"
                        name={page.page_id}
                        value="original"
                        checked={selectedVersion === "original"}
                        onChange={() =>
                            onSelectionChange(
                                page.page_id,
                                "original"
                            )
                        }
                    />

                    Keep Original

                </label>

                <label className="flex items-center gap-2 cursor-pointer">

                    <input
                        type="radio"
                        name={page.page_id}
                        value="enhanced"
                        checked={selectedVersion === "enhanced"}
                        onChange={() =>
                            onSelectionChange(
                                page.page_id,
                                "enhanced"
                            )
                        }
                    />

                    Keep Enhanced

                </label>

            </div>

        </div>

    );

}