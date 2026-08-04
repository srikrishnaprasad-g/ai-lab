import { API_BASE_URL } from '../../config/api';
import { ResearchResult } from '../../types/research';

export const generateResearchReport = async (query: string): Promise<ResearchResult> => {
  const response = await fetch(`${API_BASE_URL}/api/v1/research`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query }),
  });

  if (!response.ok) {
    throw new Error('Failed to generate research report');
  }

  const result = await response.json();
  
  if (result.status !== 'success') {
    throw new Error(result.message || 'Failed to generate research report');
  }

  // Map backend response to frontend ResearchResult
  return {
    executiveSummary: result.data.executive_summary,
    keyInsights: result.data.key_insights,
    reportId: result.data.report_id
  };
};
