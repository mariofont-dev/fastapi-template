# Step 1: Choose a base image (Python runtime)
FROM python:3.11-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 2.5: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Step 3: Copy requirements file first (for Docker layer caching)
COPY requirements.txt .

# Step 4: Install uv (fast Python package installer)
RUN pip install --no-cache-dir uv

# Step 5: Install dependencies using uv (much faster than pip)
RUN uv pip install --system -r requirements.txt

# Step 6: Copy your application code
COPY . .

# Step 7: Expose port 8000 (where FastAPI runs)
EXPOSE 8000

# Step 8: Command to run when container starts
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]

