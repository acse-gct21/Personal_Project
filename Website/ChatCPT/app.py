from flask import Flask
import Heap_Class as hc

app = Flask(__name__)

@app.route('/')
def run_code():
    arr = [ 12, 11, 13, 5, 6, 7]
    hc.MinHeap(arr)