from transformers import pipeline

classifier = pipeline("sentiment-analysis")

texts = ["I love this!", "This is terrible.", "URGENT: verify your account now or it will be suspended"]
for t in texts:
    print(t, "->", classifier(t))