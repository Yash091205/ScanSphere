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