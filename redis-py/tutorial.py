import time

import redis

HOST = '192.168.59.103' # value returned by `boot2docker ip`
pool = redis.ConnectionPool(host=HOST, port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

# Note: Unix Socket is available for same-server connections.
# Note: The hiredis parser implemented in C can be much faster but must be
#       installed separately.

r.set('foo', 'bar')
print 'foo', r.get('foo')

# Use Pipeline to batch commands.
pipe = r.pipeline()
res = pipe \
    .set('foo', 'bar') \
    .get('foo') \
    .get('bing') \
    .get('bang') \
    .execute()
print 'Pipeline', res

# PubSub.
pubsub = r.pubsub(ignore_subscribe_messages=True)
#pubsub.subscribe('image-upload-channel')

def sub_handler(msg):
    print 'subscriber received', msg['data']
pubsub.subscribe(**{'image-upload-channel': sub_handler})
thread = pubsub.run_in_thread()
time.sleep(.1) # wait for thread to start...
r.publish('image-upload-channel', 'user U uploaded image I1')
r.publish('image-upload-channel', 'user U uploaded image I2')
thread.stop()

# Skimmed sections on Lua Scripting, Sentinel, Scan.
