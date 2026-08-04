import { ResearchResult } from '../../types/research';

export const generateMockResearchReport = async (query: string): Promise<ResearchResult> => {
  console.log('Generating for query:', query);
  // Simulate network delay
  await new Promise((resolve) => setTimeout(resolve, 2000));
  
  return {
    executiveSummary: "Artificial Intelligence agents are fundamentally transforming the Enterprise SaaS landscape by automating complex workflows, enhancing personalization, and shifting focus from feature-based to outcome-based software delivery. This paradigm shift mandates a re-evaluation of product strategy, pricing models, and talent requirements to maintain competitive advantage.",
    keyInsights: [
      'Agents enable outcome-based pricing models.',
      'Workflow automation reduces operational overhead by 40%.',
      'Human-in-the-loop remains critical for strategic oversight.',
    ],
  };
};
