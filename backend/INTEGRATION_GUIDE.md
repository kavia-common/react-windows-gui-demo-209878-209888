# Backend Integration and Docs

This Flask backend exposes:
- Health: GET /
- Swagger UI: /docs (e.g., http://localhost:3001/docs)
- OpenAPI JSON: /openapi.json

## Run locally

1) Create venv and install deps:
   - python -m venv .venv && source .venv/bin/activate
   - pip install -r requirements.txt

2) Start server on port 3001:
   - export PORT=3001
   - python run.py

3) Verify:
   - curl http://localhost:3001/        -> {"message":"Healthy"}
   - Open http://localhost:3001/docs    -> Swagger UI
   - Open http://localhost:3001/openapi.json

CORS is enabled for demo convenience (origins="*"). Restrict in production.

## Notes

- The health check blueprint is registered at root (“/”).
- Tag naming in the generated OpenAPI uses “Health Check”. If you see “Healt Check” in any old spec files, that was a typo and has been corrected in the current spec generation.
