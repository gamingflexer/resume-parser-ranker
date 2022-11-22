FROM python:3.7

# Install parser
RUN git clone https://github.com/gamingflexer/resume-parser-ranker.git /parser
WORKDIR /parser

# Install parser-web
RUN git clone https://github.com/gamingflexer/resume-parser-web.git /parser-web
WORKDIR /parser-web

RUN apt update && apt upgrade -y

RUN pip install -e .