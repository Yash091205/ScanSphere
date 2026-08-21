import apiClient from "../api/apiClient";

export async function generateDocument(sessionId) {
    const response = await apiClient.post(
        `/session/${sessionId}/document`
    );

    return response.data;
}

export function getDownloadUrl(sessionId) {
    return `${apiClient.defaults.baseURL}/session/${sessionId}/download`;
}