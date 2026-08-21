import { useEffect, useState } from "react";

import { getSession } from "../services/reviewService";
import { getSession as getStoredSession } from "../utils/session";

export default function useEnhancementReviewActions() {

    const [loading, setLoading] = useState(true);
    const [session, setSession] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {

        async function loadSession() {

            try {

                const sessionId = getStoredSession();

                const data = await getSession(sessionId);

                setSession(data);

            } catch (err) {

                console.error(err);

                setError(
                    err.response?.data?.detail ||
                    "Failed to load session."
                );

            } finally {

                setLoading(false);

            }

        }

        loadSession();

    }, []);

    return {
        loading,
        session,
        error,
    };

}