#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon, Mar 21

@authors: Baiju Mohanan Plasseril
"""
import logging
from flask import Flask, jsonify, request

app = Flask(__name__)  


# logger
log_level = "DEBUG"
logger = logging.getLogger()
consoleHandler = logging.StreamHandler() 
logFormatter = logging.Formatter(
  "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
logger.setLevel(log_level)

@app.route("/hello", methods= ["GET"])
def hello():
  logger.debug ("hello")
  return jsonify({
    'message' : 'Hello world from First Program'
  })
  
@app.route("/", methods= ["GET"])
def empty():
  return hello()

## health api
@app.route("/health", methods= ["GET"])
def health():
  logger.debug ("health")
  return jsonify({
    'message' :  "Host is healthy"
  })
  
if __name__ == '__main__':
  app.run()