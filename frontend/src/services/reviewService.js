import apiClient from "../api/apiClient";

export async function getSession(sessionId) {

    const response = await apiClient.get(
        `/session/${sessionId}`
    );

    return response.data;
}

export async function deletePage(
    sessionId,
    pageId,
) {

    const response = await apiClient.delete(
        `/session/${sessionId}/page/${pageId}`
    );

    return response.data;
}

export async function replacePage(sessionId, pageId, file) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await apiClient.put(
        `/session/${sessionId}/page/${pageId}`,
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}

export async function appendPages(sessionId, files) {
    const formData = new FormData();
    Array.from(files).forEach((file) => {
        formData.append("files", file);
    });

    const response = await apiClient.post(
        `/session/${sessionId}/append`,
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}

export async function reorderPages(sessionId, pageOrder) {
    const response = await apiClient.put(
        `/session/${sessionId}/reorder`,
        {
            page_order: pageOrder,
        }
    );

    return response.data;
}