import flask
import time

delay = 0
app = flask.Flask(__name__)

def get_status(file_path):
    f = open(file_path, encoding='utf-8', newline='')
    status = f.readline()
    f.close()
    return status

def get_response(file_path):
    f = open(file_path, encoding='utf-8', newline='')
    f.readline()
    response = f.readline()
    f.close()
    return response

@app.route('/')
def main():
     return 'This is mock service for MSK Longenvity'

@app.route('/api/mobile/v1/login', methods=['POST'])
def login():
        time.sleep(delay)
        return flask.Response(
            status=get_status('POST_api_mobile_v1_login.txt'),
            mimetype='application/json',
            response=get_response('POST_api_mobile_v1_login.txt')
        )

@app.route('/api/mobile/v1/restpassword', methods=['POST'])
def restpassword():
        time.sleep(delay)
        return flask.Response(
            status=get_status('POST_api_mobile_v1_restpassword.txt'),
            mimetype='application/json',
            response=get_response('POST_api_mobile_v1_restpassword.txt')
        )

@app.route('/api/mobile/v1/lessons', methods=['GET'])
def lessons():
        time.sleep(delay)
        return flask.Response(
            status=get_status('GET_api_mobile_v1_lessons.txt'),
            mimetype='application/json',
            response=get_response('GET_api_mobile_v1_lessons.txt').replace("11.11.2019", time.strftime("%d.%m.%Y", time.localtime()))
        )

@app.route('/api/mobile/v1/datetime', methods=['GET'])
def datetime():
        time.sleep(delay)
        return flask.Response(
            status=get_status('GET_api_mobile_v1_datetime.txt'),
            mimetype='application/json',
            response=get_response('GET_api_mobile_v1_datetime.txt')
        )

@app.route('/api/mobile/v1/feedbackparams', methods=['GET'])
def feedbackparams():
        time.sleep(delay)
        return flask.Response(
            status=get_status('GET_api_mobile_v1_feedbackparams.txt'),
            mimetype='application/json',
            response=get_response('GET_api_mobile_v1_feedbackparams.txt')
        )

@app.route('/api/mobile/v1/lessons/<id>', methods=['POST'])
def lessons_save(id):
        time.sleep(delay)
        return flask.Response(
            status=get_status('POST_api_mobile_v1_lessons_id.txt'),
            mimetype='application/json',
            response=get_response('POST_api_mobile_v1_lessons_id.txt')
        )

@app.route('/api/mobile/v1/notifications', methods=['GET'])
def notifications():
        time.sleep(delay)
        return flask.Response(
            status=get_status('GET_api_mobile_v1_notifications.txt'),
            mimetype='application/json',
            response=get_response('GET_api_mobile_v1_notifications.txt')
        )

@app.route('/api/mobile/v1/notifications/<id>', methods=['PATCH'])
def notifications_read(id):
        time.sleep(delay)
        return flask.Response(
            status=get_status('PATCH_api_mobile_v1_notifications_id.txt'),
            mimetype='application/json',
            response=get_response('PATCH_api_mobile_v1_notifications_id.txt')
        )

@app.route('/api/mobile/v1/systemnotification', methods=['GET'])
def systemnotification():
        time.sleep(delay)
        return flask.Response(
            status=get_status('GET_api_mobile_v1_systemnotification.txt'),
            mimetype='application/json',
            response=get_response('GET_api_mobile_v1_systemnotification.txt')
        )

@app.route('/api/mobile/v1/systemnotifications/<id>', methods=['PATCH'])
def systemnotification_read(id):
        time.sleep(delay)
        return flask.Response(
            status=get_status('PATCH_api_mobile_v1_systemnotifications_id.txt'),
            mimetype='application/json',
            response=get_response('PATCH_api_mobile_v1_systemnotifications_id.txt')
        )

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8080)