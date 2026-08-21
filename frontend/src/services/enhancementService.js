import apiClient from "../api/apiClient";

export async function enhanceSession(sessionId) {
    const response = await apiClient.post(
        `/session/${sessionId}/enhance`
    );
    return response.data;
}
