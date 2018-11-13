import pymongo
import json

def lambda_handler(event, context):
	client = pymongo.MongoClient('mongodb://username:password@ds046267.mlab.com:46267/zoeystudios_test')
	db = client['zoeystudios_test']
	collection = db['hkexnews']
	cur=collection.find({'code': event['queryStringParameters']['code']}, { 'share_holding': 1, 'date': 1, '_id':0 }).sort("date")
	from bson.json_util import dumps
	return {
		"statusCode": 200,
		"headers": {
            
            "Access-Control-Allow-Origin" :"*"
        },
		"body":dumps(cur)
		}
	