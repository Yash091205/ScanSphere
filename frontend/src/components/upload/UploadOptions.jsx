import UploadCard from "./UploadCard";
import useUploadActions from "../../hooks/useUploadActions";

export default function UploadOptions() {

    const {
        pdfInputRef,
        imageInputRef,

        openPdfPicker,
        openImagePicker,

        handlePdfUpload,
        handleImageUpload,

    } = useUploadActions();

    return (
        <>

            {/* PDF input */}
            <input
                type="file"
                accept=".pdf"
                ref={pdfInputRef}
                className="hidden"
                onChange={handlePdfUpload}
            />

            {/* Image input */}
            <input
                type="file"
                accept=".jpg,.jpeg,.png"
                multiple
                ref={imageInputRef}
                className="hidden"
                onChange={handleImageUpload}
            />

            <div className="grid gap-6">

                {/* PDF */}
                <UploadCard
                    icon="📄"
                    title="Upload PDF"
                    description="Select a PDF document."
                    onClick={openPdfPicker}
                />

                {/* Images */}
                <UploadCard
                    icon="🖼️"
                    title="Upload Images"
                    description="Upload JPG, JPEG or PNG images."
                    onClick={openImagePicker}
                />

                <div className="text-center text-slate-500 font-semibold">
                    OR
                </div>

                {/* Camera - still disabled */}
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