import config 
from TextSimilarityModule import BaseSimilarity
from DBHandler import DatabaseHandler


if __name__ == "__main__":
    db_handler = DatabaseHandler(host='docker')
    db_handler.set_doc_ids('elibrary_dataset_similarities')

    dataset = db_handler.get_db_table_text_summaries()
    handlers = [BaseSimilarity(i) for i in config.SIMILARITY_MODELS]


    for row in dataset:
        similarities = []
        for handler in handlers:
            text_1 = row[1]
            emb1 = handler.generate_embedding(text_1)

            text_similarities = []
            # lingvo_summary, mt5_summary, mbart_summary, rut5_summary, t5_summary
            for text_2 in row[3:]:
                if text_2:
                    emb2 = handler.generate_embedding(text_2)
                    text_similarities.append(handler.calculate_similarity(emb1, emb2))

            print('elibrary_dataset_similarities', handler.column, row[0], text_similarities)
        break
            # db_handler.upload_data('elibrary_dataset_similarities', handler.column, row[0], text_similarities)
            # similarities.append(text_similarities)

