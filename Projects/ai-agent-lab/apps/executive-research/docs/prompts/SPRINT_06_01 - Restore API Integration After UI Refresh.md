Sprint 6.1 – Restore API Integration After UI Refresh

The UI redesign has been successfully integrated and approved.

The application UI, responsive layout, and user experience are satisfactory.

However, the research flow is currently broken.

Symptoms:

Clicking "Commission the report" results in
Failed to fetch

The browser Network tab shows the frontend attempting to call

http://localhost:8000/api/v1/research

instead of using the configured API base URL.

The redesign sprint was intended to modify only the UI.

Please perform the following:

1. Audit

Review every frontend file for hardcoded API URLs.

Search for:

localhost:8000
127.0.0.1
/api/v1
fetch(
axios
API_BASE_URL
NEXT_PUBLIC_API_BASE_URL
2. Restore

Ensure every API request uses

API_BASE_URL

from

src/config/api.ts

Do not hardcode any URL.

3. Preserve

Do not modify:

backend
API routes
Render configuration
Runtime
PDF generation
4. Validate

Run

npm run dev

Verify:

research request succeeds
executive summary appears
key findings appear
PDF downloads
5. Deliver

Provide:

files changed
root cause
validation
git diff

Do not commit.
Do not deploy.