# Institutional Quantitative Research Environment
# Optimized for high-performance data analysis and statistical modeling

FROM python:3.10-slim

# System-level dependencies for scientific computing
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Establish working directory
WORKDIR /opt/castle-trade/quant-suite

# Install core data science stack
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and research infrastructure
COPY src/ ./src/
COPY notebooks/ ./notebooks/
COPY docs/ ./docs/
COPY data/ ./data/

# Security: Service user for container runtime
RUN useradd -m quantsvc
USER quantsvc

# Environment configuration for numerical stability
ENV PYTHONOPTIMIZE=1
ENV NUMEXPR_MAX_THREADS=4

# Default execution context
CMD ["python", "src/indicators/volatility.py"]
