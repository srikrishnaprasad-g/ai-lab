'use client';

import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { ArrowRight, Loader2, RotateCcw } from 'lucide-react';

const schema = z.object({
  query: z
    .string()
    .min(20, 'Please write at least 20 characters so the desk has enough to work with.')
    .max(5000, 'Keep the brief under 5000 characters.'),
});

type FormData = z.infer<typeof schema>;

interface QueryInputProps {
  onGenerate: (query: string) => void;
  onReset?: () => void;
  isProcessing: boolean;
  hasResults: boolean;
}

export const QueryInput = ({ onGenerate, onReset, isProcessing, hasResults }: QueryInputProps) => {
  const [charCount, setCharCount] = useState(0);
  const {
    register,
    handleSubmit,
    reset: resetForm,
    formState: { errors },
  } = useForm<FormData>({ resolver: zodResolver(schema) });

  const { onChange: rhfOnChange, ...queryField } = register('query');

  const onSubmit = (data: FormData) => onGenerate(data.query);

  const handleNewBrief = () => {
    resetForm({ query: '' });
    setCharCount(0);
    onReset?.();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="w-full">
      <form onSubmit={handleSubmit(onSubmit)} className="w-full">
        <div className="rounded-md border border-hairline bg-paper-raised shadow-[0_1px_3px_rgba(18,22,31,0.06)]">

          {/* ── Form header bar ── */}
          <div className="flex items-center justify-between border-b border-hairline px-5 py-3">
            {/* font-body 13px semibold, full ink colour — was mono 11px muted */}
            <span className="font-body text-[13px] font-semibold text-ink">
              Research Brief
            </span>
            <span className="font-body text-[13px] text-slate">
              {charCount} / 5000
            </span>
          </div>

          {/* ── Textarea ── */}
          <textarea
            {...queryField}
            onChange={(e) => { rhfOnChange(e); setCharCount(e.target.value.length); }}
            rows={4}
            disabled={isProcessing}
            className="w-full resize-none bg-transparent px-5 py-4 font-body text-[16px] leading-relaxed text-ink placeholder:text-slate-soft focus:outline-none focus-brass disabled:opacity-50"
            placeholder="Analyze the impact of AI agents on enterprise SaaS pricing and delivery models over the next three years..."
          />
        </div>

        {/* ── Hint / error text ── */}
        <div className="mt-2.5">
          {errors.query ? (
            // Error: body font, 14px, full rust colour
            <p className="font-body text-[14px] font-medium text-rust">
              {errors.query.message}
            </p>
          ) : (
            // Hint: body font, 14px, slate (not muted grey-blue) — much more readable
            <p className="font-body text-[14px] text-slate">
              Be specific. The desk works best with a real decision behind the question.
            </p>
          )}
        </div>

        {/* ── Buttons ── */}
        <div className="mt-4 flex items-center gap-3">
          <button
            type="submit"
            disabled={isProcessing}
            className="group flex-1 inline-flex items-center justify-center gap-2 rounded-md bg-ink py-3.5 font-body text-[15px] font-semibold text-paper transition-colors duration-200 hover:bg-ink-soft disabled:cursor-not-allowed disabled:opacity-50 focus-brass"
          >
            {isProcessing ? (
              <><Loader2 className="h-4 w-4 animate-spin text-brass-light" />Assembling the brief…</>
            ) : (
              <>Commission the report <ArrowRight className="h-4 w-4 text-brass-light transition-transform duration-200 group-hover:translate-x-0.5" /></>
            )}
          </button>

          {hasResults && !isProcessing && (
            <button
              type="button"
              onClick={handleNewBrief}
              className="inline-flex items-center gap-2 rounded-md border border-hairline px-4 py-3.5 font-body text-[15px] font-medium text-slate transition-colors duration-200 hover:border-brass hover:text-brass focus-brass"
              title="Clear and start a new brief"
            >
              <RotateCcw className="h-4 w-4" strokeWidth={2} />
              New brief
            </button>
          )}
        </div>
      </form>
    </div>
  );
};
