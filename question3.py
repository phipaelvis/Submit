from urllib import request
import os
import time
start_time = time.time()
url = os.environ['url']
iterations = os.environ['iterations']
for i in range(iterations):
    response = request.get(url)
print("--- %s seconds ---" % (time.time() - start_time))