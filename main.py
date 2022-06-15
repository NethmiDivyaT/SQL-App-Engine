import os

from flask import Flask, flash, redirect, request, render_template
import pymysql

import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'user1',
    'password': 'abc123',
    'host': '34.133.184.1',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

app = Flask(__name__)


@app.route('/')
def main():
    connection = pymysql.connect(**config)
    cur = connection.cursor()

    if request.method == 'GET':
        with connection:
            with cur as cursor:

                cursor.execute("select * from country")
                result = cursor.fetchall()

            cur.close()

    return str(current_msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
