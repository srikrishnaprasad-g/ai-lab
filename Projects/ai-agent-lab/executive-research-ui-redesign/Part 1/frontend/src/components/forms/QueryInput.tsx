'use client';

import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { ArrowRight, Loader2 } from 'lucide-react';

const schema = z.object({
  query: z
    .string()
    .min(20, 'Give the desk a bit more to work with — 20 characters minimum.')
    .max(5000, 'Keep the brief under 5000 characters.'),
});

type FormData = z.infer<typeof schema>;

interface QueryInputProps {
  onGenerate: (query: string) => void;
  isProcessing: boolean;
}

export const QueryInput = ({ onGenerate, isProcessing }: QueryInputProps) => {
  const [charCount, setCharCount] = useState(0);
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  const { onChange: rhfOnChange, ...queryField } = register('query');

  const onSubmit = (data: FormData) => {
    onGenerate(data.query);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="w-full">
      <div className="rounded-md border border-hairline bg-paper-raised shadow-[0_1px_2px_rgba(18,22,31,0.04)]">
        <div className="flex items-center justify-between border-b border-hairline px-5 py-3">
          <span className="font-mono text-[11px] tracking-[0.16em] uppercase text-slate">
            Research Brief
          </span>
          <span className="font-mono text-[11px] text-slate-soft">
            {charCount}/5000
          </span>
        </div>
        <textarea
          {...queryField}
          onChange={(e) => {
            rhfOnChange(e);
            setCharCount(e.target.value.length);
          }}
          rows={5}
          className="w-full resize-none bg-transparent px-5 py-4 font-body text-[15px] leading-relaxed text-ink placeholder:text-slate-soft focus:outline-none focus-brass"
          placeholder="Analyze the impact of AI agents on enterprise SaaS pricing and delivery models over the next three years..."
        />
      </div>

      <div className="mt-2 flex items-start justify-between">
        {errors.query ? (
          <p className="font-mono text-[12px] text-rust">{errors.query.message}</p>
        ) : (
          <p className="font-mono text-[12px] text-slate-soft">
            Be specific. The desk works best with a real decision behind the question.
          </p>
        )}
      </div>

      <button
        type="submit"
        disabled={isProcessing}
        className="group mt-4 inline-flex w-full items-center justify-center gap-2 rounded-md bg-ink py-3.5 font-body text-[14px] font-medium text-paper transition-colors duration-200 hover:bg-ink-soft disabled:cursor-not-allowed disabled:bg-slate-soft focus-brass"
      >
        {isProcessing ? (
          <>
            <Loader2 className="h-4 w-4 animate-spin text-brass-light" />
            Assembling briefing…
          </>
        ) : (
          <>
            Commission the report
            <ArrowRight className="h-4 w-4 text-brass-light transition-transform duration-200 group-hover:translate-x-0.5" />
          </>
        )}
      </button>
    </form>
  );
};
