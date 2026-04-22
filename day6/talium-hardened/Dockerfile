# Stage 1 — Builder
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2 — Hardened runtime
FROM python:3.11-alpine

# Install security updates on build
RUN apk update && apk upgrade && rm -rf /var/cache/apk/*

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY app.py .

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set ownership
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Healthcheck — Docker monitors this
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:5000/ || exit 1

EXPOSE 5000

CMD ["python", "app.py"]
