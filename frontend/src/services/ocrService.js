import apiClient from "../api/apiClient";

export async function processOCR(sessionId, pages) {

    const response = await apiClient.post(
        `/session/${sessionId}/ocr`,
        {
            pages,
        }
    );

    return response.data;
}

export async function fetchOCRReview(sessionId) {

    const response = await apiClient.get(
        `/session/${sessionId}/ocrfetch`
    );

    return response.data;
}

export async function saveOCRReview(sessionId, pages) {

    const response = await apiClient.put(
        `/session/${sessionId}/ocrreview`,
        {
            pages,
        }
    );

    return response.data;
}