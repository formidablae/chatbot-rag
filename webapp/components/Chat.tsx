"use client";

import { useState } from "react";
import { sendQuery } from "../app/utils/api";

export default function Chat() {
    const [query, setQuery] = useState("");
    const [response, setResponse] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleQuery = async () => {
        if (!query.trim()) return;
        setLoading(true);
        setResponse(null);

        try {
            const res = await sendQuery(query);
            setResponse(res);
        } catch (error) {
            setResponse("An error occurred while retrieving the response.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-lg w-full p-6 bg-white rounded-lg shadow-md">
            <textarea
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="w-full p-2 border rounded"
                placeholder="Type your question..."
            />
            <button
                onClick={handleQuery}
                className="mt-3 px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-400"
                disabled={loading}
            >
                {loading ? "Loading..." : "Send"}
            </button>
            {response && (
                <div className="mt-4 p-3 bg-gray-100 border rounded">
                    <strong>Response:</strong>
                    <p>{response}</p>
                </div>
            )}
        </div>
    );
}
