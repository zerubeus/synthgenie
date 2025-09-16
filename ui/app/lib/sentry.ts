import * as Sentry from "@sentry/react";

export function initSentry() {
  const dsn = import.meta.env.VITE_SENTRY_DSN;
  
  if (!dsn) {
    console.warn("Sentry DSN not provided. Sentry will not be initialized.");
    return;
  }

  Sentry.init({
    dsn,
    environment: import.meta.env.VITE_SENTRY_ENVIRONMENT || "development",
    integrations: [
      Sentry.browserTracingIntegration(),
      Sentry.replayIntegration({
        maskAllText: false,
        blockAllMedia: false,
      }),
    ],
    // Performance Monitoring
    tracesSampleRate: import.meta.env.VITE_SENTRY_TRACES_SAMPLE_RATE 
      ? parseFloat(import.meta.env.VITE_SENTRY_TRACES_SAMPLE_RATE) 
      : 0.1,
    // Session Replay
    replaysSessionSampleRate: import.meta.env.VITE_SENTRY_REPLAY_SESSION_SAMPLE_RATE
      ? parseFloat(import.meta.env.VITE_SENTRY_REPLAY_SESSION_SAMPLE_RATE)
      : 0.1,
    replaysOnErrorSampleRate: import.meta.env.VITE_SENTRY_REPLAY_ERROR_SAMPLE_RATE
      ? parseFloat(import.meta.env.VITE_SENTRY_REPLAY_ERROR_SAMPLE_RATE)
      : 1.0,
  });
}