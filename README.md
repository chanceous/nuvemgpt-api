# NuvemGPT - API

NuvemGPT is a highly cost-effective AI query engine based on OpenAI. It combines the potential of the common OpenAI API (text-Davinci-003) with a local vector database, allowing you to store an almost infinite dataset of trained documents.

## How does it work?

- In the "training" folder, you should upload the documents to be trained (currently supporting .txt and other non-encoded formats, with plans to support .pdf, .xls, .docx, etc in the future).
- When you run "python index.py" in the training folder (the small indexing process), it creates a small database of JSON vectors. This database can be a Redis or another database that accepts vectors, and you just need to configure it. Each document is sent to the OpenAI API during this process.
- Then, when a query is made from the user's side, it gets vectorized, and a cosine similarity calculation is performed based on a defined K. This provides the context necessary to answer the user's question. In simpler terms, if the user asks about tomatoes, it will respond with information about tomatoes based on the training data.
