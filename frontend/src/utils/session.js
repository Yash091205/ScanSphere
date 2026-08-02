export function saveSession(sessionId) {
    localStorage.setItem("session_id", sessionId);
}

export function getSession() {
    return localStorage.getItem("session_id");
}

export function clearSession() {
    localStorage.removeItem("session_id");
}