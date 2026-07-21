import type { ChatMessage, ChatResponse } from '../types/plan'

// Dev'de boş bırakılır (Vite proxy /api → 127.0.0.1:8000).
// Prod'da frontend ve backend ayrı host'larda deploy edildiğinde
// VITE_API_BASE_URL ile backend'in tam URL'i verilir (ör. https://healroute-api.onrender.com).
const API_BASE = import.meta.env.VITE_API_BASE_URL ?? ''

export async function sendChat(
  message: string,
  history: ChatMessage[],
): Promise<ChatResponse> {
  const res = await fetch(`${API_BASE}/api/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, history }),
  })
  if (!res.ok) throw new Error(`API error ${res.status}`)
  return res.json()
}
