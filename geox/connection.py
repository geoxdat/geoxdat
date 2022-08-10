from http import HTTPStatus
import sys
from geox.exceptions import APIKeyException, ParameterException
from requests import request, Response


def check_status_code(response: Response) -> None:
    '''checking all available status code from GeoX API'''
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        raise APIKeyException(f'Unauthorized. {response.json()["detail"]}.')
    
    elif response.status_code == HTTPStatus.BAD_REQUEST:
        raise ParameterException(f'Some of the parameter in request is invalid. {response.text}.')
    

def connect_to_endpoint(url: str, method: str, headers: dict={}, params:dict ={}) -> Response:
    '''Connect to endpoint'''
    try:
        response = request(
            method=method, 
            url=url, 
            headers = headers, 
            params = params
            )
        
        # checking status code
        check_status_code(response)

        return response
    
    except Exception as e:
        print(e)
        sys.exit()