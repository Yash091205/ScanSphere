import UploadCard from "./UploadCard";
import useUploadActions from "../../hooks/useUploadActions";

export default function UploadOptions() {

    const {

        pdfInputRef,

        openPdfPicker,

        handlePdfUpload,

    } = useUploadActions();

    return (
        <>

            <input
                type="file"
                accept=".pdf"
                ref={pdfInputRef}
                className="hidden"
                onChange={handlePdfUpload}
            />

            <div className="grid gap-6">

                <UploadCard
                    icon="📄"
                    title="Upload PDF"
                    description="Select a PDF document."
                    onClick={openPdfPicker}
                />

                <UploadCard
                    icon="🖼️"
                    title="Upload Images"
                    description="Upload JPG, JPEG or PNG images."
                    onClick={() => {}}
                />

                <div className="text-center text-slate-500 font-semibold">
                    OR
                </div>

                <UploadCard
                    icon="📷"
                    title="Capture from Camera"
                    description="Capture a document using your camera."
                    onClick={() => {}}
                />

            </div>

        </>
    );
}