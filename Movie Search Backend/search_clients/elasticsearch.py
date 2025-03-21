from elasticsearch import AsyncElasticsearch


from app_vars import ELASTICSEARCH_API_KEY, ELASTICSEARCH_HOST

es_client = AsyncElasticsearch(ELASTICSEARCH_HOST, api_key=ELASTICSEARCH_API_KEY)
