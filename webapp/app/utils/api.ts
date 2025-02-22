import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const sendQuery = async (query: string) => {
  try {
    const response = await axios.post(`${BASE_URL}/query/`, { query });
    return response.data.response;
  } catch (error) {
    console.error("Error fetching response:", error);
    return "An error occurred while retrieving the response.";
  }
};
