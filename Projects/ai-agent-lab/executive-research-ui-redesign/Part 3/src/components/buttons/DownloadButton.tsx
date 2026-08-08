import React from 'react';
import { FileText } from 'lucide-react';
import { API_BASE_URL } from '@/config/api';

interface DownloadButtonProps { isVisible: boolean; reportId: string; }

export const DownloadButton = ({ isVisible, reportId }: DownloadButtonProps) => {
  if (!isVisible) return null;

  const handleDownload = () => {
    window.location.href = `${API_BASE_URL}/api/v1/download/${reportId}`;
  };

  return (
    <div className="animate-rise-in mt-6 flex w-full items-center justify-between rounded-md border border-hairline bg-paper-raised px-6 py-5">
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 items-center justify-center rounded-full bg-moss-bg text-moss">
          <FileText className="h-4 w-4" strokeWidth={2} />
        </div>
        <div>
          <p className="font-body text-[15px] font-semibold text-ink">Report ready</p>
          {/* ref: body 13px slate — was mono 11px slate-soft */}
          <p className="font-body text-[13px] text-slate mt-0.5">REF {reportId}</p>
        </div>
      </div>
      <button
        onClick={handleDownload}
        className="rounded-md bg-ink px-5 py-2.5 font-body text-[14px] font-semibold text-paper transition-colors duration-200 hover:bg-ink-soft focus-brass"
      >
        Download PDF
      </button>
    </div>
  );
};
