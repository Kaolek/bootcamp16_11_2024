import redis

# client = redis.Redis(host='localhost', port=6379, db=0)
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

client.set('foo', 'barśż')

value = client.get('foo')
# print(value.decode('utf-8')) # barśż
print(value) # decode_responses -> barśż zwraca tekst, poprzednio zwracało byte
