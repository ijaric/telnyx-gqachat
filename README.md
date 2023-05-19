### Description
The repository is a proof-of-concept API that leverages user-provided documentation as context to answer questions. It demonstrates how ChatGPT can be integrated into a question-answering system. This PoC serves as a take-home test for Telnyx.

### Installation
1. Clone the repository using `git clone git@github.com:ijaric/telnyx-gqachat.git`.
2. Create a .env file in the `/infra directory` and populate it. You can find an example at `/infra/.env.example`.
3. The only required field is `OPENAI_API_KEY`. All other fields are optional.

### Run
Navigate to `/infra` and execute the docker compose command, i.e., `cd infra && docker compose up -d`.
You can access the API at `your_address/api/v1/gqachat/?question=your_question`. For example, `http://localhost/api/v1/gqachat/?question=What%20are%20the%20SMS%20guidelines%20for%20Ireland%3F`.
The result contains two fields: `answer` and `sources`, or it might contain an error message.
### Challenges
1. I have no prior experience in this area, so I had limited time to dive in.
2. The documentation contains a lot of identical text, which impairs legibility.
3. I ran into unexpected behavior from the langchain library.

### Next steps
1. Finalize basic setup for the project. For example, (a) transfer the ETL to a separate repo, (b) create tests, (c) set up an external database, (d) improve code quality (SOLID).
2. Implement asynchronous workflows for queries.
3. Gain a comprehensive understanding of the available company's documentation, most popular questions, and number of requests.
4. I expect potential problems with low discernibility of the documents. Thus, we may receive incorrect context, leading to a wrong answer or no answer at all.
5. We can approach this problem in a number of ways. For example, we could enrich the documentation (add tags, remove faintly discernible data), improve prompts, and introduce tools (or a chain of tools).
6. If the number of requests is very high, it might be worth benchmarking available options to reduce costs and improve performance. Another option is to implement caching.