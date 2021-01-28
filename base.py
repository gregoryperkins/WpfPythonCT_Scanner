from request import get, post
import json
import time

import ssl
import websocket
import threading

class ApiError(Exception):
    def __init__(self, *args):
        self.apiMessage = None
        self.apiObject = None
                
        message = "API ERROR: \"unknown error\""
        if args:
            message = "API ERROR: \"" + args[0] + "\""
            if len(args) == 2:
                message = "API ERROR: \"" + args[0] + " in object " + args[1] + "\""
        
        super().__init__(message)


class WebSocket:
    def __init__(self, objectName):
        self.objectName = objectName

        self.baseUrl = "wss://localhost:666/API/"
        self.webSocket = None
        self.webSocketReady = False
        self.webSocketMessage = []
        

    def webSocketOpen(self, request):
        self.ws = websocket.WebSocketApp(self.baseUrl + self.objectName + "/request/" + request,
                            on_message = lambda ws, message : self.__webSocketResponse(ws, "message", message),
                            on_error = lambda ws, error : self.__webSocketResponse(ws, "error", error),
                            on_close = lambda ws : self.__webSocketClosed(ws),
                            on_open = lambda ws : self.__webSocketOpened(ws))

        self.thread = threading.Thread(target=self.ws.run_forever, args=(None, {"cert_reqs": ssl.CERT_NONE}))
        self.thread.start()

    def webSocketOrder(self, order):
        self.__webSocketWaitReady()
        self.webSocketMessage = []
        self.ws.send(order)
        self.__webSocketWaitMessage()

        return self.webSocketMessage

    def webSocketClose(self):
        self.__webSocketWaitReady()
        self.ws.close()


    def __webSocketOpened(self, ws):
        print ("WebSocket connection opened")
        self.webSocketReady = True
    def __webSocketClosed(self, ws):
        print ("WebSocket connection closed")
        self.webSocketReady = False
    def __webSocketWaitReady(self):
        while not self.webSocketReady:
            time.sleep(1)
    def __webSocketWaitMessage(self):
        while len(self.webSocketMessage) == 0:
            time.sleep(1)
    def __webSocketResponse(self, ws, messageType, response):
        self.webSocketMessage.append(response)



class Base:
    def __init__(self, objectName):
        self.objectName = objectName

        self.baseUrl = "http://localhost:800/API/"
        self.ws = WebSocket(objectName)

    def hold(self):
        httpResponse = get(self.baseUrl + "hold")
        jsonResponse = json.loads(httpResponse)

        if (jsonResponse["response"]["type"] == "error"):
            raise ApiError(jsonResponse["response"]["message"])
        else:
            self.keyPerm = jsonResponse["response"]["message"]


    def release(self):
        placeholder = {"permission":[], "parameters":[]}
        placeholder["permission"] = self.keyPerm
        
        httpResponse = post(self.baseUrl + "release", placeholder)
        jsonResponse = json.loads(httpResponse)
        
        if (jsonResponse["response"]["type"] == "error"):
            raise ApiError(str(jsonResponse["response"]["message"]))


    def executeCommand(self, objectName, command, values=[]):
        self.hold()
        placeholder = {"permission":[], "parameters":[]}
        placeholder["permission"] = self.keyPerm
        placeholder["parameters"] = values

        httpResponse = post(self.baseUrl + objectName + "/command/" + command, placeholder)
        jsonResponse = json.loads(httpResponse)
        self.release()
        
        if (jsonResponse["response"]["type"] == "error"):
            raise ApiError(str(jsonResponse["response"]["message"]), objectName)


    def getValue(self, objectName, attribute):
        httpResponse = get(self.baseUrl + objectName + "/attribute/" + attribute)
        jsonResponse = json.loads(httpResponse)

        if (jsonResponse["response"]["type"] == "error"):
            raise ApiError(str(jsonResponse["response"]["message"]), objectName)
        else:
            return jsonResponse["response"]["message"]


    def setValue(self, objectName, attribute, value):
        self.hold()
        placeholder = {"permission":[], "parameters":[]}
        placeholder["permission"] = self.keyPerm
        placeholder["parameters"] = [value]
        
        httpResponse = post(self.baseUrl + objectName + "/attribute/" + attribute, placeholder)
        jsonResponse = json.loads(httpResponse)
        self.release()
        
        if (jsonResponse["response"]["type"] == "error"):
            raise ApiError(str(jsonResponse["response"]["message"]), objectName)
            
    def waitUntilReady(self, showProgress = False):
        ready = False
        while not ready:
            time.sleep(1)
            
            response = get(self.baseUrl + self.objectName + "/attribute/ready")
            responseStatus = get(self.baseUrl + self.objectName + "/request/status")
        
            try:
                json_response = json.loads(response)
                json_responseStatus = json.loads(responseStatus)
            except Exception as e:
                print("ERROR: " + str(e)) 

            status = json_responseStatus["response"]["message"]
            
            if json_response["response"]["type"] == "error":
                ready = True
            else:
                ready = json_response["response"]["message"] == "true"
            
            if showProgress:
                response = get(self.baseUrl + self.objectName + "/attribute/progress")
                try:
                    json_response = json.loads(response)
                except Exception as e:
                    print("ERROR: " + str(e))
                    
                progress = json_response["response"]["message"]
                
                print("Waiting object " + self.objectName + " ("+status+") progression " + progress)
            else:
                print("Waiting object " + self.objectName + "("+status+")")
    

    def webSocket(self):
        return self.ws