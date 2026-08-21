import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
    fetchOCRReview,
    saveOCRReview,
} from "../services/ocrService";

import { getSession } from "../utils/session";

export default function useOCRReviewActions() {

    const navigate = useNavigate();

    const [pages, setPages] = useState([]);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [error, setError] = useState(null);
    const [message, setMessage] = useState("");

    useEffect(() => {

        async function loadOCRReview() {

            try {

                const sessionId = getSession();

                if (!sessionId) {
                    throw new Error("No active session found.");
                }

                const data = await fetchOCRReview(sessionId);

                setPages(data.pages || []);

            } catch (error) {

                console.error(error);

                setError(
                    error.response?.data?.detail ||
                    error.message ||
                    "Failed to load OCR results."
                );

            } finally {

                setLoading(false);

            }
        }

        loadOCRReview();

    }, []);

    function handleTextChange(pageId, text) {

        setPages((prev) =>
            prev.map((page) =>
                page.page === pageId
                    ? {
                        ...page,
                        text,
                    }
                    : page
            )
        );

    }

    async function saveReview() {

        try {

            setSaving(true);
            setMessage("");
            setError(null);

            const sessionId = getSession();

            await saveOCRReview(
                sessionId,
                pages,
            );

            setMessage("OCR review saved successfully.");

            navigate("/download");

        } catch (error) {

            console.error(error);

            setError(
                error.response?.data?.detail ||
                "Failed to save OCR review."
            );

        } finally {

            setSaving(false);

        }
    }

    return {
        pages,
        loading,
        saving,
        error,
        message,
        handleTextChange,
        saveReview,
    };
}