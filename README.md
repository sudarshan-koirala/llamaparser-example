# llamaparser-example
Simple example to showcase how to use llamaparser to parse PDF files

## Videos covering these topics
### [Llamaparse LlamaIndex](https://youtu.be/wRMnHbiz5ck?si=iQZV7N6-trcuBm8M)
### [Llamaparse Qdrant Gorq](https://youtu.be/w7Ap6gZFXl0?si=05AUGmRp1quTdeZl)

### Links shown in video
- [LlamaCloud](https://cloud.llamaindex.ai/)
- [Qdrant Cloud](https://cloud.qdrant.io/)
- [Groq Cloud](https://console.groq.com/)

### create virtualenv
```
python3 -m venv .venv && source .venv/bin/activate
```

### Install packages
```
pip install -r requirements.txt
```

### Environment variables
All env variables goes to .env ( cp `example.env` to `.env` and paste required env variables)

### Run the python files (following the vieoo to run step by step is recommended)
```
python3 parser-qdrant-groq.py
```

## Additional helper documents
- [LlamaIndex blogpost about Llamaparse](https://www.llamaindex.ai/blog/launching-the-first-genai-native-document-parsing-platform)
- [Advanced demo with Reranker](https://github.com/run-llama/llama_parse/blob/main/examples/demo_advanced.ipynb)
- [Parsing instructions Llamaparse](https://colab.research.google.com/drive/1dO2cwDCXjj9pS9yQDZ2vjg-0b5sRXQYo#scrollTo=dEX7Mv9V0UvM)
