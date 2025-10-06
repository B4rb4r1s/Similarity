import config 
from TextSimilarityModule import BaseSimilarity
from DBHandler import DatabaseHandler


# def run_real_sim():
#     db_handler = DatabaseHandler(host='docker')
#     # db_handler.set_doc_ids('elibrary_dataset_similarities')

#     dataset = db_handler.get_db_table_text_real_summaries()
#     handlers = [BaseSimilarity(i) for i in config.SIMILARITY_MODELS]
#     # print(dataset[:3])
#     # return 0
#     for i, row in enumerate(dataset):
#         similarities = []
#         for handler in handlers:
#             with open('logs.txt', 'a') as f:
#                 f.write(f'Model: {handler.column}\n')
#             # ROW = [e_d.id, target_summary, e_d_s.doc_id, text_dedoc, lingvo_summary, mt5_summary, mbart_summary, rut5_summary, t5_summary]
#             text_1 = row[1]
#             emb1 = handler.get_full_text_embeddings(text_1)

#             text_similarities = []
#             # lingvo_summary, mt5_summary, mbart_summary, rut5_summary, t5_summary
#             for text_2 in row[3:]:
#                 if text_2:

#                     emb2 = handler.get_full_text_embeddings(text_2)
#                     text_similarities.append(handler.calculate_similarity(emb1, emb2))

#             print('elibrary_dataset_similarities', handler.column, row[0], text_similarities)
#             with open('simm-logs.txt', 'a') as f:
#                 f.write(f'Text {i}: {handler.column}: {text_similarities}\n')

def run_source_target():
    db_handler = DatabaseHandler(host='docker')
    dataset = db_handler.get_db_table_text_summaries_from_source()
    handlers = [BaseSimilarity(i) for i in config.SIMILARITY_MODELS]

    for row in dataset:
        doc_id = row[0]
        text_1 = row[1]
        text_2 = row[2]

        similarity_values = {}
        for handler in handlers:
            emb1 = handler.get_full_text_embeddings(text_1)
            emb2 = handler.get_full_text_embeddings(text_2)
            sim_score = handler.calculate_similarity(emb1, emb2)
            similarity_values[handler.column] = sim_score
            
        print(doc_id,
            'source_text',
            'target_summary',
            similarity_values.get('rubert-tiny2'),
            similarity_values.get('labse-ru-sts'),
            similarity_values.get('uaritm'),
            similarity_values.get('DeepPavlov-rubert'))
        
        # загружаем данные в БД
        with db_handler.connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO similarity_metrics
                    (doc_id, text_source, text_target, metric_rubert_tiny2, metric_labse_ru_sts, metric_multilingual, metric_rubert_base)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (
                doc_id,
                'source_text',
                'target_summary',
                float(similarity_values.get('rubert-tiny2')),
                float(similarity_values.get('labse-ru-sts')),
                float(similarity_values.get('uaritm')),
                float(similarity_values.get('DeepPavlov-rubert'))
            ))
            db_handler.connection.commit()

def run_real_sim():
    db_handler = DatabaseHandler(host='docker')
    dataset = db_handler.get_db_table_text_summaries_from_target()
    columns = db_handler.get_column_name()
    handlers = [BaseSimilarity(i) for i in config.SIMILARITY_MODELS]

    for row in dataset:
        doc_id = row[0]
        text_1 = row[1]
        text_2 = row[2]

        # проходим по всем текстам для сравнения
        for i, text_3 in enumerate(row[3:]):
            if not text_3:
                continue

            similarity_values = {}
            for handler in handlers:
                emb1 = handler.get_full_text_embeddings(text_1)
                emb2 = handler.get_full_text_embeddings(text_3)
                sim_score = handler.calculate_similarity(emb1, emb2)
                similarity_values[handler.column] = sim_score

            print(doc_id,
                    'target_summary',
                    columns[i+3],
                    similarity_values.get('rubert-tiny2'),
                    similarity_values.get('labse-ru-sts'),
                    similarity_values.get('uaritm'),
                    similarity_values.get('DeepPavlov-rubert'))
            # загружаем данные в БД
            with db_handler.connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO similarity_metrics
                        (doc_id, text_source, text_target, metric_rubert_tiny2, metric_labse_ru_sts, metric_multilingual, metric_rubert_base)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', (
                    doc_id,
                    'target_summary',
                    columns[i+3],
                    float(similarity_values.get('rubert-tiny2')),
                    float(similarity_values.get('labse-ru-sts')),
                    float(similarity_values.get('uaritm')),
                    float(similarity_values.get('DeepPavlov-rubert'))
                ))
                db_handler.connection.commit()

                


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
    # run_real_sim()
    run_source_target()
