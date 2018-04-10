#!/usr/bin/python

import bottle
import energenie

IDS = { 'Bed light': 1,
        'Bed radio': 2,
        'Kitchen': 3,
        'Living room': 4 }

@bottle.route('/set/<id>/<state>')
def set(id=0, state=True):
    if state=='off':
        state=False

    energenie.set_state(state, id)
    return '{"%s": %s}' % (id, (state and 'true') or 'false')
    
@bottle.route('/')
def controls():
    locations = sorted(IDS.keys())

    rows = ''

    for l in locations:
        rows += '''
            <tr><td>%s</td><td class="on" onclick="send_command(%s,true)">On</td><td class="off" onclick="send_command(%s,false)">Off</td></tr>''' % (l, IDS[l], IDS[l])

    rows += '''
            <tr><td>ALL</td><td class="on" onclick="send_command(0,true)">On</td><td class="off" onclick="send_command(0,false)">Off</td></tr>'''

    return '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<title>Energenie controller</title>
<style type="text/css">
body    { background-color: black;
          color: white;
          font-family: sans-serif;
          font-size: 30pt;
}

table	{ width: 100%%; }

td      { padding: 0.7em; }

.on     { background-color: #080; }

.off    { background-color: #c00; }
</style>
<script type="application/javascript">

send_command = function(id,state) {
    if (state) {
        state = 'on';
    } else {
        state = 'off';
    }
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/set/'+id+'/'+state);
    // no point expecting a response,
    // as the server doesn't get a response from the device.
    // Just mash the button until it works.
    xhr.send();
}
    
</script>
</head>
<body>
    <table>
        %s
    </table>
</body>''' % rows


bottle.run(host='0.0.0.0', port=8080)
