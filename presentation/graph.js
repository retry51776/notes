export const ATTENTION_TOKENS = ['Trans', 'formers', ' are', ' useful!']

export const ATTENTION_HEADS = {
  head1: {
    key: 'head1',
    name: 'Attention Head 1',
    focus: 'Sentiment',
    note: 'This head boosts emotional cues and gives the strongest weight to " useful!".',
    matrix: [
      [1.0, 0.0, 0.0, 0.0],
      [0.68, 0.32, 0.0, 0.0],
      [0.08, 0.12, 0.8, 0.0],
      [0.05, 0.1, 0.2, 0.65],
    ],
  },
  head2: {
    key: 'head2',
    name: 'Attention Head 2',
    focus: 'Syntax',
    note: 'This head tracks grammatical structure, linking predicate flow to the subject token pieces.',
    matrix: [
      [1.0, 0.0, 0.0, 0.0],
      [0.84, 0.16, 0.0, 0.0],
      [0.2, 0.58, 0.22, 0.0],
      [0.05, 0.65, 0.25, 0.05],
    ],
  },
}

function clamp01(value) {
  return Math.max(0, Math.min(1, value))
}

export function formatTokenLabel(token) {
  return token.replace(/^ +/, (spaces) => '\u2420'.repeat(spaces.length))
}

export function getCellStyle(score, isFutureToken = false) {
  if (isFutureToken) {
    return {
      backgroundColor: '#e5e7eb',
      color: '#6b7280',
      borderColor: '#d1d5db',
    }
  }

  const safe = clamp01(score)
  const r = Math.round(236 - 214 * safe)
  const g = Math.round(253 - 90 * safe)
  const b = Math.round(245 - 171 * safe)

  return {
    backgroundColor: `rgb(${r}, ${g}, ${b})`,
    color: safe > 0.58 ? '#f8fafc' : '#065f46',
    borderColor: safe > 0.58 ? 'rgba(6, 78, 59, 0.55)' : 'rgba(16, 185, 129, 0.55)',
  }
}
