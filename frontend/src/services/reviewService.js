import apiClient from "../api/apiClient";

export async function getSession(sessionId) {

    const response = await apiClient.get(
        `/session/${sessionId}`
    );

    return response.data;
}