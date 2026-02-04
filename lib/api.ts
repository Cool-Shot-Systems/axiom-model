type GenerateResponse = {
  response?: string;
};

const DEFAULT_ERROR =
  "We were unable to generate a response right now. Please try again.";

/**
 * Public environment variables are exposed to the browser in Next.js.
 * These are safe to expose because they reference a scoped API key intended
 * for client-side use and are configured in the Vercel project settings.
 */
const API_URL = process.env.NEXT_PUBLIC_AXIOM_API_URL ?? "";
const API_KEY = process.env.NEXT_PUBLIC_AXIOM_API_KEY ?? "";

export async function generateResponse(prompt: string): Promise<string> {
  if (!API_URL || !API_KEY) {
    return DEFAULT_ERROR;
  }

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt, max_tokens: 150 }),
    });

    if (!response.ok) {
      return DEFAULT_ERROR;
    }

    const data = (await response.json()) as GenerateResponse;
    if (typeof data.response !== "string" || data.response.length === 0) {
      return DEFAULT_ERROR;
    }
    return data.response;
  } catch {
    return DEFAULT_ERROR;
  }
}
