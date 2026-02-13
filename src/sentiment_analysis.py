from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

def analyze(text):
    result = sentiment_model(text)
    return result

if __name__ == "__main__":
    sample = "Reliance shares rise after strong earnings"
    print(analyze(sample))
