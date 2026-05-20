from langchain.chat_models import init_chat_model

GEMINI_API_KEY="AIzaSyDQqaBIraaaCDE1pc2UvxdyhBo4Sm5K2nw"

models = init_chat_model(
    # model = "gemini-3-flash-preview",
    model = "gemini-2.5-flash",
    model_provider="google-genai",
    api_key = GEMINI_API_KEY
)

response = models.invoke("Explain LLM and RAG in detailed words")
# final_res = response.content[0]['text']  (This is for 3-flash-preview)
final_res = response.content
print(final_res)
