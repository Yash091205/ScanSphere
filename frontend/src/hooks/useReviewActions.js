import { useEffect, useState } from "react";

import { getSession } from "../services/reviewService";
import { getSession as getStoredSession } from "../utils/session";

export default function useReviewActions() {

    const [loading, setLoading] = useState(true);

    const [session, setSession] = useState(null);

    useEffect(() => {

        async function loadSession() {

            try {

                const sessionId = getStoredSession();

                const data = await getSession(sessionId);

                setSession(data);

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);

            }

        }

        loadSession();

    }, []);

    return {

        loading,

        session,

    };

}