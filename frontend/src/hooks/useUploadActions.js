import { useRef } from "react";
import { useNavigate } from "react-router-dom";

import {
    uploadPdf,
    uploadImages,
} from "../services/uploadService";

import { saveSession } from "../utils/session";

export default function useUploadActions() {

    const navigate = useNavigate();

    const pdfInputRef = useRef(null);
    const imageInputRef = useRef(null);
    const cameraInputRef = useRef(null);

    // Open PDF picker
    const openPdfPicker = () => {
        pdfInputRef.current?.click();
    };

    // Open image picker
    const openImagePicker = () => {
        imageInputRef.current?.click();
    };

    // Handle PDF upload
    const handlePdfUpload = async (event) => {

        const file = event.target.files[0];

        if (!file) return;

        try {

            const response = await uploadPdf(file);

            saveSession(response.session_id);

            navigate("/review");

        } catch (error) {

            console.error(error);

        }

    };

    // Handle image upload
    const handleImageUpload = async (event) => {

        const files = Array.from(event.target.files);

        if (files.length === 0) return;

        try {

            const response = await uploadImages(files);

            saveSession(response.session_id);

            navigate("/review");

        } catch (error) {

            console.error(error);

        }

    };

    return {

        pdfInputRef,
        imageInputRef,
        cameraInputRef,

        openPdfPicker,
        openImagePicker,

        handlePdfUpload,
        handleImageUpload,

    };

}