import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
    getSession,
    deletePage,
    replacePage,
    appendPages,
    reorderPages,
} from "../services/reviewService";

import { enhanceSession } from "../services/enhancementService";

import {
    getSession as getStoredSession,
} from "../utils/session";

export default function useReviewActions() {

    const navigate = useNavigate();
    const [loading, setLoading] = useState(true);
    const [actionLoading, setActionLoading] = useState(false);
    const [session, setSession] = useState(null);
    const [error, setError] = useState(null);

    // Reload session from backend
    const refreshSession = async () => {
        const sessionId = getStoredSession();
        if (!sessionId) {
            setError("No active session found.");
            return;
        }
        const data = await getSession(sessionId);
        setSession(data);
    };

    useEffect(() => {
        async function loadSession() {
            try {
                await refreshSession();
            } catch (err) {
                console.error(err);
                setError(err.response?.data?.detail || "Failed to load session.");
            } finally {
                setLoading(false);
            }
        }

        loadSession();
    }, []);

    // Delete one page
    const handleDelete = async (pageId) => {
        try {
            setActionLoading(true);
            const sessionId = getStoredSession();
            const data = await deletePage(sessionId, pageId);
            setSession(data);
        } catch (err) {
            console.error(err);
            alert(err.response?.data?.detail || "Failed to delete page.");
        } finally {
            setActionLoading(false);
        }
    };

    // Replace a page
    const handleReplace = async (pageId, file) => {
        if (!file) return;
        try {
            setActionLoading(true);
            const sessionId = getStoredSession();
            const data = await replacePage(sessionId, pageId, file);
            setSession(data);
        } catch (err) {
            console.error(err);
            alert(err.response?.data?.detail || "Failed to replace page.");
        } finally {
            setActionLoading(false);
        }
    };

    // Append new pages
    const handleAppend = async (files) => {
        if (!files || files.length === 0) return;
        try {
            setActionLoading(true);
            const sessionId = getStoredSession();
            const data = await appendPages(sessionId, files);
            setSession(data);
        } catch (err) {
            console.error(err);
            alert(err.response?.data?.detail || "Failed to append pages.");
        } finally {
            setActionLoading(false);
        }
    };

    // Move page left/right (reorder)
    const handleMove = async (pageId, direction) => {
        if (!session || !session.pages) return;
        const pages = [...session.pages];
        const index = pages.findIndex(p => (p.page_id || p.id) === pageId);
        if (index === -1) return;

        const targetIndex = direction === "left" ? index - 1 : index + 1;
        if (targetIndex < 0 || targetIndex >= pages.length) return;

        // Swap in order array
        const pageOrder = pages.map(p => p.page_id || p.id);
        const temp = pageOrder[index];
        pageOrder[index] = pageOrder[targetIndex];
        pageOrder[targetIndex] = temp;

        try {
            setActionLoading(true);
            const sessionId = getStoredSession();
            const data = await reorderPages(sessionId, pageOrder);
            setSession(data);
        } catch (err) {
            console.error(err);
            alert(err.response?.data?.detail || "Failed to reorder pages.");
        } finally {
            setActionLoading(false);
        }
    };

    // Proceed to Enhancement
    const handleProceed = async () => {
        if (!session || session.pages.length === 0) {
            alert("Please upload at least one page before proceeding.");
            return;
        }
        try {
            setActionLoading(true);
            const sessionId = getStoredSession();
            await enhanceSession(sessionId);
            navigate("/enhancement-review");
        } catch (err) {
            console.error(err);
            alert(err.response?.data?.detail || "Failed to trigger enhancement process.");
        } finally {
            setActionLoading(false);
        }
    };

    return {
        loading,
        actionLoading,
        session,
        error,
        handleDelete,
        handleReplace,
        handleAppend,
        handleMove,
        handleProceed,
    };
}