import { useRef } from "react";
import { useNavigate } from "react-router-dom";

import { uploadPdf } from "../services/uploadService";
import { saveSession } from "../utils/session";

export default function useUploadActions() {

    const navigate = useNavigate();

    const pdfInputRef = useRef(null);

    const imageInputRef = useRef(null);

    const cameraInputRef = useRef(null);

    const openPdfPicker = () => {
        pdfInputRef.current.click();
    };

    const handlePdfUpload = async (event) => {

        const file = event.target.files[0];

        if (!file) return;

        try {

            const response = await uploadPdf(file);

            console.log("Response:", response);

            saveSession(response.session_id);

            console.log("Saved Session:", response.session_id);

            navigate("/review");

        }catch (error) {

            console.error(error);

        }

    };

    return {

        pdfInputRef,
        imageInputRef,
        cameraInputRef,

        openPdfPicker,

        handlePdfUpload,

    };

}