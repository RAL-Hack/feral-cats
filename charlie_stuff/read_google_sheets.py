import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/spreadsheets/d/"+id+"/export?format=csv"
    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def get_file():
    file_id = '1MyIxywEoQNF6E-mupSK6xAZMM_b4CH96WWa9OVxK4WI'
    destination = 'data.csv'
    download_file_from_google_drive(file_id, destination)



