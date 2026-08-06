export interface KeyInsight {
  title: string;
  description: string;
}

export interface ResearchResult {
  executiveSummary: string;
  keyInsights: KeyInsight[];
  reportId: string;
}

export type StepStatus = 'pending' | 'running' | 'completed';

export interface ProgressStep {
  label: string;
  status: StepStatus;
}
