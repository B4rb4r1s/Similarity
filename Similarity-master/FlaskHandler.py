import config
from TextSimilarityModule import BaseSimilarity

from flask import Flask, request, jsonify


app = Flask(__name__)



@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    text_1 = data['text_1']
    texts_2 = data['texts_2']
    # handlers = data['handlers']

    # print(texts_2, len(texts_2))

    handlers = [BaseSimilarity(i) for i in config.SIMILARITY_MODELS]

    similarities = []
    for handler in handlers:
        emb1 = handler.get_full_text_embeddings(text_1)

        text_similarities = []
        for text_2 in texts_2:
            if text_2:
                emb2 = handler.get_full_text_embeddings(text_2)
                text_similarities.append([handler.column, str(handler.calculate_similarity(emb1, emb2)), str(handler.calculate_similarity_acos(emb1, emb2))])
            else:
                text_similarities.append([handler.column, str(0)])

        similarities.append(text_similarities)

    compression = []
    for text_2 in texts_2:
        if text_2:
            compression.append(len(text_2)/len(text_1))
        else:
            compression.append(None)


    return jsonify({'similarities': similarities, 'compression': compression})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)