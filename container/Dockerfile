FROM python:3.12-slim
WORKDIR /workspace
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
COPY container/requirements-evidence.txt /tmp/requirements-evidence.txt
RUN pip install --no-cache-dir -r /tmp/requirements-evidence.txt
RUN git clone https://github.com/UBC-FRESH/fresh-solutions /fresh-solutions \
    && git -C /fresh-solutions checkout 7d3c831
COPY . /workspace
ENV PYTHONPATH=/fresh-solutions
CMD ["bash", "paper2/replay_all.sh"]
