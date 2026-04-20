# ================================
# Stage 1 — Builder
# ================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .

# Install to a custom directory so we can copy it cleanly
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ================================
# Stage 2 — Runtime (final image)
# ================================
FROM python:3.11-alpine

WORKDIR /app

# Copy installed packages from builder stage only
COPY --from=builder /install /usr/local

# Copy app code
COPY app.py .

# Run as non-root user — security best practice
RUN adduser -D appuser
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
