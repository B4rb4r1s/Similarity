import config 
from TextSimilarityModule import BaseSimilarity
from DBHandler import DatabaseHandler


def run_real_sim():
    db_handler = DatabaseHandler(host='docker')
    # db_handler.set_doc_ids('elibrary_dataset_similarities')

    dataset = db_handler.get_db_table_text_real_summaries()
    handlers = [BaseSimilarity(i) for i in config.SIMILARITY_MODELS]
    # print(dataset[:3])
    # return 0
    for i, row in enumerate(dataset):
        similarities = []
        for handler in handlers:
            with open('logs.txt', 'a') as f:
                f.write(f'Model: {handler.column}\n')
            # ROW = [e_d.id, target_summary, e_d_s.doc_id, text_dedoc, lingvo_summary, mt5_summary, mbart_summary, rut5_summary, t5_summary]
            text_1 = row[1]
            emb1 = handler.get_full_text_embeddings(text_1)

            text_similarities = []
            # lingvo_summary, mt5_summary, mbart_summary, rut5_summary, t5_summary
            for text_2 in row[3:]:
                if text_2:

                    emb2 = handler.get_full_text_embeddings(text_2)
                    text_similarities.append(handler.calculate_similarity(emb1, emb2))

            print('elibrary_dataset_similarities', handler.column, row[0], text_similarities)
            with open('simm-logs.txt', 'a') as f:
                f.write(f'Text {i}: {handler.column}: {text_similarities}\n')


def run():
    db_handler = DatabaseHandler(host='docker')
    # db_handler.set_doc_ids('elibrary_dataset_similarities')

    dataset = db_handler.get_db_table_text_summaries()
    handlers = [BaseSimilarity(i) for i in config.SIMILARITY_MODELS]
    # print(dataset[:3])
    # return 0
    for i, row in enumerate(dataset):
        similarities = []
        for handler in handlers:
            with open('logs.txt', 'a') as f:
                f.write(f'Model: {handler.column}\n')

            text_1 = row[1]
            emb1 = handler.get_full_text_embeddings(text_1)

            text_similarities = []
            # lingvo_summary, mt5_summary, mbart_summary, rut5_summary, t5_summary
            for text_2 in row[3:]:
                if text_2:

                    emb2 = handler.get_full_text_embeddings(text_2)
                    text_similarities.append(handler.calculate_similarity(emb1, emb2))

            print('elibrary_dataset_similarities', handler.column, row[0], text_similarities)
            with open('simm-logs.txt', 'a') as f:
                f.write(f'Text {i}: {handler.column}: {text_similarities}\n')
        # break
            # db_handler.upload_data('elibrary_dataset_similarities', handler.column, row[0], text_similarities)
            # similarities.append(text_similarities)


if __name__ == "__main__":
    run_real_sim()
