import http.client
import json

# This is a small example of how the http.client library works to perform http requests.
# being more specific the http methods (GET AND POST)

# Note: have running the script in the server folder, which raises a server on port 8000 

# get_method_request performs an http GET type request
def get_method_request():
    conn = http.client.HTTPConnection('localhost', 8000)

    headers = {}
    cookies = {
        "cookie1": "valor_cookie1",
        "cookie2": "valor_cookie2"
    }

    cookie_str = '; '.join([f"{key}={value}" for key, value in cookies.items()])
    headers["Cookie"] = cookie_str

    conn.request('GET', "", headers=headers)

    response = conn.getresponse()

    print(response.status, response.reason)
    print(response.read())

    response.close()
    conn.close()

# post_method_request performs an http POST type request
def post_method_request():
    conn = http.client.HTTPConnection('localhost', 8000)

    payload = {"message": "hello"}
    headers = {"Content-type": "application/json"}

    json_payload = json.dumps(payload)

    conn.request("POST", "", json_payload, headers)

    response = conn.getresponse()

    print(response.status, response.reason)
    print(response.read())

    response.close()
    conn.close()


if __name__ == "__main__":
    # Note: to use get_method_request() change post_method_request()
    try:
        # get_method_request()
        post_method_request()
    except KeyboardInterrupt:
        pass

    print("Finalized serve")
