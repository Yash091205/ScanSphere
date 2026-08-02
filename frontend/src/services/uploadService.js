import apiClient from "../api/apiClient";

export async function uploadPdf(file) {

    const formData = new FormData();

    formData.append("file", file);

    const response = await apiClient.post(
        "/upload/pdf",
        formData
    );

    return response.data;
}

export async function uploadImages(files) {

    const formData = new FormData();

    files.forEach(file => {
        formData.append("files", file);
    });

    const response = await apiClient.post(
        "/upload/images",
        formData
    );

    return response.data;
}